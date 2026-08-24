# Example: research folder

This fictional folder demonstrates recursive understanding before a taxonomy change.

```text
research/
├── sources/
│   ├── paper-a.pdf
│   └── links.md
├── notes/
│   └── synthesis.md
├── exports/
│   └── notes-export.md
└── index.md
```

The agent should inspect the references between `index.md`, `links.md`, and `synthesis.md` before moving anything. `notes-export.md` may be useful without being canonical. The plan should preserve `sources/` and `notes/` unless evidence shows a clear benefit to change.
