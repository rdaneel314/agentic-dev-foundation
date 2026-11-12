# Current engineering status

M1 live publication verification, 12 November 2026. GitHub is the source of truth after the owner's explicit publication authorization. The original M0/M1 packages and reviewed publication snapshot remain preserved; this status update is a separate change.

## Completed locally

- Verified the original M1 ZIP and 59-file manifest and its local commit 9726f21. Prepared a separate revised candidate with the explicitly approved license and sole-owner governance changes documented in DECISIONS.md.
- Applied the official Apache-2.0 LICENSE and project attribution in NOTICE. Prepared the initial main commit using the confirmed GitHub identity and GitHub noreply format.
- Retained portable setup, fake task/finding contracts, CI, deterministic gates and P1 backlog. Final local verification and independent AI review results are recorded in the private publication review; no claim of deployed role isolation is made.

## Verified on GitHub

- Published the exact approved initial commit `7dfd0170f4ebeba09523ea0ff851c82302d10959`, containing 63 reviewed files, LICENSE and NOTICE.
- Bootstrap hosted CI passed on Windows and Ubuntu, including fresh hash-locked installation, all 29 tests, structural/link, YAML/CI, dependency, current-file secret and vulnerability checks.
- Active main ruleset: PRs, two strict required checks bound to GitHub Actions integration 15368, conversation resolution, no force pushes/deletion and no bypass actors. Zero required human reviews preserves the approved sole-owner model; mandatory independent AI review/QA/security remains a separate human-inspected gate.
- Direct-main, disposable force-push and disposable deletion attempts were rejected. The disposable PR exposed both failed required checks and an unresolved-conversation merge blocker. See [live verification](docs/records/0004-m1-publication.md).

## Remaining gates and limitations

Independent review/QA/security and hosted CI for this separate status change must pass before its acceptance. A successful clean PR merge remains to be observed. Actual setup/work transfer on the owner's second physical Windows PC remains unverified; hosted fresh Windows installation is verified. AI attestations are not authenticated by GitHub, and shared agent permissions are not technical isolation. No AWS, production deployment or paid inference is part of M1.

Next action: independently review and validate this status PR, record the clean protected-merge result, and complete the documented second-PC test without overstating portability. After M1 acceptance, implement the first sequential Temporal/Python workflow with a simulated model, rejection, recovery and human approval; no architecture reopening or AWS provisioning.
