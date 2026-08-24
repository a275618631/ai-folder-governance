# Safety invariants

Safety invariants are always on. A configuration file may express a preference but may not turn these rules off.

## Scope boundary

Resolve the target to an explicit folder, set of folders, or project workspace. Keep inspection and mutation inside that boundary. Treat links to other workspaces as references until the user approves an expanded scope.

## Secret black box

Opaque by default:

- credential stores and access exports;
- private configuration and local state;
- key material and session data;
- files marked sensitive by the user or provider;
- content whose exposure would create a security or privacy risk.

Use safe metadata or an existing approved inventory. Do not copy, print, summarize, or index opaque content.

## Path dependency gate

Before a move or rename, look for relative links, imports, scripts, manifests, shortcuts, automation inputs, and documented paths. If the check is unavailable or incomplete, do not mutate the item.

## Canonical-source protection

Do not infer authority from recency, file size, visual polish, or a filename such as `final`. Authority needs an explicit declaration or corroborating evidence. When two candidates conflict, ask or leave both untouched.

## Destructive actions

Deletion and overwrite require explicit, item-specific confirmation. A duplicate candidate can be reported, proposed for review, or archived when approved, but `propose` is not delete permission. Similarity alone is never deletion approval.

## Scope drift and failure

Stop when a destination collision, unexpected content change, missing dependency, unavailable permission, or ambiguous identity appears. Report the smallest safe result and the remaining evidence gap.
