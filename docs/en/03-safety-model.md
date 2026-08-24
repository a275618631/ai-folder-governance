# 3. Safety model

The safety model protects meaning, access, and recoverability. It is part of the framework's contract, not an optional preference.

## Safety invariants

### Scope boundary

Only inspect and mutate the target named by the user. Do not follow a link into another workspace or recurse into a child tree unless the selected mode and approval allow it.

### Secret black box

Treat credential stores, private configuration, key material, session files, and files explicitly marked sensitive as opaque. Prefer metadata, filenames, or an approved inventory signal. Never copy, print, index, summarize, or include their contents in a report.

### Path dependency gate

Before a move or rename, check for references that may break: relative links, scripts, imports, manifests, shortcuts, automation inputs, and documented paths. If the dependency cannot be checked safely, leave the item in place and report the uncertainty.

### Canonical-source protection

Do not replace or delete a source because another file looks newer, cleaner, or more complete. Establish authority from explicit metadata, ownership, references, version history, or user confirmation.

### Destructive-action gate

Deletion requires explicit confirmation. “Delete duplicates” is not sufficient approval for an irreversible action when identity, retention, or references are uncertain. Prefer a reversible archive or a report of candidates.

## Approval levels

| Action | Default | Approval |
| --- | --- | --- |
| Read metadata and permitted content | Allowed within scope | No additional approval. |
| Produce an inventory or dry run | Allowed | No mutation approval needed. |
| Create a report or change ledger | Allowed in the chosen report location | No mutation approval needed. |
| Move or rename | Not automatic | Explicit approval of the change set. |
| Archive | Not automatic | Explicit approval, unless an existing policy clearly authorizes it. |
| Delete or overwrite | Blocked by default | Explicit, item-specific confirmation. |

## What to do when a scan fails

A scan failure is not permission to guess. Stop at the smallest safe boundary, report what was inspected, identify the missing evidence, and leave unverified items untouched.

## Validation is separate from scanning

Passing a preflight scan proves only that the agent could inspect the target under the declared rules. It does not prove that an organization is correct. A successful organization needs:

1. approved actions;
2. actual mutation evidence;
3. post-condition checks;
4. an out-of-scope check;
5. a clear list of unresolved items.

## Recovery-minded behavior

Use the least destructive operation that meets the goal. Preserve original names in the ledger, make batches small enough to review, and stop on an unexpected collision. If a provider cannot guarantee safe rollback, do not imply that rollback is available.
