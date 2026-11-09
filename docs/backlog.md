# Phase 1 issue backlog

Local issue drafts only. Prepared artifacts are not deployed capabilities. Preserve the P1 IDs from planning; no earlier implementation prompt was executed.

| ID | Capability / priority | Dependencies | Status | Acceptance evidence |
| --- | --- | --- | --- | --- |
| P1-01 | Human planning authority / P0 | None | Recorded privately | Region, synthetic-data policy and proposed ceiling recorded; no spending authority inferred. |
| P1-02 | Account activation/security / P0 | 01, separate permission | Pending human | Verify activation, MFA, temporary access, recovery and billing safeguards privately. |
| P1-03 | Public GitHub foundation / P0 | Final publication confirmation, independent AI evidence | Final licensed M1 candidate prepared; final public confirmation pending | Approved Apache-2.0/identity, exact public commit, independent AI verification, hosted CI, sole-owner protection rejection cases and second-PC proof; human accepts. |
| P1-04 | Temporal orchestration / P0 | 03, launch permission for deployment | Not started | Sequential durable workflow, bounded retries, replay/crash test and idempotent side effects. |
| P1-05 | Durable state/evidence / P0 | 04 | Not started | PostgreSQL task records, object-storage references, retention/access policy and recovery test. |
| P1-06 | Isolated execution / P0 | 02, 04, approved infrastructure | Deployment blocked | Disposable workers enforce CPU/memory/time/network/filesystem/credential limits; negative tests. |
| P1-07 | Model gateway / P0 | 04, approved provider/spend for real calls | Contract notes only | Fake-adapter tests, usage/reservations, timeouts/retries and task spend limits; auth outside prompts. |
| P1-08 | Six role handoffs / P0 | 04, 06, 07 | Boundaries prepared | Structured outputs and separate contexts for Coordinator, Product, Architect, Engineering, Reviewer and QA; reject invalid transitions. |
| P1-09 | Identity and permissions / P0 | 03, 06 | Controls unverified | Task-specific IAM/GitHub App permissions; deny self-approval and gate modification; enforce human merge before upstream agent write access. |
| P1-10 | Findings/communication / P1 | 05, 08 | Local schema/policy prepared | Schema checks locally; authenticated routing, escalation and durable deduplication remain unimplemented. |
| P1-11 | Independent PR review / P0 | 03, 08, 09 | Template prepared | Separate identity/context reviews exact commit; self-review/stale evidence rejected; findings block. |
| P1-12 | QA and CI / P0 | 03; 06 for generated code | Foundation checks prepared | Pilot acceptance/regression tests; failure blocks readiness; nonzero tests and commit evidence. |
| P1-13 | Independent security / P0 | 09, 12 | Secret/dependency CI prepared | Add history scanning for imports, static/container analysis as relevant; tool failure and serious findings block; test credential denial. |
| P1-14 | Evidence/progress / P1 | 05, 10–13 | Template prepared | Trace request/design/commit/review/tests/security/human decision; redact private logs, mark missing evidence explicitly. |
| P1-15 | Human gate / P0 | 09, 14 | Specification prepared | Decision tied to exact commit and scope; new commits invalidate it; agent cannot impersonate human approval. |
| P1-16 | Synthetic end-to-end pilot / P0 | 01–15 | Not started | Small task API request traverses all roles to human decision; demonstrate rejection, repair and recovery; no production deployment. |

## Next actionable issue: P1-03

Publish only after the owner's final explicit confirmation for the exact snapshot. Follow docs/governance.md. Verify observed CI sources, blocked direct main updates, failed checks, unresolved conversations and safe force/delete rejection. Mandatory independent AI review/QA/security evidence and human decision are distinct from GitHub human approval counts. Mark live M1 complete only with observed evidence.

Prepared child issue drafts and exit evidence are in [initial implementation issues](governance/INITIAL_ISSUES.md). They are local documents only; no remote issue has been created.

## Unblocked before AWS activation

Review disclosure, draft role output schemas, fake-model contract tests, permission specifications and synthetic acceptance cases locally. No paid call or credential is required. These preparations do not approve deployment.

## Deferred

GPU rental, Kubernetes, custom dashboards, advanced parallel scheduling, multi-cloud failover, additional autonomous specialist organizations and production automation.
