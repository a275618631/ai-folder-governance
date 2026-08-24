# Tests

The repository separates deterministic checks from behavioral evaluation.

## Layer A — Deterministic Repository Validation

Automated in CI by `scripts/validate_repo.py`. It checks repository structure, bilingual documentation pairs, local Markdown links, Skill package references, prompt contract markers, regression-specification presence, fixture shape, and basic publication-safety patterns.

## Layer B — Behavioral Regression Specifications

Defined in [regression-cases.md](regression-cases.md). R-001 through R-014 describe expected agent decisions such as scope boundaries, canonical-source uncertainty, path dependency failures, no-op stability, and unavailable write capability. These are manual or agent-verification specifications; they are not automatically executed AI behavior tests.

## Layer C — Real Runtime Verification

The current release records fixture-backed checks performed in the Codex runtime in [runtime-verification.md](runtime-verification.md). This is a bounded runtime check, not a benchmark and not evidence that every compatible agent or provider behaves identically.

## Running Layer A

```bash
python3 scripts/validate_repo.py
```
