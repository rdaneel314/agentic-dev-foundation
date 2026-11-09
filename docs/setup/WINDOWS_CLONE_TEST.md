# Fresh Windows clone acceptance test

Run on a different Windows computer after the repository exists and the human authorizes downloads and any test branch/push/PR. M1 preparation did not perform this test. A same-host copy or local Git clone is only a rehearsal.

## Prerequisites

- Approved Git for Windows and 64-bit Python 3.13.x, including the Python launcher and venv support. Obtain from [Git](https://git-scm.com/downloads/win) and [Python](https://www.python.org/downloads/windows/).
- Internet access to the approved GitHub repository, official package index/wheel hosting and advisory service. No AWS, containers, Temporal, model token, GitHub CLI or paid subscription is needed.
- The owner supplies the accepted public repository URL, branch and exact commit from the handoff. Configure your chosen Git identity/credential manager independently for authorized writes; never embed credentials in URLs.
- Choose a new local folder outside active cloud-drive synchronization. Do not copy .venv, .git/config, editor state or credential files from the first computer.

## Clone and verify the accepted commit

Open PowerShell in the chosen parent folder. Replace OWNER and EXPECTED_COMMIT with the accepted values after publication:

```powershell
git --version
py -3.13 --version
git clone https://github.com/OWNER/agentic-dev-foundation.git
Set-Location agentic-dev-foundation
git status --short --branch
git rev-parse HEAD
```

Compare HEAD to EXPECTED_COMMIT. If the handoff specifies a task branch, fetch/switch to that branch before comparing; investigate any mismatch. Read AGENTS.md, PROJECT_STATUS.md, ROADMAP.md, DECISIONS.md and docs/backlog.md, and identify the next task using only Git-tracked records.

## Rebuild the tools environment

With permission for these software downloads/installation on the second computer:

```powershell
py -3.13 -m venv .venv
$FoundationPython = Join-Path (Get-Location) '.venv\Scripts\python.exe'
& $FoundationPython -m pip install --only-binary=:all: --require-hashes -r requirements-ci.lock
& $FoundationPython -m pip check
& $FoundationPython -B scripts/check_foundation.py
& $FoundationPython -B -m unittest discover -s tests -v
& $FoundationPython -B scripts/check_yaml.py
& $FoundationPython -B scripts/check_dependencies.py
& $FoundationPython -B scripts/scan_secrets.py
& $FoundationPython -B -m pip_audit --strict --disable-pip --no-deps -r requirements-ci.lock
git status --porcelain
```

Require exit code zero for each command, all 29 current tests passing with no skips, and an empty final porcelain result. A failed command, unavailable scanner, hash mismatch, missing wheel or advisory error is not success. No execution-policy change or shell activation is required. If the test count changes legitimately, review the accepted commit's evidence rather than weakening the criteria.

## Handoff round trip and record

After separate write/PR authorization, create a small sanitized documentation record on a dedicated `docs/portability-test` branch. Stage only that record, inspect the diff, commit and push the branch. On the first computer, fetch it into a clean working tree and confirm the exact branch/commit and record. Submit a PR for independent AI review, QA/security evidence, checks and human merge. AI verification must not be represented as independent human approval; GitHub requires no second human approval. Do not change main protections to finish the exercise.

Record locally: test date, Windows/Python/Git versions, accepted commit, install/check exits, actual test count/skips, whether project knowledge was sufficient, round-trip commit and any failure/blocker. Public evidence should omit usernames, device names, absolute user paths, credentials and account identifiers. Keep detailed logs private. Before leaving either machine, run the [switching checklist](SWITCHING_COMPUTERS.md), inspect untracked/ignored/unpushed work and confirm successful authorized synchronization.

Portability is fully verified for this scenario only when the real second-machine fresh install and handoff succeed. Linux/macOS and other architectures remain separate coverage.
