# Voice Guide — Narrative Style & Slang Conventions

Covers prose voice and invented in-world language. Character facts live in `characters.md`; plot/continuity in `story-bible.md`; this file covers *how the words sound*.

---

## Narrative voice

Target: **Terry Pratchett-esque** — a dry, omniscient narrator who treats absurd things with total deadpan seriousness and ordinary things with mock-epic grandeur; wry asides; a fondness for taking an idiom or assumption literally and following it to its logical (ridiculous) conclusion; affection for its characters even while gently mocking them.

**What to borrow from Pratchett:**
- The narrator is a character in its own right — opinionated, funny, occasionally addresses the absurdity of events directly rather than playing them straight.
- Comic escalation through specificity — a joke lands harder with a precise, deadpan detail than a vague one.
- Undercutting grandeur — introduce something as though it's terribly important, then puncture it.
- Affection underneath the mockery — the narrator likes these people, even while laughing at them.

**What NOT to borrow:** Discworld-specific devices (Death speaking in caps, footnotes as a structural device — this reader has no footnote mechanism, so any "footnote-style" aside needs to live in the main prose, parenthetically or as its own short sentence, not as an actual footnote), any of Pratchett's actual invented terminology or named entities (that's his IP, not ours to reuse) — we're borrowing a *voice*, not his specific bits.

**Sample paragraph** (draft, for your reaction — not from any real chapter):

> Robin of Loxby had been practicing his aim for the better part of two years, which is to say he had been *missing* things for the better part of two years, with a dedication that in any other pursuit would have been called stubbornness and in this one was generously called practice. The target — a sack of straw wearing, for reasons no one now remembered, an old boot on top — had survived every single one of his arrows so far, and had begun, in the manner of things that survive long enough, to develop something like an attitude about it.

---

## Slang: "Cant" convention

Invented medieval-flavored rhyming slang (in the spirit of Cockney rhyming slang, not historically real) used by common folk throughout Sherwood/Nottingham. **Robin never understands it** — a running gag across the whole book, not just this story. In-world justification: Robin's upbringing as gentry (even estranged, even poor-ish) kept him just far enough from common life that he never picked up the local cant, and it shows every time.

**Convention:** a rhyming phrase substitutes for the intended word (the phrase's last word rhymes with the meaning); often the phrase gets shortened in casual use. Someone (usually whoever's nearby — Marian, Will, or Long John are the most fluent) has to translate for Robin, and reacts with mild disbelief that he still doesn't know this one either.

**Starter glossary** (draft — add more as chapters need them):

| Cant phrase | Rhymes with / means | Example use |
|---|---|---|
| **pig in a poke** | *broke* (penniless) | "Can't buy you a round, mate, I'm pig-in-a-poke this week." |
| **hog in the mire** | *liar* | "Don't listen to him, he's a right hog in the mire." |
| **miller's thumb** | *dumb* (foolish) | "That was a proper miller's-thumb thing to do." |
| **friar's hood** | *good* | "How's the ale?" "Proper friar's-hood, that." |
| **bell and book** | *crook* (thief) | "Watch your purse, there's bell-and-books about." |
| **gallows tree** | *free* | "Prisoner's gallows now — they let him go." |
| **plough and cart** | *heart* | "Broke his plough-and-cart, she did." |
| **hound's tooth** | *truth* | "That's the hound's-tooth, I swear it." |
| **candle wax** | *tax* | "Can't pay the candle wax this month." |
| **crow's feet** | *fleet* (quick, fast) | "Ran off proper crow's-feet when he saw the guards." |
| **beggar's cloak** | *joke* | "Don't take it as a beggar's-cloak — I mean it." |
| **widow's mite** | *fright* | "Gave me a right widow's-mite, he did, jumping out like that." |
| **cooper's barrel** | *quarrel* (a fight/argument) | "Don't want no cooper's-barrel over a few coins." |
| **hangman's rope** | *hope* | "Not much hangman's-rope left for that plan, I'll be honest." |
| **shepherd's crook** | *took* (stole) | "Someone's shepherd's-crooked me purse!" |
| **tinker's dam** | *sham* (a fake) | "That relic's a proper tinker's-dam if ever I saw one." |
| **beadle's bell** | *tell* (inform, snitch) | "Don't go beadle's-belling to the Sheriff about this." |

**Guide convention:** `guide.json` has a "Sherwood Cant" section listing every term used so far — same rule as character entries, only add a term once the chapter using it is actually built/published, so the guide never spoils an unreleased chapter's slang.

**Guide images specifically:** a character can get a **text-only** guide entry once merely *named* on the page (even in dialogue/hearsay, e.g. the Sheriff being discussed by a traveler). But don't add an `img` field until the character has actually **physically appeared and been described** in a built chapter — showing a reader a character's face before the story itself does is its own small spoiler. (Example: Vane and the Sheriff of Nottingham are named as of Ch8/Ch9 but only by reputation/hearsay; both stay text-only in the guide until they actually show up on the page.)

**CRITICAL — the guide is permanently spoiler-safe, never reveal-position-aware:** unlike narration (which can change once a reveal has happened, since it's read in order), `guide.json` is a static reference accessible to any reader at any point in the book. **Never update Pip's or Thistlewood's guide entries to reflect the Ch16 reveal (or any future reveal)** — a reader on Ch3 could open the guide and get spoiled. Their entries stay exactly as originally written (Pip as "Thistlewood's grandson," Thistlewood as merely "unusual competence") **permanently**, regardless of how far the story itself has progressed. This applies to any future reveal too: the guide only ever reflects what an uninformed reader should know, never what's been confirmed later in the timeline.

**Pip's pronouns:** **RULE CHANGED as of Ch16 (Story 4) — the reveal has happened.** Narration now uses "she/her/hers" for Pip consistently in every scene, regardless of who's present — the reader permanently knows now. Uninformed characters (everyone except Marian) still say "he" **in their own dialogue**, since their knowledge hasn't changed. Don't hedge with "they" in either direction. Full rule and reasoning in `characters.md`. (For any pre-Ch16 chapter references or excerpts, the old "he" throughout applies — this change is forward-only from Ch16.)

**Robin's incomprehension, played out:**
> "Steer clear of him," said Marian. "Right hog in the mire, that one."
> Robin frowned. "There's no mire anywhere near here."
> "It means he's a *liar*, Rob."
> "Then why not simply say liar?"
> Nobody had ever had a satisfying answer to this, and nobody was about to start now.

---

## Running gags

Running gags (character-specific comedic bits that recur and escalate across chapters) are tracked in `story-bible.md`'s **Running Gags Log**, since they need continuity tracking as they develop — this file covers the *style* of humor, that file covers *which specific bits exist and where they've appeared*. When drafting, check that log before inventing a new recurring bit, and add to it when a joke seems likely to want a callback later.

## Format implications

- **Image density:** plenty of plates, per the user's direction — aim for roughly image-to-text parity across a chapter (consistent with the "almost as many image pages as text" brief from project setup), not just an occasional illustration.
- Slang and narrator asides both work well as *text* page material rather than plate `_describe` content — keep plates focused on staging the physical comedy/action, let the prose carry the voice and wordplay.

## Open items — resolved
- [x] Sample paragraph's voice — confirmed on target by the user after Ch1's draft; unchanged since.
- [x] Starter glossary — expanded from 7 to 17 terms; 6 currently in active use through Ch7 (tracked in `guide.json`), rest available as needed.
- [x] Cant fluency — settled through practice, not a formal decision: Marian, Will, Long John, and Brother Crumb have all translated for Robin on-page at various points (Ch1–7). Thistlewood and Pip's fluency never came up and remains genuinely open if it's ever relevant.
