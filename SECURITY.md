# Security policy

Only synthetic, non-sensitive inputs belong here. Public code, issues, PRs, logs and history must contain no credentials, private account details, proprietary requirements or customer information.

Do not file an exploitable vulnerability or credential in a public issue. Use GitHub private vulnerability reporting if the owner has enabled it; otherwise ask for a private reporting route without sensitive details. No private reporting channel is claimed to exist yet.

If a secret is exposed, revoke or rotate it through the authorized owner first. Deleting the file does not remove copies or history. Review access, coordinate cleanup and document the incident privately.

Security verification is independent of Engineering: secret and dependency checks plus independent review of permissions, input handling and execution boundaries. No scan proves absence of vulnerabilities. Static analysis, container scanning and isolation verification remain backlog tasks before generated application code is executed.
