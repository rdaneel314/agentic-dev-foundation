# Agentic Development Foundation

A public-safe starter for a controlled AI engineering workflow: request → requirements → architecture → implementation → independent review → QA and security verification → evidence → human decision.

This is a foundation scaffold. It does not yet contain an autonomous agent runtime, cloud deployment or production release pipeline. Only synthetic, non-sensitive examples belong here.

- [Architecture and role boundaries](docs/architecture.md)
- [Governance and branch protection](docs/governance.md)
- [Implementation backlog](docs/backlog.md)
- [Security policy](SECURITY.md)
- [Future model compatibility](docs/model-compatibility.md)
- [Evidence template](docs/evidence-template.md)
- [Local verification results](docs/verification.md)
- [Persistent instructions](AGENTS.md), [status](PROJECT_STATUS.md), [roadmap](ROADMAP.md), [decisions](DECISIONS.md)
- [New computer](docs/setup/NEW_COMPUTER.md) and [switching computers](docs/setup/SWITCHING_COMPUTERS.md)
- [Roles](agents/README.md), [cross-agent findings](docs/CROSS_AGENT_REPORTING.md), [contracts](workflows/README.md)
- [Disclosure checklist](docs/PUBLIC_DISCLOSURE_CHECKLIST.md) and [approved license](LICENSE)
- [M1 governance targets](docs/governance/M1_CONFIGURATION.md), [initial issue drafts](docs/governance/INITIAL_ISSUES.md) and [fresh Windows clone test](docs/setup/WINDOWS_CLONE_TEST.md)

## Local checks

Python 3.13.x. Standard-library checks from the public repository root:

```text
python -m unittest discover -s tests -v
python scripts/check_foundation.py
```

Prepared Windows/Ubuntu CI also validates YAML and dependency closure, checks secrets and audits locked dependencies. See [CI scope](docs/ci.md) and [dependencies](docs/DEPENDENCIES.md). Passing scaffold checks do not demonstrate a functioning multi-agent system or independent execution authority.

Engineering cannot approve its own work. Independent review and passing checks precede the human merge decision. No agent may change its own permissions, launch paid resources or deploy to production.

Licensed under [Apache-2.0](LICENSE). Project owner: rdaneel314; see [NOTICE](NOTICE). Only public-safe generic source and synthetic material belong here.

Current state: final local publication candidate, awaiting the human owner's explicit confirmation to publish. No remote, hosted CI, branch protection or cloud isolation is claimed verified. The sole human owner uses independent AI review, QA and security evidence, then makes the final decision. GitHub requires PRs, checks and conversation resolution; it will not require an unavailable second human approval. See the [governance model](docs/governance.md).
