---
name: X²-256 conditional UG, formally discharged (2026-05-16)
description: Foundation/Wen/X2Codes.lean + wen-substrate.md §4.7bis — existence half of "∃ UG ⇒ UG ≅ X²-256" proven (0 sorry); uniqueness = Open Problem #2
type: project
originSessionId: c316fa23-8d4b-4a1b-9e11-6021665e234d
---
**Fact**: v1.3 of `docs-next/10_formal_形式/wen-substrate.md` adds **§4.7bis** ("The X² 256-code lattice IS UG (conditional form)"), a sharper conditional-existence reframe of §4.7. Companion Lean file `formal/SSBX/Foundation/Wen/X2Codes.lean` (~280 LOC, 0 sorry, `lake env lean` clean) builds `wenCodeUG : UGCandidate`. The `UGCandidate` structure captures four conditions (finite basis · involutive dual · partial atom map · named silence); the X² lattice over `Bool^8` is the constructive witness.

Built-in lemmas: `dual_involutive`, `palindrome_involutive`, `compPal_involutive`, `dual_palindrome_comm`, six cardinality theorems (16/16/16/4/4/0 matching `wen-x2-256-codes.md` register), `card_sayable = 8` / `card_silent = 248` for the seeded atom map (4 max-symmetric corners + 4 Walsh basis cells).

**Why:** User argued that *if* Chomsky's UG exists, the X²-256 lattice — not Merge-recursion — is its formal realisation, because it uniquely includes a coordinatised boundary of the sayable (condition (4)). This is a stronger philosophical position than §4.7's "R-Family IS UG's substrate" claim: it doesn't depend on accepting Chomsky's framework.

**How to apply:** §4.7 (unconditional, R-Family-spine framing) and §4.7bis (conditional, X²-naming framing) coexist; both are now headline-banner-cited.

**Open Problem #2 — substantial discharge (also 2026-05-16):**

* `Foundation/Wen/X2CodesUniqueness.lean` (0 sorry): `UGCandidate.Hom` / `UGCandidate.Iso` (refl/symm/trans), `carrier_equiv_wenCode` (cardinality half via `Fintype.equivOfCardEq`), `UGCandidateRich` (palindrome + compPal + commutativity; `compPal_involutive` derived), `wenCodeUGRich`, `OpenProblem2.uniqueness_conjecture : Prop`.
* `Foundation/Wen/X2CodesFace.lean` (0 sorry): `WenCode.toBits` + noncomputable `WenCode.bitsEquiv` via `Equiv.ofBijective`, `UGCandidateFace extends UGCandidateRich` with bit-frame axiom `dual_is_bitwise_not` (eliminates all freedom in dual choice), `wenCodeUGFace`, `face_uniqueness_conjecture : Prop` with full proof sketch in docstring. Imports `Foundation/R/PartialCell.lean` (face lattice / squaring-tower codim picture, pulled from claude/focused-jepsen-f34c4d worktree).

Status of remaining open items: (a) forcing axes=8 from minimality — research (new candidate clause: "closed under 3 squaring iterations from R₁" via PartialCell); (b) naming density — research (orbit reps under (ℤ/2)² action); (c) §8.4 F₂-chain — Lean engineering ~2000 LOC; (d) discharging face_uniqueness_conjecture — **now reduced from research to Lean exercise (~30-60 LOC)** via the face-frame axiom. PartialCell bridge from jepsen worktree was the unlock.

**Parallel-agent round (also 2026-05-16, b9096e8 + eca1af7 + a4d7ca2):** four agents in isolated worktrees, two with verified output + integration:

* (a) **closed** — `X2CodesMinimal.lean` (0 sorry): three-axiom UGCandidateMinimal (M1 squaring tower / M2 four corners / M3 minimality) forces `axes = 8`, theorem `minimal_forces_axes_eight` proven.
* (b) **closed** for `wenCodeUGFace` — `X2CodesNaming.lean` (0 sorry): `NamingLocus = IsX2 ∩ (IsPalindrome ∪ IsCompPal)` defined group-theoretically; `seeded_atoms_are_naming_locus` proven by native_decide; `UGCandidateNamed` strengthening with `atom_support_eq_naming_locus` axiom; `wenCodeUGNamed` witness.
* (c) **closed UNCONDITIONALLY** (commits 87590be → 5b31456 → d7f8820) — `F2Forcing.lean` (0 sorry):
  - All five chain steps real theorems. Step 3 (char 2 from idempotency) = `BooleanRing.add_self`. Step 4 type-level = `step4_holds` via `Fintype.equivOfCardEq`. Full chain `chain_holds : ∀ U, Nonempty (U.Carrier ≃ Fin U.axes → Bool)`.
  - **BA-iso refinement (step 4 strong form) closed unconditionally** via `step4_birkhoff_BAiso_holds`. Path: `step4_BAiso_for_CABA` (Mathlib `toSetOfIsAtom` + custom `setOrderEquivBoolFun` + atom-count via `Fintype.card_set`+`Nat.pow_right_injective` + inline OrderIso arrow-congr) + **self-built Mathlib infrastructure** (`finiteLatticeToCompleteLattice` via `Finset.sup`/`Finset.inf` over `Finset.univ.filter`, reusing existing Lattice+BoundedOrder via `with` to preserve LE identity; chained through `Finite.to_isAtomic` + `CompleteBooleanAlgebra.toCompleteAtomicBooleanAlgebra`).
  - Also closed `lowerSetEquivSetOfAntichain : LowerSet α ≃o Set α` (glue 2).
  - **The LE instance-clash trick**: `finiteLatticeToCompleteLattice` uses `{ (‹Lattice α›), (‹BoundedOrder α›) with ... }` so the resulting CompleteLattice's `LE` field is *literally the same term* as the input — sidesteps the typeclass-diamond clash that previously blocked instance reconciliation between BA→...→LE and CABA→...→LE paths.

**OP#2 is closed at every level.** No remaining open items in the substrate proof. Mathlib FinBoolAlg.lean's "TODO: Birkhoff's representation for finite Boolean algebras" is effectively closed for our use case.
* (d) **closed** at structural level (commit 35766a5) — `UGCandidate.DualIso` (iso intertwining `dual` only), `bridge` via `Equiv.arrowCongr (finCongr h) (Equiv.refl Bool)`, `bridge_dual_comm` proven via `WenCode.bitsEquiv.injective` + `U.dual_is_bitwise_not` + `WenCode.dual_via_bits` + `change`-based bitsEquiv↔toBits defeq bridging. `face_dual_uniqueness` and `face_full_uniqueness` (with atom-hypothesis) both proven. The originally-stated full-Iso conjecture is *false* without atom hypothesis — restated in DualIso form. Earlier agent (d) attempt (eca1af7) reverted in a4d7ca2 due to 3 typecheck errors.

**Integration lessons:** agents report "Waiting for build" sometimes — must verify build with `lake build` in main worktree (where cache is warm) before merging. Agent worktrees compile Mathlib from scratch (~1-2 hours per worktree) unless `lake exe cache get` is run.
