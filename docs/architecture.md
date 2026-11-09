# Phase 1 architecture and role boundaries

Preserve the initial cloud-hosted direction: Temporal orchestration, Python workers, PostgreSQL task state, object storage evidence, isolated disposable execution and cloud model APIs through a replaceable adapter. These components are planned, not deployed. Local preparation does not change the deployment baseline.

| Capability | Output | Authority boundary |
| --- | --- | --- |
| Coordinator | Plan, routing, progress and evidence index | Cannot grant itself privileges or approve Engineering. |
| Product and Requirements | Sanitized requirements and acceptance criteria | Cannot authorize spending or deployment. |
| Solution Architect | Bounded design and interfaces | Preserve settled decisions absent a material obstacle. |
| Engineering | Implementation branch, tests and rationale | Cannot approve its work or merge. |
| Independent Code Reviewer | Findings for the exact commit | Separate identity/context; cannot author the same change. |
| QA and Verification | Acceptance, regression and negative-path evidence | Cannot waive failed gates. |
| Independent security capability | Scans and risk findings | Independent verification, no extra autonomous organization needed. |
| Human | Approval, rejection and merge decision | Ultimate external-action, spending and production authority. |

Planned states: RECEIVED → REQUIREMENTS_READY → DESIGN_READY → IMPLEMENTED → INDEPENDENT_REVIEW → VERIFIED → AWAITING_HUMAN → ACCEPTED or REJECTED. Failures enter BLOCKED or REWORK. New commits invalidate review evidence. No automatic deployment or merge transition.

Handoffs carry task ID, role, artifact references, immutable commit, result, findings, usage/cost metadata and next permitted state. Untrusted repository content cannot grant permissions. Workers require CPU, memory, wall-clock, filesystem, network and credential limits; containers alone do not establish isolation. Evidence must survive worker disposal. Start sequentially without Kubernetes or unnecessary agents.

Codex remains the engineering environment; GitHub is the intended source and sanitized knowledge authority. Temporal owns durable business transitions and approval waits. External interactions belong in bounded retry-safe Activities with stable idempotency keys; harness retries must not duplicate workflow effects. No OpenClaw or Hermes layer is introduced.

Independent contexts do not imply independent permissions. Engineering, Reviewer, QA and Security require externally scoped execution identities and protected attestations; Human provides the authenticated material decision. Included predicates and [schemas](../workflows/README.md) specify data rules but cannot authenticate identity, protect evidence or grant acceptance. See [authority policy](../policies/AUTHORIZATION.md).
