#!/usr/bin/env python3
"""Validate the public shape and publication-safety basics of this repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "README.zh-TW.md",
    "LICENSE",
    "CHANGELOG.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "scripts/validate_repo.py",
    "tests/regression-cases.md",
    "tests/fixtures/minimal-inventory.json",
    "skills/ai-folder-governance/SKILL.md",
    "skills/ai-folder-governance/references/core-rules.md",
    "skills/ai-folder-governance/references/safety-invariants.md",
    "skills/ai-folder-governance/references/preference-discovery.md",
    "skills/ai-folder-governance/references/organization-modes.md",
    "skills/ai-folder-governance/references/acceptance-gates.md",
    "skills/ai-folder-governance/references/project-workspaces.md",
    "skills/ai-folder-governance/assets/config.example.yaml",
    "skills/ai-folder-governance/assets/change-ledger.example.md",
    "skills/ai-folder-governance/assets/organization-report.example.md",
    "skills/ai-folder-governance/assets/project-identity.example.yaml",
]

DOC_NAMES = [
    "01-concepts.md",
    "02-how-it-works.md",
    "03-safety-model.md",
    "04-preferences.md",
    "05-prompt-guide.md",
    "06-skill-guide.md",
    "07-project-workspaces.md",
]

PROMPT_NAMES = [
    "01-single-folder-deep-organize.md",
    "02-multi-folder-maintenance.md",
    "03-web-review-and-local-handoff.md",
    "04-project-lifecycle-review.md",
    "05-project-workspace-governance.md",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        fail(f"missing required file: {relative}")
    return path.read_text(encoding="utf-8")


def check_required_paths() -> None:
    for relative in REQUIRED_FILES:
        read(relative)

    for language in ("en", "zh-TW"):
        for name in DOC_NAMES:
            read(f"docs/{language}/{name}")

    for name in PROMPT_NAMES:
        read(f"prompts/{name}")

    for directory in (
        "examples/downloads-folder",
        "examples/research-folder",
        "examples/mixed-documents",
        "examples/dual-workspace-project",
    ):
        if not (ROOT / directory).is_dir():
            fail(f"missing example directory: {directory}")


def check_skill() -> None:
    content = read("skills/ai-folder-governance/SKILL.md")
    front_matter = re.match(
        r"^---\s*\nname:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*\n"
        r"description:\s*(.+?)\s*\n---\s*\n",
        content,
        flags=re.DOTALL,
    )
    if not front_matter:
        fail("SKILL.md has invalid YAML front matter")
    if front_matter.group(1) != "ai-folder-governance":
        fail("SKILL.md name does not match its folder")
    for required_phrase in (
        "Inspect read-only",
        "dry-run change set",
        "Wait for approval",
        "Validate and report",
    ):
        if required_phrase not in content:
            fail(f"SKILL.md is missing workflow phrase: {required_phrase}")


def check_bilingual_landing_pages() -> None:
    english = read("README.md")
    chinese = read("README.zh-TW.md")
    if "AI should understand your files before organizing them." not in english:
        fail("English tagline is missing")
    if "AI 應該先理解你的檔案，再開始整理。" not in chinese:
        fail("Traditional Chinese tagline is missing")
    if "README.zh-TW.md" not in english or "README.md" not in chinese:
        fail("language switch links are missing")
    for name in DOC_NAMES:
        if f"docs/en/{name}" not in english or f"docs/zh-TW/{name}" not in english:
            fail(f"English README is missing bilingual documentation links for {name}")


def check_fixture_json() -> None:
    try:
        fixture = json.loads(read("tests/fixtures/minimal-inventory.json"))
    except json.JSONDecodeError as exc:
        fail(f"fixture is not valid JSON: {exc}")
    if fixture.get("schema_version") != 1 or not fixture.get("items"):
        fail("fixture does not contain the expected inventory shape")


def check_publication_safety() -> None:
    # Build sensitive patterns from fragments so this validator does not flag its own source.
    user_path = re.compile(r"/(?:Users|home)/")
    windows_user_path = re.compile(r"[A-Za-z]:[\\/](?:Users|home)[\\/]")
    provider_url = re.compile(r"https?://(?:drive|docs)\.google\.com", re.IGNORECASE)
    secret_prefix = re.compile(r"(?:ghp_|github_pat_|xoxb-|AIza)[A-Za-z0-9_-]+")
    private_key = re.compile(r"BEGIN PRIVATE KEY")
    assignment_secret = re.compile(
        r"(?:token|password|secret)\s*[:=]\s*[^\s`]+", re.IGNORECASE
    )
    forbidden_terms = re.compile(r"careerops|private account information", re.IGNORECASE)

    patterns = (
        ("POSIX user path", user_path),
        ("Windows user path", windows_user_path),
        ("provider-specific private URL", provider_url),
        ("credential prefix", secret_prefix),
        ("private key material", private_key),
        ("inline secret assignment", assignment_secret),
        ("private project marker", forbidden_terms),
    )

    skip = {ROOT / "scripts/validate_repo.py"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path in skip:
            continue
        relative = path.relative_to(ROOT)
        if path.name.lower() in {".env", "id_rsa", "credentials.json"}:
            fail(f"sensitive filename found: {relative}")
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in patterns:
            if pattern.search(text):
                fail(f"publication safety pattern {label} found in {relative}")


def main() -> int:
    check_required_paths()
    check_skill()
    check_bilingual_landing_pages()
    check_fixture_json()
    check_publication_safety()
    print("Validation passed: structure, bilingual links, Skill contract, fixture, and publication safety scan.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
