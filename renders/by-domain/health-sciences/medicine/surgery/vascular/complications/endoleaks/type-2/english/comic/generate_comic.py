import json
from pathlib import Path
from typing import List, Dict

from PIL import Image, ImageDraw, ImageFont

BASE_DIR = Path(__file__).parent
STORYBOARD_PATH = BASE_DIR / "storyboard.json"
PANELS_DIR = BASE_DIR / "panels"
PDF_PATH = BASE_DIR / "type2-endoleak-comic.pdf"


def load_storyboard() -> List[Dict]:
    with STORYBOARD_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def ensure_dirs():
    PANELS_DIR.mkdir(exist_ok=True)


def choose_color(index: int) -> str:
    palette = [
        "#FDE68A", "#BFDBFE", "#C7D2FE", "#FBCFE8", "#BBF7D0", "#FCD34D",
        "#F9A8D4", "#A5F3FC", "#E9D5FF", "#FED7AA"
    ]
    return palette[index % len(palette)]


def draw_panel(panel: Dict) -> Image.Image:
    width, height = 900, 900
    img = Image.new("RGB", (width, height), choose_color(panel["panel"]))
    draw = ImageDraw.Draw(img)
    font_title = ImageFont.load_default()
    font_text = ImageFont.load_default()

    margin = 24
    title = f'{panel["panel"]:02d}. {panel["title"]}'
    draw.text((margin, margin), title, fill="black", font=font_title)

    # Visual prompt box
    vp_top = margin + 24
    draw.rounded_rectangle(
        [margin, vp_top, width - margin, vp_top + 160],
        radius=16,
        fill="#FFFFFF",
        outline="#0F172A",
        width=2,
    )
    draw.multiline_text(
        (margin + 12, vp_top + 12),
        panel["visual_prompt"],
        fill="#0F172A",
        font=font_text,
        spacing=4,
        align="left",
    )

    # Speech bubbles
    bubble_top = vp_top + 180
    bubble_gap = 16
    for idx, line in enumerate(panel["dialogue"]):
        y0 = bubble_top + idx * 120
        y1 = y0 + 100
        draw.rounded_rectangle(
            [margin, y0, width - margin, y1],
            radius=18,
            fill="#FFFFFF",
            outline="#1F2937",
            width=2,
        )
        text = f'{line["speaker"]}: "{line["text"]}"'
        draw.multiline_text(
            (margin + 14, y0 + 10),
            text,
            fill="#111827",
            font=font_text,
            spacing=4,
        )

    return img


def render_panels(panels: List[Dict]) -> List[Path]:
    files = []
    for p in panels:
        img = draw_panel(p)
        out_path = PANELS_DIR / f'panel-{p["panel"]:02d}.png'
        img.save(out_path)
        files.append(out_path)
    return files


def build_pdf(panel_files: List[Path]):
    images = [Image.open(p).convert("RGB") for p in panel_files]
    pages: List[Image.Image] = []
    per_page = 6
    cols = 3
    rows = 2
    slot_w = 720
    slot_h = 720
    pad = 40
    page_w = cols * slot_w + (cols + 1) * pad
    page_h = rows * slot_h + (rows + 1) * pad

    for i in range(0, len(images), per_page):
        page = Image.new("RGB", (page_w, page_h), "white")
        chunk = images[i:i + per_page]
        for idx, img in enumerate(chunk):
            resized = img.resize((slot_w, slot_h))
            r = idx // cols
            c = idx % cols
            x = pad + c * (slot_w + pad)
            y = pad + r * (slot_h + pad)
            page.paste(resized, (x, y))
        pages.append(page)

    if pages:
        pages[0].save(PDF_PATH, save_all=True, append_images=pages[1:])


def main():
    ensure_dirs()
    storyboard = load_storyboard()
    panel_files = render_panels(storyboard)
    build_pdf(panel_files)
    print(f"Generated {len(panel_files)} panels at {PANELS_DIR}")
    print(f"PDF created at {PDF_PATH}")


if __name__ == "__main__":
    main()
