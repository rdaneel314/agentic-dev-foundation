# Public disclosure review checklist

Publication is a human decision about the exact payload. A clean scanner is supporting evidence, not clearance. Use a new staging directory containing only the public payload; never stage its parent or private companion folder.

- [ ] Compare files to the accepted manifest; inspect hidden files, filenames and archive entries. Exclude private planning, local evidence copies, environments, logs and credentials.
- [ ] Read the full diff and content for account/infrastructure identifiers, private contacts/endpoints, proprietary requirements, customer data, internal notes and non-public decisions. Generic architecture must be explicitly acceptable for disclosure.
- [ ] Review commit author metadata and every imported history object. Before a first publication use clean reviewed history; scan any later imported history separately.
- [ ] Run structural/link, tests, YAML/CI, dependency compatibility/lock, secret and strict vulnerability checks. Tool failure or unresolved blocker is not a pass.
- [ ] Inspect CI changes independently: read-only token, pinned actions, no secrets/deployment/privileged triggers and no failure suppression. Green PR checks can be weakened by PR code.
- [ ] Verify approved Apache-2.0 LICENSE, project attribution and rights to included material; retain third-party notices as applicable.
- [ ] Confirm independent AI reviewer, QA/security evidence and human owner disposition. No agent self-approval or waiver of independent verification. GitHub requires no unavailable second human approval. Verify live check names/settings after final publication confirmation.
- [ ] Compare regenerated public archive and manifest with the final tree. Any edit after acceptance invalidates the relevant evidence and approval.
- [ ] Human records accept/reject for the exact manifest/commit, disclosure scope and permitted external actions. Keep the actual approval record private; publish only a safe summary.

Current automated checks inspect current files only, use heuristic secret/data patterns, and do not classify business confidentiality or inspect remote accounts. They do not establish legal rights, reviewer identity, configured branch protection, cloud isolation or authorization to push.
