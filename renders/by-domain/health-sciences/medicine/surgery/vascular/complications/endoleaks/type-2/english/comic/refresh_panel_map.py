import json
import re
from pathlib import Path

BASE = Path(__file__).parent
PROMPTS = BASE / "gpt-prompts.txt"
IMAGES = sorted((BASE / "panels-gpt").glob("image_*.png"))
ALT_TEXT = BASE / "panels-gpt" / "alt-text.md"
OUT = BASE / "panel-map.json"


def load_prompts():
    records = []
    for line in PROMPTS.read_text().splitlines():
        m = re.match(r"Panel\s+(\d+)[^:]*:\s*(.*)", line)
        if not m:
            continue
        num = int(m.group(1))
        records.append((num, line.strip()))
    records.sort(key=lambda x: x[0])
    return records


def load_alt_text():
    if not ALT_TEXT.exists():
        return {}
    alt_map = {}
    for line in ALT_TEXT.read_text().splitlines():
        m = re.match(r"^(\d+)\.\s*(.*)", line.strip())
        if m:
            alt_map[int(m.group(1))] = m.group(2)
    return alt_map


def build_map():
    prompts = load_prompts()
    alt = load_alt_text()
    if len(prompts) != len(IMAGES):
        print(f"Warning: prompts ({len(prompts)}) != images ({len(IMAGES)})")
    data = []
    for idx, (num, prompt_line) in enumerate(prompts):
        file = str(IMAGES[idx].relative_to(BASE)) if idx < len(IMAGES) else None
        data.append({"panel": num, "prompt": prompt_line, "file": file, "alt_text": alt.get(num)})
    OUT.write_text(json.dumps(data, indent=2))
    print(f"Wrote {OUT} with {len(data)} entries")


if __name__ == "__main__":
    build_map()
