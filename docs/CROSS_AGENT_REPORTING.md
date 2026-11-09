# Cross agent issue reporting

Every role reports material defects or risks discovered anywhere in its work, including outside its remit. A reviewer who notices a requirements defect, a QA worker who finds a permission flaw, or Engineering encountering a disclosure risk must report it rather than silently expanding scope or suppressing it.

Use the [finding schema](../workflows/schemas/finding.schema.json): finding/task ID, reporter role, affected artifact, severity, safe summary, evidence reference, owner role, blocking flag, state and disposition. References must not reveal credentials or private endpoints. Keep exploit details and sensitive evidence private and publish a sanitized index only.

1. Record the finding before handoff; notify the Coordinator through an authorized channel. Local task records suffice until external messaging is authorized.
2. Assign the responsible role and next action. Critical/high security findings block progress; any unresolved finding marked blocking also blocks acceptance.
3. Deduplicate by finding ID and affected artifact while preserving reporters and evidence. A duplicate is not a reason to lose severity or a blocker.
4. Engineering may propose a fix but cannot independently close its own blocking finding. Code review, QA and security recheck the affected exact artifact, with human disposition where required.
5. Record accepted/rejected resolution, independent verifier and evidence. Human risk acceptance must be explicit, scoped and private where necessary; it does not silently waive a mandatory quality gate.

An unavailable owner/check leaves the finding open or blocked. Updated commits invalidate stale disposition when the issue is affected. The schemas enforce shape only; authenticated routing, notification and closure enforcement remain runtime backlog items. No messages are sent by this package.
