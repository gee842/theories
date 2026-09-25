---
name: heisenberg-weyl-g11-narrative-file
description: "docs-next/10_formal_形式/heisenberg-weyl-narrative.md (868 lines, 2026-05-21) — narrative for the G11 odd-prime HW stream; closed boundary list, what's still open"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 60cba10e-e303-4834-b561-ccbb9850a7f1
---

**Where**: `docs-next/10_formal_形式/heisenberg-weyl-narrative.md` (868 lines, created 2026-05-21 in commit `dbb0758`).

**Scope**: Documents the ~25-commit Heisenberg-Weyl / coordinate Hilbert stream (≤ 2026-05-21 HEAD `588f37a`).

**What's covered**:
- `HeisenbergWeylZModP.lean` — phase-space (ZMod p)^{2n}, alternating symplectic pairing
- `HeisenbergWeylOperators.lean` (1164 lines) — primitive complex characters, clock/shift unitary operators, multi-site faithfulness, Fourier sums, irreducibility, pure-shift reachability
- `StabilizerQM.lean`, `PauliRingIso.lean`, `PhasedPauli.lean`, `HilbertPauliFunctor.lean` — 1-qubit + n-qubit Pauli, retained phases, Hilbert-Schmidt orthogonality, spanning Mat_{2^n}(ℂ)
- `Doctrine/Instance/HilbertEnriched.lean` — `FinHilbObject`, dagger / coordinate tensor / Kronecker / reindexing isometries / coherence / dagger tensor boundaries
- Lands in `Doctrine/Instance/Quantum.lean` as canonical TGUTRealisation

**Closure shape**: All HW theorems closed (no sorry in stream); 0 new axioms.

**Open** (explicitly flagged in §6 of narrative):
- Full `FdHilb` dagger-SMCC (categorical level, not just boundaries)
- Categorical exponential / monoidal-closed Hilbert
- **Heisenberg-Weyl ↔ Cell256 / R₈ / 易卦 specialisation at (p=2, n=8)** — natural next step, NOT YET wired
- Power 1999 §4.5 V-natural universal sayability

**How to apply**: When the user mentions Heisenberg-Weyl / quantum / G11 / Pauli / coordinate Hilbert, read this narrative first; it cross-references the ledger rows. The closed `quantum_complete_universal_sayability` is built on F₂ stabilizer branch — the HW odd-prime work supplies *matching boundary packages* at p≠2 without (yet) a corresponding top-level theorem.

**Companion**: [[reference-claim-status-ledger]] for status terminology.
