# Git Workflow

- Write commit messages in imperative mood ("Add feature" not "Added feature")
- Create new commits rather than amending -- amending after hook failure destroys previous work
- No force-push to main/master without explicit user confirmation
- Stage specific files by name -- avoid `git add -A` or `git add .` (catches secrets, binaries)
- Never skip hooks (`--no-verify`) or bypass signing unless the user explicitly asks
- Never push to any remote without user confirmation
- Investigate merge conflicts rather than discarding changes
