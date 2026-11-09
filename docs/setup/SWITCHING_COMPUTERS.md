# Switch computers without losing work

GitHub synchronizes committed and successfully pushed source after publication is authorized. It does not preserve ignored files, unpushed branches, stashes or credentials. Each computer has its own clone and recreated environment; do not synchronize active clones through Drive, OneDrive or Dropbox.

## Before leaving a computer

Update engineering status, decisions, backlog and a sanitized [task record](../../agents/TASK_TEMPLATE.md). Capture next action, blockers, current branch and commit. In an initialized clone:

```text
git status --short --branch
git diff
git diff --cached
git diff --check
git ls-files --others --exclude-standard
git status --short --ignored
```

Inspect ignored/untracked useful work; move only sanitized source into tracked locations. Never stage credentials. Run relevant checks, stage explicit reviewed files and commit to the task branch, even for an unfinished handoff. A local commit is not remote backup.

Only after remote synchronization is explicitly authorized:

```text
git fetch origin
git status --short --branch
git push -u origin YOUR_TASK_BRANCH
git rev-parse HEAD
git rev-parse @{upstream}
git log --oneline @{upstream}..HEAD
git status --porcelain
```

In PowerShell quote `'@{upstream}'`. Compare hashes after a successful push and fetch; local HEAD and upstream must match, the ahead-commit list must be empty, and porcelain output must be empty. A missing upstream or failed push is an unresolved handoff. Check untracked/ignored files separately; do not silently stash, force-push, discard or rebase a dirty tree. Record the branch/commit without private identifiers.

Before a remote exists, transfer only the reviewed public starter or a sanitized local Git bundle using an approved private method. Keep a checked backup. Do not call this GitHub synchronization. Private companion documents need a separate approved restricted backup; do not place them in public Git.

## Resume on the next computer

1. Follow [new-computer setup](NEW_COMPUTER.md). Recreate venv; restore no copied `.git/config`, editor memory or credential store.
2. For a new clone, compare HEAD to the handoff commit. For a clean existing clone, fetch, switch to the handoff branch and `git pull --ff-only`. To track a new branch use `git switch --track origin/YOUR_TASK_BRANCH`.
3. Read the four continuity files, backlog and task record. Run the documented checks and record actual results.
4. Restore secrets through approved per-machine credential management only if an authorized task needs them; offline starter checks need none.

Avoid concurrent editing of the same branch on two computers. Use separate branches for parallel work and review conflicts. Switching the computer, Codex client or model must not require reconstructing project knowledge from chat history.
