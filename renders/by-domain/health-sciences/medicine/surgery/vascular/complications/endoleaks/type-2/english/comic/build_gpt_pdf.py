from pathlib import Path
from PIL import Image

BASE = Path(__file__).parent
SRC = BASE / "panels-gpt"
PDF = BASE / "type2-endoleak-comic-gpt.pdf"
PDF_FEATURED = BASE / "type2-endoleak-comic-gpt-featured.pdf"
FEATURED_INDEX = 14  # 0-based, panel 15 (microbubble research highlight)


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


def build_featured_pdf(images):
    if not images:
        print("No images to build featured PDF")
        return
    if FEATURED_INDEX >= len(images):
        print("Featured index out of range; skipping featured PDF")
        return
    imgs = [Image.open(p).convert("RGB") for p in images]
    featured = imgs[FEATURED_INDEX]
    remaining = imgs[:FEATURED_INDEX] + imgs[FEATURED_INDEX + 1:]

    slot_w, slot_h = 720, 480
    featured_h = int(slot_h * 1.5)
    pad = 32
    page_w = 2 * slot_w + 3 * pad
    page_h = pad + featured_h + pad + 2 * slot_h + 2 * pad

    pages = []
    chunk_start = 0
    while chunk_start < len(remaining):
        chunk = remaining[chunk_start:chunk_start + 4]
        chunk_start += 4

        page = Image.new("RGB", (page_w, page_h), "white")
        # featured on top spanning width
        f_resized = featured.resize((page_w - 2 * pad, featured_h))
        page.paste(f_resized, (pad, pad))

        # grid below (2x2)
        for idx, img in enumerate(chunk):
            resized = img.resize((slot_w, slot_h))
            r = idx // 2
            c = idx % 2
            x = pad + c * (slot_w + pad)
            y = pad + featured_h + pad + r * (slot_h + pad)
            page.paste(resized, (x, y))
        pages.append(page)

    pages[0].save(PDF_FEATURED, save_all=True, append_images=pages[1:])
    print(f"Featured PDF written to {PDF_FEATURED}")


if __name__ == "__main__":
    imgs = collect_images()
    build_pdf(imgs)
    build_featured_pdf(imgs)
