# Organization modes

Choose the smallest mode that satisfies the request.

## `SHALLOW_ORGANIZE`

Inspect and plan only direct children of the target folder. Do not recurse. Use for bounded cleanup where the user wants minimal disruption.

## `INCREMENTAL_MAINTENANCE`

Inspect only new or recently changed items within an explicit set of folders. Compare with a trusted prior ledger when available; otherwise state that the baseline is missing. Do not redesign the whole tree.

## `RECURSIVE_DEEP_ORGANIZE`

Inspect the full recursive tree under one approved target. Recursive inspection is allowed inside that target, but never outside it. Do not follow external links or enter another workspace without explicit approval. Use when relationships, nested structure, or canonical-source evidence cannot be understood at a shallower depth.

## `PROJECT_LIFECYCLE_REVIEW`

Review project identity, ownership, source-of-truth boundaries, cross-references, and lifecycle. Classify as active, related, historical, archive, duplicate, or delete-candidate. Do not treat a label as permission to mutate.

## Mode selection output

Report the selected mode, why it is sufficient, the boundary it creates, and what it intentionally excludes. For recursive mode, state that recursion stops at the target boundary. If a deeper mode would reduce uncertainty, ask before switching.
