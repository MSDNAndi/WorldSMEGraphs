from pathlib import Path
from PIL import Image

BASE = Path(__file__).parent
SRC = BASE / "panels-gpt"
PDF = BASE / "type2-endoleak-comic-gpt.pdf"


def collect_images():
    files = sorted(SRC.glob("image_*.png"))
    if len(files) != 32:
        print(f"Warning: expected 32 images, found {len(files)}")
    return files


def build_pdf(images):
    if not images:
        print("No images to build PDF")
        return
    imgs = [Image.open(p).convert("RGB") for p in images]
    pages = []
    per_page = 6
    cols, rows = 3, 2
    slot_w, slot_h = 768, 512
    pad = 32
    page_w = cols * slot_w + (cols + 1) * pad
    page_h = rows * slot_h + (rows + 1) * pad

    for i in range(0, len(imgs), per_page):
        chunk = imgs[i:i + per_page]
        page = Image.new("RGB", (page_w, page_h), "white")
        for idx, img in enumerate(chunk):
            resized = img.resize((slot_w, slot_h))
            r = idx // cols
            c = idx % cols
            x = pad + c * (slot_w + pad)
            y = pad + r * (slot_h + pad)
            page.paste(resized, (x, y))
        pages.append(page)

    pages[0].save(PDF, save_all=True, append_images=pages[1:])
    print(f"PDF written to {PDF}")


if __name__ == "__main__":
    imgs = collect_images()
    build_pdf(imgs)
