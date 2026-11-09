# Dependencies and reproducibility

Runtime/scaffold logic uses Python 3.13.x standard library. No Temporal, provider SDK, model, container runtime or application framework is installed or required by M0. `pyproject.toml` is compatibility metadata, not an installable application.

`requirements-ci.txt` holds four direct tool choices inherited from the security foundation. `requirements-ci.lock` pins the complete 29-package tools closure, including pip, with SHA-256 hashes of non-yanked wheels obtained from official PyPI release metadata. [Provenance](dependency-provenance.json) records exact source URLs, dependency constraints and wheel identities. The selected versions came from the existing validated tools environment rather than a fresh install.

With permission to install the documented tools on a new machine:

```text
python -m pip install --only-binary=:all: --require-hashes -r requirements-ci.lock
python -m pip check
python scripts/check_dependencies.py
```

Only wheels are allowed; no implicit source build dependencies. SHA hashes protect distribution identity relative to the reviewed lock, not publisher trust or installed-file integrity. Different OS/architecture wheel availability and a fresh installation still require real execution. Marker/constraint checks cover Windows, Linux and macOS Python 3.13 contexts; they are not runtime tests on those systems. Hosted OS images and Python patch releases are mutable.

The existing tools were reused without modification. No installation occurred in M0. Vulnerability auditing uses the exact lock with `--disable-pip --no-deps`; it queries advisory metadata without installing/resolving packages. Findings or service failures block that audit, and results age as advisories change.

## Deliberate regeneration

Review tool necessity, compatibility, licenses and vulnerabilities before any change. In a separately approved isolated tools environment containing the intended direct versions, run:

```text
python scripts/generate_ci_lock.py
python scripts/check_dependencies.py
python -m pip check
```

The generator uses already installed distribution metadata to follow required extras and dependencies across three OS marker contexts, and reads official PyPI metadata for exact versions/wheel hashes. It installs nothing, does not upgrade tools and is not a latest-version resolver. It needs the currently locked packaging library and network access. Review input, lock, provenance and CI together. Reject missing dependencies or fabricated hashes. Verify a fresh hash-checked install on supported systems before treating a changed lock as portable.

Action dependencies are full-SHA pinned in CI. Check upstream identity and compatibility during upgrades; a pin alone is not a source audit. Recreate `.venv` per computer. Do not commit arbitrary `pip freeze`, wheel caches, machine paths or installed environments.
