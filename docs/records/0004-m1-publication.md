# M1 publication and live verification

The owner explicitly authorized public repository creation and publication of the exact reviewed initial commit `7dfd0170f4ebeba09523ea0ff851c82302d10959`. The initial commit contains 63 reviewed files, Apache-2.0 LICENSE and NOTICE. It was pushed unchanged; subsequent status records are separate changes, never an amendment of that snapshot. Original local delivery packages and the reviewed ZIP remain preserved.

## Observed controls

- Hosted [bootstrap CI](https://github.com/rdaneel314/agentic-dev-foundation/actions/runs/42719200940) succeeded on Ubuntu and Windows: fresh locked dependency installation, compatibility, structural checks, 29 behavioral tests, YAML/CI checks, current-file secret scan and known-vulnerability audit.
- One active branch ruleset requires PRs, up-to-date checks from GitHub Actions integration 15368, conversation resolution, and prohibits force pushes and deletion. There are no bypass actors. Required human approvals are zero; last-push and code-owner approval requirements are disabled, preserving the approved sole-owner model.
- The required contexts are `foundation-checks (ubuntu-24.04)` and `foundation-checks (windows-latest)`, taken from successful hosted results rather than assumed names.
- A direct main push of an empty synthetic commit was rejected for missing PR and both required checks. Force-pushing and deleting a disposable branch under the same ruleset were rejected explicitly. Main was never used for force/deletion tests.
- Actions defaults are read-only; workflow PR creation/approval is disabled. Full-length action SHA pinning is required, and external-contributor runs require approval. No agent collaborators, deploy keys or new agent credentials were granted by this work. This does not prove absence of every pre-existing credential outside the repository.

## Negative PR results and remaining acceptance

The [disposable negative-test PR](https://github.com/rdaneel314/agentic-dev-foundation/pull/1) was closed without merge. Both required jobs failed the deliberate behavioral test (30 tests, exactly one intentional failure), and GitHub disabled merging. With its synthetic thread unresolved, GitHub explicitly displayed a conversation-resolution blocker. After resolving the synthetic thread, the failed required checks remained a separate blocker. These are observed UI/native gate results, not a claim of independently authenticated AI review. The disposable branch remains protected under the same ruleset for preservation of test evidence.

Independent review/QA/security and hosted CI of this separate status update, a clean protected PR merge, and the owner's second-PC transfer test remain open acceptance work.

## Limits retained

GitHub authenticates the configured CI source, not independent AI attestations. Independent review, QA and security evidence for the exact commit remain mandatory human-inspected policy gates. Separate Codex contexts share permissions and do not technically enforce segregation of duties. The sole human owner can edit repository settings; no claim of immutable human-only merging is made.

Hosted Windows checkout and fresh dependency installation are verified. Setup and work transfer on the owner's second physical Windows PC remain unverified; follow [the Windows clone test](../setup/WINDOWS_CLONE_TEST.md). No AWS, production deployment, paid model call or paid runner was used.

The hosted checkout action emitted a Node 20 deprecation warning while being run on Node 24. The approved pin was deliberately preserved during publication; review an action upgrade in a separate maintenance change.

Public branch protections/rulesets are supported on GitHub Free. Standard public-repository hosted runners are free; larger runners and other paid services are outside this authorization. See [GitHub ruleset availability](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository) and [runner billing](https://docs.github.com/en/actions/reference/runners/github-hosted-runners).
