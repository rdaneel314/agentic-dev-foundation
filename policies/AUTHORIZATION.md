# Human authority and permissions

| Action | Boundary |
| --- | --- |
| Local preparation and verification | Within the user's concrete task; preserve unrelated work |
| External repository, push, issues/PRs, invitations or settings | Separate explicit human authorization |
| Paid API, infrastructure, GPU rental, subscription or purchase | Exact scope/cost approval first; budget proposals grant nothing |
| Acceptance and merge | Independent code review, QA/security evidence and authenticated human decision for exact commit |
| Production deployment | No authority for coding agents; separately controlled human process |
| Destructive cleanup or history rewrite | Reviewed concrete scope and explicit authorization |

Permissions must be enforced outside prompts using least-privilege identities, restricted credentials, protected evidence and bounded isolated jobs. Do not give Engineering review/admin/deployment credentials. Neither the readiness predicate, a schema nor multiple subagent prompts implements this boundary. Missing independent AI review or unavailable mandatory evidence blocks acceptance. The sole human owner makes final decisions; GitHub does not require a second human review. Coding agents receive no upstream write/admin credential and cannot modify governance.

Record approver, scope, artifact/commit, time, limits and evidence privately; publish sanitized references only. New commits or changed scope require fresh relevant approval. Finish authorized local work before asking for a concrete external decision. Secrets never belong in prompts or task files.
