# Specialist roles and authority

These are portable responsibilities, not configured processes or independent identities. All roles inherit AGENTS.md and policies. The workflow is sequential initially. No role may expand its own permissions or grant external authorization.

| Role | Input | Output | Restriction |
| --- | --- | --- | --- |
| Coordinator | Authorized objective, status and backlog | Bounded task, routing, evidence index and escalation | Cannot approve Engineering or suppress findings |
| Product and Requirements | Sanitized need | Acceptance criteria, constraints and synthetic examples | Cannot authorize access, spending or deployment |
| Solution Architect | Requirements and accepted decisions | Interfaces, threat/permission boundaries and design rationale | Material direction changes require human approval |
| Engineering | Task, design, immutable base and allowed paths | Patch, tests and rationale | No self-approval, policy waiver, administration or production deployment |
| Independent Code Reviewer | Exact patch/commit and acceptance | Findings and disposition for that commit | Cannot author the same implementation; separate trusted authority required |
| Independent QA | Clean artifact, acceptance cases | Actual pass/fail, negative paths and limits | Cannot accept implementation based on Engineer's claims alone |
| Independent security capability | Sanitized diff, dependencies and execution design | Scans, permission/disclosure findings and blockers | Cannot waive its own unresolved blockers; private incident details stay private |
| Human authority | Concrete artifact, findings and evidence | Scope-specific accept/reject/publication/cost decision | Ultimate material authority; new artifact invalidates stale approval |

Code review, QA and security must be independent of Engineering and supported by separately scoped execution/evidence channels. A role label or distinct chat alone proves neither identity nor independence. Codex subagents can inherit parent permissions. The M0 package contains specifications and deterministic data checks, not operational segregation. See [governance](../docs/governance.md).

Use [task handoffs](TASK_TEMPLATE.md), [finding reporting](../docs/CROSS_AGENT_REPORTING.md) and [schemas](../workflows/README.md). Report cross-role issues immediately with an owner and evidence; do not wait for a role handoff to surface a blocker.
