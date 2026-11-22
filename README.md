# Build kit

Everything you need to start your own build with Claude Code. Copy this whole folder, rename it after your project, and open it in Claude Code.

## What is inside

| File | What it does |
|---|---|
| `DESIGN.md` | Your design, in two parts. Part 1 is for you, in plain words. Part 2 is the build spec for the agent. |
| `CLAUDE.md` | The project's memory. Claude reads it at the start of every session. Holds the rules. |
| `.claude/skills/` | Five commands you type with `/` (below). |
| `.claude/agents/reviewer.md` | A second Claude that checks the work with fresh eyes. It cannot change files. |
| `.claude/settings.json` | Safety settings: Claude cannot read your keys, push to main or deploy to live. |
| `.claude/hooks/protect-secrets.py` | A second lock on your keys, plus a Mac notification when Claude finishes. |
| `.env.example` | Where your keys go. Copy it to `.env` and type them yourself. |
| `.gitignore` | Keeps `.env` and clutter out of GitHub. |
| `examples/` | A finished design for a made up quote helper, written by `/design`, to see what good looks like. |

The `.claude` folder is hidden. On a Mac press **Cmd Shift .** in Finder to see it.

## Start

1. Copy the folder and rename it, for example `my-quote-helper`.
2. Open it in Claude Code (desktop app: choose the folder; terminal: `cd` into it, then `claude`).
3. Type **/design** and one sentence about your idea, for example:
   `/design a helper that turns my site visit notes into a client quote`
4. Answer its five questions. It writes both parts of DESIGN.md and marks its guesses **(to confirm)**.
5. Correct Part 1 in your own words. That is the part only you can do.
6. Type **/next-step**. It builds one small step, tests it and saves a checkpoint. Repeat.

Prefer to write it yourself? Fill in Part 1 of DESIGN.md by hand, then ask: *Read my Part 1 in DESIGN.md and write Part 2 as a full build spec.*

## Commands

| Type | When |
|---|---|
| `/design <idea>` | At the start. Writes the design, builds nothing. |
| `/next-step` | To build. One step at a time, tested, saved. |
| `/check-examples` | After any change. Runs your examples with known right answers. |
| `/explain-it` | Any time you want to know what something does, in plain English. |
| `/ship-check` | Before you share a link or put it online. |
| "Ask the reviewer to check this" | Before anything important. |

## Good to know

- Put useful documents in the folder before `/design`: notes, a price list, examples of good work. Remove real client names first.
- Your knowledge goes in Part 1, section 3. The better that table, the better the tool.
- When an answer is wrong in real use, say so. It becomes a new example, tested every time.
- The hook needs Python 3, which comes with the Mac developer tools. On Windows, delete the `hooks` part of `.claude/settings.json` and rely on the deny rules.
