# Acceptance gates

Use these gates to keep scanning, planning, execution, and validation separate.

## Preflight gate

Pass only when:

- the target and mode are explicit;
- the allowed read and write scope is known;
- the agent can perform the required inspection safely;
- sensitive and dependency boundaries are recognized;
- material preferences are resolved or clearly marked;
- no mutation has happened during inspection.

Failure result: `SCAN_BLOCKED` with the evidence gap and untouched items.

## Plan gate

Pass only when every proposed mutation has a current path, destination or action, reason, evidence, confidence, dependency assessment, approval requirement, and post-condition. A plan may include no-op entries when they explain why an item remains in place.

Failure result: `PLAN_INCOMPLETE`; do not ask for broad approval of an underspecified plan.

## Approval gate

Approval must identify the change set or individual items. “Go ahead” is not enough when the report contains multiple materially different actions. Deletion and overwrite require item-specific confirmation.

Failure result: `WAITING_FOR_APPROVAL`.

## Execution gate

Before each action, confirm that the source, destination, content, dependency state, and scope still match the approved plan. Stop on a collision or unexpected state. Record actual results rather than assuming success.

Failure result: `PARTIAL_WITH_UNRESOLVED_ITEMS`.

## Post-condition gate

Pass only when:

- every approved destination or archive location exists;
- source handling matches the plan;
- references and dependencies remain valid or are intentionally updated;
- no unapproved or out-of-scope item changed;
- the change ledger matches actual observations;
- unresolved items and limitations are reported.

Failure result: `VALIDATION_FAILED`; do not report `ORGANIZATION_PASS`.

## No-change gate

Use `NO_CHANGE_NEEDED_PROOF` only when the inventory, evidence, preference state, and stability check explain why no mutation is justified.
