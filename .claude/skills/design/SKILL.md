---
name: design
description: Turn the owner's idea into a two part design in DESIGN.md before anything is built. Use when the user says design, plan my idea, fill in the design doc, or starts a new project from an idea.
---
The idea: $ARGUMENTS (if empty, ask for it in one sentence).

Do not build anything in this skill. Only write DESIGN.md and CLAUDE.md.

1. Read DESIGN.md (keep its headings), CLAUDE.md and any documents in this folder the owner has added (notes, price lists, examples, old emails with names removed).
2. Ask the owner up to five short questions, all at once, about the things only they know: who it is for, what a good result looks like, what it must never do, and three examples where they already know the right answer. Wait for the answers.
3. Write Part 1 in plain British English for someone who does not code. Fill section 3 (their business, in their words) from their answers and their documents. Mark every guess with **(to confirm)**. No jargon. Write it in the owner's own voice ("I", "my").
4. Write Part 2 as a complete build spec for an agent: pieces, flow with gates, the contract, decisions with reasons, the full folder tree, settings, build steps small enough to test one at a time, and a definition of done. Choose the smallest design that works. Check current model names and prices before writing them. Call the owner "the owner" or "they"; never guess he or she.
5. Fill in the "What this is", "Read first" and "Layout" sections of CLAUDE.md from the design.
6. Show the owner a short summary: what it will do, what it will never do, the build steps, and every line marked (to confirm). Ask them to correct Part 1 in their own words. Their words win.
7. Offer to turn DESIGN.md into a shared artifact so they can read it on their phone or send it to someone.

When they say yes to the design, tell them the next command is `/next-step`.
