# FOR_CLAUDE — Instructions for Claude when starting a new book on this framework

**Read this first when the user says they want to begin a new illustrated serial book using this framework.** It tells you what the framework is, how its files fit together, and the working method that produced the first book (*Unwoven*) successfully. Follow it so you can pick up quickly and help the user draft, build, and maintain a new project.

---

## What this framework is

A content-driven web reader for an **illustrated serial book**. The reader (`index.html`) is generic; a book is defined entirely by data files and images. Your job is to help the user produce those data files (chapters, guide, manifest) and images-workflow, not to rewrite the engine.

### File map
- `index.html` — generic reader engine. **Do not add story content here.** Re-theme CSS only if asked.
- `manifest.json` — `{ title, cover{image,title,author,tagline}, chapters:[...] }`. The `chapters` array is reading order (filenames without `.json`).
- `chapters/chN.json` — one per chapter. Shape:
  `{ "eyebrow": "...", "title": "...", "sequence": [ {"image": "path", "_describe": "prompt/notes"}, {"text": ["para", ...]}, ... ] }`
  - Entries interleave in listed order. Each entry is EITHER `image` OR `text` (array of paragraphs).
  - Never place two `image` entries adjacent; separate plates with text.
  - Any field beginning with `_` (e.g. `_describe`) is IGNORED by the reader — use `_describe` to store the image-generation prompt beside its plate.
- `guide.json` — `{ title, intro, sections:[ {heading, entries:[ {name, kind, img?, blurb, say?} ]} ] }`. Spoiler-free. `img` refers to a file in `images/guide/` (filename only). Missing/absent images degrade gracefully to a decorative tile.
- `images/` (chapter plates + cover), `images/guide/` (guide images).
- `build.py` — bundles chapters + cover + guide (with images embedded as downscaled data-URIs) into `build/book.html` for offline reading. Placeholders `BUNDLE_PLACEHOLDER` and `GUIDE_PLACEHOLDER` in index.html must remain for build.py to work.
- `checkprofiles.py` — flags non-sRGB images. Web needs sRGB; Rec.2020 renders wrong.

### How the reader loads (so you reason about it correctly)
- Hosted: fetches `manifest.json`, each `chapters/*.json`, and `guide.json` live.
- Offline (`file://`): uses data baked in by `build.py` (`BUNDLED_DATA`, `BUNDLED_GUIDE`).
- So: adding a chapter = write `chapters/chN.json` + add `"chN"` to manifest. Rebuild for offline.

---

## Images are the USER's job, via a separate tool

The user generates images themselves (for *Unwoven*, in ChatGPT) from: (a) the per-plate `_describe` text in the chapter JSON, (b) a reference-image library for character/style consistency, and (c) an "image bible" of style anchors and rules. **You do not generate final images.** You DO write clear `_describe` prompts in each plate, and you can help maintain the image bible and reference conventions. Expect image filenames to follow a convention like `NAME_ref_bg_01.png` (portrait) / `NAME_ref_hab_01.png` (habitat); plates like `chN_plate_M_name.jpg`.

---

## The working method that succeeded (use it again)

1. **Q&A-first drafting.** Before drafting any chapter, surface 2–4 concrete structural decisions as explicit, mutually-exclusive choices for the user to answer (POV anchor, how a climax stages, where the chapter ends, whether a beat lands here or later). Draft only AFTER they answer. This keeps the user in authorial control and prevents wasted drafting. Use the interactive choice tool when available.
2. **Draft to the answers**, in the book's established voice. Then **revise against the user's feedback** — their corrections are authoritative, always. Don't defend drafts.
3. **Deliver each chapter as both** a readable prose draft (`chapterN_draft.md`) AND the built `chN.json` with a plate sequence and `_describe` prompts. Validate JSON; check no two plates are adjacent.
4. **Guard continuity.** Maintain a story bible and (authoritative) character docs. Character facts (esp. genders) live in the user's character docs; the bible defers to them. Watch for drift — a pronoun-consistency scanner (`check_pronouns.py`) exists as a pattern; flags are candidates to READ, not verdicts.
5. **Keep sources non-overlapping** to prevent drift: character identity in character docs; plot/structure/continuity in the story bible; system/build facts in an architecture doc; image rules in the image bible.

## Content & safety norms carried from the first book
- Written to be readable by a wide audience (the first book was written with the user's elderly mother as a chapter-by-chapter reader) — keep violence non-graphic; power through restraint, not gore.
- Honesty about AI involvement: if the user publishes, help them disclose AI-assisted text and AI-generated images plainly.

## Practical build/deploy reminders to give the user
- sRGB images only; filenames are case-sensitive when hosted (Windows hides this).
- After deploy, hard-refresh (Ctrl+Shift+R). The offline `book.html` is gitignored; regenerate with `build.py`.
- Commit just this framework folder to git; the dummy story is safe to replace and commit over.

---

## First moves when the user starts a new project
1. Ask the premise/world and the intended shape (how many chapters, tone, audience).
2. Set up `manifest.json` (title/author/cover/first chapters) and, with the user, the world's core canon (a short world + character doc) BEFORE drafting — this is the anti-drift foundation.
3. Establish the image conventions and an image-bible stub if the user wants illustrations.
4. Then begin chapter 1 with a Q&A session per the method above.
5. Replace the dummy `ch1/ch2.json` and `guide.json` as real content arrives; keep the dummy structure as a template reference until then.
