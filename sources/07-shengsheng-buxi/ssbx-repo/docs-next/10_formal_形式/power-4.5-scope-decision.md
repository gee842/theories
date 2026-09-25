---
title: "Power 1999 Theorem 4.5 — V-Hypothesis Scope Decision"
status: "Path A Phase A.0 kickoff"
date: 2026-05-21
author: "Claude (Opus 4.7), at user's direction"
supersedes: nothing
related:
  - enriched-universal-sayability-plan.md
  - phase-1-4-scaffolding-handoff.md
  - claim-status-ledger.md
---

# Power 1999 Theorem 4.5 — V-Hypothesis Scope Decision

> **Decision document, not a plan.** This file records the precise scope of `V`
> we commit to for the Lean 4 formalisation of Power 1999 §4 Theorem 4.5,
> kicking off Path A (full proof) Phase A.0. The accompanying plan
> (`enriched-universal-sayability-plan.md`) describes *how* and *when*; this
> file fixes *what V looks like*.
>
> **TL;DR**: We start with **V cartesian closed locally finitely presentable
> (cccc lfp)**. This is Power 1999's original setting, covers our first five
> target instances (Set / Cat / Ab / R-Mod / FinSet), and admits a clean Lean
> formalisation. The Kelly-1989 locally-bounded generalisation needed for Hilb
> is deferred to Phase A.9; SMCC-only (no lfp) is rejected for Phase A.

---

## 0. Frame

This is the **Phase A.0** deliverable of "Path A" — the decision, made by the
user on 2026-05-21, to pursue Power 1999 Theorem 4.5 in full as a Lean 4
proof, rather than continuing to supply it as opaque comparison data
(`EnrichedLawvereFinitaryMonadComparisonData`).

The preceding scaffolding (PR #70, post-#70 hardening through 2026-05-21) gave
us:

| File | Status |
|---|---|
| `Foundation/Enriched/Cotensor.lean` | Class + universal property + naturality + `V = Type` instance, 0 sorry |
| `Foundation/Enriched/Weighted.lean` | Class + cotensor↔weighted bridge supplied-data, 0 sorry |
| `Foundation/Enriched/Monad.lean` | `EnrichedMonad` class + V-monad-law supplied data, 0 sorry |
| `Foundation/Enriched/Finitary.lean` | `FinitaryEnrichedMonad` + Type-specialisation supplied data, 0 sorry |
| `Foundation/Enriched/Power.lean` | Theorem 4.5 *statement* with comparison data as input |
| `Foundation/Doctrine/EnrichedLawvereTheory.lean` | Theory/model/free-forgetful supplied-data layer, 0 executable sorry |
| `Foundation/Doctrine/T_GUT_Enriched.lean` | Scoped non-vacuous bridge proven; full V-natural theorem open |

Path A's Phase A goal is to **replace the comparison-data input of
`theory_monad_equiv` with a proof** following Power 1999 §3–§4 directly.

Before any Lean code is written, the V-hypothesis must be fixed. That is what
this document does.

---

## 1. Power 1999 Theorem 4.5 — Precise Statement

### 1.1 The theorem (Power 1999 §4.5)

> **Theorem 4.5 (Power, TAC 6 no. 7, 1999, §4).**
> Let `V` be a locally finitely presentable cartesian closed category.
> Then the 2-category `Th_V` of `V`-enriched Lawvere theories is
> 2-equivalent to the 2-category `Mnd_f(V)` of finitary `V`-monads on `V`:
>
>   `Th_V  ≃  Mnd_f(V)`.

The forward functor (Power §3) sends a `V`-theory `L` to the monad of free
`L`-algebras; the backward functor (Power §4) sends a finitary `V`-monad `T`
to the opposite of the full sub-`V`-category of `T`-free algebras on
finitely-presentable generators.

### 1.2 V's hypotheses, as Power writes them

Power 1999 §2.1 fixes once-and-for-all:

> "Throughout, `V` denotes a *locally finitely presentable cartesian closed
> category*."

This expands into the following Lean-actionable data:

| Hypothesis | What it gives |
|---|---|
| `V` is a category | basic objects/morphisms |
| `V` has finite products and a terminal `1_V` | products `X × Y`, finite-arity operations |
| `V` is cartesian closed | exponential objects `Y^X`, internal hom |
| `V` is locally small | hom-sets are sets, not proper classes |
| `V` is cocomplete | filtered colimits exist, used essentially in §4 |
| `V` is locally finitely presentable | `V` has a strong generator of finitely-presentable objects; `V ≃ Lex(V_f^op, Set)` for `V_f` = full subcat of f.p. objects |

The cartesian-closed assumption is *not* used for the existence of the
equivalence — Power notes this in §2.3 and Hyland-Power 2007 §3 makes it
explicit — it is used to give the most elementary description of the
forward functor. SMCC suffices, at the cost of a longer construction.

### 1.3 What "finitary V-monad" means in Power's setting

> **Definition (Power §2.4).** A `V`-monad `T` on `V` is **finitary** if its
> underlying `V`-endofunctor preserves filtered conical colimits.

Equivalently (Kelly 1982 §6.5; Power §2.4), `T` is the left Kan extension
along `V_f ↪ V` of its restriction to `V_f`. In cccc-lfp setting these are
the same.

### 1.4 What "V-enriched Lawvere theory" means

> **Definition (Power §2.5).** A **`V`-enriched Lawvere theory** is a
> `V`-category `L` with the same objects as `V_f^op` (the opposite of the
> full subcategory of finitely-presentable objects), together with an
> identity-on-objects `V`-functor `i : V_f^op → L` strictly preserving
> finite products (cotensors with f.p. objects).

The 2-category `Th_V` has theories as objects, identity-on-objects
finite-product-preserving `V`-functors as 1-cells, and `V`-natural
isomorphisms as 2-cells.

### 1.5 Why this exact form

Power's framing is the right one because:

- "Identity on objects" pins down the carrier — no skeleton drift.
- "Finite-product-preserving" makes `Th_V` a category of *algebraic*
  presentations, in the strict sense of finite arities.
- "Finitary V-monad" is precisely what corresponds to those finite arities on
  the monad side, by Kelly–Lack–Power finitariness.

References:

- Power 1999 §2.1 (V-hypothesis), §2.4 (finitary V-monad), §2.5 (V-enriched
  Lawvere theory), §3 (forward functor), §4 (backward functor), §4.5 (the
  equivalence).
- Hyland–Power 2007 §2 (modern exposition), §3 (cartesian-closed not
  essential).
- Kelly 1982 Ch. 5 (V-monads), §6.5 (algebras and finitariness).
- Adamek–Rosicky 1994 §1.A (lfp categories), Th. 1.46 (Gabriel–Ulmer duality
  for lfp categories).

---

## 2. Hypothesis Comparison Table

### 2.1 The four reasonable scope options

We compare four levels of V-hypothesis. Each is a strict weakening of the
previous (less assumed on V, more theorem versions / more instances covered,
but more technical work).

| Option | V hypothesis | Theorem version | Reference |
|---|---|---|---|
| **(A)** | cartesian closed, lfp | Power 1999 Theorem 4.5 | Power 1999 §4.5 |
| **(B)** | SMCC, lfp | Hyland–Power 2007 §3.1 generalisation | HP07 §3 |
| **(C)** | SMCC, **locally bounded** | Kelly 1989 / Lack–Rosický 2011 generalisation | Kel89; LR11 §4 |
| **(D)** | SMCC only (no lfp/bounded) | known to fail in general | Kel82 §6.5 counterexamples |

### 2.2 Side-by-side comparison

| Aspect | (A) cccc-lfp | (B) SMCC-lfp | (C) SMCC-loc-bdd | (D) SMCC-only |
|---|---|---|---|---|
| Power 1999 Thm 4.5 holds? | **yes (verbatim)** | yes (HP07 §3 reformulation) | yes (Kel89 generalisation) | **no in general** |
| `V_f` = full subcat of f.p. objects well-behaved? | yes — generates V | yes — generates V | replaced by α-bounded objects | not generally |
| Free models / left adjoints from `V_f^op` | direct via cccc | needs adjoint functor theorem | needs Kelly transfinite small-object | rarely exist |
| Finite products in `V` distribute over filtered colimits | **automatic** (cccc) | needs explicit hypothesis | needs explicit hypothesis | not in general |
| Monoidal structure on V | cartesian (= ×) | general ⊗ | general ⊗ | general ⊗ |
| Lean / Mathlib API maturity | high (`HasFiniteProducts`, `CartesianClosed`) | medium (`SymmetricMonoidalClosed`, `MonoidalClosed`) | low (locally bounded not in Mathlib) | medium (no lfp) |
| Proof length, page-count | ~30 pages (Power) | ~40 pages (HP07 expansion) | ~60+ pages (Kel89 + L–R 2011) | unbounded |
| Lean LOC estimate (Phase A) | 4–6k | 6–8k | 12k+ | n/a |
| Hilb / Top / Met covered? | **no** (none are cartesian closed in the needed sense) | partial (some lfp issues) | **yes** (Hilb is loc-bdd over Set) | sometimes |
| Risk of subtle gap in proof | low (original setting) | low | medium (delicate small-object) | high |

### 2.3 Lost without each hypothesis

#### What's lost without cartesian closure (going to SMCC):

- The internal hom `[X, Y]` is no longer `Y^X`; it's a separate piece of
  structure tied to a non-cartesian monoidal product `⊗`.
- The forward functor in Power §3 uses `[X, Y]` = `Y^X` essentially in
  constructing free algebras. Going to SMCC requires re-doing §3 by
  hand-constructing free algebras via coequalisers (Kelly 1980; HP07 §3).
- Many concrete identifications become non-trivial. E.g., for `V = Cat` (which
  is cartesian closed), `[X, Y]` is the functor category; for `V = Ab` (SMCC
  but not cartesian closed), `[X, Y]` is hom-with-pointwise-addition, *not*
  product functions.

#### What's lost without lfp:

- The finitely-presentable objects `V_f` no longer generate `V`. The theory
  carrier — "V-category with the same objects as `V_f^op`" — becomes
  meaningless or has to be replaced by something else (`α-presentable` for
  some regular cardinal `α`, or a strong generator).
- Filtered colimits no longer commute with finite limits. Finitariness loses
  its punchy form.
- The backward functor in Power §4 uses lfp essentially: it builds the theory
  from the monad as the opposite of the free-algebra functor restricted to
  `V_f`. Without lfp, we'd need a chosen strong generator and the construction
  becomes far more delicate.

#### What's lost going SMCC + loc-bdd → SMCC only:

- Without local boundedness, there's no small-object argument to construct
  free algebras for arbitrary V-signatures. The whole forward-direction
  collapses.
- Counterexamples exist (Kelly 1982 §6.5 final remarks; concretely: V = full
  Cat-large abelian groups; full Top with all topological spaces).

### 2.4 Target instances under each scope

| Target instance | (A) cccc-lfp | (B) SMCC-lfp | (C) SMCC-loc-bdd | (D) SMCC only |
|---|---|---|---|---|
| **Set** (sets, functions) | yes | yes | yes | yes |
| **Cat** (small categories) | yes | yes | yes | yes |
| **Ab** (abelian groups) | **no** (not cccc, only SMCC) | yes | yes | yes |
| **R-Mod** (modules over R) | **no** (ditto) | yes | yes | yes |
| **FinSet** (finite sets) | yes (lfp = itself) | yes | yes | yes |
| **Vect_k** (finite-dim) | no | yes | yes | yes |
| **Top** (topological spaces) | borderline — see §2.5 | borderline | yes (Kelly 1989) | maybe |
| **Hilb** (sep. Hilbert spaces) | **no** | **no** (not lfp) | **yes** (loc-bdd) | maybe |
| **Ban** (Banach spaces) | no | no | yes (loc-bdd) | maybe |
| **Met** (metric spaces) | no | no | yes (loc-bdd) | maybe |

**Critical observation**: cccc-lfp covers **Set, Cat, FinSet** outright;
**Ab, R-Mod, Vect_k** want SMCC-lfp. To deliver our first five target
instances {Set, Cat, Ab, R-Mod, FinSet} we either need scope (B) or a
two-step delivery within (A): first cccc-lfp for {Set, Cat, FinSet}, then
SMCC-lfp upgrade for {Ab, R-Mod}.

### 2.5 The Top borderline

`Top` is **cartesian** (× exists, terminal exists) and **closed** for the
*compactly generated* version `CGHaus` or `kTop`. But:

- Full `Top` is not lfp (the "finitely presentable" topological spaces are
  precisely the *finite discrete* spaces, which do *not* generate `Top` —
  e.g., they can't see indiscrete topologies).
- `kTop` (compactly generated weak Hausdorff) is cartesian closed and
  reasonable; whether it's lfp is the subject of long-running debate
  (Hyland 1979; Day 1972). It is *not* lfp in the standard sense.
- `Top` is locally bounded (Kelly 1989), so scope (C) covers it.

We treat `Top` as **out-of-scope** for cccc-lfp Phase A; if we want it later,
we either (i) restrict to a cccc-lfp subcategory or (ii) escalate to scope (C).

---

## 3. Decision

### 3.1 The decision

> **We commit to scope (A): V cartesian closed locally finitely presentable
> for Phase A of Path A.**
>
> This is Power 1999's original setting, verbatim. It directly proves Power
> 1999 Theorem 4.5 without scope creep, and is sufficient for our first
> instance batch {Set, Cat, FinSet}.

### 3.2 Decision rationale

Six factors, in order of weight:

#### (1) Mathematical cleanliness

Scope (A) is what Power *actually proved* in 1999. Every page of §3, §4,
§4.5 of the paper assumes cccc-lfp. Diverging from this means we're not
formalising Power 1999, we're formalising HP07 (scope B) or Kelly 1989
(scope C). Those proofs are longer and have more moving parts.

#### (2) Mathlib infrastructure availability

Mathlib (as of 2026-05-21) has solid support for:

- `HasFiniteProducts` (✓ tested, widely used)
- `CartesianClosed` (✓ tested, widely used)
- `IsFiltered`, filtered colimits (✓)
- Locally presentable categories — **partial**. There is
  `CategoryTheory.LocallyPresentable` scaffolding but the API is thinner
  than `CartesianClosed`. We may need to upstream lemmas.

Scope (B) needs `MonoidalClosed` (medium maturity) plus everything in (A);
scope (C) needs locally-bounded categories, **not in Mathlib at all** as of
2026-05-21. Verified by inspection of
`.lake/packages/mathlib/Mathlib/CategoryTheory/LocallyBounded*.lean` (absent).

#### (3) Coverage of first-priority instances

Our committed first 5 target instances are: **Set, Cat, Ab, R-Mod, FinSet**.
Of these:

- **Set, Cat, FinSet** are cccc-lfp → covered by (A).
- **Ab, R-Mod** are *not* cccc; they are SMCC-lfp.

For Ab/R-Mod, we plan to deliver them in **Phase A.6** (after the core
cccc-lfp theorem lands), by carrying out the SMCC-lfp extension as a
follow-up sub-PR. This treats SMCC-lfp as a *staged generalisation*, not
the entry point.

Net: scope (A) covers 3/5 first instances directly; the remaining 2/5 are
deferred to a clearly-scoped Phase A.6 extension.

#### (4) Hilb deferral is acceptable

The whole point of Path A is **not Hilb-specific** — it is a verified Power
1999 §4.5 in Lean. Hilb is one downstream target. By scoping (A) for
Phase A and (C) for Phase A.9, we get:

- A clean Phase A deliverable (Power's original theorem) in 4–6k LOC.
- A clean Phase A.9 extension (Kelly 1989 locally-bounded generalisation)
  in another 6–8k LOC, attempted only after Phase A lands.

If we tried scope (C) up front, Phase A's LOC estimate doubles and the
proof difficulty triples. We'd be likely to stall and produce nothing.

#### (5) Risk minimisation

Power 1999's proof, narrowly read, has been verified informally by many
category theorists and is stable. Going beyond it (scope B or C) means
producing the first Lean formalisation of HP07's reformulation or Kelly
1989's extension — a research deliverable in its own right, with research
risk.

#### (6) Reversibility

If Phase A succeeds and we discover a clean path to scope (B) or (C), we
can extend by adding hypotheses to V and re-proving the modified theorem.
The architecture of the supplied-data layer
(`EnrichedLawvereFinitaryMonadComparisonData`) is already general enough
for any V — only the constructive *proof* is specific to (A).

If Phase A fails and we discover (A) is wrong (e.g., a load-bearing
counterexample), we can downscope to a still smaller setting (say, V = Set
only — back to Lawvere 1963), without losing the infrastructure work.

### 3.3 What is *committed* by this decision

| Commitment | Locked? |
|---|---|
| V cartesian closed lfp for Phase A.0 through A.5 | **YES** |
| First 5 instances {Set, Cat, Ab, R-Mod, FinSet} delivered, with Ab/R-Mod via Phase A.6 SMCC-lfp upgrade | **YES** |
| Top out of scope for Phase A; eligible for Phase A.9 (loc-bdd) | **YES** |
| Hilb deferred to Phase A.9 | **YES** |
| Phase A.9 extends to Kelly 1989 loc-bdd | provisional — re-decide after Phase A.5 |
| 2-categorical version of §4.5 | out of scope for Path A entirely (1-categorical only) |

### 3.4 What is *not* committed

We are not committing to:

- A specific universe-level choice (`{v} V` vs `{u} V`) — see §6 open question O1.
- Skeleton vs up-to-iso for theory objects — see §6 open question O2.
- A specific Mathlib upstream path vs vendored — see §6 open question O5.

These are Phase A.1 calibration decisions, to be revisited as the
construction proceeds.

---

## 4. First 5 Target Instances — Concrete Plans

Each instance gets a one-page plan: confirmation it satisfies the V-hypothesis,
the desired V-enriched Lawvere theory, Mathlib infrastructure status, and an
LOC estimate.

### 4.1 V = Set

#### Hypothesis check

| Property | Holds? | Reference |
|---|---|---|
| Cartesian | yes (×, 1) | trivial; `Mathlib.CategoryTheory.Limits.Shapes.BinaryProducts` |
| Cartesian closed | yes (`Y^X = X → Y`) | `Mathlib.CategoryTheory.Closed.Cartesian` |
| Locally finitely presentable | yes (FinSet is the dense f.p. subcategory) | Adamek–Rosicky 1994 Ex. 1.10 |
| Set is its own enrichment | yes (V-Cat = Cat trivially) | folklore |

#### V-enriched Lawvere theory of interest

The **classical Lawvere theory** of a single binary operation with axioms
(monoid theory, group theory, abelian-group theory, etc.). Concretely:
take `T = Th(monoid)` = the opposite of the category of finitely-generated
free monoids; V-models in Set = ordinary monoids.

#### Mathlib infrastructure

- `Mathlib.CategoryTheory.Limits.Types` — finite products in Set: ✓
- `Mathlib.CategoryTheory.Closed.Cartesian` — cartesian closure: ✓
- `Mathlib.CategoryTheory.Monad.*` — ordinary monad theory: ✓
- LFP-Set: not as a named instance, but constructible from
  `IsLocallyPresentable` skeleton.

#### LOC estimate

- Instance file `Foundation/Doctrine/Instance/SetEnriched.lean`: **~200 LOC**
- Includes: cccc-lfp instance witnesses, an example V-Lawvere theory
  (groups), one non-vacuous T-algebra construction.

#### Risks

Low — Set is the trivial case, almost free from the general construction.

### 4.2 V = Cat

#### Hypothesis check

| Property | Holds? | Reference |
|---|---|---|
| Cartesian | yes (product cat, terminal cat) | `Mathlib.CategoryTheory.Products.Basic` |
| Cartesian closed | yes (`[A, B]` = functor cat) | `Mathlib.CategoryTheory.Closed.FunctorCategory` |
| Locally finitely presentable | yes (Cat is lfp; f.p. cats = finitely-generated free cats) | Makkai–Pare 1989; Adamek–Rosicky 1994 §3.D |
| 2-Cat structure on V-Cat | known; gives 2-Lawvere theories | Power 1999 ⊕ Lack 2010 |

#### V-enriched Lawvere theory of interest

A **2-Lawvere theory** (Lack 2010). E.g., the theory of a monoidal category as
a Cat-enriched theory. V-models in Cat = monoidal categories.

#### Mathlib infrastructure

- `Mathlib.CategoryTheory.Products.Basic`: ✓
- `Mathlib.CategoryTheory.Closed.FunctorCategory`: ✓ (cartesian closure
  of Cat)
- `Mathlib.CategoryTheory.Enriched.Basic` + `Ordinary.Basic`: ✓ for V-Cat
- LFP-Cat: not yet a named instance; need Phase A.3 lemma.

#### LOC estimate

- `Foundation/Doctrine/Instance/CatEnriched.lean`: **~400 LOC**
- LFP-Cat lemma: **~100 LOC** (may upstream).

#### Risks

Medium — universe-level juggling between objects of Cat (which are
categories, themselves of some universe) and Cat itself. Need to fix
`{v}` carefully (see §6 O1).

### 4.3 V = Ab

#### Hypothesis check

| Property | Holds? | Reference |
|---|---|---|
| Cartesian | yes (Ab has × = ⊕ as categorical product) | `Mathlib.Algebra.Category.Grp.Basic` |
| **Cartesian closed** | **no** (the canonical closure is symmetric monoidal via ⊗_Z, not cartesian) | folklore; Linton 1966 |
| Symmetric monoidal closed | yes (⊗_Z, internal Hom = Hom_Ab) | `Mathlib.Algebra.Category.ModuleCat.Monoidal` (ZMod case) |
| Locally finitely presentable | yes (f.p. Ab = finitely-presented abelian groups = `Z^n ⊕ (finite torsion)`) | Adamek–Rosicky 1994 Ex. 1.7 |

#### Important: Ab does **not** satisfy scope (A)

Ab is SMCC-lfp (scope B), not cccc-lfp (scope A). The cartesian closure
of Ab in the categorical sense (taking × = ⊕ as the "monoidal" product
for the V-Lawvere theory) gives only V-monads enriched in **the additive
structure of Hom**, which is *not* what Linton 1966 / classical additive
theories want.

For Ab, the natural enrichment is V = Ab with ⊗_Z, the tensor product of
abelian groups. This is SMCC, not cccc.

#### V-enriched Lawvere theory of interest

The **additive Lawvere theory** (Linton 1966): for example, the theory of a
ring as an Ab-enriched theory (one Ab-object for arity, plus multiplication
and unit). V-models in Ab = rings.

#### Mathlib infrastructure

- `Mathlib.Algebra.Category.Grp.Basic`: ✓ category of abelian groups.
- `Mathlib.Algebra.Category.ModuleCat.Monoidal`: ✓ monoidal structure on
  R-Mod, specialises to Ab for R = ℤ.
- `Mathlib.CategoryTheory.Closed.Monoidal`: ✓ MonoidalClosed class.
- LFP-Ab: probably exists in some form; needs locating.

#### LOC estimate

- `Foundation/Doctrine/Instance/AbEnriched.lean`: **~500 LOC**
- Plus Phase A.6 SMCC-lfp upgrade core: **~1000 LOC** (the actual
  generalisation of Power §3 forward direction)

#### Phase A.6 status

Delivered as **part of Phase A.6 — SMCC-lfp upgrade**. Phase A core proves
cccc-lfp; Phase A.6 generalises to SMCC-lfp following HP07 §3.

### 4.4 V = R-Mod

#### Hypothesis check

| Property | Holds? | Reference |
|---|---|---|
| Cartesian | yes (R-Mod has × = ⊕) | `Mathlib.Algebra.Category.ModuleCat.Basic` |
| **Cartesian closed** | **no** (same as Ab) | folklore |
| Symmetric monoidal closed | yes (⊗_R, internal Hom = Hom_R) | `Mathlib.Algebra.Category.ModuleCat.Monoidal` |
| Locally finitely presentable | yes (f.p. R-Mod = finitely-presented R-modules) | Adamek–Rosicky 1994 Ex. 1.7 |

R-Mod is the natural generalisation of Ab to a general ring R; Ab = (Z-Mod).

#### V-enriched Lawvere theory of interest

The R-Mod-enriched Lawvere theory of an **R-algebra** (associative,
unital). V-models in R-Mod = associative R-algebras.

#### Mathlib infrastructure

- `Mathlib.Algebra.Category.ModuleCat.Basic`: ✓
- `Mathlib.Algebra.Category.ModuleCat.Monoidal`: ✓ (this is the canonical
  example of MonoidalCategory in Mathlib)
- LFP-(R-Mod): same status as LFP-Ab.

#### LOC estimate

- `Foundation/Doctrine/Instance/RModEnriched.lean`: **~500 LOC**
- Reuses Phase A.6 SMCC-lfp upgrade.

#### Phase A.6 status

Same as V = Ab; delivered in Phase A.6.

### 4.5 V = FinSet

#### Hypothesis check

| Property | Holds? | Reference |
|---|---|---|
| Cartesian | yes (FinSet has finite ×, 1) | `Mathlib.CategoryTheory.Limits.Shapes.Types` |
| Cartesian closed | yes (FinSet is cccc, `Y^X` is the f.p. function set) | classical |
| Locally finitely presentable | yes — FinSet is its own f.p. core, equivalent to itself | trivial |
| FinSet ↪ Set is the V_f inclusion | yes by construction | Power 1999 §2.1 example |

FinSet is the most "concrete" instance and a natural sanity case: every
finitely-presentable object in Set is in FinSet, so a FinSet-enriched Lawvere
theory is essentially a classical (one-sorted, finitary) Lawvere theory in
the *narrow* sense.

#### V-enriched Lawvere theory of interest

A **classical Lawvere theory** in the original sense: a category with
objects ℕ (or equivalently finite sets `n = {0,...,n-1}`) and morphisms
generated by an algebraic signature.

#### Mathlib infrastructure

- `Mathlib.CategoryTheory.Limits.Shapes.Types` — Type has limits: ✓
- `Mathlib.Data.Fintype.Basic` — finite types: ✓
- No `FinSet` named category in Mathlib (only `Fintype` predicate); needs
  thin wrapper.

#### LOC estimate

- `Foundation/Doctrine/Instance/FinSetEnriched.lean`: **~250 LOC**
- Includes thin `FinSet : Type` wrapper, cccc-lfp instance witnesses, an
  example V-Lawvere theory (commutative-monoid theory).

#### Risks

Low — most "trivial" instance. Possibly delivered as Phase A.1 sanity check.

### 4.6 Summary table

| Instance | Scope | Phase | LOC | Risk |
|---|---|---|---|---|
| FinSet | (A) cccc-lfp | A.1 (sanity) | ~250 | low |
| Set | (A) cccc-lfp | A.5 | ~200 | low |
| Cat | (A) cccc-lfp | A.5 | ~400 + 100 (LFP-Cat) | medium |
| Ab | (B) SMCC-lfp | A.6 | ~500 + 1000 (SMCC core) | medium |
| R-Mod | (B) SMCC-lfp | A.6 | ~500 | low (after Ab) |
| **Totals** | | | **~3000 LOC** | |

Compared with the original plan's 2850–5350 LOC for Phase 1–4 (full enriched
universal sayability), the first-5-instance delivery alone is in the same
range. Reason: most of the LOC budget goes to the V-hypothesis-free core
(Power 1999 §3 + §4); each instance is a thin specialisation.

---

## 5. What's Out of Scope (Explicit)

### 5.1 Hilb (deferred to Phase A.9)

The category `Hilb` of separable Hilbert spaces with bounded linear maps and
Hilbert tensor product is:

- **SMCC** (with `⊗ = ⊗_Hilb`, internal Hom = bounded linear maps), but
- **not lfp** — f.p. Hilbert spaces would have to be the finite-dimensional
  ones, but these don't generate Hilb in the lfp sense (the inclusion
  FinHilb ↪ Hilb is not a dense `K`-functor for any reasonable `K`).
- **locally bounded** (Kelly 1989 §1.2; Lack–Rosický 2011 §4.3).

Therefore Hilb requires **scope (C) — SMCC-locally-bounded — Kelly 1989
generalisation of Power 1999**. This is Phase A.9 — a follow-up
extension after the cccc-lfp core proof lands.

The pre-existing `Foundation/Doctrine/Instance/HilbertEnriched.lean` work
on FinHilb (the finite-dim subcategory) remains useful: FinHilb *is*
SMCC-lfp (it equals its own f.p. core), so the V = FinHilb case fits in
Phase A.6 — same scope as V = Ab, V = R-Mod.

| Substrate | Scope | Phase |
|---|---|---|
| FinHilb (finite-dim) | (B) SMCC-lfp | A.6 (alongside Ab, R-Mod) |
| Hilb (separable infinite-dim) | (C) SMCC-loc-bdd | A.9 |

### 5.2 Ban — never targeted

The category `Ban` of Banach spaces with bounded linear maps and projective
tensor product is locally bounded but **never on our roadmap**:

- SSBX has no Ban-flavoured substrate.
- The motivating quantum / categorical work is Hilb-shaped, not Banach-shaped.
- Adding Ban would expand the Phase A.9 scope without payoff.

Decision: **Ban out of scope for Path A**.

### 5.3 2-categorical version of §4.5

Power 1999 Theorem 4.5 is stated and proved as a **2-equivalence** between
**2-categories**. Our delivery is the **1-categorical reduction** only:

- We prove `Th_V_1 ≃ Mnd_f(V)_1` (equivalence of underlying 1-categories).
- We do *not* prove the full 2-equivalence (with coherent adjoint 2-cells).

This is consistent with the existing `enriched-universal-sayability-plan.md`
§3.3, which already places 2-categorical content out of scope.

Why: 2-equivalences in Lean require either a 2-categorical infrastructure
(Mathlib has partial support: `Mathlib.CategoryTheory.Bicategory.*`) or
explicit handling of coherence 2-cells, which can multiply the proof's
length by 2–3×. The 1-categorical reduction is sufficient for our downstream
goal (V-enriched universal sayability), which only needs categorical iso
in the model category.

### 5.4 Higher V-enrichment

We do **not** target:

- V-enriched 2-categories (Cat-enriched-in-V, with V itself enriched in some
  other base).
- Internal type theory for V-categories (e.g., a HoTT-style internal
  language of V).
- V-enriched ∞-categories.

These would all require infrastructure far beyond Mathlib. Out of scope for
Path A in any phase.

### 5.5 Re-decisions left to later phases

Some choices are deferred to specific phases, not eliminated outright:

| Item | Re-decided in | Decision rule |
|---|---|---|
| Phase A.9 scope (Kelly loc-bdd) | After Phase A.5 lands | proceed iff cccc-lfp core proof is stable |
| 2-categorical extension | Never in Path A; possibly Path B | n/a |
| Universe handling rewrite | Phase A.1 | follow Mathlib idiom |
| Mathlib upstream vs vendored | Phase A.2 | follow Mathlib reviewer guidance |

---

## 6. Open Questions for Future Phases

These are intentionally deferred — recorded here so a future agent can pick
them up without re-deriving the context.

### O1. Universe level handling for `V` and `C`

**The question**: V-categories live in size-rich type universes. The Mathlib
convention has `[Category.{v'} V]` and `[Category.{v} C]` as separate
universe parameters. Power 1999's framework — particularly the V_f^op
construction — silently assumes V is small enough that V_f^op is a V-category
of the same size.

**The options**:

| Option | Tradeoff |
|---|---|
| Force `v' = v` | simplest; loses generality |
| Allow `v' ≠ v` with explicit `ULift` | preserves generality; more boilerplate |
| Restrict `V` to `Type u` only | matches `V = Type` instance pattern; loses V-as-Cat |

**Decision rule**: defer to Phase A.1; choose whatever the Mathlib reviewer
prefers when we first show them the cotensor file.

**Related**: `enriched-universal-sayability-plan.md` §4.3 first bullet.

### O2. Skeleton vs up-to-iso for theory objects

**The question**: Power 1999 §2.5 defines a V-enriched Lawvere theory as
a V-category *with the same objects as `V_f^op`* — i.e., the theory object
inclusion `V_f^op → L` is **strictly identity-on-objects**.

In Lean/Mathlib, "identity on objects" can mean:

- (a) Equality of object types and `obj L = obj V_f^op` definitionally
  (strict skeleton).
- (b) An equivalence-on-objects with a chosen splitting.
- (c) A reflective subcategory with chosen replacement.

Mathlib idiom tends toward (c); Power 1999's narrative wants (a); HP07's
modern presentation uses (b).

**Decision rule**: defer to Phase A.2 carrier construction; (a) is
mathematically cleanest, (c) is most Mathlib-idiomatic. We'll need a
conversion lemma either way.

**Related**: `enriched-universal-sayability-plan.md` §11 row 3.

### O3. Conical vs weighted as primary

**The question**: Mathlib's existing enriched-limits API (`HasConicalLimits`,
`HasConicalProducts`, `HasConicalTerminal`) uses **conical** as the primary
notion. Power 1999 uses **weighted** as the primary notion.

Cotensors and weighted limits are equivalent in expressivity (cotensors +
conical = weighted, Kelly 1982 §3.7), but the *primary* development can
go either way.

**The options**:

| Option | Tradeoff |
|---|---|
| Make weighted primary, derive conical | Power-idiomatic; conflicts with Mathlib |
| Keep conical primary, derive weighted | Mathlib-idiomatic; bridge lemmas needed |
| Develop both as peers | clean; ~2× LOC |

**Decision rule**: defer to Phase A.2. Recommendation: keep conical primary
(as Mathlib does) and *derive* weighted via cotensors + conical products.
This matches our existing `Cotensor.lean`/`Weighted.lean` split.

### O4. Strictness of the V-functor `i : V_f^op → L`

**The question**: Power §2.5's V-functor `i : V_f^op → L` is required to
**strictly preserve finite products**. In Lean, "strictly preserve" can be:

- Definitionally — `i (X × Y) = i X × i Y` as types.
- Up to specified iso — there's a chosen iso `μ : i (X × Y) ≅ i X × i Y`.
- Up to canonical iso — Mathlib's `PreservesFiniteProducts` class.

**Decision rule**: defer to Phase A.2 along with O2. They are linked
(strictness on objects + strictness on functors = full strictness).

### O5. Mathlib upstream vs SSBX-vendored

**The question**: For each new file (cotensor, weighted, monad, finitary,
power), do we upstream to Mathlib first or vendor locally?

| Approach | Tradeoff |
|---|---|
| Upstream first | aligned with Mathlib; 3–6 month review delay |
| Vendor first | fast progress; creates parallel maintenance |
| Hybrid (vendor + upstream concurrently) | maximises throughput; doubles work |

**Decision rule**: defer to each PR. Current bias: vendor first
(`SSBX.Foundation.Enriched.*`), upstream once stable and Phase A.5 lands.
This matches the existing pattern in `Foundation/Enriched/{Cotensor,Weighted,
Monad,Finitary,Power}.lean` files (all carry "SSBX vendor notice"
docstrings pointing to upstream Mathlib namespaces).

**Related**: `enriched-universal-sayability-plan.md` §3.2.

### O6. Choice principle dependencies

**The question**: Power 1999's proof uses **classical choice** in several
places (existence of free algebras, transfinite small-object argument when
generalised). What `#print axioms` footprint do we accept?

| Acceptable footprint | What it permits |
|---|---|
| `propext, Classical.choice, Quot.sound` | full Mathlib idiom |
| Above + `axiom` declarations | avoid! breaks the "no axiom" rule |
| Above + `Nat.recOn` only (constructive) | rules out Power 1999 essentially |

**Decision rule**: stick to Mathlib idiom (top row). The memory rule
`feedback_no_axiom_for_zero_sorry` is non-negotiable.

### O7. 2-categorical follow-up (if ever attempted)

**The question**: After Phase A core lands, do we (optionally) extend to
the full 2-equivalence of Power 1999 §4.5?

**Considerations**:

- Mathlib has partial bicategory support (`Mathlib.CategoryTheory.Bicategory.*`).
- 2-cells in Power's framework are V-natural isos; coherence is non-trivial.
- Downstream consumers (e.g., `T_GUT_Enriched.lean`) only need the
  1-categorical version.

**Decision rule**: not currently planned; defer to "Path C" if user requests.
Phase A's deliverable is 1-categorical only.

---

## 7. References

### 7.1 Primary

- **Power, J.** 1999. *Enriched Lawvere theories*. *Theory and Applications
  of Categories* 6 no. 7, 83–93. [TAC link](http://www.tac.mta.ca/tac/volumes/6/n7/6-07abs.html).
  — **THE** central reference. Theorem 4.5 (§4) is the target. V-hypothesis
  in §2.1; finitary V-monad in §2.4; V-enriched Lawvere theory in §2.5;
  forward functor in §3; backward functor and equivalence in §4.

- **Kelly, G. M.** 1982. *Basic Concepts of Enriched Category Theory*.
  Cambridge University Press; TAC Reprint 10 (2005).
  [TAC reprint link](http://www.tac.mta.ca/tac/reprints/articles/10/tr10abs.html).
  — V-category foundations. §3.7 V-cotensors / powers; §3.1–§3.5 weighted
  limits; Ch. 5 V-monads; §6.5 V-T-models and finitariness.

### 7.2 Modern expositions

- **Hyland, J. M. E.** and **Power, J.** 2007. *The category theoretic
  understanding of universal algebra: Lawvere theories and monads*.
  *Electronic Notes in Theoretical Computer Science* 172, 437–458.
  [doi:10.1016/j.entcs.2007.02.019](https://doi.org/10.1016/j.entcs.2007.02.019).
  — Modern survey of Power 1999. §2 historical context; §3 makes the
  cartesian-closed-is-not-needed observation explicit; §3 SMCC-lfp
  generalisation.

- **Borceux, F.** 1994. *Handbook of Categorical Algebra*, vol. 2:
  *Categories and Structures*. Cambridge University Press. ISBN
  978-0-521-44179-7.
  — Ch. 6 weighted limits (the encyclopedic version); Ch. 4 enriched
  categories.

### 7.3 Locally presentable and locally bounded

- **Adamek, J.** and **Rosicky, J.** 1994. *Locally Presentable and
  Accessible Categories*. London Mathematical Society Lecture Note Series
  189. Cambridge University Press. ISBN 978-0-521-42261-1.
  — **THE** reference for lfp. §1.A foundations; Th. 1.46 Gabriel–Ulmer
  duality; Ex. 1.7 (Ab is lfp); Ex. 1.10 (Set is lfp); §3.D (Cat is lfp).

- **Kelly, G. M.** 1989. *A unified treatment of transfinite constructions
  for free algebras, free monoids, colimits, associated sheaves, and so on*.
  *Bulletin of the Australian Mathematical Society* 22 no. 1, 1–83.
  — Locally bounded V; transfinite small-object argument for V-monads.
  Reference for Phase A.9.

- **Lack, S.** and **Rosický, J.** 2011. *Enriched weakness*.
  *Journal of Pure and Applied Algebra* 216 no. 8–9, 1807–1816.
  [doi:10.1016/j.jpaa.2011.11.030](https://doi.org/10.1016/j.jpaa.2011.11.030).
  — §4 modern treatment of locally bounded enriched categories.

### 7.4 Historical / first-instance references

- **Lawvere, F. W.** 1963. *Functorial Semantics of Algebraic Theories*.
  PhD thesis, Columbia University; TAC Reprint 5 (2004).
  [TAC reprint link](http://www.tac.mta.ca/tac/reprints/articles/5/tr5abs.html).
  — The original V = Set Lawvere theory. Reference for V = Set instance.

- **Linton, F. E. J.** 1966. *Some aspects of equational categories*. In
  *Proceedings of the Conference on Categorical Algebra (La Jolla, 1965)*,
  Springer, 84–94.
  — V = Ab additive theories. Reference for V = Ab instance.

- **Lack, S.** 2010. *A 2-categories companion*. In *Towards Higher
  Categories*, IMA Volumes in Math. Appl. 152, Springer, 105–191.
  [arXiv:math/0702535](https://arxiv.org/abs/math/0702535).
  — 2-Lawvere theories; reference for V = Cat instance.

- **Pisier, G.** 2003. *Introduction to Operator Space Theory*. London
  Mathematical Society Lecture Note Series 294. Cambridge University Press.
  — Hilb SMCC structure. Reference for Phase A.6 V = FinHilb and Phase A.9
  V = Hilb.

### 7.5 SSBX framework cross-references

- `docs-next/10_formal_形式/enriched-universal-sayability-plan.md` — the
  multi-phase plan this decision feeds into.
- `docs-next/10_formal_形式/phase-1-4-scaffolding-handoff.md` — current
  scaffolding state.
- `docs-next/10_formal_形式/claim-status-ledger.md` — v0.8 row "V-enriched
  universal sayability".
- `formal/SSBX/Foundation/Enriched/{Cotensor,Weighted,Monad,Finitary,Power}.lean`
  — supplied-data scaffolding to be replaced with proofs in Phase A.
- `formal/SSBX/Foundation/Doctrine/EnrichedLawvereTheory.lean` — Phase A.4
  closes the supplied-data layer here.
- `formal/SSBX/Foundation/Doctrine/T_GUT_Enriched.lean` — Phase A.7
  downstream consumer of the closed theorem.

---

## 8. Phase A Roadmap (Forward Pointer)

This decision document fixes the V-hypothesis. The Phase A plan — what code
is written, in what order — lives in a separate document
(`power-4.5-phase-a-plan.md`, to be drafted next). At a glance:

| Phase | Deliverable | Depends on |
|---|---|---|
| A.0 (this doc) | V-hypothesis scope decision | none |
| A.1 | Universe + skeleton calibration; FinSet sanity instance | A.0 |
| A.2 | Cotensor / Weighted full proof (replace supplied data) | A.1 |
| A.3 | LFP-Cat lemma; Finitary V-monad full theory | A.2 |
| A.4 | Power §3 forward functor; close `EnrichedLawvereTheory.lean` | A.3 |
| A.5 | Power §4 backward functor + Theorem 4.5 proof; close `Power.lean` | A.4 |
| A.6 | SMCC-lfp generalisation (HP07 §3); Ab, R-Mod, FinHilb instances | A.5 |
| A.7 | `T_GUT_Enriched.lean` closure; full V-natural universal sayability | A.5 (A.6 for non-cccc V) |
| A.8 | Mathlib upstream PRs (vendor → upstream migration) | A.7 |
| A.9 | Kelly 1989 loc-bdd extension; Hilb / Top / Met / Ban | A.7 (conditional) |

End-state of Phase A.7: `enriched_universal_sayability` proved, 0-axiom
0-sorry, non-vacuously instantiated at V ∈ {Set, Cat, Ab, R-Mod, FinSet,
FinHilb}.

---

## 9. Acceptance and Sign-off

This document is the Phase A.0 deliverable. It is accepted when:

- [x] §3.1 states the V-hypothesis decision unambiguously.
- [x] §3.2 justifies the decision with at least 4 named factors.
- [x] §4 has a concrete plan for each of the first 5 target instances.
- [x] §5 explicitly excludes Hilb, Ban, 2-cat, and higher V.
- [x] §6 records at least 5 open questions specific enough for handoff.
- [x] §7 includes the 5 named primary references.

Phase A.1 can begin once this document is committed.

---

**End of Phase A.0 deliverable.**

**Last updated**: 2026-05-21.

**Next document**: `power-4.5-phase-a-plan.md` (the actual implementation
plan; deferred to Phase A.1 kickoff).
