# Image Bible — Style Anchors & Rules

Covers visual style only. Character *facts* live in `characters.md`; this file covers how they (and the world) should *look*.

---

## Format
Graphic-novel / comic-style illustrated plates, one image per chapter "beat" (per the framework: never two images adjacent — text separates every plate).

## Workflow

**Primary tool: ChatGPT**, using the same method that worked for *Unwoven*: a dedicated project, project memory, uploaded reference images, and detailed per-image prompts. That combination is what's actually carrying consistency here — not any single prompt — so the practical steps are:

1. Create a project for this book (separate from any other project, so memory doesn't cross-contaminate).
2. Generate each character's anchor reference image first (prompts below), upload it into the project once you're happy with it, and treat it as the visual source of truth going forward.
3. For every later image involving that character, reference the uploaded image directly (attach it or point to it) rather than relying on memory alone — memory helps with narrative/style consistency, but attaching the actual reference image is what keeps faces and outfits from drifting.
4. Keep prompts detailed and consistent in wording across sessions — reuse the same descriptive phrases from this file rather than re-describing characters freeform each time, since consistent language helps the model latch onto the same mental image.
5. When a generation drifts (happens most often after several images in a row), re-anchor by re-attaching the original reference image rather than trying to prompt your way back.

## Style anchors

- **Overall style:** warm painterly-cartoon hybrid — painted texture and rich color like a storybook illustration, but with expressive, slightly exaggerated proportions and poses so physical comedy reads clearly. Not flat vector cartoon; not photoreal.
- **Color palette / mood:** warm, saturated, slightly exaggerated — greens/golds/browns for Sherwood, warm firelight tones for camp scenes, cooler stone tones reserved for Nottingham/authority spaces to contrast against the crew's warmth.
- **Line/rendering approach:** visible painterly brushwork, soft edges rather than hard vector outlines, expressive faces that can carry big comedic reactions.

**Base style phrase** (include in every reference and plate prompt, worded consistently each time):
*"warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone"*

**Aspect ratios:**
- **Chapter plates** (what actually goes in the book): **3:2** — this is what the reader displays, so all final `chN_plate_M_name.jpg` images must be generated/cropped to 3:2. Specify "3:2 landscape aspect ratio" in the prompt, or crop after generation if the tool doesn't hit it reliably.
- **Character portrait refs** (`NAME_ref_bg_01.png`): a portrait/vertical framing (e.g. 2:3) is fine — these are working references, not plates, so they don't need to match the reader's aspect ratio.
- **Character habitat refs / location refs**: generate at 3:2 to match, since these are closer in framing to what an actual plate looks like and you may end up using one directly or near-directly as a plate.

---

## Character visual references

Draft physical descriptions below — please correct anything that's off; these lock in once approved. Convention: `NAME_ref_bg_01.png` (portrait/bust reference), `NAME_ref_hab_01.png` (habitat/setting reference). **In practice, `NAME` is the character's name in all-caps with no separators between words** (e.g. `LONGJOHNLITTLE`, `MASTERTHISTLEWOOD`, `AGNESHALE`) — match this exact style for any new reference images so filenames stay consistent across the whole set.

**Note on backgrounds:** `bg` (portrait) refs use a plain neutral gray studio background deliberately — it isolates the character so nothing about a background style leaks into your read of the face/costume when comparing generations, and it's cleaner to attach as a reference for later scenes. `hab` (habitat) refs keep a real environment, since those exist specifically to test the character in context.

### Robin of Loxby
Late 20s, lean but not imposing — his build undercuts the "hero" expectation. Sandy/tousled brown hair, an earnest open face, slightly too-big hand-me-down leather jerkin, a bow he clearly hasn't mastered slung crookedly across his back. Expression default: hopeful determination, often about to go slightly wrong.
- **Prompt (bg):** *"Portrait of a lean, earnest young man in his late 20s, tousled sandy brown hair, hopeful determined expression, wearing an ill-fitting hand-me-down leather jerkin, a bow slung crookedly across his back, medieval Sherwood forest archer. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same young man standing in a sun-dappled Sherwood forest clearing, crooked practice arrows stuck in a badly-missed target nearby. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

### Long John Little
Enormous — head and shoulders above everyone, broad but soft-featured, not sculpted-muscular. Big worried eyes, a gentle round face that doesn't match his size at all. Patchy leather armor clearly resized/handed down, probably doesn't fit.
- **Prompt (bg):** *"Portrait of an enormous, gentle-faced man, towering height, broad soft build, big worried kind eyes, wearing ill-fitting patchy leather armor, medieval forest setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same giant man ducking through low forest branches, visibly too big for his surroundings, comedic sense of scale. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

### Will Scarlett-Sleeves
Mid-20s, conventionally handsome and knows it, mid-length dark hair styled carefully despite forest living. One genuinely fine red/scarlet sleeve or garment he's absurdly protective of amid otherwise scruffy travel clothes. Expression default: pleased with himself, often at the worst moment.
- **Prompt (bg):** *"Portrait of a vain, handsome young man in his mid-20s, carefully styled dark hair, wearing one fine scarlet sleeve or garment amid otherwise scruffy travel clothes, self-satisfied expression, medieval forest rogue. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same young man admiring his reflection in a puddle or blade, oblivious to a visible danger just behind him. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

### Brother Crumb
Stout, round-bellied friar, tonsured hair, simple brown robes with visible food stains, rosy cheeks, perpetually holding or reaching for food. Warm, sleepy, contented expression even in danger.
- **Prompt (bg):** *"Portrait of a stout, jolly friar, tonsured hair, round rosy face, simple brown robes with food stains, holding a meat pie, contented sleepy expression, medieval setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same friar napping against a tree with a half-eaten feast beside him, comedic chaos happening unnoticed in the background. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

### Marian Fletcher
Late 20s, sharp intelligent eyes, practical clothing (no frills, ready to move), hair pulled back functionally. The most put-together silhouette in the group — everyone else is slightly disheveled, she isn't. Default expression: exasperated competence.
- **Prompt (bg):** *"Portrait of a sharp, practical young woman in her late 20s, hair pulled back functionally, plain sturdy medieval traveling clothes, exasperated competent expression. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same woman calmly redirecting chaos around her while the rest of the group flails, medieval forest camp setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

### Master Thistlewood
Older, fussy, robes that are trying too hard to look impressively wizardly and not quite managing (slightly askew hat, a robe hem that's fraying). Expressive eyebrows, perpetually exasperated-but-fond expression. Carries a staff he doesn't strictly need.
- **Prompt (bg):** *"Portrait of an older, fussy wizard, expressive eyebrows, slightly askew pointed hat, elaborate but slightly frayed robes, carrying a staff, exasperated but fond expression, medieval fantasy setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same wizard watching from hidden concealment — behind a tree or in a window — mid a small, secretive magical gesture, unnoticed by others. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

### Pip
19, but reads younger — slight build, cropped or tucked-up hair, dressed as a boy (loose tunic, practical trousers, a cap). Sharp, watchful eyes that suggest more awareness than her apparent age. Default expression: quietly amused, like she's in on a joke no one else can see.
- **Height note:** "reads younger" should come from build (slight, wiry) and face, **not from being short or child-sized**. She needs to be tall enough to pass convincingly as an adolescent boy (early-to-mid teens in apparent age, not a young child) and to physically hold her own fighting alongside Thistlewood, as established on-page in Ch6 ("moved through the chaos like she'd been doing it her whole life"). Aim for a lean, average-for-a-teenager height — noticeably smaller than the adult men in the cast, but not dramatically so.
- **Prompt (bg):** *"Portrait of a slight, wiry young person of teenage height (not a young child), androgynous boyish clothing, cropped or tucked-up hair under a cap, sharp watchful amused eyes, a lean build rather than a small one, medieval fantasy assistant. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same lean, teenage-height young person perched on a windowsill or fence, half-hidden, quietly watching events unfold with a knowing smile. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

---

## Antagonist visual references

Same convention as the crew: `NAME_ref_bg_01.png` (portrait) / `NAME_ref_hab_01.png` (habitat). Visually, antagonists should lean into the cooler stone-toned palette reserved for Nottingham/authority spaces (see Style anchors above), to read as visually distinct from Sherwood's warmth even before any dialogue.

### The Sheriff of Nottingham
Middle-aged, self-important bearing that reads as slightly too puffed-up for his actual authority — a man who thinks he looks commanding and doesn't quite. Elaborate, fussy official regalia (a chain of office, an overly large hat/badge of rank) slightly too ornate for a provincial sheriff, hinting at vanity and overreach. Sharp calculating eyes undercut by a perpetually reddening, apoplectic face — he's always one setback from a furious outburst. Default expression: smug certainty right before it curdles into rage.
- **Prompt (bg):** *"Portrait of a middle-aged, self-important medieval sheriff, puffed-up commanding bearing that doesn't quite land, elaborate fussy official regalia with an oversized chain of office, sharp calculating eyes, a perpetually reddening face on the edge of temper, smug certain expression. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same sheriff mid-tantrum in a Nottingham courtyard or hall, an elaborate scheme visibly falling apart around him, guards looking away in secondhand embarrassment. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio, cooler stone-toned palette."*

### One-off episode antagonists
No standing reference needed until one is introduced — generate a reference image for a one-off antagonist only if a chapter's threat turns out to recur or matters for later continuity (per `characters.md`).

---

## Supporting recurring cast visual references

### Abbot Percival
Elderly, portly, dressed in proper monastic robes (a visual contrast to Brother Crumb's scruffier version of the same). Perpetually disappointed expression, hands often clasped in a way that reads as patient exasperation rather than anger. Not a threat visually — should read as harmless and a little pitiable, not intimidating.
- **Prompt (bg):** *"Portrait of an elderly, portly abbot in proper formal monastic robes, perpetually disappointed but gentle expression, hands clasped patiently, medieval setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same abbot standing in an abbey doorway or courtyard, arms crossed, watching Brother Crumb's antics from a distance with weary disapproval. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

### Ferret Tam
Wiry, shifty-eyed, quick movements, dressed in mismatched secondhand clothes with lots of hidden pockets. A permanent expression of nervous calculation — always in the middle of a deal that might or might not go well. Not menacing, just twitchy and transactional.
- **Prompt (bg):** *"Portrait of a wiry, shifty-eyed medieval trader/fence, quick nervous energy, mismatched secondhand clothing with visible hidden pockets, an expression of nervous calculation. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same wiry trader haggling in a crowded medieval market stall, surrounded by a chaotic assortment of dubious goods. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

### Agnes Hale
Sturdy, practical, weathered from farm work — sleeves rolled up, hair tied back out of the way, the build of someone used to physical labor rather than a delicate storybook peasant. Expression default: fierce and unimpressed, arms crossed or hands on hips, ready to argue with anyone including the person who just "helped" her.
- **Prompt (bg):** *"Portrait of a sturdy, weathered village woman, practical clothing with sleeves rolled up, hair tied back, arms crossed, fierce unimpressed expression, medieval farm setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same woman standing protectively in front of her home or cart, chin raised, radiating 'don't test me' energy. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

### Wat Hale
A scrappy village boy of about 9, patched practical clothes, quick and wiry rather than sturdy, an expression that's equal parts mischievous and street-smart-beyond-his-years. Always looks like he's about to seize an opportunity before anyone notices it's there.
- **Prompt (bg):** *"Portrait of a scrappy medieval village boy, about 9 years old, patched practical clothes, quick wiry build, mischievous street-smart expression, medieval setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same boy mid-dash, clutching some reclaimed household object triumphantly, darting through a village scene. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

---

## Animal Cast visual references

Same convention: `NAME_ref_bg_01.png` (portrait) / `NAME_ref_hab_01.png` (habitat).

### Gideon (the goat)
Sturdy farm goat, otherwise ordinary-looking — the comedy is in the expression range, not the design. Default calm, level expression; needs a second "trigger" expression option (sudden bellicose glare, lowered head as if about to charge) for the temper-flip gag.
- **Prompt (bg):** *"Portrait of a sturdy farm goat with a calm, level, faintly wise expression, ordinary realistic goat features, medieval farm setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same goat mid-temper-flip, head lowered and glaring with sudden bellicose intensity, a stark contrast to a level-headed default demeanor, comedic framing. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

### Grimalkin ("Grim") — the tomcat
Lean old tomcat, battle-worn (a notched ear, a slightly ragged coat), half-lidded permanently unimpressed eyes. Default expression: pure deadpan disdain — until Marian is involved, when his posture visibly softens.
- **Prompt (bg):** *"Portrait of a lean, old, battle-worn tomcat, notched ear, slightly ragged coat, half-lidded unimpressed deadpan expression, medieval setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same tomcat perched watchfully nearby Marian Fletcher, visibly more relaxed and attentive toward her than his usual aloof demeanor, medieval forest camp setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

### Barley (the dog)
Young, scruffy medium-sized mutt, floppy ears, an expression permanently poised between hope and overexcitement. Default pose: alert, ready to launch toward literally anything — food, attention, danger, all treated with equal enthusiasm.
- **Prompt (bg):** *"Portrait of a young scruffy medium-sized mixed-breed dog, floppy ears, an expression of eager hopeful overexcitement, medieval setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same dog mid-leap or mid-dash toward some minor stimulus — a dropped scrap of food, a raised hand — with wildly disproportionate enthusiasm. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*



Convention: `LOCATION_ref_01.png` (establishing/wide reference), additional numbered variants for different angles or times of day as needed. Generate at **3:2 landscape aspect ratio** to match the reader's plate format.

### Sherwood Camp (the crew's hideout)
Lived-in forest clearing, patched tents/lean-tos, a central fire pit, mismatched furniture clearly scavenged/stolen, laundry strung between trees — cozy and a little chaotic, warm firelight tones.
- **Prompt:** *"A lived-in forest hideout clearing, patched tents and lean-tos, a central campfire, mismatched scavenged furniture, laundry lines strung between trees, warm golden late-afternoon light, medieval Sherwood forest. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*

### Nottingham (town/market)
Timber-framed medieval town, market stalls, cobbled streets, cooler stone tones contrasted against the forest's warmth, a sense of watchful authority (guards, banners) without being oppressive/grim.
- **Prompt:** *"A medieval timber-framed market town, cobbled streets, market stalls, banners, watchful guards in the background, cooler stone tones, bustling but slightly tense atmosphere. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*

### Thistlewood's Dwelling
A modest cottage or tower that's messier/more cluttered than grand — books, half-finished magical tinkering, evidence of Pip's presence (a second cot, boyish clothes drying), a bit more magical glow/detail than the rest of the world.
- **Prompt:** *"A cluttered wizard's cottage interior, overflowing bookshelves, half-finished magical apparatus, warm magical glow, lived-in and slightly messy rather than grand, medieval fantasy setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*

### Loxby Manor (Robin's father's home)
Robin's father is alive but off-page (locked in `story-bible.md`) — he may send word or act through the debt-chain without appearing on-page, so the manor itself may still show up (a letter arriving from it, a messenger leaving it) even without him in frame. Modest gentry manor, not grand nobility — respectable but a little worn, reflecting a family that's seen better days. Warm but slightly melancholy compared to Sherwood's chaotic warmth — quieter, emptier.
- **Prompt:** *"A modest medieval gentry manor house exterior, respectable but slightly worn and faded, quiet and somewhat empty grounds, warm but melancholy late-afternoon light. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*

### The Sheriff's Keep (interior)
The Sheriff's home turf for scheming — distinct from the general Nottingham town/market reference. A stone great hall or private chamber, trying hard to look imposing (banners, an oversized chair/throne-like seat) but slightly overdone/gaudy in a way that undercuts him, consistent with his character. Cooler stone tones, more shadow than Sherwood or the manor.
- **Prompt:** *"A medieval stone great hall or private chamber, trying too hard to look imposing — banners, an oversized ornate chair, slightly gaudy overdone decor that undercuts its own grandeur. Cooler stone tones, more shadow and less warmth than a forest setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*

### The Abbey (Brother Crumb's order)
A modest, quiet monastery — plain stone, orderly gardens, a sense of calm and discipline that stands in gentle comedic contrast to Crumb's chaotic life with the crew. Not grim or oppressive, just very orderly and a little dull — visually the "straight life" Crumb left behind.
- **Prompt:** *"A modest medieval abbey exterior, plain stone architecture, orderly quiet gardens, calm disciplined atmosphere, soft overcast or gentle daylight. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*

*(Add more locations here as chapters introduce them.)*

## Cover image

`manifest.json` points to `images/RobinHoodCover.jpg`. Suggested approach: a group shot of the crew (Robin, Long John Little, Will Scarlett-Sleeves, Brother Crumb, Marian) in the Sherwood Camp setting, energetic and a little chaotic — capturing the "lucky bumblers" tone at a glance. Thistlewood and Pip are deliberately **not** in a cover group shot (they're the secret) — the cover should represent what the crew looks like to the world, not the hidden hand behind them.
- **Prompt:** *"A group of five medieval outlaws — an earnest young archer, a gentle giant, a vain sharply-dressed young man, a stout jolly friar, and a sharp practical young woman — caught mid-chaos in a sunlit Sherwood forest clearing, energetic and slightly disheveled, warm golden light. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide book-cover composition, 2:3 portrait aspect ratio, room at the top for a title."*

Once you have a cover you like, update `manifest.json`'s `cover.title` and `cover.author` fields (currently placeholders) to match.

## Guide images

`guide.json` entries reference images via a path relative to `images/guide/` (both the live reader and `build.py` always prefix `images/guide/` onto whatever's in the `img` field). To reuse an existing character reference image **without duplicating the file**, point `img` at it with a `../` prefix — e.g. `"img": "../robin_ref_bg_01.png"` resolves to `images/robin_ref_bg_01.png`, one folder up from `images/guide/`. This has been verified to work both in the live hosted reader and in `build.py`'s offline bundling (plain filesystem/URL path traversal, no special handling needed). Match the exact filename and casing of whatever you actually named the reference image — filenames are case-sensitive once hosted. Missing/mistyped paths degrade gracefully to a decorative tile per the framework, so a typo won't break the guide, just silently lose the image.

## Plate naming convention
`chN_plate_M_name.jpg` — chapter N, plate M, short descriptive name.

## Rules
- sRGB only (web needs sRGB; Rec.2020 renders wrong — use `checkprofiles.py` to check).
- Keep comedic beats visually legible — the humor should read even as a thumbnail (this is a fast-paced comedy; avoid overly busy/cluttered compositions on the panels carrying jokes).
