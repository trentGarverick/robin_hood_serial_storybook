"""
checkprofiles.py — verify the color profiles of exported images.

Scans the images_new folder (recursively) and reports each image's embedded
ICC color profile, flagging anything that is NOT sRGB so you can catch stray
Rec. 2020 (or other wide-gamut) files before publishing.

USAGE:
    1. Place this file in the container folder that holds "images_new"
       (the same folder where "images" and "images_new" live).
    2. Run:   python checkprofiles.py
       (If that doesn't work, try:  python3 checkprofiles.py )

Requires Pillow (you already have it if you use build.py). If not:
    pip install Pillow

WHAT THE OUTPUT MEANS:
    "sRGB IEC61966-2.1"   -> correct; nothing to do.
    "... NOT sRGB ..."    -> wide-gamut (e.g. Rec. 2020); re-export this one.
    "NO PROFILE"          -> no embedded profile. Browsers assume sRGB, so it
                             usually looks fine, but re-exporting with
                             "Embed Color Profile" checked removes all doubt.
"""

from pathlib import Path
import io
import sys

try:
    from PIL import Image, ImageCms
except ImportError:
    print("ERROR: Pillow is not installed. Run:  pip install Pillow")
    sys.exit(1)

# Folder to scan. Change this if your folder has a different name.
FOLDER = Path("images\guide")

IMAGE_EXTS = {".jpg", ".jpeg", ".png"}

def main():
    if not FOLDER.exists():
        print(f"ERROR: folder '{FOLDER}' not found.")
        print("Place this script in the folder that CONTAINS 'images_new', then run it again.")
        sys.exit(1)

    files = sorted(p for p in FOLDER.rglob("*") if p.suffix.lower() in IMAGE_EXTS)
    if not files:
        print(f"No image files found in '{FOLDER}'.")
        return

    total = 0
    srgb = 0
    no_profile = 0
    suspect = []

    print(f"Scanning {len(files)} image(s) in '{FOLDER}'...\n")

    for p in files:
        total += 1
        # show path relative to the scanned folder, so subfolders (e.g. guide/) are visible
        rel = p.relative_to(FOLDER)
        try:
            im = Image.open(p)
            icc = im.info.get("icc_profile")
            if not icc:
                no_profile += 1
                print(f"  NO PROFILE                                 : {rel}")
                continue
            prof = ImageCms.ImageCmsProfile(io.BytesIO(icc))
            desc = ImageCms.getProfileDescription(prof).strip()
            if "srgb" in desc.lower():
                srgb += 1
                print(f"  {desc:40} : {rel}")
            else:
                suspect.append((rel, desc))
                print(f"  {desc:40} : {rel}   <-- NOT sRGB, RE-EXPORT THIS")
        except Exception as e:
            print(f"  ERROR reading {rel}: {e}")

    # Summary
    print("\n" + "-" * 60)
    print(f"Total images scanned : {total}")
    print(f"  sRGB (good)        : {srgb}")
    print(f"  No profile         : {no_profile}  (usually fine; browsers assume sRGB)")
    print(f"  NOT sRGB (fix)     : {len(suspect)}")
    if suspect:
        print("\nFiles that are NOT sRGB (re-export these):")
        for rel, desc in suspect:
            print(f"  - {rel}   [{desc}]")
    else:
        print("\nNo wide-gamut files found. Every image is sRGB or untagged. Clean sweep.")

if __name__ == "__main__":
    main()
