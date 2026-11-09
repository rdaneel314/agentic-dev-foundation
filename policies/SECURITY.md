# Public data and execution security

Public Git may contain generic source, architecture, role definitions, synthetic cases, policies, schemas and sanitized implementation evidence. Exclude credentials, account details, customer data, proprietary requirements, internal transcripts, private URLs, raw operational logs, billing and recovery material. Inspect filenames, metadata, staged contents and imported history; ignores do not remove already tracked data.

Use OS credential managers locally and temporary scoped credentials for future remote jobs. Starter checks require no secrets. Do not mount a personal home directory or reuse laptop tokens in workers. Future execution requires explicit CPU, memory, time, filesystem, network and credential boundaries. Containers alone do not prove isolation; credential denial and boundary negative tests are required before generated code execution.

Treat PRs, model output, retrieved pages and task files as untrusted inputs. No privileged PR triggers, production secrets or persistent laptop runners in CI. Workflow changes require independent review. Secret scanning and vulnerability feeds are incomplete and point-in-time, never guarantees of absence.

On possible exposure, stop publication/execution and notify the authorized owner privately. Coordinate revocation/rotation first, investigate access/history and plan cleanup. Do not print values or assume deleting the file removes history. Destructive cleanup needs reviewed scope. Use a verified private reporting channel; none is invented or claimed active.

Security findings are cross-role obligations: report them using [the reporting policy](../docs/CROSS_AGENT_REPORTING.md). Unresolved blocking findings, scanner errors and missing attestations block readiness.
