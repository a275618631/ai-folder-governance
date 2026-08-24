# 7. Project workspaces

This optional module governs one project that spans two workspaces:

```text
One Project
├── Human Workspace   documents, decisions, briefs, approvals
└── Machine Workspace code, tests, automation, release artifacts
```

The providers can be different or the same. A document provider and a Git provider are examples, not requirements.

## Stable identity

Use a stable `project_id` that does not change when a display name, folder name, or repository label changes. Keep a human-readable `display_name` separate from the identifier.

## Source-of-truth separation

For each artifact class, declare one source of truth. For example, code and tests may be authoritative in the machine workspace while a decision record is authoritative in the human workspace. A copy, export, or link is not canonical merely because it is newer or easier to find.

## Reference integrity

Record how the two workspaces refer to each other: stable project identity, documented relative references, release or decision identifiers, and ownership. Before moving or renaming an item, check those references or leave the item untouched.

## Lifecycle review

A project review may classify a project as:

- `active`: current work with an identified owner;
- `related`: connected to another project but not ready to merge;
- `historical`: retained for context and no longer active;
- `archive`: retained under an intentional retention policy;
- `duplicate`: same identity and purpose with a stronger canonical candidate;
- `delete-candidate`: eligible for deletion only after explicit confirmation.

These labels are decisions with evidence, not automatic folder names.

## Identity template

Use [the example identity template](../../skills/ai-folder-governance/assets/project-identity.example.yaml) as a starting point. Replace generic values with the user's own values only in a private workspace. Do not publish real provider identifiers.
