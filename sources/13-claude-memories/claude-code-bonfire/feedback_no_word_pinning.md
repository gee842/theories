---
name: feedback-no-word-pinning
description: "OWNER RULE — pin observable behavior, never wording, source bytes, or provenance; renames are in scope by default"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 09373820-c6ee-487e-8c3b-881636c86f4e
---

The "byte-identical behavior" discipline and inline plan-code justification
comments were agent-emergent, never an owner instruction. Owner (2026-07-11):
"we should never [have] added this, neither was I aware of it."

**Why:** it directly worked against the owner's highest-priority goal ([[unified-mental-frame-direction]] — words ARE the mental frame) and mis-generalized [[feedback-no-backwards-compat]] (which bans compat *cushions*, i.e. wants clean breaks — the opposite instinct).

**How to apply, in every Bonfire session:**
- "Behavior-preserving" may pin what consumers observe at runtime: storage
  rows, wire shapes, and event payloads with external readers. It never pins
  identifiers, file names, comments, error prose, checker source, transcripts,
  or provenance. Renames are in scope by default.
- Frozen storage strings — UID prefixes, stored dimension fields, marker ids,
  and durable event kinds — are data, not vocabulary. Changing one is a
  separately chosen data migration, not a word sweep.
- Code comments are present-tense: what the code does and what constraint
  binds it. No plan-code citations, tombstones, or reviewer-directed
  justification. Do not copy the obsolete surrounding style.
- New plans do not use "byte-identical" acceptance criteria unless a real
  external consumer requires that behavior and is named.
- Public-surface pin tests are governance, not freezes: update the pin file in
  the same change as an intentional rename.
- Treat byte-pin language in older plans as history, not standing law.

Superseded verification details are governed by
[[verification-regime-2026-08-14]].
