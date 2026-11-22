---
name: ship-check
description: The checklist before putting a project online or sharing it. Use when the user says ship, deploy, launch, go live, share it, or "is this ready".
---
Check the project and report each item as OK, Fix needed, or Not applicable, in a table:

1. Secrets: no API keys or passwords in any file except `.env`, and `.env` is in `.gitignore`. Check the git history too.
2. Cost: if it calls an AI model, is there a limit (max output, a cap on requests, a spend limit set on the provider by the owner)?
3. Wrong answers: what happens when the AI is wrong or makes something up? Is the rule checked in code, or is a human in the loop?
4. Bad input: empty input, very long input, or someone typing instructions to trick it.
5. Errors: does the user see a friendly message if something fails?
6. Tests: do the owner's examples pass (`/check-examples`)?
7. Privacy: does it store or send personal data anywhere it should not? Who can open the link?
8. Promises: every line in DESIGN.md, Part 1, section 4 holds.

Then ask the `reviewer` agent for a second opinion. Finish with the top three things to fix before sharing, in plain English. Do not deploy; the owner does that.
