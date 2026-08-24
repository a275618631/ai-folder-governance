# 4. Preferences

Preferences shape organization choices; they cannot disable safety invariants.

## Discover preferences progressively

1. Inspect read-only.
2. Infer what can be inferred without asking.
3. Ask only the smallest set of questions that could materially change the plan.
4. Offer session-only use or saving preferences for the target folder.

Do not ask every user every question on every run.

## Preference dimensions

| Dimension | Options | Ask when |
| --- | --- | --- |
| Restructure level | `preserve-first`, `moderate`, `redesign` | Proposed destinations would change existing structure. |
| Depth | `current`, `one-level`, `recursive` | The requested boundary is not explicit. |
| Archive | `keep-in-place`, `archive`, `ask-per-item` | Older or historical items need a lifecycle decision. |
| Delete | `confirm` by default | Any deletion or overwrite is proposed. |
| Naming language | `keep`, a chosen language | A rename is necessary and language affects findability. |
| Date prefix | `never`, `when-useful`, `always` | A rename is necessary and dates improve retrieval. |
| Naming style | `concise`, `descriptive` | A rename is necessary and both styles are plausible. |

## Example configuration

The file is optional and applies only to the intended folder or session:

```yaml
version: 1

organization:
  depth: recursive
  structure_policy: preserve-first

archive:
  strategy: semantic

delete:
  mode: confirm
  exact_duplicates: allow

naming:
  language: keep
  date_prefix: when-useful
  style: descriptive

safety:
  secret_black_box: true
  check_path_dependencies: true
```

An agent may suggest saving the configuration after the first review. The user should be able to choose `Save preferences for this folder` or `Session only`.

## Configuration rules

- Unknown keys should be reported, not silently interpreted.
- Invalid values should stop planning for the affected preference.
- Safety keys are assertions, not switches; setting them false must not disable the corresponding invariant.
- A preference file is not proof of authority, ownership, or permission to delete.
- A later run should explain which saved preference affected the plan.
