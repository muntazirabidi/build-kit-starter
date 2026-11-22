# Quote helper

<!-- Claude reads this file at the start of every session. Keep it short. -->

## What this is

A helper for a small builder. It turns the owner's rough site visit notes into a draft quote in Word, priced from their own rates and price list, for them to check and send themselves. It never sends anything, never invents a price, measurement or job, and never promises a finish date.

The owner is not a programmer. Explain choices in plain words, and ask before anything risky or anything that costs money.

## Read first

1. `DESIGN.md`. Part 1 is the owner's brief in their words. Part 2 is the build spec. Follow it. If the work needs something the design does not say, stop and ask, then update DESIGN.md.
2. `business/rates.toml`, `business/prices.csv` and `business/wording.toml`: the owner's rates, price list and wording. Prices only ever come from here or from a £ figure in the notes.
3. `tests/examples/`: the owner's three examples with known right answers.

## Layout

- `quote.py`: the one command, `python3 quote.py notes/<file>.txt`.
- `helper/`: schema, Claude extraction, gates, pricing (in pence), Word draft.
- `business/`: the owner's rates, price list and wording. They edit these.
- `notes/`, `drafts/`, `logs/`: real notes, drafts and run log. Never in git.
- `tests/`: examples, fake model output, one test per promise. `--live` calls the real model; ask first.
- `.claude/skills/quote/`: `/quote <notes file>` for the owner.

## Commands

- `/quote <notes file>`: make a draft quote (once built).
- `/design <idea>`: interview the owner and fill in DESIGN.md. Nothing is built.
- `/next-step`: build the next unfinished step from DESIGN.md, test it, save a checkpoint.
- `/check-examples`: run the owner's examples with known right answers.
- `/explain-it`: explain the project or the last change in plain English.
- `/ship-check`: the checklist before anything goes online or is shared.
- `reviewer` agent: a second opinion with fresh eyes before shipping.

## Rules

- Never open, print or change `.env`. If a key is needed, ask the owner to type it there.
- Never send, publish, pay, delete or email anything without the owner saying yes in chat.
- Never invent facts, names, links or numbers. If something must never happen, check it in code, not only in a prompt.
- No real client names or personal data in code, tests or examples. Use made up ones.
- Small steps. After each step that works, save a git checkpoint with a plain message.
- Work on a branch. Never push to main or deploy to live; the owner does that.
- Ask before running anything that calls a paid AI model or service, and say roughly what it costs.
- Plain British English in anything the owner reads. Short sentences.
