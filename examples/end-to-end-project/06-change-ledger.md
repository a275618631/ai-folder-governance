# Change ledger

| ID | Actual result | Post-condition |
| --- | --- | --- |
| C-001 | Five role-based moves executed after approval. | Each destination exists; source paths are absent; no unapproved file changed. |
| C-002 | Not executed. | `meridian-config/` remains untouched. |
| C-003 | Not executed; review recommendation recorded. | Historical root remains available for review. |
| C-004 | Blocked. | `README.md` remains at the original path; stale reference remains visible for follow-up. |
| C-005 | Not executed. | Both report candidates remain available; no deletion or overwrite occurred. |
