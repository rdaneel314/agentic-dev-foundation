# Engineering roadmap

This file owns milestones; [backlog](docs/backlog.md) preserves P1 task IDs and detailed acceptance. No listed milestone grants external authority.

| Milestone | Scope | Exit evidence | Status |
| --- | --- | --- | --- |
| M0 | Portable local foundation | Reconciled public/private boundary; instructions, schemas, checks, provenance and preservation evidence | Provisionally accepted; verification limits retained |
| M1 / P1-03 | Protected GitHub foundation | Approved payload/license; authorized public remote; actual required CI checks; independent reviewer; rejection cases; clean clone and computer-switch evidence | Revised licensed candidate prepared; final explicit publication confirmation pending; live protections/CI/portability unverified |
| M2 / P1-04/07/08/12/15 | One sequential synthetic workflow | Temporal/Python with fake model Activities; bounded retries, crash/replay, side-effect deduplication, stale/self-approval rejection and authenticated human gate design | Not implemented |
| M3 / P1-05/06/09/13/14 | Bounded cloud execution | Authorized disposable worker, durable task/evidence state, temporary permissions, isolation negative tests, verified cleanup and approved cost exposure | Deferred |
| M4 / P1-16 | Synthetic end-to-end pilot | Roles pass one task through independent review, QA/security, repair/recovery and human decision | Deferred |

Cloud activation is not required for local checks or GitHub preparation. Multiple models and rented GPU inference remain adapter options requiring later measured quality/cost justification and explicit authorization. No OpenClaw, Hermes, Kubernetes, dashboard or extra scheduler is part of M0.
