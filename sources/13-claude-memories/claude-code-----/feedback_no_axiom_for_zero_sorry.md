---
name: no-axiom-for-zero-sorry
description: "Never introduce a new `axiom` declaration just to hit \"0 sorry\"; axioms silently extend the trust base and can be unsound. Use `sorry` with a doctrine note instead."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c3eb568e-1426-4359-86cc-32ef2b00ed99
---

**Rule**: When a Lean proof is hard, leave `sorry` with a doctrine note explaining the gap. Do NOT introduce a new `axiom` declaration to retire the `sorry`.

**Why**: Sorries are visible in build output as warnings and stay isolated to the single theorem; new axioms silently extend the logical foundation and can be unsound — they don't show up unless you explicitly `#print axioms`. Verified incident 2026-05-17 (PR #51, branch `claude/naughty-hopper-04ad32`): `sierpinski_cube_JT_factorization` in `formal/SSBX/Foundation/Doctrine/Instance/Topological.lean` was introduced as a final-step "JT axiom" to close 5 → 0 sorries in `Foundation/`. The statement was provably False:

- Counterexample at `N = M = 2`: `φ u v := u 0 ⊓ v 1` satisfies all four `IsJTFrameBilinear` clauses (frame distributivity gives `sSup`-preservation; `v 1 ⊓ v 1 = v 1` idempotence gives `inf`-preservation) but cannot factor through the pointwise meet `fun i => u i ⊓ v i`: at `u₁=(⊤,⊥), v₁=(⊥,⊤)` the value is `⊤` while at `u₂=(⊤,⊤), v₂=(⊥,⊥)` the value is `⊥`, yet both inputs project to the same pointwise meet `(⊥,⊥)` — so the witness `ψ` would have to be multivalued.
- Root cause: JT factoring geometrically goes through `Fin (N*M) → Ω` (outer product over `Spec` of the cube), not `Fin (min N M) → Ω` (pointwise meet). The axiom's conclusion shape was geometrically wrong.
- Caught at PR-review by independent agent before merge. `origin/main` was protected only because PR #51 hadn't merged yet; if it had, every downstream theorem in SSBX would have been compromised.

**How to apply**:

1. When closing the last few sorries in a doctrine file, **resist** the temptation to wrap the residual claim as an `axiom`. If the proof is too hard to discharge, leave `sorry` plus a multi-paragraph note explaining: (a) what's being claimed, (b) where the obstruction sits, (c) what external machinery would discharge it (e.g., "awaits Mathlib `frameCoprod` PR").
2. Before introducing an `axiom`, **explicitly verify the statement's consistency** — write down a candidate counterexample and check it doesn't satisfy the hypotheses. If you can't think of one in 10 minutes, that's not validation, that's blindness.
3. After any session that touches axioms, run `#print axioms ‹top-level-theorem›` on representative theorems to inspect what got added. Any new axiom beyond `Classical.choice`, `propext`, `Quot.sound` is a red flag.
4. Reserve `axiom` for: (a) Mathlib upstream gaps where the math is well-established (e.g., a Mathlib PR is open and the statement matches Mathlib's stated form), (b) genuinely external classical principles already accepted. Never use it for: "I couldn't prove this in time".
5. The user's prior feedback `[[dont-drop-theorems]]` (don't weaken a theorem statement to keep sorry-count at 0) is the *sibling* principle — together they say: don't game the metric in either direction (don't drop theorems, don't paper-over with axioms). Preserve the genuine epistemic state.

Related: [[dont-drop-theorems]], [[minimal-builds]].
