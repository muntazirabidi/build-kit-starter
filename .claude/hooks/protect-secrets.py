#!/usr/bin/env python3
"""PreToolUse hook: stop Claude from reading or editing .env files.
Claude Code sends the tool call as JSON on stdin. Exit code 2 blocks it and
the message on stderr is shown to Claude."""
import json, sys
call = json.load(sys.stdin)
inp = call.get("tool_input", {})
target = " ".join(str(inp.get(k, "")) for k in ("file_path", "path", "pattern", "command"))
if ".env" in target and ".env.example" not in target:
    print("Blocked: .env holds secret keys. Do not read or change it. "
          "Ask the user to edit it themselves if a key is needed.", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
