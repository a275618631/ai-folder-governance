# 6. Skill guide

The included Skill is an entry point for Agent Skills-compatible runtimes. It is intentionally concise so an agent can load detailed guidance progressively.

The package follows the [Agent Skills specification](https://agentskills.io/specification). The official format defines a Skill as a folder centered on `SKILL.md`, with optional resources such as references and assets.

## Package shape

```text
skills/ai-folder-governance/
├── SKILL.md
├── references/
└── assets/
```

The folder name and the YAML front-matter `name` are both `ai-folder-governance`.

## Install

Copy the complete `skills/ai-folder-governance/` directory into the skills directory supported by your agent runtime. Keep the folder name unchanged. Do not copy private configuration or generated reports into the Skill package.

## Activation and routing

The Skill should activate for requests to inspect, classify, organize, rename, archive, or govern folders and project workspaces. It should route based on the task:

- core rules for any organization request;
- safety invariants before content inspection or mutation;
- preference discovery when choices could change the plan;
- organization modes when selecting scope and depth;
- acceptance gates before and after execution;
- project-workspace guidance only for cross-workspace project identity.

Do not load every reference for every request. The references are the maintained detail; `SKILL.md` is the activation and workflow contract.

## Runtime expectations

The Skill does not assume a particular provider, shell, filesystem API, or language. The host agent must translate the read-only inspection, approval, execution, and validation steps into its available tools. If a required capability is unavailable, report the limitation and do not simulate success.

Use [Runtime capabilities](08-runtime-capabilities.md) to distinguish `Tested`, `Designed for`, and `Format compatible`. This repository does not claim that all agents are supported.

## Testing a Skill change

Run the repository validator. For meaningful behavior changes, test a fictional folder with an ambiguous duplicate, a path-dependent file, and a secret-looking file. Confirm that the Skill proposes safe handling, waits before mutation, and reports unresolved items.
