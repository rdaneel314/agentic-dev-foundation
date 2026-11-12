# CI scope and verification commands

Foundation CI has Windows and Ubuntu jobs with Python 3.13, ten-minute timeouts, read-only contents permission and full-SHA-pinned checkout/Python setup. Checkout does not persist credentials. No stored secrets, deployments, privileged PR trigger, self-hosted runner or model call is configured. Bootstrap hosted execution succeeded on both operating systems, including fresh locked installation and 29 tests. The emitted names are foundation-checks (ubuntu-24.04) and foundation-checks (windows-latest), from GitHub Actions integration 15368; both are required on main. See [live verification](records/0004-m1-publication.md).

From the public root with the pinned tools interpreter, run:

```text
python scripts/check_foundation.py
python -m unittest discover -s tests -v
python scripts/check_yaml.py
python -m pip check
python scripts/check_dependencies.py
python scripts/scan_secrets.py
python -m pip_audit --strict --disable-pip --no-deps -r requirements-ci.lock
```

Both matrix jobs run all gates. The workflow installs from the complete hash-locked wheel-only requirements; a missing wheel or mismatch fails installation. M0 reused existing tools and performed no installation. See [dependencies](DEPENDENCIES.md) and [new-computer setup](setup/NEW_COMPUTER.md).

Structural checks validate required paths, local file links, Python metadata and public-boundary heuristics. Link checking excludes external URLs and heading anchors. YAML parsing rejects duplicate keys and checks expected commands/permissions/matrix/actions; it is not the GitHub Actions service validator or a full attack detector. Dependency checks compare installed versions, wheel hash provenance and transitive constraints across three OS marker contexts; they do not perform fresh installs or verify installed files against wheels.

Secret scanning covers current files with offline credential verification disabled; it does not send candidate credentials to providers. It does not scan Git history or classify business confidentiality. Invalid output, scanner failure or candidates block. The audit queries known-advisory metadata for the exact lock, with no package installation or dependency resolution. A failed service query is a failed check. Do not suppress findings or scanner errors.

Published wheel digests trigger entropy heuristics. The wrapper verifies digest-field membership in the reviewed lock, normalizes only those digest values in a temporary metadata view, and scans all other metadata fields plus the remaining tree. It anchors each scanner invocation to its target directory so relocated and temporary paths are actually covered. Real nonfunctional signature tests verify blocking in both ordinary files and other metadata fields; no global entropy filter is disabled.

Unit tests cover negative paths including malformed contracts, stale/self-review/QA/security readiness, invalid scanner output, escaped links, missing continuity, optimized-Python validation and modified CI controls. The policy predicate compares supplied data only; authentication and independent evidence enforcement remain unimplemented.

Independent review must inspect code and CI changes because PR code can weaken its own checks. Neither passing tests nor YAML configures branch protection, proves reviewer independence/human-only merging, verifies cloud isolation or undoes initial disclosure. History scanning and application-specific static/container/isolation tests are future prerequisites when relevant code or history is introduced. See [governance](governance.md) and [verification](verification.md).
