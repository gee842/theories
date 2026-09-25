---
name: vocabulary-sweep-executed
description: "CLAUDE.md Naming and docs/VOCABULARY.md are the current vocabulary law"
metadata: 
  node_type: memory
  type: project
  originSessionId: 09373820-c6ee-487e-8c3b-881636c86f4e
---

# Current vocabulary law

Read the repository root `CLAUDE.md` Naming section and
`docs/VOCABULARY.md` before naming or renaming code. The latter is the source
of truth for current winners and banned synonyms. In particular, storage-level
uid prefixes, stored dimension keys, `core:*` marker ids, and durable event
kinds are frozen data rather than vocabulary and require a data migration to
change.

The historical rename map is at
`docs/yi/archive/48-vocabulary-unification.md`. It is history, not a list of
unfinished source edits.

Public-surface pins do not veto an intentional rename; update the expected
surface in the same change. Old execution counts, header-pinning instructions,
and snapshot ceremony are superseded by [[verification-regime-2026-08-14]].
