# 8. Runtime capabilities

The framework separates what an agent can reason about from what its host runtime can actually do. Capability names are not platform support claims.

## Capability matrix

| Host capability | Scan | Plan | Execute | Validate |
| --- | --- | --- | --- | --- |
| Chat only | Use a user-provided inventory | Yes | No | Compare the next user-provided inventory or report limitations |
| User-provided inventory | Inspect the supplied evidence | Yes | No | Validate only against supplied evidence |
| Read-only filesystem | Read permitted metadata and content | Yes | No | Re-scan read-only and report what cannot be proven |
| Read/write filesystem | Read within scope | Yes | Approved moves, renames, or archive actions | Re-scan and verify post-conditions |
| Remote workspace connector | Use connector-supported read scope | Yes | Only if connector write capability and approval exist | Read back through the connector |
| Git plus filesystem | Inspect files, links, and Git state | Yes | Approved file changes; commits and pushes remain separate actions | Filesystem checks plus Git status, diff, and test checks |

The table describes a decision boundary, not an automatic permission grant. A runtime with no write capability must return `PLAN_READY`, not `ORGANIZATION_PASS`.

## Tested vs designed

Use these labels precisely:

- **Tested:** the specific runtime, version or context, fixture, date, and limitations are recorded in [runtime verification](../../tests/runtime-verification.md).
- **Designed for:** the workflow is written to fit the capability, but this repository release does not claim that a particular product or provider was executed.
- **Format compatible:** the Skill package follows the Agent Skills file shape; compatibility does not prove behavioral support.

This release records a fixture-backed verification in the current Codex runtime. It does not claim that all agents, cloud providers, filesystems, or connectors support the same operations.

## Capability discovery

Before planning a mutation, determine:

1. whether the target can be read within scope;
2. whether the runtime can detect path dependencies;
3. whether it can write, move, rename, archive, or delete;
4. whether it can read back the result independently;
5. whether Git actions are available and separately approved.

If any required capability is missing, stop at the highest truthful state and report the limitation. Never infer write or validation capability from the ability to chat about files.

## Runtime-neutral reporting

Report capability facts with the result, for example:

```text
runtime: read-only filesystem
scan: pass
plan: ready
execute: unavailable
validate: read-only re-scan only
result: PLAN_READY
```

Avoid claims such as “all agents supported.”
