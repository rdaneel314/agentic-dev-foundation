# Contributing

Use an issue with acceptance criteria, a topic branch and a PR targeting main. Attach sanitized test and security evidence for the exact commit. A separate reviewer evaluates the implementation; QA verifies acceptance and failure paths. Human approval is required to merge.

Do not commit credentials, private requirements, account identifiers, customer data, internal endpoints or raw agent transcripts. Use synthetic fixtures. Review the entire diff before pushing: CI runs after disclosure and cannot undo a leak.

Workflow, permission and scanner changes receive independent security review. Tool failures and missing evidence block readiness. See docs/governance.md.

Read the four root continuity files before work; update status/backlog/decisions and sanitized records as relevant. Follow [setup](docs/setup/NEW_COMPUTER.md), [computer switching](docs/setup/SWITCHING_COMPUTERS.md), [complete checks](docs/ci.md) and [finding reporting](docs/CROSS_AGENT_REPORTING.md). Independent AI review, QA and security verification remain mandatory under the sole human owner's oversight; no prompt-only segregation is claimed. Apache-2.0 is approved; see [license](LICENSE) for reuse conditions.
