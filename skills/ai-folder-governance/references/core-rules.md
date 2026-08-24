# Core rules

These rules apply to every organization mode.

## Evidence hierarchy

Use the strongest available evidence in this order, while recognizing that no single signal is always decisive:

1. explicit user or owner declaration;
2. source-of-truth and lifecycle metadata;
3. authoritative references from related artifacts;
4. content and structure;
5. version history or change evidence;
6. filename and folder position;
7. topic similarity alone.

Record conflicting evidence rather than hiding it.

## Required distinctions

- An inventory describes what was observed.
- A classification explains how evidence was interpreted.
- A plan proposes what could change.
- An approval authorizes a specific change set.
- An execution report records what actually changed.
- A validation report proves post-conditions.

Do not collapse these into a single “done” statement.

## Stable organization

Prefer categories that remain meaningful when new files arrive. Avoid creating a new folder for every small topic, date, or filename variation. Preserve existing structure when the benefit of change is unclear.

## Idempotency

A plan is idempotent when applying it once makes the same plan unnecessary on the next run. Use stable destination rules, avoid sorting by unstable timestamps alone, and record why an item was intentionally left in place.

## Output vocabulary

Use `SCAN_PASS`, `PLAN_READY`, `WAITING_FOR_APPROVAL`, `ORGANIZATION_PASS`, `PARTIAL_WITH_UNRESOLVED_ITEMS`, and `NO_CHANGE_NEEDED_PROOF` consistently. These are reporting states, not permissions.
