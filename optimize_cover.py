#!/usr/bin/env python3
"""
optimize_cover.py - resize and compress RobinHoodCover.jpg for web/social use.

Your current cover is 2400x3600 at 9.46MB - print resolution, and well over
Facebook's 8MB og:image cap (likely why the Sharing Debugger reports it as
"corrupted"). This script creates a web-appropriate version.

Usage:
    pip install Pillow --break-system-packages   # if not already installed
    python3 optimize_cover.py

Edit SOURCE / OUTPUT below if your paths differ.
"""
from PIL import Image
from pathlib import Path

SOURCE = Path("images/RobinHoodCover.jpg")   # your current file
OUTPUT = Path("images/RobinHoodCover.jpg")   # overwrite in place
MAX_WIDTH = 1200                              # plenty sharp for web/social; matches
                                               # Facebook's own recommended og:image width
JPEG_QUALITY = 85

def main():
    if not SOURCE.exists():
        print(f"ERROR: {SOURCE} not found. Run this from your project root,")
        print("or edit the SOURCE path at the top of this script.")
        return

    original_size = SOURCE.stat().st_size

    im = Image.open(SOURCE).convert("RGB")
    print(f"Original: {im.width}x{im.height}, {original_size/1024/1024:.2f} MB")

    if im.width > MAX_WIDTH:
        new_height = int(im.height * MAX_WIDTH / im.width)
        im = im.resize((MAX_WIDTH, new_height), Image.LANCZOS)

    # Write to a temp file first so we don't clobber the original if something goes wrong
    temp_path = OUTPUT.with_suffix(".tmp.jpg")
    im.save(temp_path, format="JPEG", quality=JPEG_QUALITY, optimize=True)

    new_size = temp_path.stat().st_size
    temp_path.replace(OUTPUT)

    print(f"New:      {im.width}x{im.height}, {new_size/1024/1024:.2f} MB")
    print(f"Saved to: {OUTPUT}")
    print(f"Reduction: {(1 - new_size/original_size)*100:.0f}% smaller")

    if new_size > 8 * 1024 * 1024:
        print("\nWARNING: still over Facebook's 8MB og:image limit. Lower JPEG_QUALITY and re-run.")
    else:
        print("\nWell under Facebook's 8MB limit.")

if __name__ == "__main__":
    main()
