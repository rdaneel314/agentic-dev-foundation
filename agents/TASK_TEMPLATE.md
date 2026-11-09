# Portable task and handoff record

Copy a sanitized completed record under docs/records. Private task payloads, approvals and raw logs belong in an approved restricted store; public Git holds safe references and engineering knowledge.

- Task ID and P1 backlog reference:
- State, owner role and next permitted transition:
- Objective, non-goals and synthetic inputs:
- Repository-relative allowed paths and immutable base/result commit (or explicitly no Git yet):
- Acceptance checks, allowed tools and side effects (default external actions: none):
- Authorization scope and sanitized evidence reference; time/cost limits:
- Patch/artifact references, dependency changes and reproducibility instructions:
- Independent code review identity/context reference, reviewed artifact, findings:
- Independent QA identity/context reference, exact commands/results and tested artifact:
- Security assessment, scan versions, private finding reference and sanitized blockers:
- Cross-agent findings: severity, owner, blocking state and independent disposition:
- Human decision, exact artifact, scope, timestamp and authenticated evidence reference:
- Environment versions, unverified checks, blockers and next resumable action:
- Before machine switch: branch, commit, dirty/untracked/ignored/unpushed work and successful authorized synchronization:

This record does not authorize actions or prove authenticated identity. Use [workflow schemas](../workflows/README.md) for machine-readable contracts. A new commit invalidates previous review/approval evidence.
