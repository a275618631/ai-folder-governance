# Security Policy

## Scope and privacy boundary

AI Folder Governance is a governance framework, not a privacy boundary around the host runtime.

This repository itself does not receive, store, or transmit user files or credentials. The agent runtime, filesystem tool, cloud service, or model provider selected by the user may process or transmit permitted file contents according to its own privacy and data-handling policies.

Review the host runtime and connected provider policies before using the framework with sensitive material. The Skill's black-box rules reduce unnecessary exposure; they cannot change how an external runtime handles data.

## Reporting a vulnerability

Use the repository's [GitHub Security tab](https://github.com/a275618631/ai-folder-governance/security) and choose **Report a vulnerability** for a private report. Do not include credentials, tokens, cookies, private links, personal data, or full file contents in a public issue.

If the private reporting control is unavailable, do not disclose details publicly. Use a private channel with the repository owner and state that the GitHub private-reporting feature was unavailable.

When reporting, include:

- the affected file or workflow;
- a minimal, fictional reproduction;
- the expected safe behavior;
- the observed behavior and impact.

## Safety expectations for contributions

Contributions must keep destructive actions behind explicit confirmation, avoid provider-specific secrets or identifiers, and preserve the distinction between inspection, planning, execution, and validation.
