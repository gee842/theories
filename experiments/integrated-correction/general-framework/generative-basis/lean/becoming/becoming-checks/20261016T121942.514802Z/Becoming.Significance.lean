import Becoming.Regions
import Becoming.Standpoints

/-!
# Significance: the one axiom, the condition of chapter §6.15 (not asserted)

On 16 October 2026 Ren folded Part II into Part I as one conditional section after the
generative space (chapter §6.15): the theory does not assert the axiom below and states what
follows with it as a condition.

On 10 October 2026 Ren proposed one axiom: “for anything, its continuation into the future has
significance(doesn't have to be positive, we could argue as long as not harm), or continuation
into the future needs to create more significance(being generative)”. Ren chose to state the
strongest claim without axiom first and to add this axiom after it, with G0 as the target
theorem. Ren also wrote that a center and its boundary exist only within cognitive structure and
dynamics, formed within the same system, so there is no question of whose continuation matters
that would need an axiom, and that “not harm” is “a phase transition with a clear boundary”.
This module states the axiom on the spine and what follows from it with the results of Part I.

* **The axiom.** A significance says, for a standpoint, a step and a formation, whether from
  the standpoint the formation's continuation at the step has significance. The axiom is that
  nothing restricts it (`Unrestricted`): boundary neutrality (`Neutral`) for the significance
  of continuation, over anything, at every step, from every standpoint. A rival keeps the same
  rule inside each standpoint's region (`bounded_rival`).
* **G0 follows.** Consider any reading in which a claim's significance from a standpoint is
  the significance of some formation's continuation at some step. Under the axiom G0 holds at
  the level of claims, and so do S0 at every standpoint, both neutralities, and a seed wherever
  something lives (`Valuation.premises_of_unrestricted`). No connection is used. The stepwise
  reading, the reading of relations and the whole-run reading are such readings
  (`Web.significant_of_unrestricted`, `Conditions.significant_of_unrestricted`). The step is
  immediate: G0 is the axiom restricted to living claims, and the axiom is stronger, for it
  covers events that are not living and formations not yet formed. On the level paths of a web
  (`Web.paths`), G0 holds with unindexed significance, and so does C, with “better” read as
  retaining and adding what has significance (`Web.paths_g0_comparison`).
* **What has significance is what can form.** From a standpoint, one level path *retains* what
  has significance along another when it admits every continuation with significance that the
  other admits (`Web.Retains`). It *adds* when it admits one that the other does not
  (`Web.Adds`). Under the axiom retaining is inclusion and adding is exceeding
  (`Web.retains_iff_includes`, `Web.adds_iff_exceeds`), from every standpoint alike
  (`Web.retains_agree`). So the four cases of a part in `Becoming.Admission` are the four cases
  of significance.
* **Not harm is an exact boundary.** The levels with a part retain what has significance
  without it exactly when the part's net draw stays within the margin for every continuation
  with significance that the levels without it admit
  (`Flow.Balances.retains_iff_within_margin`). The part loses a continuation with significance
  exactly where its net draw exceeds the margin (`Flow.Balances.loses_iff_beyond_margin`). It
  adds one exactly where its net exchange brings within the margin a formation that the levels
  without it do not admit (`Flow.Balances.adds_iff_within_margin`). Each holds with balance
  only at the conditions of the continuations compared, across the steps before each
  (`Flow.retains_iff_within_margin_at`, `Flow.loses_iff_beyond_margin_at`,
  `Flow.adds_iff_within_margin_at`).
* **No ending is licensed.** A level path that retains what has significance along another
  ends none of it (`Web.Retains.not_added`). Under the axiom the conveyor's part is unordered,
  each path adding what the other lacks (`Transfer.unordered`), so ordering it needs a measure,
  a further premise. The giver's part retains and adds (`Restoring.Inflow.retains_adds`).
* **What has not yet formed counts.** In `Preemption` a drawer takes a condition's unit before
  any dependence on it forms. Its event is active and not undermining, so it is living on the
  stepwise reading. Yet its part narrows what can form: a formation requiring the condition from
  the next step on is admitted at every step without the part and at no later step with it.
  Under the axiom the part loses a continuation with significance
  (`Preemption.not_undermining_yet_loses`). The stepwise reading counts only dependences that
  have been met; retaining also counts what can still form.
* **The whole first.** Where fewer continuations have significance, more is retained
  (`Web.Retains.of_fewer`). Significance bounded by a region retains what is admitted within
  the region (`Web.retains_bounded_iff`). Under the axiom, what retains in the whole retains
  within every region, a system's or a self's (`Web.Retains.within`). What holds within a
  system holds within every region inside it (`Web.AdmitsWithin.narrow`).

  The converse fails. In `Clearing`, let each formation's significance stop at what its
  continuation depends on. From the clearer's standpoint, its part retains what has
  significance at every step; from the dweller's standpoint, it loses the dweller
  (`Clearing.centers_disagree`). Under the axiom the part loses the dweller from every
  standpoint. Meanwhile, the levels without the part admit every formation at every step, and
  the clearer is supported throughout, so withholding the part ends nothing
  (`Clearing.free_rider_loses`).
* **The generative space, with no axiom.** With balance at the conditions each formation
  requires, across the steps before it, the levels with a part widen those without it exactly
  when its net draw stays within the margin for everything the levels without it admit and
  its net exchange brings one more formation within the margin
  (`Flow.widens_iff_within_margin_at`; in a balanced flow,
  `Flow.Balances.widens_iff_within_margin`). On level paths, an extension in which every
  claim counts as living is exactly a widening, so C holds for every reading of `living`
  with “better” read as widening, with no axiom (`Web.paths_extension_iff_widens`,
  `Web.paths_comparison_widens`). With the axiom as a condition, widening is retaining and
  adding, keeping the same is retaining both ways, and being mixed is adding both ways
  (`Web.widens_iff_retains_adds`, `Web.keeps_iff_retains`, `Web.mixed_iff_adds`): the
  reduction to possibilities loses nothing, and the rules above need no axiom (Ren, 11
  October 2026: “as long as the derivation of the rules doesn't rely on axiom, don't use
  one”).
* **The axiom is needed.** Where nothing has significance, every level path retains every
  other and none adds, and G0 fails at any event that lives (`Web.significance_undetermined`).
  No law of the dynamics mentions significance, so the dynamics does not decide it.

Significance here is not graded, and, as Ren wrote, it need not be positive. A part does no
harm when the levels with it retain what has significance without it, and it is generative when
it also adds.

**AI reading, adopted on Ren's delegation of 15 October 2026 (DELEGATED-CHOICES D16).**
- `Unrestricted` reads Ren's axiom. The formation index reads “anything”, a formation's
  continuation at a step reads “its continuation into the future”, and the standpoint index
  reads “has significance” unqualified, with no center privileged.
- Retaining reads “as long as not harm”. Adding reads “create more significance” and Ren's
  “more possibilities of becoming”.
- Ren wrote that the self “can not justify itself without some sort of "belief"”. This reads
  onto `bounded_rival` and `Web.significance_undetermined`: a significance bounded by a region
  is supplied, as the axiom is, and the dynamics decides neither.
- G0 is a theorem of this axiom and, since Ren folded it on 11 October 2026, no longer an axiom.

What is not derived:
- the step from significance to a reason (A), the lifting (L), and practical judgment (J1–J4);
- the measure that would order a mixed part;
- the level at which formations are individuated, members or lineages, which fixes what counts
  as a loss;
- which reading of `living` G0 names. The stepwise reading counts participation in a fall
  below a need met. Retaining counts the part's difference against the levels without it,
  possibilities included, and the two differ (`Preemption`).
- the normative warrant of the axiom itself.

Recognition and motivation belong to the later attempt without axiom. The representation
commits to discrete steps, natural quantities and a decided part.
-/

namespace Becoming

open Generative

variable {F C Pos : Type}

/-! ## The axiom and its rivals -/

/-- No standpoint, step or formation restricts significance: from every standpoint, the
continuation of anything has significance at every step. This is boundary neutrality
(`Neutral`) for the significance of continuation. -/
def Unrestricted (sig : Pos → Nat → F → Prop) : Prop :=
  Neutral fun i : Pos × Nat × F => sig i.1 i.2.1 i.2.2

/-- Significance kept inside each standpoint's region: from `p`, the continuation of `f` has
significance exactly when `f` lies in `p`'s region. -/
def bounded (region : Pos → F → Prop) : Pos → Nat → F → Prop :=
  fun p _ f => region p f

/-- A bounded significance is the axiom's rule accepted inside a formed boundary. Where some
formation lies outside some standpoint's region, it is not the axiom. -/
theorem bounded_rival {region : Pos → F → Prop} :
    Within (fun i : Pos × Nat × F => region i.1 i.2.2) (fun i => bounded region i.1 i.2.1 i.2.2) ∧
      ((∃ p f, ¬ region p f) → ¬ Unrestricted (bounded region)) :=
  ⟨fun _ inside => inside, fun ⟨p, f, outside⟩ all => outside (all (p, 0, f))⟩

/-! ## Retaining and adding what has significance -/

namespace Web

variable (W : Web F C)

/-- From standpoint `p`, the level path `l` retains what has significance along `l'`: it admits
every continuation with significance that `l'` admits. -/
def Retains (sig : Pos → Nat → F → Prop) (p : Pos) (l l' : Nat → C → Nat) : Prop :=
  ∀ t f, sig p t f → W.Admits (l' t) t f → W.Admits (l t) t f

/-- From standpoint `p`, the level path `l` adds a continuation with significance that `l'` does
not admit. -/
def Adds (sig : Pos → Nat → F → Prop) (p : Pos) (l l' : Nat → C → Nat) : Prop :=
  ∃ t f, sig p t f ∧ W.Admits (l t) t f ∧ ¬ W.Admits (l' t) t f

variable {W}

/-- Retaining is reflexive. -/
theorem Retains.refl (sig : Pos → Nat → F → Prop) (p : Pos) (l : Nat → C → Nat) :
    W.Retains sig p l l :=
  fun _ _ _ admits => admits

/-- Retaining is transitive. -/
theorem Retains.trans {sig : Pos → Nat → F → Prop} {p : Pos} {l l' l'' : Nat → C → Nat}
    (first : W.Retains sig p l l') (second : W.Retains sig p l' l'') : W.Retains sig p l l'' :=
  fun t f significant admits => first t f significant (second t f significant admits)

/-- Comparison by retaining licenses no ending: a level path that retains what has significance
along another ends none of it, so the other adds nothing to it. -/
theorem Retains.not_added {sig : Pos → Nat → F → Prop} {p : Pos} {l l' : Nat → C → Nat}
    (retains : W.Retains sig p l l') : ¬ W.Adds sig p l' l
  | ⟨t, f, significant, admitted, ended⟩ => ended (retains t f significant admitted)

/-- Inclusion retains, whatever has significance. -/
theorem Includes.retains {l l' : Nat → C → Nat} (includes : W.Includes l l')
    (sig : Pos → Nat → F → Prop) (p : Pos) : W.Retains sig p l l' :=
  fun t f _ admits => includes t f admits

/-- Adding exceeds, whatever has significance. -/
theorem Adds.exceeds {sig : Pos → Nat → F → Prop} {p : Pos} {l l' : Nat → C → Nat} :
    W.Adds sig p l l' → W.Exceeds l l'
  | ⟨t, f, _, admits, not⟩ => ⟨t, f, admits, not⟩

/-- Under the axiom, retaining is inclusion: what has significance is what can form. -/
theorem retains_iff_includes {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig)
    (p : Pos) {l l' : Nat → C → Nat} : W.Retains sig p l l' ↔ W.Includes l l' :=
  ⟨fun retains t f => retains t f (unrestricted (p, t, f)), fun includes => includes.retains sig p⟩

/-- Under the axiom, adding is exceeding. -/
theorem adds_iff_exceeds {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig)
    (p : Pos) {l l' : Nat → C → Nat} : W.Adds sig p l l' ↔ W.Exceeds l l' :=
  ⟨Adds.exceeds, fun ⟨t, f, admits, not⟩ => ⟨t, f, unrestricted (p, t, f), admits, not⟩⟩

/-- Under the axiom no standpoint is privileged: every standpoint retains alike. -/
theorem retains_agree {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig)
    (p q : Pos) {l l' : Nat → C → Nat} : W.Retains sig p l l' ↔ W.Retains sig q l l' :=
  (retains_iff_includes unrestricted p).trans (retains_iff_includes unrestricted q).symm

/-- The one-axiom case. With the axiom as a condition, retaining and adding what has significance
is widening what can form: the reduction to possibilities loses nothing. -/
theorem widens_iff_retains_adds {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig)
    (p : Pos) {l l' : Nat → C → Nat} : W.Widens l l' ↔ W.Retains sig p l l' ∧ W.Adds sig p l l' :=
  ⟨fun ⟨includes, exceeds⟩ => ⟨(retains_iff_includes unrestricted p).mpr includes,
     (adds_iff_exceeds unrestricted p).mpr exceeds⟩,
   fun ⟨retains, adds⟩ => ⟨(retains_iff_includes unrestricted p).mp retains, adds.exceeds⟩⟩

/-- The one-axiom case. With the axiom as a condition, keeping what can form the same is retaining
what has significance both ways. -/
theorem keeps_iff_retains {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig)
    (p : Pos) {l l' : Nat → C → Nat} : W.Keeps l l' ↔ W.Retains sig p l l' ∧ W.Retains sig p l' l :=
  ⟨fun ⟨first, second⟩ => ⟨(retains_iff_includes unrestricted p).mpr first,
     (retains_iff_includes unrestricted p).mpr second⟩,
   fun ⟨first, second⟩ => ⟨(retains_iff_includes unrestricted p).mp first,
     (retains_iff_includes unrestricted p).mp second⟩⟩

/-- The one-axiom case. With the axiom as a condition, being mixed is each adding what has
significance that the other lacks. -/
theorem mixed_iff_adds {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig)
    (p : Pos) {l l' : Nat → C → Nat} : W.Mixed l l' ↔ W.Adds sig p l l' ∧ W.Adds sig p l' l :=
  ⟨fun ⟨first, second⟩ => ⟨(adds_iff_exceeds unrestricted p).mpr first,
     (adds_iff_exceeds unrestricted p).mpr second⟩,
   fun ⟨first, second⟩ => ⟨first.exceeds, second.exceeds⟩⟩

/-- Where fewer continuations have significance, more is retained. -/
theorem Retains.of_fewer {sig sig' : Pos → Nat → F → Prop}
    (fewer : ∀ p t f, sig' p t f → sig p t f) {p : Pos} {l l' : Nat → C → Nat}
    (retains : W.Retains sig p l l') : W.Retains sig' p l l' :=
  fun t f significant admits => retains t f (fewer p t f significant) admits

/-- Significance bounded by a region retains exactly what is admitted within the region at every
step. -/
theorem retains_bounded_iff {region : Pos → F → Prop} {p : Pos} {l l' : Nat → C → Nat} :
    W.Retains (bounded region) p l l' ↔ ∀ t, W.AdmitsWithin (region p) (l t) (l' t) t :=
  ⟨fun retains t f inside => retains t f inside, fun within t f inside => within t f inside⟩

/-- The whole first. Under the axiom, what retains from a standpoint retains from it within every
region, a system's or a self's: the whole's judgment decides every narrower one. -/
theorem Retains.within {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig) {p : Pos}
    {l l' : Nat → C → Nat} (retains : W.Retains sig p l l') (region : Pos → F → Prop) :
    W.Retains (bounded region) p l l' :=
  retains.of_fewer fun p t f _ => unrestricted (p, t, f)

end Web

/-! ## Not harm is an exact boundary -/

namespace Flow

variable {L : Flow F C} {part : F → Bool} {W : Web F C}

/-- From standpoint `p`, with balance only at the conditions required by the continuations with
significance that the levels without the part admit, across the steps before each: the levels with
the part retain what has significance without it exactly when, for each such continuation, the
part's net draw on each condition the formation requires stays within the margin. -/
theorem retains_iff_within_margin_at {l : Nat → C → Nat} (without : L.WithheldLevels part W l)
    {sig : Pos → Nat → F → Prop} {p : Pos}
    (balances : ∀ t f, sig p t f → W.Admits (l t) t f → ∀ c, W.requires t f c → ∀ s, s < t →
      L.BalancesOn W [c] s) :
    W.Retains sig p W.level l ↔ ∀ t f, sig p t f → W.Admits (l t) t f → ∀ c, W.requires t f c →
      W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
        l t c + total (steps 0 t) (fun s => L.partGiven part s c) :=
  ⟨fun retains t f significant admits =>
      (supported_iff_within_margin_at without (balances t f significant admits)).mp
        (retains t f significant admits),
   fun within t f significant admits =>
      (supported_iff_within_margin_at without (balances t f significant admits)).mpr
        (within t f significant admits)⟩

/-- From standpoint `p`, with balance as in `retains_iff_within_margin_at`: a part loses a
continuation with significance exactly where the levels without it admit the formation and the
part's net draw on some condition it requires exceeds the margin. -/
theorem loses_iff_beyond_margin_at {l : Nat → C → Nat} (without : L.WithheldLevels part W l)
    {sig : Pos → Nat → F → Prop} {p : Pos}
    (balances : ∀ t f, sig p t f → W.Admits (l t) t f → ∀ c, W.requires t f c → ∀ s, s < t →
      L.BalancesOn W [c] s) :
    W.Adds sig p l W.level ↔ ∃ t f, sig p t f ∧ W.Admits (l t) t f ∧ ¬ ∀ c, W.requires t f c →
      W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
        l t c + total (steps 0 t) (fun s => L.partGiven part s c) :=
  ⟨fun ⟨t, f, significant, admits, lost⟩ => ⟨t, f, significant, admits, fun within =>
      lost ((supported_iff_within_margin_at without (balances t f significant admits)).mpr
        within)⟩,
   fun ⟨t, f, significant, admits, beyond⟩ => ⟨t, f, significant, admits, fun supported =>
      beyond ((supported_iff_within_margin_at without (balances t f significant admits)).mp
        supported)⟩⟩

/-- From standpoint `p`, with balance only at the conditions required by the continuations with
significance that the levels without the part do not admit, across the steps before each: a part
adds a continuation with significance exactly where the levels without it do not admit the
formation and, with the part's net exchange, its need is met within the margin on every condition
it requires. -/
theorem adds_iff_within_margin_at {l : Nat → C → Nat} (without : L.WithheldLevels part W l)
    {sig : Pos → Nat → F → Prop} {p : Pos}
    (balances : ∀ t f, sig p t f → ¬ W.Admits (l t) t f → ∀ c, W.requires t f c → ∀ s, s < t →
      L.BalancesOn W [c] s) :
    W.Adds sig p W.level l ↔ ∃ t f, sig p t f ∧ (∀ c, W.requires t f c →
      W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
        l t c + total (steps 0 t) (fun s => L.partGiven part s c)) ∧ ¬ W.Admits (l t) t f :=
  ⟨fun ⟨t, f, significant, supported, fresh⟩ => ⟨t, f, significant,
      (supported_iff_within_margin_at without (balances t f significant fresh)).mp supported,
      fresh⟩,
   fun ⟨t, f, significant, within, fresh⟩ => ⟨t, f, significant,
      (supported_iff_within_margin_at without (balances t f significant fresh)).mpr within,
      fresh⟩⟩


/-- From standpoint `p`, the levels with a part retain what has significance without it exactly
when, at every step, for every continuation with significance that the levels without it admit,
the part's net draw on each condition the formation requires stays within the margin. -/
theorem Balances.retains_iff_within_margin (balances : L.Balances W) {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {sig : Pos → Nat → F → Prop} {p : Pos} :
    W.Retains sig p W.level l ↔ ∀ t f, sig p t f → W.Admits (l t) t f → ∀ c, W.requires t f c →
      W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
        l t c + total (steps 0 t) (fun s => L.partGiven part s c) :=
  retains_iff_within_margin_at without fun _ _ _ _ c _ s _ => balances.on [c] s

/-- From standpoint `p`, a part loses a continuation with significance exactly where the levels
without it admit the formation and the part's net draw on some condition it requires exceeds the
margin. -/
theorem Balances.loses_iff_beyond_margin (balances : L.Balances W) {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {sig : Pos → Nat → F → Prop} {p : Pos} :
    W.Adds sig p l W.level ↔ ∃ t f, sig p t f ∧ W.Admits (l t) t f ∧ ¬ ∀ c, W.requires t f c →
      W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
        l t c + total (steps 0 t) (fun s => L.partGiven part s c) :=
  loses_iff_beyond_margin_at without fun _ _ _ _ c _ s _ => balances.on [c] s

/-- From standpoint `p`, a part adds a continuation with significance exactly where the levels
without it do not admit the formation and, with the part's net exchange, its need is met within
the margin on every condition it requires. -/
theorem Balances.adds_iff_within_margin (balances : L.Balances W) {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {sig : Pos → Nat → F → Prop} {p : Pos} :
    W.Adds sig p W.level l ↔ ∃ t f, sig p t f ∧ (∀ c, W.requires t f c →
      W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
        l t c + total (steps 0 t) (fun s => L.partGiven part s c)) ∧ ¬ W.Admits (l t) t f :=
  adds_iff_within_margin_at without fun _ _ _ _ c _ s _ => balances.on [c] s

/-- The exact boundary of the generative space, with no axiom, and balance only where it is used:
at the conditions each formation requires, across the steps before it. The levels with a part
widen those without it exactly when the part's net draw stays within the margin for every
formation the levels without it admit, and, at some step, its net exchange brings within the
margin a formation the levels without it do not admit. -/
theorem widens_iff_within_margin_at {l : Nat → C → Nat} (without : L.WithheldLevels part W l)
    (balances : ∀ t f c, W.requires t f c → ∀ s, s < t → L.BalancesOn W [c] s) :
    W.Widens W.level l ↔
      (∀ t f, W.Admits (l t) t f → ∀ c, W.requires t f c →
        W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
          l t c + total (steps 0 t) (fun s => L.partGiven part s c)) ∧
      ∃ t f, (∀ c, W.requires t f c →
        W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
          l t c + total (steps 0 t) (fun s => L.partGiven part s c)) ∧ ¬ W.Admits (l t) t f :=
  ⟨fun ⟨includes, t, f, admits, not⟩ =>
    ⟨fun t f admitted => (supported_iff_within_margin_at without (balances t f)).mp
        (includes t f admitted),
     t, f, (supported_iff_within_margin_at without (balances t f)).mp admits, not⟩,
   fun ⟨within, t, f, brought, not⟩ =>
    ⟨fun t f admitted => (supported_iff_within_margin_at without (balances t f)).mpr
        (within t f admitted),
     t, f, (supported_iff_within_margin_at without (balances t f)).mpr brought, not⟩⟩

/-- In a balanced flow, the exact boundary of the generative space (`widens_iff_within_margin_at`). -/
theorem Balances.widens_iff_within_margin (balances : L.Balances W) {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) :
    W.Widens W.level l ↔
      (∀ t f, W.Admits (l t) t f → ∀ c, W.requires t f c →
        W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
          l t c + total (steps 0 t) (fun s => L.partGiven part s c)) ∧
      ∃ t f, (∀ c, W.requires t f c →
        W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
          l t c + total (steps 0 t) (fun s => L.partGiven part s c)) ∧ ¬ W.Admits (l t) t f :=
  widens_iff_within_margin_at without fun _ _ c _ s _ => balances.on [c] s

end Flow

/-! ## G0 and the premise card follow -/

/-- Under the axiom, G0 holds at the level of claims on every reading in which a claim's
significance from a standpoint is the significance of some formation's continuation at some
step. With it hold S0 at every standpoint, both neutralities, and a seed wherever something
lives. No connection is used. -/
theorem Valuation.premises_of_unrestricted {Q : Type} {V : Valuation Pos Q}
    {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig) (formation : Q → F)
    (step : Q → Nat) (reads : ∀ p c, sig p (step c) (formation c) → V.sig p c) :
    V.Significant ∧ (∀ p, V.SelfGood p) ∧ Neutral V.transmits ∧ Neutral V.shares ∧
      ∀ c, V.living c → Pos → V.Seed :=
  have all : V.Significant := fun p c _ => reads p c (unrestricted (p, step c, formation c))
  ⟨all, fun p c _ alive => all p c alive, fun ⟨p, _, d⟩ _ _ alive => all p d alive,
   fun ⟨_, q, c⟩ alive _ => all q c alive, fun c alive p => ⟨p, c, alive, all p c alive⟩⟩

/-- Read stepwise, and read through relations, G0 follows from the axiom: an event's or a
relation's significance from a standpoint is that of its formation's continuation at its step. -/
theorem Web.significant_of_unrestricted (W : Web F C) {sig : Pos → Nat → F → Prop}
    (unrestricted : Unrestricted sig) (own : Pos → F × Nat → Prop)
    (own' : Pos → F × C × Nat → Prop) :
    (W.valuation own fun p e => sig p e.2 e.1).Significant ∧
      (W.relations own' fun p e => sig p e.2.2 e.1).Significant :=
  ⟨fun p e _ => unrestricted (p, e.2, e.1), fun p e _ => unrestricted (p, e.2.2, e.1)⟩

/-- Read through a run, G0 follows from the axiom the same way. -/
theorem Conditions.significant_of_unrestricted {S A Cond : Type} {P : Process S A}
    (K : Conditions S F Cond) (r : Run P) {sig : Pos → Nat → F → Prop}
    (unrestricted : Unrestricted sig) (own : Pos → F × Nat → Prop) :
    (K.valuation r own fun p e => sig p e.2 e.1).Significant :=
  fun p e _ => unrestricted (p, e.2, e.1)

/-- The frame of a web's level paths: a claim is a formation at a step, realized along a level
path when the levels admit it there. Nothing steps. -/
def Web.paths (W : Web F C) : Frame (Nat → C → Nat) Unit (F × Nat) :=
  ⟨⟨fun _ _ _ => False⟩, fun l e => W.Admits (l e.2) e.2 e.1⟩

/-- On level paths, under the axiom, G0 holds with unindexed significance for every reading of
`living`, and so does C, with “better” read as retaining and adding what has significance. -/
theorem Web.paths_g0_comparison (W : Web F C) {sig : Pos → Nat → F → Prop}
    (unrestricted : Unrestricted sig) (living : F × Nat → Prop) (p : Pos) :
    G0 W.paths living (fun _ e => ∀ q, sig q e.2 e.1) ∧
      Comparison W.paths living fun l' l => W.Retains sig p l l' ∧ W.Adds sig p l l' :=
  ⟨fun _ e _ _ q => unrestricted (q, e.2, e.1),
   fun _ _ ⟨keeps, e, _, realized, fresh⟩ =>
     ⟨fun t f _ admits => keeps (f, t) admits,
      ⟨e.2, e.1, unrestricted (p, e.2, e.1), realized, fresh⟩⟩⟩

/-- C with no axiom. On level paths, an extension in which every claim counts as living is exactly
a widening. -/
theorem Web.paths_extension_iff_widens (W : Web F C) {l l' : Nat → C → Nat} :
    Extension W.paths (fun _ => True) l' l ↔ W.Widens l l' :=
  ⟨fun ⟨keeps, e, _, realized, fresh⟩ => ⟨fun t f admits => keeps (f, t) admits, e.2, e.1, realized, fresh⟩,
   fun ⟨includes, t, f, admits, not⟩ =>
    ⟨fun e admits => includes e.2 e.1 admits, (f, t), trivial, admits, not⟩⟩

/-- C with no axiom. On level paths, C holds for every reading of `living` with “better” read as
widening what can form: the comparison by possibilities is a law, not a premise. -/
theorem Web.paths_comparison_widens (W : Web F C) (living : F × Nat → Prop) :
    Comparison W.paths living fun l' l => W.Widens l l' :=
  fun _ _ ⟨keeps, e, _, realized, fresh⟩ =>
    ⟨fun t f admits => keeps (f, t) admits, e.2, e.1, realized, fresh⟩

/-- The axiom is needed. Where nothing has significance, every level path retains every other
and none adds, and G0 fails at any event that lives; where everything has significance G0 holds.
The dynamics decides neither. -/
theorem Web.significance_undetermined (W : Web F C) (own : Pos → F × Nat → Prop) (p : Pos)
    {e : F × Nat} (alive : W.active e.2 e.1 ∧ ¬ W.UnderminingAt e.2 e.1) :
    (∀ l l' : Nat → C → Nat, W.Retains (fun _ _ _ => False) p l l' ∧
        ¬ W.Adds (fun _ _ _ => False) p l l') ∧
      (W.valuation own fun _ _ => True).Significant ∧
      ¬ (W.valuation own fun _ _ => False).Significant :=
  ⟨fun _ _ => ⟨fun _ _ no => (nomatch no), fun ⟨_, _, no, _⟩ => no⟩,
   fun _ _ _ => trivial, fun all => all p e alive⟩

/-! ## Witnesses -/

namespace Clearing

/-- Without the clearer's part every formation is admitted at every step: the source requires
nothing, the resource rises by one at each step and the habitat stays at two. -/
theorem admitted_all_without {l : Nat → Place → Nat}
    (without : flow.WithheldLevels clearerPart web l) : ∀ t f, web.Admits (l t) t f
  | _, .source => fun _ no => nomatch no
  | t, .clearer => fun c requires => match c, requires with
    | .resource, _ => Nat.le_trans (Nat.succ_le_succ (Nat.zero_le t))
        (Nat.le_of_eq (without.unique withheld t .resource).symm)
    | .habitat, no => nomatch no
    | .fuel _, no => nomatch no
  | t, .dweller => admitted_without without t

/-- The axiom counts what a free rider ends. Under it, from every standpoint, the clearer's part
loses the dweller, so the levels with it do not retain what has significance without it. The
levels without it retain what has significance with it, and the clearer is supported at every
step and admitted without its part: withholding the part ends nothing. -/
theorem free_rider_loses {l : Nat → Place → Nat} (without : flow.WithheldLevels clearerPart web l)
    {sig : Pos → Nat → Formation → Prop} (unrestricted : Unrestricted sig) (p : Pos) :
    web.Adds sig p l web.level ∧ ¬ web.Retains sig p web.level l ∧
      web.Retains sig p l web.level ∧
      ∀ t, web.Supported t .clearer ∧ web.Admits (l t) t .clearer :=
  have adds : web.Adds sig p l web.level :=
    ⟨2, .dweller, unrestricted (p, 2, .dweller), admitted_without without 2, unsupported_with 0⟩
  ⟨adds, fun retains => retains.not_added adds,
   fun t f _ _ => admitted_all_without without t f,
   fun t => ⟨dependent t .clearer trivial, admitted_all_without without t .clearer⟩⟩

/-- Each formation's region along its dependence: the clearer with the source that feeds its
resource; the source and the dweller, which nothing feeds, alone. -/
def dependenceRegion : Formation → Formation → Prop
  | .clearer, f => alongDependence f
  | .source, f => f = .source
  | .dweller, f => f = .dweller

/-- Centers bounded by their dependence license the free rider and disagree. With each
formation's significance stopping at its region along its dependence, the clearer's part retains
what has significance from the clearer's standpoint at every step, and loses the dweller from
the dweller's. -/
theorem centers_disagree {l : Nat → Place → Nat}
    (without : flow.WithheldLevels clearerPart web l) :
    web.Retains (bounded dependenceRegion) .clearer web.level l ∧
      web.Adds (bounded dependenceRegion) .dweller l web.level :=
  ⟨Web.retains_bounded_iff.mpr fun t => ((loses_beyond without).1 t).2.2,
   ⟨2, .dweller, rfl, admitted_without without 2, unsupported_with 0⟩⟩

end Clearing

namespace Transfer

/-- Under the axiom the conveyor's part is unordered: each level path adds a continuation with
significance that the other lacks, so neither retains the other. Ordering it needs a measure. -/
theorem unordered {l : Nat → Bool → Nat} (without : flow.WithheldLevels conveyorPart web l)
    {sig : Pos → Nat → Formation → Prop} (unrestricted : Unrestricted sig) (p : Pos) :
    web.Adds sig p web.level l ∧ web.Adds sig p l web.level ∧
      ¬ web.Retains sig p web.level l ∧ ¬ web.Retains sig p l web.level :=
  match mixed without with
  | ⟨gains, loses, _⟩ =>
    have adds := (Web.adds_iff_exceeds unrestricted p).mpr gains
    have lost := (Web.adds_iff_exceeds unrestricted p).mpr loses
    ⟨adds, lost, fun retains => retains.not_added lost, fun retains => retains.not_added adds⟩

end Transfer

namespace Restoring.Inflow

/-- Under the axiom the giver's part retains and adds: the levels with it retain what has
significance without it and add a continuation with significance. -/
theorem retains_adds {l : Nat → Unit → Nat} (without : flow.WithheldLevels giverPart web l)
    {sig : Pos → Nat → Bool → Prop} (unrestricted : Unrestricted sig) (p : Pos) :
    web.Retains sig p web.level l ∧ web.Adds sig p web.level l :=
  match widens without with
  | ⟨includes, exceeds, _⟩ =>
    ⟨includes.retains sig p, (Web.adds_iff_exceeds unrestricted p).mpr exceeds⟩

end Restoring.Inflow


/-! A drawer takes a condition's unit before any dependence on it forms. -/

namespace Preemption

/-- Across the first step the drawer `true` takes the condition's one unit; nothing gives. -/
def flow : Flow Bool Unit where
  present t := match t with
    | 0 => [true]
    | _ + 1 => []
  take t x _ := match t, x with
    | 0, true => 1
    | 0, false => 0
    | _ + 1, _ => 0
  give _ _ _ := 0

/-- The drawer requires nothing and is active at the first step. `false` requires the condition
at need one from the second step on and is never active. -/
def web : Web Bool Unit where
  level t _ := unitDrop t
  active t x := match x with
    | true => t = 0
    | false => False
  requires t x _ := match x with
    | true => False
    | false => 0 < t
  need _ _ _ := 1
  draws t x _ := match t, x with
    | 0, true => True
    | 0, false => False
    | _ + 1, _ => False

/-- The drawer's part. -/
def drawerPart : Bool → Bool
  | true => true
  | false => false

/-- Without the drawer's part the condition stays at one. -/
theorem withheld : flow.WithheldLevels drawerPart web fun _ _ => 1 :=
  ⟨fun t () => match t with
    | 0 => rfl
    | _ + 1 => rfl,
   fun () => rfl⟩

/-- Living, yet closing a possibility. The flow balances, only active formations give, and only
active formations take, and only from what they draw on; activity needs support. The drawer's
event at the first step is active and not undermining, since no dependence on the condition has
formed. Yet `false` is admitted at every step without the drawer's part and supported at no step
after the first with it: the part narrows what can form. Under the axiom it loses a continuation
with significance from every standpoint, so the levels with it do not retain what has
significance without it. -/
theorem not_undermining_yet_loses {l : Nat → Unit → Nat}
    (without : flow.WithheldLevels drawerPart web l) {sig : Pos → Nat → Bool → Prop}
    (unrestricted : Unrestricted sig) (p : Pos) :
    flow.Balances web ∧ flow.Acting web ∧ flow.Taking web ∧ web.Dependent ∧
      (web.active 0 true ∧ ¬ web.UnderminingAt 0 true) ∧
      (∀ t, web.Admits (l t) t false ∧ ¬ web.Supported (t + 1) false) ∧
      web.Includes l web.level ∧ web.Adds sig p l web.level ∧ ¬ web.Retains sig p web.level l :=
  have balances : flow.Balances web := fun t () => match t with
    | 0 => rfl
    | _ + 1 => rfl
  have each : ∀ t, web.Admits (l t) t false ∧ ¬ web.Supported (t + 1) false := fun t =>
    ⟨fun () _ => Nat.le_of_eq (without.unique withheld t ()).symm,
     fun supported => Nat.not_succ_le_zero 0 (supported () (Nat.succ_pos t))⟩
  have adds : web.Adds sig p l web.level :=
    ⟨1, false, unrestricted (p, 1, false), (each 1).1, (each 0).2⟩
  ⟨balances, fun _ _ _ _ gives => absurd gives (Nat.lt_irrefl 0),
   fun t x _ _ takes => match t, x, takes with
    | 0, true, _ => ⟨rfl, trivial⟩
    | 0, false, takes => absurd takes (Nat.lt_irrefl 0)
    | _ + 1, _, takes => absurd takes (Nat.lt_irrefl 0),
   fun _ x active _ requires => match x, active, requires with
    | true, _, no => (nomatch no)
    | false, no, _ => (nomatch no),
   ⟨rfl, fun ⟨(), _, g, requires, _⟩ => match g, requires with
    | true, no => no
    | false, no => Nat.lt_irrefl 0 no⟩,
   each, balances.opens_nothing without fun t _ => match t with
    | 0 => Nat.zero_le _
    | _ + 1 => Nat.zero_le _, adds,
   fun retains => retains.not_added adds⟩

end Preemption

end Becoming
