---
name: next-step
description: Build the next unfinished step of the plan in DESIGN.md, test it and save a checkpoint. Use when the user says next step, keep building, carry on, or build it.
---
1. Read DESIGN.md, Part 2, "Build steps". Find the first step not marked done. If Part 1 still has lines marked (to confirm) that matter for this step, ask about them first.
2. Say in one or two plain sentences what this step will do and how it will be tested. If it costs money, calls a paid service, or touches anything outside this folder, wait for a yes.
3. If this is the first step, make sure git is set up and you are on a branch, not main.
4. Build only this step. Use fake data or a fake AI client until the tests really need the real one.
5. Test it the way DESIGN.md says. If it fails, fix it, at most three tries, then stop and explain the problem in plain words.
6. When it passes, mark the step done in DESIGN.md, save a git checkpoint with a plain message, and tell the owner what now works and what the next step is.

One step per run. Do not race ahead.
