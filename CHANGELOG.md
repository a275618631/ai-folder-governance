# Changelog

All notable changes to this project are documented here.

## 0.1.2 — 2026-08-24

- Corrected the README evidence-led example so the final state contains only explicitly approved changes.
- Clarified that unapproved cleanup is scope drift.

## 0.1.1 — 2026-08-24

- Clarified recursive scope: recursion is allowed inside the approved target and forbidden outside it without approval.
- Changed exact-duplicate handling from `allow` to `propose`; proposal is not deletion permission.
- Clarified the repository versus host-runtime privacy boundary in `SECURITY.md`.
- Added runtime capability documentation, explicit tested-versus-designed language, and the end-to-end fictional project example.
- Expanded regression specifications from R-001–R-008 to R-001–R-014.
- Hardened the dependency-free validator with local link, Skill-reference, prompt-contract, and regression-coverage checks.

## 0.1.0 — 2026-08-24

- Added the bilingual public landing pages.
- Added seven bilingual documentation guides.
- Added five standalone prompts for folder and project-workspace governance.
- Added the `ai-folder-governance` Agent Skill with routed references and safe templates.
- Added fictional examples, regression cases, fixtures, and a dependency-free repository validator.
