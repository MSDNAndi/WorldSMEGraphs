import json
import argparse
from pathlib import Path
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description='Build PDF from comic panel images')
    parser.add_argument('--input-dir', type=str, default='panels-gpt', help='Input directory containing images')
    parser.add_argument('--output', type=str, default='type2-endoleak-comic-gpt.pdf', help='Output PDF file')
    args = parser.parse_args()
    
    BASE = Path(__file__).parent
    SRC = BASE / args.input_dir
    PDF = BASE / args.output
    PDF_FEATURED = BASE / args.output.replace('.pdf', '-featured.pdf')
    PANEL_MAP = BASE / "panel-map.json"
    DEFAULT_FEATURED_PANEL = 15  # panel number (1-based)
    
    return SRC, PDF, PDF_FEATURED, PANEL_MAP, DEFAULT_FEATURED_PANEL

def collect_images(src_dir):
    files = sorted(src_dir.glob("image_*.png"))
    if len(files) != 32:
        print(f"Warning: expected 32 images, found {len(files)}")
    return files


def get_featured_index(panel_map_path, default_featured=15):
    try:
        data = json.loads(panel_map_path.read_text())
        for entry in data:
            if entry.get("featured"):
                return max(entry["panel"] - 1, 0)
    except Exception as e:
        print(f"Warning: unable to read featured panel from panel-map.json ({e})")
    return default_featured - 1


def build_pdf(images, pdf_path):
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

    pages[0].save(pdf_path, save_all=True, append_images=pages[1:])
    print(f"PDF written to {pdf_path}")


def build_featured_pdf(images, pdf_featured_path, featured_idx):
    if not images:
        print("No images to build featured PDF")
        return
    if featured_idx >= len(images):
        print("Featured index out of range; skipping featured PDF")
        return
    imgs = [Image.open(p).convert("RGB") for p in images]
    featured = imgs[featured_idx]
    remaining = imgs[:featured_idx] + imgs[featured_idx + 1:]

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

    pages[0].save(pdf_featured_path, save_all=True, append_images=pages[1:])
    print(f"Featured PDF written to {pdf_featured_path}")


if __name__ == "__main__":
    SRC, PDF, PDF_FEATURED, PANEL_MAP, DEFAULT_FEATURED_PANEL = main()
    imgs = collect_images(SRC)
    build_pdf(imgs, PDF)
    featured_idx = get_featured_index(PANEL_MAP, DEFAULT_FEATURED_PANEL)
    build_featured_pdf(imgs, PDF_FEATURED, featured_idx)
