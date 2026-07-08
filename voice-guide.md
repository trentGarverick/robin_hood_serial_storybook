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

## Open items
- [ ] Confirm the sample paragraph's voice is on target (adjust before drafting Ch1 in earnest)
- [ ] Confirm/expand the starter glossary — add, cut, or reword any entries
- [ ] Decide if any *specific* characters are cant-fluent vs. cant-illiterate (draft assumption: Marian, Will, Long John are fluent; Brother Crumb probably picked some up on the road; Pip and Thistlewood's fluency is TBD but likely irrelevant since they're hidden this story anyway)
