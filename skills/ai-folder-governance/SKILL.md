---
name: ai-folder-governance
description: Guide safe, provider-neutral AI inspection and organization of folders or project workspaces; use when a task involves classifying, moving, renaming, archiving, or validating files.
---

# AI Folder Governance

Use the user's language for interaction. This Skill governs decisions; it does not assume a provider, filesystem API, shell, or permission to mutate.

## Workflow

1. **Activate within scope.** Name the target and refuse vague scope such as “organize everything.” Recursive inspection is allowed only inside the explicitly approved target.
2. **Inspect read-only.** Build a bounded inventory before proposing a move. Load [core rules](references/core-rules.md) and [safety invariants](references/safety-invariants.md).
3. **Discover material preferences.** Load [preference discovery](references/preference-discovery.md) only when a choice could change the result.
4. **Select a mode.** Use [organization modes](references/organization-modes.md); never widen scope or depth silently.
5. **Plan and ask.** Separate facts, inferences, confidence, and unresolved questions. Produce a dry-run change set with pre-conditions and post-conditions. A duplicate proposal is not deletion permission. Wait for approval, and require it to be explicit and item-specific, before moving, renaming, archiving, overwriting, or deleting.
6. **Execute narrowly.** Re-check each pre-condition, keep a change ledger, and stop on unexpected collisions, dependency uncertainty, or scope drift.
7. **Validate and report.** Load [acceptance gates](references/acceptance-gates.md). Re-scan, verify post-conditions and out-of-scope integrity, report untouched items, and confirm that a second run is close to a no-op.

## Optional project-workspace route

When one project spans a human workspace and a machine workspace, load [project workspaces](references/project-workspaces.md). Do not assume that either workspace is canonical for every artifact class.

## Safety boundary

Treat credential stores, private configuration, key material, session data, and marked-sensitive files as a black box. Use metadata only when possible and never reproduce sensitive contents in output. Safety invariants cannot be disabled by user configuration. If required evidence or capability is unavailable, leave the affected item untouched and report the limitation.
