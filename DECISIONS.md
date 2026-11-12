# Generic engineering decisions

One register for this public candidate. Project-specific and non-public decisions remain private. Prepared architecture is not deployed capability.

| ID | State | Decision and consequence |
| --- | --- | --- |
| E001 | Retained direction | Codex engineering; Git/GitHub store source and durable sanitized project knowledge; each computer uses an independent clone. |
| E002 | Retained direction | Temporal is intended durable workflow engine; Python workers, PostgreSQL task state and object-storage evidence. No runtime introduced in M0. |
| E003 | Mandatory policy | Independent code review, independent QA and security assessment precede human acceptance. No agent self-approval or waiver of independent verification. GitHub human approval counts are distinct from required independent AI review. |
| E004 | Mandatory policy | Material decisions, external changes, spending, license, publication and production stay under explicit human authority. Coding agents have no production authority. |
| E005 | Reconciliation choice | Use Package 2 behavior/security foundation; adapt Package 1 portable startup, continuity, task contract and setup procedures. Preserve original P1 backlog IDs. |
| E006 | Reconciliation choice | Python 3.13.x, standard-library runtime, separate CI tool input and complete transitive version/hash lock. See dependency documentation for regeneration and verification limits. |
| E007 | Security design | Prompts and Codex subagents do not create independent permission boundaries. Future independent jobs need scoped identities/credentials, isolated workspaces and protected evidence. |
| E008 | Reconciliation choice | Explicit failures replace validation assertions so optimized Python cannot remove gates; links cannot escape the repository. |
| E009 | Boundary | Generic instructions, schemas and sanitized engineering records belong in public Git; actual accounts, operational planning, raw evidence and non-public decisions do not. |
| E010 | Owner approved and applied | Apache-2.0 applied to the original framework; exact LICENSE and project-owner attribution in NOTICE. No invented legal identity or third-party rights. |
| E011 | Deferred | No OpenClaw or Hermes adoption; future providers and rented GPU endpoints stay behind a tested capability-aware adapter. |
| E012 | Historical preparation scope; external restriction superseded by E015 | M0 is the provisional canonical base. Prepare local Git history and publication/governance artifacts in a separate candidate; retain M0 unchanged. At that stage external actions were not authorized. |
| E013 | Owner confirmed; publication executed under E015 | rdaneel314/agentic-dev-foundation, public, main; Apache-2.0. Use confirmed GitHub identity and ID-based noreply for initial commit. |
| E014 | Supersedes earlier second-human requirement | Sole human owner plus independent AI Reviewer, QA and Security. PRs/checks/conversation resolution enforced by GitHub; required human approvals zero, last-push approval false. Mandatory independent AI evidence and human final decision remain. |
| E015 | Explicit owner authorization; observed 2026-11-09 through 2026-11-12 | Publish exactly initial commit 7dfd0170f4ebeba09523ea0ff851c82302d10959 and configure/verify M1 GitHub governance. Initial publication is unchanged. Status updates use separate commits and normal PR controls. No agent upstream privileges, AWS provisioning or paid cloud services are authorized. See record 0004 for observed results and limits. |

For changes, append date, authority, rationale, consequences and evidence; mark superseded entries rather than erasing history. Do not fabricate missing historical ADR bodies. Consult [license decision](docs/LICENSE_DECISION.md), [architecture](docs/architecture.md) and [governance](docs/governance.md).
