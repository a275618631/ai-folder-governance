# Preference discovery

Discover preferences after a read-only pass and before a plan that depends on them.

## Ask only material questions

Ask if the answer could change:

- target or recursion depth;
- whether existing structure is preserved;
- whether an item is archived or kept in place;
- whether a rename is needed and how it should look;
- whether a destructive action is allowed.

Do not ask for preferences that do not affect the proposed change set.

## Dimensions

```text
restructure: preserve-first | moderate | redesign
depth: current | one-level | recursive
archive: keep-in-place | archive | ask-per-item
delete: confirm (default)
naming.language: keep | user-selected language
naming.date_prefix: never | when-useful | always
naming.style: concise | descriptive
delete.exact_duplicates: propose (default)
```

## Save choice

Offer `Save preferences for this folder` or `Session only`. If saved, explain the target and the next run that will use it. A preference file is not a grant of access or proof of canonical status.

## Invalid or conflicting preferences

Report unknown keys and invalid values. If preferences conflict, prefer the safer interpretation and ask before planning a materially different result. Never allow a preference to disable secret protection, scope boundaries, dependency checks, approval gates, or validation.

`delete.exact_duplicates: propose` permits the agent to list candidates for review; it never authorizes deletion.
