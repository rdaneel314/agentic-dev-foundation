"""Small specification of readiness; never grants merge or deployment rights."""


def ready_for_human(author, reviewer, reviewed_commit, current_commit,
                    tests_passed, security_passed, findings_open=0, *,
                    qa_identity=None, security_identity=None,
                    qa_commit=None, security_commit=None):
    identities = (author, reviewer, qa_identity, security_identity)
    if any(not isinstance(value, str) or not value.strip() for value in identities):
        return False
    if len({value.strip().casefold() for value in identities}) != 4:
        return False
    return bool(
        isinstance(current_commit, str) and current_commit.strip()
        and current_commit and reviewed_commit == current_commit
        and qa_commit == current_commit and security_commit == current_commit
        and tests_passed is True and security_passed is True
        and type(findings_open) is int and findings_open == 0
    )
