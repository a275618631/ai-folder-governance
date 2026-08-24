# 1. Concepts

AI Folder Governance is a decision contract for file organization. It helps an agent decide what it knows, what it may change, and what evidence is required after a change.

## The core loop

```text
Understand → Classify → Plan → Ask when necessary → Execute → Validate
```

The loop is deliberately ordered. Moving files before understanding them destroys evidence that could have resolved ambiguity.

## Key terms

| Term | Meaning |
| --- | --- |
| Target | The explicitly bounded folder, set of folders, or project workspace under review. |
| Inventory | A read-only record of paths, metadata, content signals, ownership signals, links, and dependencies. |
| Canonical source | The item or location that is authoritative for a specific purpose. It must be supported by evidence. |
| Reference copy | A useful copy that points to or derives from a canonical source. It is not authoritative by default. |
| Change set | A proposed list of moves, renames, archive actions, or deletions with reasons and confidence. |
| Post-condition | A statement that must be true after an approved change, such as a preserved link or an empty source directory. |
| Material ambiguity | An unknown whose answer could change the target, action, ownership, source-of-truth choice, or risk. |
| No-op | A repeat run that finds no new approved change because the prior result is stable. |

## Core invariants

These rules are stronger than a folder taxonomy:

1. Content is stronger evidence than a filename.
2. Ownership is stronger evidence than topic similarity.
3. A canonical source is stronger than an existing copy.
4. Understand before move.
5. Preserve existing structure unless a change has clear value.
6. Do not cross the declared scope boundary.
7. Treat secrets and credentials as a black box.
8. Check path dependencies before moving or renaming.
9. Uncertainty means ask or leave untouched.
10. A scan pass is not an organization pass.
11. An inventory is not an execution report.
12. Every mutation needs a change set and post-condition evidence, or a `NO_CHANGE_NEEDED_PROOF`.
13. The second run should be close to a no-op.

## What the framework does not decide for you

It does not impose folders such as `active`, `archive`, or `reference` on every user. A useful taxonomy depends on the user's work, provider features, access model, and existing habits. The agent should discover preferences after inspection and ask only when the answer changes the result.

## Scope examples

- A direct-child cleanup of one folder is a narrow target.
- A weekly review of newly changed folders is an incremental target.
- A recursive review of a project tree is a deep target.
- A human document workspace paired with a machine repository is a project-workspace target.

The target must be named before inspection begins. “Organize everything” is not a safe scope.
