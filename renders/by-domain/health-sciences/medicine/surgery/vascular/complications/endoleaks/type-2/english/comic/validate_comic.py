import json
from pathlib import Path

BASE = Path(__file__).parent
PROMPTS = BASE / "gpt-prompts.txt"
IMAGES = list((BASE / "panels-gpt").glob("image_*.png"))
MAP = BASE / "panel-map.json"
ALT = BASE / "panels-gpt" / "alt-text.md"
PDF = BASE / "type2-endoleak-comic-gpt.pdf"
PDF_FEATURED = BASE / "type2-endoleak-comic-gpt-featured.pdf"


def main():
    ok = True

    if not PROMPTS.exists():
        ok = False
        print("❌ missing prompts file")
    else:
        prompts = [ln for ln in PROMPTS.read_text().splitlines() if ln.strip()]
        print(f"Prompts: {len(prompts)}")
        ok &= len(prompts) >= 32

    if not IMAGES:
        ok = False
        print("❌ no GPT images found")
    else:
        print(f"Images: {len(IMAGES)}")
        ok &= len(IMAGES) >= 32

    if MAP.exists():
        mp = json.loads(MAP.read_text())
        print(f"Map entries: {len(mp)}")
        ok &= len(mp) >= 32
        for entry in mp:
            if not entry.get("file"):
                ok = False
                print(f"❌ missing file for panel {entry.get('panel')}")
            else:
                path = BASE / entry["file"]
                if not path.exists():
                    ok = False
                    print(f"❌ missing image file on disk: {path}")
            if not entry.get("alt_text"):
                ok = False
                print(f"❌ missing alt_text for panel {entry.get('panel')}")
    else:
        ok = False
        print("❌ missing panel-map.json")

    if ALT.exists():
        alt_lines = [ln for ln in ALT.read_text().splitlines() if ln and ln[0].isdigit()]
        print(f"Alt text entries: {len(alt_lines)}")
        ok &= len(alt_lines) >= 32
    else:
        ok = False
        print("❌ missing alt-text.md")

    if PDF.exists():
        print(f"PDF present: {PDF.stat().st_size} bytes")
    else:
        ok = False
        print("❌ missing PDF")
    if PDF_FEATURED.exists():
        print(f"Featured PDF present: {PDF_FEATURED.stat().st_size} bytes")
    else:
        ok = False
        print("❌ missing featured PDF")

    print("✅ OK" if ok else "⚠️ Issues detected")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
