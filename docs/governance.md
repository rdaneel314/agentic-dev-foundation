# Approved sole owner governance

The project has one human owner. Engineering implements; a separate AI reviewer assesses the exact change; QA runs checks; Security assesses disclosure/permissions; the human owner makes final consequential decisions. Mandatory independent AI verification is retained. AI review is never represented as independent human approval.

GitHub will require PRs, actual relevant CI checks and conversation resolution, and prohibit force pushes/deletion. Its required human approval count is zero because no second human reviewer exists. Last-push approval and code-owner review are disabled so they do not indirectly reintroduce that requirement. This explicitly approved model supersedes earlier documents requiring one independent human approval; it does not waive independent AI verification.

Coding agents get no upstream write/admin/deployment credentials and cannot change governance rules. The human owner is the only upstream write/admin actor. A PR author cannot approve their own change as an independent human reviewer; the owner may merge their own PR only after all mandatory AI/QA/security evidence and actual checks have passed. Blocking or missing evidence prevents the human decision even when GitHub's native checks are satisfied.

Separate Codex contexts may inherit permissions and share tools/files. They provide independent assessments, not independently enforced identities or permission boundaries. This package does not authenticate AI attestations or claim cloud isolation. Protected external evidence and scoped runtime identities remain later implementation work.

Use [target configuration](governance/M1_CONFIGURATION.md), [ruleset target](governance/main-ruleset.target.json), [classic fallback](governance/branch-protection.target.json) and [initial issues](governance/INITIAL_ISSUES.md). Deploy one active strategy, not overlapping stale requirements. Actual hosted contexts/source app IDs must be observed before applying the final check-source configuration. No live setting is verified before readback and negative tests.
