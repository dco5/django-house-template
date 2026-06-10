# Agent Workflow

Read CLAUDE.md first — it contains the commands and architecture rules.

## Issue tracking

If beads (`bd`) is initialized in this repo, use it for ALL task tracking (not markdown TODOs):
`bd ready` → find work, `bd create` / `bd update` / `bd close` → manage, `bd sync` before push.

## Non-interactive shell

Use `-f` flags (`cp -f`, `rm -f`), `ssh -o BatchMode=yes`, never commands that prompt.

## Landing the plane (mandatory session close)

1. File remaining work as issues.
2. Run quality gates: tests, ruff, mypy.
3. Close finished issues.
4. `git pull --rebase && git push` (plus `bd sync` if using beads).
5. Verify `git status` shows "up to date with origin" — work is NOT complete until pushed.
