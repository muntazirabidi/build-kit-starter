# Design: [name of your project]

<!--
HOW TO USE THIS FILE
Two ways. Pick one.

A. Let Claude fill it in (easiest). In Claude Code, in this folder, type:
     /design [one sentence about what you want to build]
   It asks you up to five questions, drafts both parts and marks every guess
   with (to confirm). Without the kit's skills, switch to Plan mode and paste:
     Fill in DESIGN.md for my idea: [one sentence]. Draft Part 1 from what I
     tell you and from any documents in this folder. Mark every guess with
     (to confirm). Ask me up to five questions first. Then write Part 2 as a
     full build spec. Do not build anything yet.

B. Fill in Part 1 yourself, in your own words. Leave Part 2 to Claude:
     Read my Part 1 in DESIGN.md and write Part 2 as a full build spec.

Then:
1. Read Part 1 and correct it in your own words. Your words win.
2. Optional: "Turn DESIGN.md into an artifact I can share."
3. Build one step at a time: /next-step

AGENT: keep these headings. Replace every [bracket]. Write Part 1 in plain
British English for someone who does not code: no jargon, short sentences,
in the owner's voice ("I", "my"). Elsewhere say "the owner" or "they".
Write Part 2 for an agent that will build it: exact, complete, testable.
Never put real client names, personal data or secrets in this file.
-->

> Two parts for two readers. **Part 1** is for the owner, in plain words. **Part 2** is for the agent that builds it.

---

# Part 1. For the owner: the plain brief

Read this part, correct anything wrong, and say yes or change it. Nothing is built until you are happy with it.

## 1. What it is for
- **The problem, in one or two sentences:** [what takes too long, gets forgotten or goes wrong today]
- **Who uses it:** [you, your team, your clients]
- **What they get:** [the result, in one sentence]
- **What it does not do:** [the part that stays human]

## 2. How it will be used
1. [What the person does first]
2. [What the tool does]
3. [What it decides or checks]
4. [What the person gets back]

**One worked example (made up):** [input] gives [output].

## 3. Your business, in your words
The agent drafts these from what you tell it and from your documents. Correct every line.

| Question | Why it matters | Answer |
|---|---|---|
| Who are your customers or readers? | So it judges work for real people | [ ] |
| What do they ask you most often? | These are the jobs worth doing first | [ ] |
| What does a good result look like? | So it knows when it is done | [ ] |
| What must it never do or say? | Becomes a rule, and a test | [ ] |
| What must it never touch? | Files, systems, money, people | [ ] |
| Your words: tone, terms, categories | So the output sounds like you | [ ] |
| Busy times or deadlines in your year | So it plans around them | [ ] |
| What is private here? | So private data stays out | [ ] |
| Three examples where you know the right answer | These become the tests it must pass | 1. [ ] 2. [ ] 3. [ ] |

## 4. Promises built into it
- It never [sends, publishes, pays or deletes] without you.
- It never invents [facts, figures, names or links]. Anything that must never happen is checked in code, not just asked for.
- It never sees your passwords or keys.
- [Your own promise]

## 5. Your decisions
1. Say yes to this brief, or change it.
2. Try each change on a preview before it goes live.
3. Approve each change yourself (on GitHub: press Merge).
4. When an answer is wrong, say so. It becomes a new test.

## 6. Finished means
- [3 of 3] of your examples give the right answer.
- [0] made up facts or links.
- [Fast enough / works on a phone / other]
- You can change the rules yourself, in plain English.

---

# Part 2. For the agent: the build spec

Agent: Part 1 is the requirements. Build exactly what this part says, in this order. Stop and ask when anything here is unclear, risky or costs money.

## Pieces
A diagram (as a simple flowchart) and one line per piece: what it is, which file, what it reads and writes.
Prefer the smallest design that works: no database, server or service unless Part 1 needs it, and say why.

## Flow: one run, start to finish
A flowchart of one run. Every check is a gate with a yes path and a plain failure message for the owner.
The last gates (anything in Part 1, section 4) are enforced in code.

## Contract
- The one function or command everything depends on: name, inputs, outputs.
- Inputs: each with its source and limits.
- Output: each field, its type, and the rule that checks it (use a fixed schema for model output).
- Errors: cause, where it is caught, the exact plain message the owner sees.

## Decisions
| Choice | Why | When to think again |
|---|---|---|
| [model and effort] | [ ] | [ ] |
| [how context is given: full text, cached, or search] | [ ] | [ ] |
| [hosting] | [ ] | [ ] |

## Folder
The full file tree, one line per file saying what it is for. Include CLAUDE.md, this DESIGN.md, `.claude/` (skills, agents, hooks, settings), tests, `.env.example`, `.gitignore`.

## Settings
| Layer | Setting | Value | Why |
|---|---|---|---|
| Building (Claude Code) | Deny reading or editing `.env` | `.claude/settings.json` | Agent never sees secrets |
| Building | Deny deploying to live and pushing to main | `.claude/settings.json` | Only the owner ships |
| Building | Hook: block any tool call that mentions `.env` | `.claude/hooks/` | Second lock |
| Running | Model, effort, max output, caching, timeouts | [ ] | [ ] |
| Running | Input limits and any password | [ ] | [ ] |
| Secrets | [NAME]: where it lives locally and online | `.env` / host settings | Typed by the owner only |

Also list every skill and subagent: name, when it is used, what it may touch.

## Build with subagents
Only if the work splits cleanly into separate files. A table: subagent, files it owns, done when, never touches.
The contract above is agreed first. A read only reviewer checks the result. Include the exact prompt to start them.

## Build steps
Numbered, small, each with how it is tested before the next. Write each as `- [ ] 1. step: how it is tested`; `/next-step` ticks it `[x]` when it passes. Save a git checkpoint after each step that works. Use fake data or a fake client until the tests need the real thing, and ask before any step that costs money.

## Definition of done
| Check | How to prove it |
|---|---|
| Every example in Part 1, section 3 passes | [test command] |
| Every promise in Part 1, section 4 holds | [a test per promise] |
| No secret in git | `.env` ignored, diff checked |
| Reviewed | reviewer findings fixed or explained |

## GitHub
Work on a branch, small commits, open a pull request with a plain English summary and a preview link. The owner merges. How to undo a bad change.

## Deploy
Where it runs, what the owner sets by hand (keys, passwords, spend limit), and what updates automatically.

## Keep it working
| When | What | How |
|---|---|---|

## Monitor
Three or four numbers to watch (cost per run, errors, use, any guardrail that fired) and where to see them.

## Cost
Cost per run with the chosen model and a cheaper one, building versus running, and the cap. Check current prices before writing numbers.

## Hand over
How the owner opens it, asks for changes, adds a test when an answer is wrong, and what to build next.
