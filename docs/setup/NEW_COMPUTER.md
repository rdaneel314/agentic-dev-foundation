# Set up a new development computer

Required: Git, Python 3.13.x, a terminal and an editor. Obtain Git and Python through your approved software process from [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads). M0 did not install software. No AWS CLI, model client, containers, Temporal, OpenClaw or Hermes is required for starter checks.

## Obtain the source

Before publication, extract the reviewed public-only ZIP into a folder you choose. Do not copy private notes, local credentials, caches or virtual environments. After separate authorization and creation of the remote, replace OWNER with the confirmed account:

```text
git clone https://github.com/OWNER/agentic-dev-foundation.git
cd agentic-dev-foundation
git status --short --branch
```

That remote is a future publication target, not an existing service claimed by this package. Authenticate writes independently per computer using a credential manager or a key outside the clone. Never put tokens in clone URLs. Prefer a privacy-preserving commit email if appropriate; public commit metadata is disclosure.

Read AGENTS.md, PROJECT_STATUS.md, ROADMAP.md, DECISIONS.md and docs/backlog.md. No particular Codex installation, model or remembered chat is required to resume.

## Windows PowerShell

From the public repository root:

```powershell
git --version
py -3.13 --version
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -B scripts/check_foundation.py
.\.venv\Scripts\python.exe -B -m unittest discover -s tests -v
```

If `py` is unavailable and `python --version` reports 3.13.x, substitute `python` for `py -3.13`. No activation or execution-policy change is needed.

## macOS and Linux

Use an approved Python 3.13 installation without replacing system Python. Distribution package names and venv availability vary; do not run guessed installation commands.

```sh
git --version
python3.13 --version
python3.13 -m venv .venv
.venv/bin/python -B scripts/check_foundation.py
.venv/bin/python -B -m unittest discover -s tests -v
```

## Complete tooling checks

Basic structural tests use only the standard library. YAML, dependency and secret checks need the pinned CI tools. With permission to download/install the documented tools on the new computer, use that computer's venv Python:

```text
python -m pip install --only-binary=:all: --require-hashes -r requirements-ci.lock
python -m pip check
python scripts/check_dependencies.py
python scripts/check_yaml.py
python scripts/scan_secrets.py
python -m pip_audit --strict --disable-pip --no-deps -r requirements-ci.lock
```

Replace `python` with `.\.venv\Scripts\python.exe` on Windows or `.venv/bin/python` on macOS/Linux. The audit performs network vulnerability queries; failure is not a pass. The lock includes the selected pip version. Review package updates and hashes before changing it. See [dependencies](../DEPENDENCIES.md) and [CI](../ci.md).

No secrets or `.env` values are required. The [example configuration](../../.env.example) documents unused future options; scripts do not load it. Do not run `pip install .`: this foundation is not packaged as an application. Record actual OS/interpreter/tool versions and results in a sanitized implementation record. A second-machine test is complete only after it is actually executed. Follow [switching computers](SWITCHING_COMPUTERS.md) for later moves.
