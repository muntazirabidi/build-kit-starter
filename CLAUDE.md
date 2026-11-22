# [Project name]

<!-- Claude reads this file at the start of every session. Keep it short.
After /design, Claude fills in the first two sections from DESIGN.md. -->

## What this is

[One or two sentences: what it does, who it is for.]

The owner is not a programmer. Explain choices in plain words, and ask before anything risky or anything that costs money.

## Read first

1. `DESIGN.md`. Part 1 is the owner's brief in their words. Part 2 is the build spec. Follow it. If the work needs something the design does not say, stop and ask, then update DESIGN.md.
2. [Any other file that holds the owner's knowledge: a profile, a price list, examples]

## Layout

[Filled in from DESIGN.md, Part 2, Folder. One line per folder or important file.]

## Commands

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
- Plain British English in anything the owner reads. Short sentences. Call the owner "you" or "they", never a guessed he or she.
