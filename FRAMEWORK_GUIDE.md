# Serial Illustrated Book Framework — How to Use It

This folder is a **reusable framework** for building an illustrated serial book that reads in a custom web reader (the same engine behind *Unwoven*), with a spoiler-free Guide, a Table of Contents, a cover page, and an offline single-file build. It ships with a short **dummy test story and guide** so you can confirm everything works before adding your own content.

---

## What's in this folder

```
index.html          The reader (generic engine — you should rarely need to touch this)
build.py            Bundles everything into a standalone offline book.html
checkprofiles.py    Utility: scans images for non-sRGB color profiles (web wants sRGB)
manifest.json       Book title, cover, and the ordered list of chapters   ← you edit
guide.json          The spoiler-free who's-who / where-is-where            ← you edit
chapters/           One JSON file per chapter (ch1.json, ch2.json, ...)    ← you edit
  ch1.json          Dummy Chapter One (replace)
  ch2.json          Dummy Chapter Two (replace)
images/             Chapter plates and the cover go here                   ← you add art
  cover.jpg         (add your cover here; name is set in manifest.json)
  guide/            Guide images go here (referenced by guide.json)        ← you add art
build/              Created by build.py; holds the offline book.html (gitignored)
```

The reader is **content-driven**: it reads `manifest.json`, the `chapters/*.json` files, and `guide.json`, and renders whatever they contain. You build a book by editing those data files and adding images — not by editing `index.html`.

---

## Quick start (test it first)

1. **Host the folder** on any static web host (Netlify, etc.) — or run a local web server in it — and open it. You should see the dummy "Test Story," be able to flip pages, open the **Guide** button (top), and open the **Contents**. Images are absent (none ship with the framework), so plates show blank and guide images show a small decorative tile — that's expected.
2. **Build the offline file:** run `python build.py` (needs Pillow: `pip install Pillow`). It writes `build/book.html`, a single self-contained file you can double-click to read offline. The dummy story should read there too.

Once the dummy story works both ways, you're ready to replace it with a real book.

> **Why two ways to read?** Hosted, the reader loads the live JSON files (so you can add a chapter by dropping in a file). Opened as a local `file://`, browsers block that loading, so `build.py` bakes everything into `book.html` for offline use. Re-run `build.py` whenever content or images change.

---

## Building a real book

### 1. Set the book details — `manifest.json`
```json
{
  "title": "Your Book Title",
  "cover": {
    "image": "images/cover.jpg",
    "title": "Your Book Title",
    "author": "Your Name",
    "tagline": "Your tagline"
  },
  "chapters": [ "ch1", "ch2", "ch3" ]
}
```
The `chapters` array is the **reading order** and lists the filenames (without `.json`) in `chapters/`. The cover block is optional; drop it to skip the cover page.

### 2. Write chapters — `chapters/chN.json`
Each chapter is a `sequence` of entries that interleave in the order you list them:
```json
{
  "eyebrow": "Chapter One",
  "title": "The Lantern",
  "sequence": [
    { "image": "images/ch1_plate_0.jpg",
      "_describe": "Optional: your image prompt/notes. The reader ignores this field." },
    { "text": [
      "First paragraph. The first text page of a chapter shows the title.",
      "Second paragraph."
    ] },
    { "image": "images/ch1_plate_1.jpg" },
    { "text": [ "More prose after the second plate." ] }
  ]
}
```
Rules of thumb:
- An entry has **either** `"image"` **or** `"text"`. Text is an array of paragraphs.
- Avoid two image entries back-to-back; put text between plates.
- The `_describe` field (or any field starting with `_`) is for **your** notes — the reader ignores it. It's a handy place to keep the image-generation prompt next to the plate it belongs to.
- To add a chapter later: drop `chN.json` in `chapters/`, add `"chN"` to `manifest.json`, redeploy.

### 3. Fill the Guide — `guide.json`
```json
{
  "title": "A Guide to <Your World>",
  "intro": "One spoiler-free line shown at the top of the guide.",
  "sections": [
    { "heading": "People", "entries": [
      { "name": "Name", "kind": "short descriptor", "img": "NAME.png",
        "blurb": "A sentence or two, spoiler-free.",
        "say": "You'll know them as: a visual cue." }
    ] }
  ]
}
```
- `img`, `say` are optional. Guide images live in `images/guide/` and are referenced by filename only. If an image is missing, a graceful decorative tile shows instead — so you can ship the guide before the art is ready.
- `guide.json` itself is optional; delete it and the Guide button simply shows nothing.

### 4. Add images — `images/` and `images/guide/`
- Chapter plates and the cover go in `images/` at the paths your chapter JSON / manifest reference.
- Guide images go in `images/guide/`.
- **Use sRGB.** The web assumes sRGB; wide-gamut profiles (e.g. Rec. 2020) render wrong in browsers. Run `python checkprofiles.py` (point it at `images/` or `images/guide/`) to flag any non-sRGB files. Untagged files are treated as sRGB and are usually fine.
- **Filenames are case-sensitive on the web** (Netlify) even though Windows ignores case. Keep references and files exactly matching, or images will work locally and break once hosted.

### 5. Build / deploy
- Offline file: `python build.py` → `build/book.html`.
- Hosted: deploy the folder (e.g. `netlify deploy --prod`), then **hard-refresh** (Ctrl+Shift+R) since content is cached.

---

## Putting just the framework in git

This folder is designed to be committed as-is. The `.gitignore` already excludes the build output (`build/`, `book.html`) and OS cruft. The empty `images/` folders are kept in git via `.gitkeep` files.

A clean first commit:
```
git init
git add .
git commit -m "New book from serial framework (dummy test story)"
```
Then replace the dummy content and commit your real book. If your images are large, consider **Git LFS** for `images/` (`git lfs track "*.png" "*.jpg"`) — and remember that the offline `book.html` is intentionally gitignored (regenerate it with `build.py` rather than committing it).

---

## What you should NOT normally need to edit

`index.html` is the generic engine — the page-flip logic, cover flow, TOC, guide rendering, and offline loader. You can re-theme it (the CSS near the top: colors, fonts) if you want a different look, but you shouldn't need to touch it to publish a new story. All story content lives in the data files.

---

## If you want help building the next book

There's a companion file, **`FOR_CLAUDE.md`**, written as instructions to Claude. When you start a new project on this framework and want Claude's help, point Claude at that file — it explains the framework's structure and conventions so Claude can pick up quickly and help you draft chapters, build the guide, and keep continuity, the same way *Unwoven* was made.
