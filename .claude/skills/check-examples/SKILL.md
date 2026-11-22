---
name: check-examples
description: Test the project on the owner's examples where the right answer is already known. Use after any change to prompts, rules, the model or the data, and before sharing or deploying.
---
1. Read the examples in DESIGN.md, Part 1, section 3, and any test files listed in Part 2, "Definition of done". If there is no test script yet, offer to write one that runs every example and saves a dated table in `output/`.
2. If running them calls a paid AI model, say how many calls and roughly what it costs. Wait for a yes.
3. Run them. Show a table: example, expected, got, pass or fail. Add the cost of the run if known.
4. For each fail, say in one line whether the tool is wrong or the expected answer looks out of date. Never change an expected answer just to make a test pass; ask the owner.
5. When the owner tells you an answer was wrong in real use, offer to add it as a new example, so it is tested every time from now on.
