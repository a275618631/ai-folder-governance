# 5. Prompt guide

The prompt pack is designed for agents that can inspect a filesystem, a connected document workspace, or a user-provided inventory. Each prompt can be used without the Skill.

## Choose a prompt

| Prompt | Use it when |
| --- | --- |
| [01-single-folder-deep-organize](../../prompts/01-single-folder-deep-organize.md) | One folder needs a deliberate deep review. |
| [02-multi-folder-maintenance](../../prompts/02-multi-folder-maintenance.md) | Several folders need incremental maintenance. |
| [03-web-review-and-local-handoff](../../prompts/03-web-review-and-local-handoff.md) | One agent can review remotely and another can perform local changes. |
| [04-project-lifecycle-review](../../prompts/04-project-lifecycle-review.md) | Project folders need lifecycle decisions. |
| [05-project-workspace-governance](../../prompts/05-project-workspace-governance.md) | One project spans human and machine workspaces. |

## What a prompt should preserve

When adapting a prompt, keep these clauses even if the wording changes:

- identify the target and scope;
- perform read-only inspection first;
- classify by content, ownership, authority, and dependencies;
- distinguish facts, inferences, and unresolved questions;
- choose a mode explicitly;
- produce a dry-run change set;
- ask before material ambiguity and mutation;
- protect secrets and path dependencies;
- validate post-conditions and report untouched items;
- make a second run close to a no-op.

## Supplying context safely

Provide the target description, relevant preferences, and the smallest useful inventory. Do not paste credential contents, private links, session data, or unrelated personal information into a prompt. If the agent cannot safely inspect a dependency, state that it must leave the item untouched.

## Reviewing a response

A useful response has four separate sections: inventory, reasoning and uncertainty, proposed change set, and validation report. Reject a response that jumps directly to “done,” hides assumptions, or treats a filename as proof of canonical status.
