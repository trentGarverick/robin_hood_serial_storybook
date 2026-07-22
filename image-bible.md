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
- **Continuity note (Ch6):** sustained a serious side wound defending Wat Hale during the highwaymen raid. If any future plate shows him shirtless, bathing, or in a state of undress, include a healed scar on his side/torso for consistency.
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
**IMPORTANT — reveal-timing lock applies to appearance, not just plot:** until the actual wizard reveal (a future story), Thistlewood must look like an **entirely ordinary old man** — no robes, no pointed hat, no magical glow, no visible spellcasting. Plain, practical traveling clothes. His only "unusual" object is a plain gnarled wooden walking staff — an ordinary old man's walking stick, not a visibly magical one. Older, a little worn, expressive eyebrows, a fussy and particular manner that comes through in expression and posture, not costume. Default expression: exasperated but fond. **Do not generate him in wizard-coded clothing or mid-spellcast** — this would visually spoil what the text is carefully not confirming.
- **Prompt (bg):** *"Portrait of an ordinary elderly man, plain practical traveling clothes, no robes or wizard-coded costume, expressive eyebrows, a slightly fussy and particular bearing, carrying a plain gnarled wooden walking staff, medieval setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same ordinary-looking elderly man walking with his staff along a forest path, unremarkable and unhurried, nothing about his appearance suggesting anything unusual. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*
- **Future note (not yet):** once the actual reveal story happens, it may be worth generating a *second*, visibly wizardly reference set for post-reveal chapters. Don't create that yet — flagging it here so it isn't forgotten when the time comes.

### Pip
19, but reads younger — slight build, cropped or tucked-up hair, dressed as a boy (loose tunic, practical trousers, a cap). Sharp, watchful eyes that suggest more awareness than her apparent age. Default expression: quietly amused, like she's in on a joke no one else can see.
- **Height note:** "reads younger" should come from build (slight, wiry) and face, **not from being short or child-sized**. She needs to be tall enough to pass convincingly as an adolescent boy (early-to-mid teens in apparent age, not a young child) and to physically hold her own fighting alongside Thistlewood, as established on-page in Ch6 ("moved through the chaos like she'd been doing it her whole life"). Aim for a lean, average-for-a-teenager height — noticeably smaller than the adult men in the cast, but not dramatically so.
- **Prompt (bg):** *"Portrait of a slight, wiry young person of teenage height (not a young child), androgynous boyish clothing, cropped or tucked-up hair under a cap, sharp watchful amused eyes, a lean build rather than a small one, medieval fantasy assistant. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same lean, teenage-height young person perched on a windowsill or fence, half-hidden, quietly watching events unfold with a knowing smile. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

**⚠ USAGE RULE — read before generating any Pip plate:** as of Ch16, there are now **two** valid references for Pip, and using the wrong one in the wrong scene breaks the story's own reveal mechanics:
- **Disguised reference (above, `PIP_ref_bg_01.png`)** — use for **every scene where anyone other than Marian is present**, or any scene before Ch16. This is still her default, primary reference for the vast majority of plates.
- **True-appearance reference (below, new)** — use **only** for private Pip-and-Marian-alone scenes, from Ch16 onward (e.g. Ch16 Plates 2–5, and any future private conversation between just the two of them). If Robin, Will, Long John, Crumb, or anyone uninformed is in the frame, use the disguised reference instead, even after Ch16 — the disguise continues in front of everyone but Marian.

### Pip (true appearance — Marian-only private scenes, Ch16+)
Same person as the disguised reference above — same face, same sharp watchful eyes, same slight/wiry build and teenage-appropriate height. The only real change is the absence of performance: no cap, hair however she'd actually wear it day-to-day (kept practical/short-to-shoulder rather than a dramatic flowing change — this is a costume dropping, not a transformation), and a softer, more open posture/expression than her carefully-maintained boyish default.
- **Prompt (bg):** *"Portrait of the same slight, wiry young woman, 19 years old, teenage-appropriate height, no cap or disguise, practical hair worn naturally rather than tucked away, sharp watchful eyes now open and unguarded rather than performing, a softer more genuine expression than her usual careful default, medieval fantasy setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same young woman sitting quietly with another young woman (Marian Fletcher) in a moonlit forest clearing at night, a private and trusting atmosphere, cap resting beside her rather than worn. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio, soft moonlit nighttime lighting."*

---

## Antagonist visual references

Same convention as the crew: `NAME_ref_bg_01.png` (portrait) / `NAME_ref_hab_01.png` (habitat). Visually, antagonists should lean into the cooler stone-toned palette reserved for Nottingham/authority spaces (see Style anchors above), to read as visually distinct from Sherwood's warmth even before any dialogue.

### The Sheriff of Nottingham
**CORRECTED (post-Ch23) to match confirmed on-page characterization — the previous version below described a "pompous/bumbling" conception that was never actually used once he appeared on-page. If you generated a reference from the old prompt, it needs regenerating.** Middle-aged, controlled and composed rather than puffed-up — restrained, well-tailored rather than gaudy (contrast Vane's ostentation), the quiet authority of a man who doesn't need to raise his voice. Calm, watchful eyes. Default expression: unhurried, faintly appraising, giving little away. His one visual "tell": when frustrated, a small tightening at the corner of his jaw — subtle, not a broad grimace or reddening face.
- **Prompt (bg):** *"Portrait of a middle-aged, composed medieval sheriff, restrained well-tailored clothing (not gaudy or overly ornamented), calm watchful eyes, an unhurried faintly appraising expression that gives little away, quiet authority rather than bluster. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same sheriff seated in a formal stone hall, unhurried and composed, studying someone standing before him with calm unreadable attention. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio, cooler stone-toned palette."*

### One-off episode antagonists
No standing reference needed until one is introduced — generate a reference image for a one-off antagonist only if a chapter's threat turns out to recur or matters for later continuity (per `characters.md`). **Exception in practice:** a one-off antagonist central to a multi-chapter story (like Vane in "The Weaver's Debt," Story 2) still needs a reference for consistency across that story's own chapters, even if he won't appear again afterward.

### Ellen (Story 3 — "The Devil's Own Luck")
Woman in her middle years, work-roughened hands from weaving, an exhaustion she carries carefully rather than dramatically. Practical clothes, no-nonsense bearing — someone who's used to managing hardship quietly rather than complaining about it.
- **Prompt (bg):** *"Portrait of a middle-aged weaver woman, work-roughened hands, practical clothing, an expression of carefully-carried exhaustion and quiet determination, medieval setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same woman arriving at a forest camp with two boys, urgency and hope in her posture. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

### Vane (Story 2 — "The Weaver's Debt")
Prosperous tax farmer, new money rather than old aristocracy — well-fed, well-groomed, fine but slightly gaudy clothing that reads as trying too hard to look important. An ostentatious accessory (a large signet ring, an overly ornate chain) signals his bought status rather than inherited one. Smug, calculating expression — a man confident he's untouchable.
- **Prompt (bg):** *"Portrait of a prosperous middle-aged tax farmer, well-fed and well-groomed, fine but slightly gaudy clothing, an ostentatious signet ring, smug calculating expression, medieval setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same man in a proud, slightly overdecorated manor house study, counting coin at a desk, self-satisfied. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio, cooler stone-toned palette."*

### Captain Rowena Blackwood (Story 5 — "The Sheriff's Reckoning")
**Recurs across a 7-part story — reference is essential.** A genuine soldier, deliberately visually distinct from every antagonist so far: plain, functional armor with no ornamentation (contrast Vane's gaudiness), upright bearing, sharp watchful eyes. Middle-aged, weathered from real campaigns rather than soft living. Default expression: calm, alert, giving nothing away — competence rather than menace.
- **Prompt (bg):** *"Portrait of a middle-aged female soldier, plain functional armor with no ornamentation, upright disciplined bearing, sharp watchful eyes, weathered from real campaigns, calm alert expression giving nothing away, medieval setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same soldier at the head of a disciplined military column, giving orders, soldiers moving with crisp coordinated precision around her. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio, cooler stone-and-steel toned palette."*

### Witchfinder Josiah Crane (Story 5 — "The Sheriff's Reckoning")
**Recurs across the rest of this story — reference is essential.** A third, deliberately distinct visual flavor: spare, unremarkable, plain dark clothes (not military like Blackwood, not gaudy like Vane) — deliberately forgettable-looking, someone who blends into a village crowd. Small, careful hands (always shown with a notebook). Default expression: patient, unhurried, giving nothing away — calm in a way that reads as unsettling rather than reassuring once you notice it.
- **Prompt (bg):** *"Portrait of a spare, unremarkable middle-aged man in plain dark clothes, deliberately forgettable appearance, small careful hands holding a notebook, a patient unhurried expression that reads as quietly unsettling, medieval setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same man seated with patient stillness in a village square, taking careful notes while listening to a villager, a small crowd gathered around. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

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

### Tom Weaver
**Story 2 character — recurs across all 3 parts of "The Weaver's Debt," so a reference is warranted despite being a single-story character.** Middle-aged, lean/wiry build from detail work rather than heavy labor, weathered hands, a leather work-apron over simple practical clothes. Careworn, quietly proud expression — a man used to being steady for his son's sake even when things are bad.
- **Prompt (bg):** *"Portrait of a middle-aged weaver, lean wiry build, weathered hands, leather work apron over simple practical clothes, careworn but quietly proud expression, medieval setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same man standing at a wooden loom in a small modest home workshop, a folded official notice visible on a table nearby. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

### Hob Weaver
**Story 2 character — recurs across all 3 parts.** About 9, Wat Hale's friend — deliberately distinct from Wat visually (lighter/sandier hair, a more earnest and worried default expression rather than Wat's mischievous energy). Simple practical clothes with a hint of his father's craft (a woven scarf or patched cloth).
- **Prompt (bg):** *"Portrait of an earnest medieval village boy, about 9 years old, sandy or light brown hair, simple practical clothes with a woven scarf, worried but determined expression, medieval setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same boy running urgently through a village, out of breath, clear determination on his face. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

---

## Animal Cast visual references

Same convention: `NAME_ref_bg_01.png` (portrait) / `NAME_ref_hab_01.png` (habitat).

### Gideon (the goat)
Sturdy farm goat, otherwise ordinary-looking — the comedy is in the expression range, not the design. Default calm, level expression; needs a second "trigger" expression option (sudden bellicose glare, lowered head as if about to charge) for the temper-flip gag.
- **Size note (fixes inconsistent scale across generations):** full-grown adult goat, **roughly waist-to-chest height on a standing adult human at the shoulder** (approximately 30–34 inches / 75–85cm at the shoulder) — a substantial dairy-goat build (think Nubian or Alpine breed), not a small pygmy/dwarf goat. This size is load-bearing for the story: he's knocked full-grown men off their feet with headbutts (Ch7, Ch12) and reaches up to chew at Will's sleeve while standing on all fours. Always specify this size explicitly in the prompt — don't rely on "sturdy farm goat" alone, which is too vague and has produced inconsistent results.
- **Prompt (bg):** *"Portrait of a large, sturdy adult farm goat (Nubian or Alpine build, roughly 32 inches/80cm at the shoulder — substantial, not a small pygmy goat), a calm, level, faintly wise expression, ordinary realistic goat features, medieval farm setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Portrait framing, plain neutral gray studio background."*
- **Prompt (hab):** *"The same large, sturdy adult goat (roughly 32 inches/80cm at the shoulder, substantial dairy-goat build) mid-temper-flip, head lowered and glaring with sudden bellicose intensity, a stark contrast to a level-headed default demeanor, comedic framing. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide shot, 3:2 landscape aspect ratio."*

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
**Reveal-timing lock applies here too:** an eccentric old scholar's cottage, not a "wizard's cottage." No magical glow, no visible magical apparatus. Per the actual on-page description (Ch7): shelves stacked two deep with books, herbs drying in bundles from every beam, and a clutter that reads as careful rather than chaotic — "the specific disorder of a man who knew exactly where everything was." Cozy, lived-in, a little cramped, with a yard containing one crooked apple tree (where the animals convene). Warm and welcoming rather than mysterious.
- **Prompt:** *"A cluttered but carefully-organized old scholar's cottage interior, shelves stacked two deep with books, herbs drying in bundles from the beams, warm and cozy rather than mysterious, no magical or supernatural elements visible, lived-in medieval fantasy setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*
- **Yard variant prompt:** *"A cozy cottage yard with one crooked apple tree, a vegetable patch, modest and lived-in, warm late-afternoon light. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*

### Loxby Manor (Robin's father's home)
Robin's father is alive but off-page (locked in `story-bible.md`) — he may send word or act through the debt-chain without appearing on-page, so the manor itself may still show up (a letter arriving from it, a messenger leaving it) even without him in frame. Modest gentry manor, not grand nobility — respectable but a little worn, reflecting a family that's seen better days. Warm but slightly melancholy compared to Sherwood's chaotic warmth — quieter, emptier.
- **Prompt:** *"A modest medieval gentry manor house exterior, respectable but slightly worn and faded, quiet and somewhat empty grounds, warm but melancholy late-afternoon light. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*

### The Sheriff's Keep (interior)
**CORRECTED (post-Ch23) to match confirmed on-page characterization** — the version below described a "trying too hard / gaudy" conception matching the old pompous-Sheriff planning note, which was never actually used once he appeared on-page (see his own corrected entry above). The Sheriff's home turf for scheming — distinct from the general Nottingham town/market reference. A stone great hall or private chamber that reflects restrained, deliberate authority rather than showy grandeur — good materials, well-kept, but nothing ostentatious. Cooler stone tones, more shadow than Sherwood or the manor, but composed rather than overdone.
- **Prompt:** *"A medieval stone great hall or private chamber, restrained and deliberate rather than showy — good materials, well-kept, quietly authoritative without being ornate or overdone. Cooler stone tones, more shadow and less warmth than a forest setting. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*

### The Abbey (Brother Crumb's order)
A modest, quiet monastery — plain stone, orderly gardens, a sense of calm and discipline that stands in gentle comedic contrast to Crumb's chaotic life with the crew. Not grim or oppressive, just very orderly and a little dull — visually the "straight life" Crumb left behind.
- **Prompt:** *"A modest medieval abbey exterior, plain stone architecture, orderly quiet gardens, calm disciplined atmosphere, soft overcast or gentle daylight. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*

### Hale Village
Small, modest farming village — Agnes and Wat Hale's home. Recurred twice now (Ch1's tax seizure, Ch6's highwaymen raid), and flagged as a possible recurring beneficiary location. Humble timber-and-thatch cottages, a central square/market area, unpretentious and a little worn, warm and human-scaled rather than picturesque.
- **Prompt:** *"A small modest medieval farming village, humble timber and thatch cottages, a central square, unpretentious and lived-in, warm human-scaled atmosphere. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*

### Vane's Manor House (Story 2 — "The Weaver's Debt")
A manor house its owner is very proud of, and it shows — new money trying to look like old money, slightly overdone. Grander than Loxby Manor but gaudier, less tasteful. This is the heist target for Part Two. Cooler stone tones, ornate but a little tacky.
- **Prompt:** *"A grand but slightly gaudy medieval manor house exterior, new-money trying to look like old-money, overly ornate details that undercut its own elegance. Cooler stone tones. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*

### Ashcombe (Story 3 — "The Devil's Own Luck")
Another small, modest town — similar scale to Hale Village but distinct, its own identity rather than a repeat. Worn down by direct taxation from the Sheriff's own deputies (no middleman this time). Humble, a little threadbare, proud people bearing a hard season.
- **Prompt:** *"A small modest medieval town, humble timber buildings, worn but proud, a sense of quiet hardship rather than despair. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide establishing shot, 3:2 landscape aspect ratio."*

*(Add more locations here as chapters introduce them.)*

## Cover image

`manifest.json` points to `images/RobinHoodCover.jpg`. Suggested approach: a group shot of the crew (Robin, Long John Little, Will Scarlett-Sleeves, Brother Crumb, Marian) in the Sherwood Camp setting, energetic and a little chaotic — capturing the "lucky bumblers" tone at a glance. Thistlewood and Pip are deliberately **not** in a cover group shot (they're the secret) — the cover should represent what the crew looks like to the world, not the hidden hand behind them.
- **Prompt:** *"A group of five medieval outlaws — an earnest young archer, a gentle giant, a vain sharply-dressed young man, a stout jolly friar, and a sharp practical young woman — caught mid-chaos in a sunlit Sherwood forest clearing, energetic and slightly disheveled, warm golden light. Warm painterly storybook illustration style, expressive and slightly exaggerated proportions, rich saturated color, soft painterly brushwork, comedic tone. Wide book-cover composition, 2:3 portrait aspect ratio, room at the top for a title."*

Once you have a cover you like, update `manifest.json`'s `cover.title` and `cover.author` fields (currently placeholders) to match.

## Guide images

`guide.json` entries reference images via a path relative to `images/guide/` (both the live reader and `build.py` always prefix `images/guide/` onto whatever's in the `img` field). To reuse an existing character reference image **without duplicating the file**, point `img` at it with a `../` prefix — e.g. `"img": "../ROBIN_ref_bg_01.png"` resolves to `images/ROBIN_ref_bg_01.png`, one folder up from `images/guide/`. This has been verified to work both in the live hosted reader and in `build.py`'s offline bundling (plain filesystem/URL path traversal, no special handling needed). Match the exact filename and casing of whatever you actually named the reference image — filenames are case-sensitive once hosted. Missing/mistyped paths degrade gracefully to a decorative tile per the framework, so a typo won't break the guide, just silently lose the image.

## Plate naming convention
`chN_plate_M_name.jpg` — chapter N, plate M, short descriptive name.

## Rules
- sRGB only (web needs sRGB; Rec.2020 renders wrong — use `checkprofiles.py` to check).
- Keep comedic beats visually legible — the humor should read even as a thumbnail (this is a fast-paced comedy; avoid overly busy/cluttered compositions on the panels carrying jokes).
