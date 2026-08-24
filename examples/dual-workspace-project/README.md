# Example: dual-workspace project

This fictional project uses a human workspace for decisions and a machine workspace for code and tests. The providers are intentionally unspecified.

```text
project-alpha/
├── human-workspace/
│   ├── brief.md
│   └── decision-log.md
└── machine-workspace/
    ├── src/
    ├── tests/
    └── release-notes.md
```

Expected source-of-truth map:

| Artifact class | Source of truth |
| --- | --- |
| Briefs and decisions | Human workspace |
| Code and tests | Machine workspace |
| Release notes | Ask; authority is not assumed |

Use a stable project identity and verify references between the two workspaces before any rename or archive action.
