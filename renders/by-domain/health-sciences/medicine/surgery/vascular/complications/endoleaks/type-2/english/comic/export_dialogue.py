import json
from pathlib import Path

BASE = Path(__file__).parent
STORYBOARD = BASE / "storyboard.json"
OUT = BASE / "dialogue.md"


def export():
    data = json.loads(STORYBOARD.read_text())
    lines = ["# Dialogue Script", ""]
    for panel in data:
        lines.append(f"## Panel {panel['panel']:02d} — {panel['title']}")
        lines.append(f"_Visual prompt:_ {panel['visual_prompt']}")
        lines.append("")
        for line in panel["dialogue"]:
            lines.append(f"- **{line['speaker']}**: {line['text']}")
        lines.append("")
    OUT.write_text("\n".join(lines))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    export()
