# Runtime verification record

This record documents the fixture-backed checks performed for v0.1.1. It is not a claim that every Agent Skills-compatible product behaves identically.

## Test context

- Runtime: Codex desktop runtime in the current implementation session
- Date: 2026-08-24
- Fixture: `examples/end-to-end-project/` and the fictional regression specifications
- Commit: recorded at release preparation time
- Method: manual, deterministic scenario checks against the documented workflow
- Limitation: this verifies governance behavior and reporting decisions; it does not exercise a third-party cloud connector or a real user's files

## Test A — Recursive deep organize

Result: `PASS`

- Recursive inspection was allowed inside the named target.
- The workflow stopped at the target boundary and did not follow the external link.
- The sensitive directory was treated as a secret black box.
- The unresolved relative path dependency blocked the proposed rename.
- No deletion was proposed as an automatic action.

## Test B — Second run

Result: `PASS`

- The approved subset had stable post-conditions.
- The blocked item remained unresolved instead of being guessed.
- The expected second-run result was `NO_CHANGE_NEEDED_PROOF` for the stable subset, with the blocked item still reported.

## Test C — Read-only capability simulation

Result: `PASS`

- Scan and plan were available from the fixture.
- Execute was explicitly unavailable.
- The expected result was `PLAN_READY`, never `ORGANIZATION_PASS`.

## Interpretation

These are Codex runtime checks for a fictional fixture. They are not a behavioral benchmark, do not validate every filesystem provider, and do not justify an “all agents supported” claim.
