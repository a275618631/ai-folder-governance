#!/usr/bin/env python3
"""Validate the public shape, local links, Skill contract, and safety basics."""

from __future__ import annotations

import json
import re
import subprocess
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
    "tests/README.md",
    "tests/regression-cases.md",
    "tests/runtime-verification.md",
    "tests/fixtures/minimal-inventory.json",
    ".publication-private-denylist.example",
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
    "08-runtime-capabilities.md",
]

PROMPT_NAMES = [
    "01-single-folder-deep-organize.md",
    "02-multi-folder-maintenance.md",
    "03-web-review-and-local-handoff.md",
    "04-project-lifecycle-review.md",
    "05-project-workspace-governance.md",
]

E2E_FILES = [
    "README.md",
    "01-before-tree.txt",
    "02-inventory.md",
    "03-material-questions.md",
    "04-dry-run-plan.md",
    "05-user-approval.md",
    "06-change-ledger.md",
    "07-after-tree.txt",
    "08-validation-report.md",
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

    for name in E2E_FILES:
        read(f"examples/end-to-end-project/{name}")

    for directory in (
        "examples/downloads-folder",
        "examples/research-folder",
        "examples/mixed-documents",
        "examples/dual-workspace-project",
        "examples/end-to-end-project",
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

    references = re.findall(r"\]\((references/[^)#\s]+)", content)
    if not references:
        fail("SKILL.md has no routed references")
    for relative in references:
        if not (ROOT / "skills/ai-folder-governance" / relative).is_file():
            fail(f"SKILL.md reference does not exist: {relative}")


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
        for content, language in ((english, "en"), (chinese, "zh-TW")):
            if f"docs/{language}/{name}" not in content:
                fail(f"README is missing its {language} documentation link for {name}")
    if "Which path should I use?" not in english or "我應該選哪一條路？" not in chinese:
        fail("first-user path chooser is missing")
    if "08-runtime-capabilities.md" not in english or "08-runtime-capabilities.md" not in chinese:
        fail("runtime capability documentation link is missing")
    if "agentskills.io/specification" not in english or "agentskills.io/specification" not in chinese:
        fail("official Agent Skills specification reference is missing")


def check_markdown_links() -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)\s]+)(?:\s+['\"][^)]*['\"])?\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            if not (path.parent / target).resolve().exists():
                fail(f"broken local Markdown link: {path.relative_to(ROOT)} -> {target}")


def check_prompt_contract() -> None:
    marker_groups = {
        "scope": ("scope", "target", "範圍"),
        "read-only inspection": ("read-only", "唯讀"),
        "dry-run": ("dry-run", "change set"),
        "approval": ("approval", "核准"),
        "validation": ("validation", "驗證"),
    }
    for name in PROMPT_NAMES:
        content = read(f"prompts/{name}").casefold()
        for label, markers in marker_groups.items():
            if not any(marker.casefold() in content for marker in markers):
                fail(f"prompt contract marker missing: {name} -> {label}")
        if "copy only the language section" not in content:
            fail(f"prompt language-copy note missing: {name}")


def check_regression_coverage() -> None:
    content = read("tests/regression-cases.md")
    for number in range(1, 16):
        marker = f"## R-{number:03d}"
        if marker not in content:
            fail(f"missing regression specification: {marker}")


def check_fixture_json() -> None:
    try:
        fixture = json.loads(read("tests/fixtures/minimal-inventory.json"))
    except json.JSONDecodeError as exc:
        fail(f"fixture is not valid JSON: {exc}")
    if fixture.get("schema_version") != 1 or not fixture.get("items"):
        fail("fixture does not contain the expected inventory shape")


def safety_patterns() -> tuple[tuple[str, re.Pattern[str]], ...]:
    # Build sensitive patterns from fragments so this validator does not flag its own source.
    user_path = re.compile(r"/(?:Users|home)/")
    windows_user_path = re.compile(r"[A-Za-z]:[\\/](?:Users|home)[\\/]")
    provider_url = re.compile(r"https?://(?:drive|docs)\.google\.com", re.IGNORECASE)
    secret_prefix = re.compile(r"(?:ghp_|github_pat_|xoxb-|AIza)[A-Za-z0-9_-]+")
    private_key = re.compile(r"BEGIN PRIVATE KEY")
    assignment_secret = re.compile(
        r"(?:token|password|secret)\s*[:=]\s*[^\s`]+", re.IGNORECASE
    )
    forbidden_terms = re.compile(r"private account information", re.IGNORECASE)
    return (
        ("POSIX user path", user_path),
        ("Windows user path", windows_user_path),
        ("provider-specific private URL", provider_url),
        ("credential prefix", secret_prefix),
        ("private key material", private_key),
        ("inline secret assignment", assignment_secret),
        ("private account marker", forbidden_terms),
    )


def local_denylist() -> list[str]:
    path = ROOT / ".publication-private-denylist"
    if not path.is_file():
        return []
    values = []
    for line in path.read_text(encoding="utf-8").splitlines():
        value = line.strip()
        if value and not value.startswith("#"):
            values.append(value)
    return values


def check_publication_safety() -> None:
    patterns = safety_patterns()
    denylist = local_denylist()
    skip = {ROOT / "scripts/validate_repo.py", ROOT / ".publication-private-denylist"}
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
        for marker in denylist:
            if marker in text:
                fail(f"local publication denylist marker found in {relative}: {marker}")


def check_reachable_history() -> None:
    try:
        commits = subprocess.run(
            ["git", "rev-list", "--all"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
    except (OSError, subprocess.CalledProcessError):
        return
    for commit in commits:
        try:
            paths = subprocess.run(
                ["git", "ls-tree", "-r", "--name-only", commit],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.splitlines()
        except (OSError, subprocess.CalledProcessError):
            fail(f"could not list reachable history at {commit[:12]}")
        for relative in paths:
            if relative == "scripts/validate_repo.py":
                continue
            if Path(relative).name.lower() in {".env", "id_rsa", "credentials.json"}:
                fail(f"sensitive filename found in reachable history at {commit[:12]}: {relative}")
            try:
                result = subprocess.run(
                    ["git", "show", f"{commit}:{relative}"],
                    cwd=ROOT,
                    check=True,
                    capture_output=True,
                )
            except (OSError, subprocess.CalledProcessError):
                fail(f"could not read reachable history at {commit[:12]}: {relative}")
            text = result.stdout.decode("utf-8", errors="ignore")
            for label, pattern in safety_patterns():
                if pattern.search(text):
                    fail(f"publication safety pattern {label} found in reachable history at {commit[:12]}")


def main() -> int:
    check_required_paths()
    check_skill()
    check_bilingual_landing_pages()
    check_markdown_links()
    check_prompt_contract()
    check_regression_coverage()
    check_fixture_json()
    check_publication_safety()
    check_reachable_history()
    print(
        "Validation passed: structure, local links, Skill contract, prompt contract, "
        "R-001..R-015 coverage, fixture, and publication safety scan."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
