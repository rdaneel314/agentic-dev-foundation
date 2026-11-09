# M1 sole owner protection targets

Target: public personal-Free repository, main branch, one human owner. Configuration remains prepared until final publication confirmation. Public Free supports branch rulesets and classic protections under current GitHub documentation.

## Preferred active main ruleset

- Branch target refs/heads/main; enforcement active; no bypass actors.
- Require pull request, required human approval count zero, no last-push or code-owner human approval requirement. Keep conversation resolution required.
- Require both actual successful Windows/Ubuntu Foundation CI jobs, strict/up-to-date checks and observed GitHub Actions integration ID. Expected contexts are foundation-checks (ubuntu-24.04) and foundation-checks (windows-latest); verify actual contexts instead of assuming them.
- Disallow non-fast-forward updates and branch deletion. No agent administrator, upstream writing identity, production secret or deployment authority.
- Read-only Actions token; checkout credentials not persisted; no Actions PR creation/approval, auto-merge, larger runner, self-hosted runner or paid storage additions.

Use main-ruleset.target.json after resolving source IDs. If rulesets cannot be applied through the authorized account/tool, use the equivalent classic branch-protection target with enforce_admins true, review count zero, require_last_push_approval false, strict checks, conversations and disabled force/deletion. Record the selected strategy; do not layer an old one-human-approval rule over it.

## Mandatory verification beyond native GitHub settings

Before every consequential merge, the human checks independent AI review, QA and security evidence for the exact commit. Missing, stale, blocking or unavailable evidence stops acceptance. Those attestations are currently human-inspected policy gates, not authenticated automated GitHub checks. This limitation must not be represented as technical role segregation.

The owner can edit settings and merge after native conditions pass; personal Free does not offer every organization-only actor restriction. Keep coding agents without upstream write/admin authority. A compromised human credential remains outside immutable enforcement. CI can be changed by PR code: independently inspect governance/CI changes and actual successful job conclusions, including no skipped or neutral substitute.

## Verify only after final publication confirmation

1. Independently reviewed bootstrap import under human control, then actual hosted CI. Record contexts, source integration, run and commit; resolve placeholders.
2. Apply one selected active protection strategy and read it back: PR required, approval count zero, last-push/code-owner false, strict two-source checks, conversations, no bypass and force/deletion disabled.
3. Test missing/failing checks and unresolved conversations block merge; a direct main update is rejected. AI evidence missing or stale must cause the human to withhold approval; GitHub alone does not enforce that policy.
4. Test force/deletion rejection on an authorized disposable protected branch with equivalent settings, never main. Test a clean PR only after independent AI/QA/security evidence and human disposition.
5. Verify no agent collaborators, admin credentials or workflow PR-approval permission were granted. Retain private settings/actor/run evidence and sanitized public summaries. Actual second-PC fresh setup remains a separate test.

Sources: [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [rules API](https://docs.github.com/en/rest/repos/rules).
