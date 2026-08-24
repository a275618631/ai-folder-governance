# Change ledger

Target: `example-folder`
Mode: `SHALLOW_ORGANIZE`
Approval: `pending`

| ID | Current path | Proposed path | Action | Reason | Approval | Actual result | Post-condition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-001 | `notes/meeting-draft.md` | `working/meeting-draft.md` | move | Content is an active draft; no canonical conflict found. | pending | not executed | Source is absent; destination exists; references remain valid. |
| C-002 | `exports/summary.pdf` | unchanged | no-op | Export is useful but authority is unproven. | not needed | unchanged | Original path and contents remain intact. |

## Unresolved items

- `secrets/` is a black box and was inspected only through metadata.
- A relative link to an unlisted folder could not be checked safely.
