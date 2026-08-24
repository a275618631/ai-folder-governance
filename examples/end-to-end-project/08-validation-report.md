# Validation report

Result: `PARTIAL_WITH_UNRESOLVED_ITEMS`

## Post-conditions

- Approved five destinations exist: pass.
- Approved five source paths are handled as planned: pass.
- No unapproved file changed: pass.
- `meridian-config/` remained an opaque black box: pass.
- Historical root was not silently treated as active: pass.
- Stale README reference: fail; `REFERENCE_INTEGRITY_FAIL` remains open.
- Canonical report authority: unresolved; both candidates remain.

## Second run

The approved five moves produce no new move proposals: the stable subset is `NO_CHANGE_NEEDED_PROOF`. The stale reference and canonical-report question are reported again, so the overall result is a near no-op with two explicit unresolved items rather than a false `ORGANIZATION_PASS`.
