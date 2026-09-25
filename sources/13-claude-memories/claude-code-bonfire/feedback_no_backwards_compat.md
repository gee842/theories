---
name: feedback-no-backwards-compat
description: "Bonfire is pre-production; do NOT add backwards-compat layers, alias shims, or deprecated-but-kept code paths. Elegance > legacy."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4d6d4f0e-80e9-4f39-8a6d-d92da26fe9c8
---

When designing or executing phased substrate evolutions in Bonfire, do
NOT propose or write:
- Backwards-compat alias layers ("legacy alias for one version")
- Deprecation cycles that keep both old and new code paths alive
- Migration cushions that preserve consumer APIs
- "Deprecated but kept around" types or methods

**Why:** Bonfire is pre-production. There are no external consumers
to protect. Every alias layer / compat shim is a permanent tax on
clarity. The user explicitly chose elegance over legacy when this
came up during the unified-Class plan: "we are not in production, no
Backwards-compat at all, not comprimsing elegance over legacy."

**How to apply:** A refactor lands the new shape cleanly and fixes affected
consumers forward. Tests that exercise legacy code paths are deleted or
rewritten, not preserved alongside new tests. Keep the change series small
and focused, but do not create compatibility layers or process artifacts to
make the break look safer. A suite reddened by the series is fixed or deleted
inside that series.

Verification follows [[verification-regime-2026-08-14]]; obsolete gates do
not justify preserving an obsolete interface.
