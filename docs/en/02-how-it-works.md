# 2. How it works

## Six phases

### 1. Understand

Inspect read-only within the declared scope. Capture paths, file types, timestamps, sizes, visible headings, ownership signals, links, duplicate indicators, and possible path dependencies. Do not open secret-bearing content merely to improve classification.

### 2. Classify

Classify by purpose and authority, not only by topic. Useful labels include working material, canonical source, reference, export, historical record, archive candidate, duplicate candidate, and unresolved.

Record the evidence and confidence for each label. A guessed label is not a fact.

### 3. Plan

Choose the smallest organization mode that satisfies the request. Produce a dry-run change set with:

- current path and proposed path;
- action type;
- reason and evidence;
- confidence;
- dependency impact;
- required user decision;
- post-condition.

### 4. Ask when necessary

Ask only material questions. For example, whether to archive old project material can be material; whether a user prefers one of two equivalent folder names is not material unless a rename is proposed.

### 5. Execute

Wait for explicit approval before moving, renaming, archiving, or deleting. Apply one approved change at a time or in a recoverable batch. Keep a change ledger and stop if an expected pre-condition is false.

### 6. Validate

Re-scan the target. Verify that approved destinations exist, source items are handled as planned, links and path dependencies remain valid or are intentionally updated, no out-of-scope item changed, and the report matches the actual result.

## Organization modes

| Mode | Boundary | Best use |
| --- | --- | --- |
| `SHALLOW_ORGANIZE` | Direct children only | A bounded one-folder cleanup. |
| `INCREMENTAL_MAINTENANCE` | New or recently changed items | Routine maintenance with low disruption. |
| `RECURSIVE_DEEP_ORGANIZE` | Full recursive tree | A deliberate project or archive review. |
| `PROJECT_LIFECYCLE_REVIEW` | Project identities and lifecycle | Decide active, related, historical, archive, duplicate, or delete-candidate status. |

Never silently widen a shallow request into a recursive operation. If a deeper view is required, explain why and ask before expanding scope.

## Stable result states

- `SCAN_PASS`: inspection completed within scope.
- `PLAN_READY`: dry-run change set is ready for review.
- `WAITING_FOR_APPROVAL`: a mutation is proposed but not authorized.
- `ORGANIZATION_PASS`: approved changes were executed and validated.
- `PARTIAL_WITH_UNRESOLVED_ITEMS`: safe work completed; ambiguous or blocked items remain untouched.
- `NO_CHANGE_NEEDED_PROOF`: no mutation is justified, with evidence.

## Idempotency check

After execution, run the same inspection logic again. A stable result should show no new move or rename proposal unless new files, new evidence, or a changed preference exists. If every run proposes another rearrangement, the taxonomy or acceptance criteria is not stable enough.
