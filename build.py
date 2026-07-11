#!/usr/bin/env python3
"""
build.py - bundle the serial book into a single standalone offline file.

Reads manifest.json (title, cover, chapter list), embeds every image as a
downscaled data-URI so the result opens by double-click, bundles the optional
guide.json, and injects it all into a copy of index.html -> book.html.

  python3 build.py

Requires Pillow (one-time):   pip install Pillow

Output: ./build/book.html by default (change OUTPUT_DIR below if you like).
"""
import json, base64, io, sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("ERROR: Pillow not installed. Run:  pip install Pillow")
    sys.exit(1)

# --- tuning knobs ---------------------------------------------------
MAX_WIDTH    = 1600   # px; images wider than this are scaled down
JPEG_QUALITY = 80     # 1-95; 80 is visually clean and much smaller
# Where to write book.html. Default: a ./build folder next to this script.
# (Kept out of any cloud-synced path issues by being local to the project.)
OUTPUT_DIR   = Path(__file__).parent / "build"
# --------------------------------------------------------------------

ROOT = Path(__file__).parent
manifest = json.loads((ROOT/"manifest.json").read_text(encoding="utf-8"))

def embed(img_rel, label):
    """Return a downscaled JPEG data-URI for an image path, or '' if missing."""
    if not img_rel:
        return img_rel
    p = ROOT/img_rel
    if not p.exists():
        print(f"  ! {label}: image '{img_rel}' not found - will show no image")
        return ""
    try:
        im = Image.open(p).convert("RGB")
        if im.width > MAX_WIDTH:
            h = int(im.height * MAX_WIDTH / im.width)
            im = im.resize((MAX_WIDTH, h), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=JPEG_QUALITY, optimize=True)
        data = base64.b64encode(buf.getvalue()).decode("ascii")
        return f"data:image/jpeg;base64,{data}"
    except Exception as e:
        print(f"  ! {label}: could not process '{img_rel}': {e}")
        return ""

# --- chapters -------------------------------------------------------
chapters = []
for cid in manifest["chapters"]:
    cpath = ROOT/"chapters"/f"{cid}.json"
    if not cpath.exists():
        print(f"  ! skipping {cid}: chapters/{cid}.json not found")
        continue
    ch = json.loads(cpath.read_text(encoding="utf-8"))
    if ch.get("image"):
        ch["image"] = embed(ch["image"], cid)
    if isinstance(ch.get("sequence"), list):
        for entry in ch["sequence"]:
            if isinstance(entry, dict) and entry.get("image"):
                entry["image"] = embed(entry["image"], cid)
    chapters.append(ch)
    print(f"  - {cid} embedded")

# --- cover (optional) ----------------------------------------------
cover = None
if isinstance(manifest.get("cover"), dict) and manifest["cover"].get("image"):
    cover = dict(manifest["cover"])
    cover["image"] = embed(cover["image"], "cover")
    print("  - cover embedded")

bundle = {"title": manifest.get("title","Untitled"), "chapters": chapters}
if manifest.get("comingSoon"):
    bundle["comingSoon"] = manifest["comingSoon"]
if cover:
    bundle["cover"] = cover

# --- guide (optional) ----------------------------------------------
# guide.json holds the spoiler-free who's-who. We embed its images too, so the
# guide works fully offline in book.html.
guide = None
gpath = ROOT/"guide.json"
if gpath.exists():
    try:
        guide = json.loads(gpath.read_text(encoding="utf-8"))
        for sec in guide.get("sections", []):
            for e in sec.get("entries", []):
                if e.get("img"):
                    e["img_embedded"] = embed(f"images/guide/{e['img']}", f"guide:{e.get('name','')}")
        print("  - guide embedded")
    except Exception as e:
        print(f"  ! could not process guide.json: {e}")
        guide = None

# --- inject into the reader shell ----------------------------------
shell = (ROOT/"index.html").read_text(encoding="utf-8")

ph_data = "const BUNDLED_DATA = null; /* BUNDLE_PLACEHOLDER */"
if ph_data not in shell:
    print("ERROR: could not find the bundle placeholder in index.html"); sys.exit(1)
shell = shell.replace(ph_data, f"const BUNDLED_DATA = {json.dumps(bundle, ensure_ascii=False)};")

ph_guide = "const BUNDLED_GUIDE = null; /* GUIDE_PLACEHOLDER */"
if ph_guide in shell:
    guide_js = json.dumps(guide, ensure_ascii=False) if guide else "null"
    shell = shell.replace(ph_guide, f"const BUNDLED_GUIDE = {guide_js};")

# --- write output --------------------------------------------------
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
out_path = OUTPUT_DIR / "book.html"
out_path.write_text(shell, encoding="utf-8")

mb = out_path.stat().st_size/1024/1024
print(f"  Built book.html  ({len(chapters)} chapter(s)"
      f"{', + cover' if cover else ''}{', + guide' if guide else ''}, {mb:.1f} MB)")
print(f"  Written to: {out_path}")
print("  Double-click book.html to read locally.")
