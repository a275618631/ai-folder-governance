# Project workspaces

This reference applies only when one project spans a human workspace and a machine workspace.

## Identity contract

Keep these concepts separate:

- `project_id`: stable identifier;
- `display_name`: human-facing label;
- `human_workspace`: location for briefs, decisions, approvals, or supporting documents;
- `machine_workspace`: location for code, tests, automation, or release artifacts;
- `sources_of_truth`: one authoritative workspace per artifact class.

Use the provider-neutral template in [project-identity.example.yaml](../assets/project-identity.example.yaml).

## Review method

1. Confirm the project identity from explicit evidence.
2. Inspect both workspaces independently and read-only.
3. Map artifact classes to their source of truth.
4. Record cross-workspace references and owners.
5. Classify copies as canonical, reference, export, historical, or unresolved.
6. Ask before changing identity, ownership, retention, or cross-references.
7. Validate both sides independently after approved execution.

## Provider neutrality

A document provider, issue tracker, Git host, local folder, or other workspace is valid if the user can identify its boundaries and authority rules. Do not hard-code provider assumptions into the governance model.

## Cross-workspace safety

Do not expose real provider identifiers or private links in public reports. A local verification cannot substitute for remote verification. If one side cannot be read or validated, say so and leave the affected relationship unresolved.

## Project-local unresolved issues and approval gates

A cross-project summary is a navigation and aggregation view, **not** the sole authoritative backlog. Every unresolved contradiction, dependency, permission restriction, manual acceptance gate, or approval decision must be discoverable from the **owning project's existing canonical status entry or approved issue/task tracker**. Reuse the project's declared source of truth; do not create a parallel `CURRENT`, new issue registry, or global queue.

For each material unresolved item, record or link to the existing record containing:

- a stable item ID and project identity;
- an accurate current state (e.g. `OPEN`, `BLOCKED`, `WAITING_FOR_APPROVAL`, `CONFLICT`, or `UNVERIFIED`, retaining the project's own vocabulary);
- the precise discrepancy/restriction, its impact and evidence level;
- authoritative links or repo-relative paths to branch, commit, PR, tests, decisions, or relevant human-workspace record;
- the responsible actor/approval authority, prerequisites, next action, acceptance gate, and last verification date.

A human workspace may be canonical for decisions and progress, while a Git repository is canonical for implementation and test state. **Link to both instead of copying technical claims into an independent status truth.** Distinguish committed code, open PR, mock tests, real integration tests, and production acceptance. Never infer that documentation, a passing unit test, or a successful local run has resolved an external permission or human-acceptance gate.

The cross-project roll-up may cite those project-local records and show summary status, but must point back to them; a blocker found only in the roll-up is an **information-integrity gap**, not a resolved item. On mismatch, report `CONFLICT`; when evidence or access is insufficient, report `UNVERIFIED` and keep the gate open. Updating a status document is not authorization to merge PRs, deploy, change permissions, or mark the underlying technical issue resolved.
