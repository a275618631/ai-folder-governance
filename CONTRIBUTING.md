# Contributing

Thank you for helping improve AI Folder Governance.

## Before opening a change

- Read the README and the relevant safety references.
- Keep examples fictional and provider-neutral.
- Do not add credentials, cookies, private URLs, personal names, absolute machine paths, or private project identifiers.
- Prefer a small rule or reference over a new framework layer.

## Content requirements

New prompts must be independently usable and must include read-only inspection, uncertainty handling, approval before mutation, and post-condition validation. New Skill guidance belongs in `SKILL.md` only when it is routing or activation logic; substantial procedures belong in `references/`.

Prompt files contain English and Traditional Chinese sections. Keep the copy-only-language note at the top of each prompt. New runtime claims must be labeled `Tested`, `Designed for`, or `Format compatible` with evidence; do not claim universal agent support.

English documentation is primary. Add a Traditional Chinese equivalent when changing a public guide or landing-page behavior.

## Local validation

Run:

```bash
python3 scripts/validate_repo.py
```

The validator checks structure, local documentation links, Skill front matter and reference integrity, prompt contract markers, regression-specification presence, and basic public-content safety patterns. It is not a replacement for GitHub secret scanning, a dedicated security scanner, manual security review, or behavioral AI evaluation. Review the diff manually as well; passing a scan does not prove that a proposed organization is semantically safe.

## Pull requests

Describe the behavior changed, the safety boundary affected, and the validation commands run. Keep unrelated formatting or generated files out of the change.
