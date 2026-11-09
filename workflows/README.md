# Portable workflow contracts

[Task schema](schemas/task.schema.json) and [finding schema](schemas/finding.schema.json) use JSON Schema Draft 2020-12 and a deliberately small subset: object/array/string/integer/boolean types, required/properties/additionalProperties, enum, pattern, minLength, minItems, minimum and items. No external schema references are needed.

`python scripts/validate_contract.py task workflows/examples/task.json` and `python scripts/validate_contract.py finding workflows/examples/finding.json` validate synthetic examples with the included standard-library subset validator plus domain rules. Unsupported schema keywords fail rather than silently disappearing. This is not a general JSON Schema implementation or a running workflow engine.

Task state direction remains RECEIVED → REQUIREMENTS_READY → DESIGN_READY → IMPLEMENTED → INDEPENDENT_REVIEW → VERIFIED → AWAITING_HUMAN → ACCEPTED/REJECTED, with BLOCKED/REWORK for failures. M0 validates record shape, never authorizes or executes a transition. Allowed paths must be relative and cannot escape. Initial side-effect authority is `none`.

Findings identify severity, affected artifact, evidence, owner, blocker, status and disposition. Critical/high findings must carry a blocking flag; a resolved finding needs an independent verifier and disposition evidence. Identity strings and references are untrusted inputs until an external authenticated evidence boundary verifies them. Future Temporal execution must enforce transitions and authenticated approvals separately.

The readiness predicate is a deterministic specification only. It compares Engineer, Reviewer, QA and Security identities and exact artifact references, but cannot authenticate them or protect its own inputs. Separate Code Review, QA and Security contexts/credentials and human authority remain required.
