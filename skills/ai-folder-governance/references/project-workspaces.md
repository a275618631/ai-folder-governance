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
