import Becoming.Inquiry
import Becoming.Dependence

/-!
# The Universal Metaethical Core on the Becoming spine

Evaluation is stated over the same frame as the dynamics. Positions, their own
regions and their significance are formed within the unfolding; `own` is a region
of formed relations, not an owner. `related` stands for formed relation
(conditioning, dependence, descent, cooperation) and `living` for the claims that are
living and further generation, 生生. Both are inputs of a valuation. The readings the
Becoming layer supplies below are narrower: `related` is co-participation in a
condition, which includes co-dependence without interaction, and `living` is activity
that does not undermine the dependence of others. Neither contains further generation:
an active formation participating in nothing counts as living.

The premise card, every item named and visible:
* S0, `SelfGood`: a position's own living and further generation has positive
  significance for it. Any S0-holding position with own living supplies a `Seed`.
* N, boundary neutrality. Each rule below is accepted, by its rivals, inside some
  formed boundary (`Within`); the premise is that no formed boundary restricts it
  (`Neutral`):
  - N_rel, `transmits`: significance passes along a formed relation to living
    content (patient side: self and other, kin, species, temporal distance);
  - N_std, `shares`: significance of living content holds from every standpoint;
  - A, `articulates`: a response a position has access to, which secures positive
    content from its standpoint on the response's scope, supplies a contributory
    reason (addressee side: no endorsement condition).
* C, `Comparison`: a no-loss extension realizing more living content is better.
* L, `LiftBetter`: outcome comparisons lift to responses with several outcomes;
  conservative default, every outcome better than every outcome.
* J1–J4: `PracticalJudgment` (protection priority, frontier selection, assigned
  responsibility), additional commitments outside the core; `Becoming.Bridge`
  states them on configurations by `BetterAt`.
* Correspondence: E (formation), `Connected`, and the reading of `living`. For one
  run the Becoming layer can supply the last two: `Conditions.valuation` and
  `Web.valuation` read its formation events, so that `living` is activity that does
  not undermine others' dependence and `related` is participation in a common
  condition. Connection then rests on which conditions are counted: one that every
  formation requires at level zero connects any web without changing `living`, while
  a coarse common condition that every formation draws on empties `living` once a
  dependence on it fails. `Becoming.Correspondence` states one discipline: a condition
  relates two events only when one draws on it and the other depends on it at a
  positive level, so that idle conditions connect nothing and connection through a
  condition is made by its living use. Both readings are relative to a run, while
  `G0`, `Comparison` and `universal_reason` take a `living` fixed across
  configurations; joining them needs a construction not given here.

Results:
* `significant_iff`: on a connected whole with some living content, living significance for every
  standpoint is equivalent to a seed with N_rel and N_std. This characterizes the
  content of living significance with no axiom; since Ren folded living significance (`G0`) (11 October 2026) it is a condition,
  and a theorem of the continuation condition of `Becoming.Significance`. The forward direction is
  nearly immediate; the content lies in the backward direction and in minimality.
* `positioned_articulation_of_articulates`: the positioned articulation D follows
  from A with living significance read with unindexed significance.
* `universal_reason`: a sound inquiry whose goal is new living content gives every
  position with access a contributory reason for it.
* What C asks of the comparison it constrains, with no premise. Extensions are irreflexive
  and compose (`Extension.irrefl`, `Extension.trans`). A comparison read off a description of
  configurations and comparing no description with itself satisfies C only if the description
  tells every extension apart from its base (`Comparison.separates`). A natural-number score
  satisfying C rises by at least one at every link of an endless chain of extensions
  (`Comparison.climbs`), so it ranks some link above any configuration whatever
  (`Comparison.outgrows`); a bounded score is not constrained so.
* Minimality: dropping the seed, N_rel, N_std, connection or A each leaves a
  consistent countermodel. Each rival accepts the same rule inside a formed
  boundary: its own region, its own standpoint, or endorsers.
* On a run read relationally, an event is living when its formation is active and
  does not consume in the run. A condition in which every living formation
  participates discharges connection (`significant_iff_of_common`); without one,
  connection can fail (`Separate.not_connected`). A consuming formation and a formation
  that loses its support co-participate in the drawn condition, so under N_rel a
  standpoint valuing the consumer's activity holds significant the living events of
  the formation that loses its support (`valuing_consumption_reaches`). The
  transmission runs along co-participation and does not use the consumption.
* Read stepwise, with dependences that may change (`Web.valuation`), an event is
  living when it is active and not undermining: it does not draw on a condition at a
  step after which the condition is below both the present need of a dependence on it
  and a need of that dependence met while it held. This is the stepwise reading, kept beside the
  whole-run and relation-level readings on Ren's delegation of 15 October 2026; no comparison uses
  it (DELEGATED-CHOICES D1, D10). Being within renewal at the step is not used as `living`, since it
  withholds the event of a formation whose own dependence breaks (`Renewable.broken_formation`); not
  breaking is not used either, since it includes drawing after a loss, which in `Renewable` keeps
  the condition from returning (`Renewable.drawing_after_loss`). The same results hold: a common
  condition discharges connection, and an event drawing at a step that breaks a dependence is
  related to the broken formation, so under N_rel valuing it reaches that formation's living events
  (`Web.valuing_breaking_reaches`). On fixed dependences the two readings share `related`, both
  include the broken formation's own event, and they include different events in both directions
  (`Renewable.readings_differ`).
* Read through relations (`Web.relations`), a claim is a formation's relation to a
  condition at a step, living when the formation is active, participates in the
  condition and the relation is not undermining. The stepwise reading of events is the
  conjunction of the reading of relations (`Web.living_iff_relations`), and one event
  can have a living relation and an undermining one (`Mixed.one_event_two_relations`).

Nothing here proves S0, N, A, C, L or J, binds a position that rejects them, or
treats bringing new lives into existence. A contributory reason is not a duty, a
ranking or a prediction of recognition or compliance. Every declaration has an
empty axiom report.

The core imports only its own layers and the foundation. Living significance, C, D and the secured positive
ground are stated here once; `Becoming.Bridge` shows that the definitions of
`GenerativeComparison` and `PositionedPositiveReason` are these, so their theorems
apply without the core depending on them.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

/-! ## Boundaries and neutrality -/

/-- A rule accepted only inside a formed boundary. -/
def Within {I : Type} (bound : I → Prop) (rule : I → Prop) : Prop :=
  ∀ i, bound i → rule i

/-- Boundary neutrality: no formed boundary restricts the rule. -/
def Neutral {I : Type} (rule : I → Prop) : Prop :=
  ∀ i, rule i

theorem Neutral.within {I : Type} {rule : I → Prop} (neutral : Neutral rule)
    (bound : I → Prop) : Within bound rule :=
  fun i _ => neutral i

/-! ## Significance across formed relations and standpoints -/

/-- The patient and standpoint side of evaluation within one unfolding. -/
structure Valuation (Pos C : Type) where
  living : C → Prop
  related : C → C → Prop
  own : Pos → C → Prop
  sig : Pos → C → Prop

namespace Valuation

variable {Pos C : Type} (V : Valuation Pos C)

/-- Formed relations as a process on claims: a step reaches a related living claim. -/
def relations : Process C Unit :=
  ⟨fun c _ d => V.related c d ∧ V.living d⟩

/-- Every two living claims are linked through formed relations among living claims. -/
def Connected : Prop :=
  ∀ c d, V.living c → V.living d → Reach V.relations c d

/-- S0 at a position. -/
def SelfGood (p : Pos) : Prop :=
  ∀ c, V.own p c → V.living c → V.sig p c

/-- Some living claim has positive significance from some standpoint. -/
def Seed : Prop :=
  ∃ p c, V.living c ∧ V.sig p c

/-- N_rel's rule. -/
def transmits : Pos × C × C → Prop
  | (p, c, d) => V.sig p c → V.related c d → V.living d → V.sig p d

/-- N_std's rule. -/
def shares : Pos × Pos × C → Prop
  | (p, q, c) => V.living c → V.sig p c → V.sig q c

/-- What living significance needs beyond the frame: a seed and both neutralities. -/
def Grounds : Prop :=
  V.Seed ∧ Neutral V.transmits ∧ Neutral V.shares

/-- Living significance at the level of claims: every living claim is significant from every standpoint. -/
def Significant : Prop :=
  ∀ p c, V.living c → V.sig p c

variable {V}

theorem seed_of_selfGood {p : Pos} {c : C} (self : V.SelfGood p) (own : V.own p c)
    (alive : V.living c) : V.Seed :=
  ⟨p, c, alive, self c own alive⟩

/-- Under N_rel, each standpoint's significance is an invariant of the formed relations. -/
theorem transmits_invariant (neutral : Neutral V.transmits) (p : Pos) :
    Invariant V.relations (V.sig p) :=
  fun c _ d step held => neutral (p, c, d) held step.1 step.2

/-- Significance reaches every living claim linked to a valued one. -/
theorem reaches (neutral : Neutral V.transmits) {p : Pos} {c d : C}
    (linked : Reach V.relations c d) (held : V.sig p c) : V.sig p d :=
  (transmits_invariant neutral p).reach linked held

theorem significant_of_grounds (connected : V.Connected) : V.Grounds → V.Significant
  | ⟨⟨p₁, c₁, alive₁, held⟩, transmit, share⟩, p, c, alive =>
    reaches transmit (connected c₁ c alive₁ alive) (share (p₁, p, c₁) alive₁ held)

/-- Characterization of living significance's content on a connected whole with some living claim. -/
theorem significant_iff (connected : V.Connected) (p₀ : Pos) {c₀ : C}
    (alive₀ : V.living c₀) : V.Significant ↔ V.Grounds :=
  ⟨fun all => ⟨⟨p₀, c₀, alive₀, all p₀ c₀ alive₀⟩,
      fun ⟨p, _, d⟩ _ _ alive => all p d alive,
      fun ⟨_, q, c⟩ alive _ => all q c alive⟩,
    significant_of_grounds connected⟩

end Valuation

/-! ## Living significance, D and the universal reason on the frame -/

variable {S A C Pos : Type}

/-- Living significance on the frame: living content realized at a configuration is positively
relevant there. -/
def G0 (F : Frame S A C) (living : C → Prop) (positive : S → C → Prop) : Prop :=
  ∀ s c, living c → F.realized s c → positive s c

/-- Claim-level significance is living significance for the frame, with unindexed positive relevance. -/
theorem Valuation.g0 (F : Frame S A C) {V : Valuation Pos C} (all : V.Significant) :
    G0 F V.living (fun _ c => ∀ p, V.sig p c) :=
  fun _ c alive _ p => all p c alive

/-- Every admitted outcome of the response holds positive content absent before it. -/
def SecuresPositiveGround {H R : Type} (admitted : R → H → Prop) (before : H → C → Prop)
    (positive : H → C → Prop) (r : R) : Prop :=
  ∀ h, admitted r h → ∃ c, positive h c ∧ ¬ before h c

/-- D: positioned articulation. Endorsement does not occur in it. -/
def PositionedArticulation {H R : Type} (access : Pos → R → Prop)
    (admitted : R → H → Prop) (before : H → C → Prop) (positive : H → C → Prop)
    (Reason : Pos → R → Prop) : Prop :=
  ∀ p r, access p r → SecuresPositiveGround admitted before positive r → Reason p r

/-- A's rule: securing positive content from one's own standpoint, with access,
supplies a contributory reason. -/
def articulates {H R : Type} (V : Valuation Pos C) (access : Pos → R → Prop)
    (admitted : R → H → Prop) (before : H → C → Prop) (Reason : Pos → R → Prop) :
    Pos × R → Prop
  | (p, r) => access p r →
      SecuresPositiveGround admitted before (fun _ c => V.sig p c) r → Reason p r

/-- D follows from A with living significance read with unindexed significance. -/
theorem positioned_articulation_of_articulates {H R : Type} {V : Valuation Pos C}
    {access : Pos → R → Prop} {admitted : R → H → Prop} {before : H → C → Prop}
    {Reason : Pos → R → Prop} (articulate : Neutral (articulates V access admitted before Reason)) :
    PositionedArticulation access admitted before (fun _ c => ∀ p, V.sig p c) Reason :=
  fun p r available secured => articulate (p, r) available fun h inScope =>
    match secured h inScope with
    | ⟨c, all, fresh⟩ => ⟨c, all p, fresh⟩

/-- A sound inquiry whose goal is new living content gives every position with access
to it a contributory reason. Seed, N_rel, N_std and A are the normative premises;
connection and soundness are facts about the unfolding and the inquiry. -/
theorem universal_reason {R : Type} {k : Nat} (F : Frame S A C) (V : Valuation Pos C)
    (before : S → C → Prop) {safe : S → A → S → Prop} {sense : S → A → S → Fin k}
    {response : R → List A} {B : S → Prop}
    (access : Pos → Policy A R k → Prop) (Reason : Pos → Policy A R k → Prop)
    (grounds : V.Grounds) (connected : V.Connected)
    (articulate : Neutral (articulates V access (Scope F.P sense response B) before Reason))
    (policy : Policy A R k)
    (sound : Sound F.P safe (Novel F V.living before) sense response policy B) :
    ∀ p, access p policy → Reason p policy :=
  fun p available => positioned_articulation_of_articulates articulate p policy available
    fun t reached => match Scope.secures sound t reached with
      | ⟨c, alive, held, fresh⟩ =>
        ⟨c, Valuation.g0 F (Valuation.significant_of_grounds connected grounds) t c alive held,
          fresh⟩

/-- Access as a realized claim: a position's access is formed in the unfolding. -/
def AccessAt {R : Type} (F : Frame S A C) (claim : Pos → R → C) (s : S) (p : Pos) (r : R) :
    Prop :=
  F.realized s (claim p r)

/-! ## Comparison, lifting and practical judgment on the frame -/

/-- A generative extension: the second configuration keeps every claim of the first
and realizes some living claim the first does not. -/
def Extension (F : Frame S A C) (living : C → Prop) (s t : S) : Prop :=
  (∀ c, F.realized s c → F.realized t c) ∧
    ∃ c, living c ∧ F.realized t c ∧ ¬ F.realized s c

/-- C on the frame. `Better s t` says that `t` is strictly better. -/
def Comparison (F : Frame S A C) (living : C → Prop) (Better : S → S → Prop) : Prop :=
  ∀ s t, Extension F living s t → Better s t

/-- **What C needs to see.** Where a comparison is read off a description of configurations and
compares no description with itself, C makes the description tell every extension apart from its
base: a description identifying a configuration with an extension of it supports no comparison
satisfying C. -/
theorem Comparison.separates {F : Frame S A C} {living : C → Prop} {D : Type} {π : S → D}
    {compare : D → D → Prop} (irreflexive : ∀ d, ¬ compare d d)
    (comparison : Comparison F living fun s t => compare (π s) (π t)) {s t : S}
    (extension : Extension F living s t) : π s ≠ π t :=
  fun same => irreflexive (π t) (Eq.subst (motive := fun d => compare d (π t)) same
    (comparison s t extension))

/-- No configuration extends itself. -/
theorem Extension.irrefl {F : Frame S A C} {living : C → Prop} {s : S} :
    ¬ Extension F living s s :=
  fun ⟨_, _, _, now, before⟩ => before now

/-- Extensions compose. -/
theorem Extension.trans {F : Frame S A C} {living : C → Prop} {s t u : S}
    (first : Extension F living s t) (second : Extension F living t u) : Extension F living s u :=
  ⟨fun c held => second.1 c (first.1 c held),
    let ⟨c, live, now, before⟩ := second.2
    ⟨c, live, now, fun earlier => before (first.1 c earlier)⟩⟩

/-- **A natural-number score satisfying C climbs.** Along an endless chain of extensions, a
natural-number score whose strict order satisfies C rises by at least one at every link. -/
theorem Comparison.climbs {F : Frame S A C} {living : C → Prop} {score : S → Nat}
    (comparison : Comparison F living fun s t => score s < score t) {next : Nat → S}
    (chain : ∀ i, Extension F living (next i) (next (i + 1))) :
    ∀ m, score (next 0) + m ≤ score (next m)
  | 0 => Nat.le_refl _
  | m + 1 => Nat.le_trans (Nat.succ_le_succ (Comparison.climbs comparison chain m))
      (comparison _ _ (chain m))

/-- **No configuration stays above an endless chain of extensions.** A natural-number score
satisfying C ranks some link of the chain above any configuration whatever: the link
`score s + 1` steps along. The force is the unit step of the natural numbers: a bounded score
(with values `k / (k + 1)`, say) can satisfy C without this. -/
theorem Comparison.outgrows {F : Frame S A C} {living : C → Prop} {score : S → Nat}
    (comparison : Comparison F living fun s t => score s < score t) {next : Nat → S}
    (chain : ∀ i, Extension F living (next i) (next (i + 1))) (s : S) :
    score s < score (next (score s + 1)) :=
  Nat.le_trans (Nat.le_add_left (score s + 1) (score (next 0)))
    (Comparison.climbs comparison chain (score s + 1))

/-- L, conservative default: every outcome of `a` is better than every outcome of `b`. -/
def LiftBetter (F : Frame S A C) (better : S → S → Prop) (s : S) (a b : A) : Prop :=
  ∀ t, F.P.step s a t → ∀ t', F.P.step s b t' → better t t'

theorem LiftBetter.trans {F : Frame S A C} {better : S → S → Prop} {s : S} {a b c : A}
    (transitive : ∀ {x y z}, better x y → better y z → better x z)
    (ab : LiftBetter F better s a b) (bc : LiftBetter F better s b c)
    (live : Enabled F.P s b) : LiftBetter F better s a c :=
  fun t ht t' ht' => match live with
    | ⟨m, hm⟩ => transitive (ab t ht m hm) (bc m hm t' ht')

theorem LiftBetter.irrefl {F : Frame S A C} {better : S → S → Prop} {s : S} {a : A}
    (irreflexive : ∀ x, ¬ better x x) (live : Enabled F.P s a) : ¬ LiftBetter F better s a a :=
  fun lifted => match live with
    | ⟨t, ht⟩ => irreflexive t (lifted t ht t ht)

/-- The default implies the weaker "some outcome beats some outcome" when both act. -/
theorem LiftBetter.some {F : Frame S A C} {better : S → S → Prop} {s : S} {a b : A}
    (lifted : LiftBetter F better s a b) (liveA : Enabled F.P s a) (liveB : Enabled F.P s b) :
    ∃ t t', F.P.step s a t ∧ F.P.step s b t' ∧ better t t' :=
  match liveA, liveB with
  | ⟨t, ht⟩, ⟨t', ht'⟩ => ⟨t, t', ht, ht', lifted t ht t' ht'⟩

/-! ## The relational reading supplied by the Becoming layer -/

section Reading

open RelationalRenewal

/-- Formation events of a run read through its conditions. An event is living when
its formation is active and does not consume in the run (the relational reading of
`RenewalComparison`); two events are related when their formations participate in a
common condition. Standpoints, their regions and significance remain supplied. -/
def Conditions.valuation {F Cond : Type} {P : Process S A} (K : Conditions S F Cond)
    (r : Run P) (own sig : Pos → F × Nat → Prop) : Valuation Pos (F × Nat) where
  living e := (K.along r).active e.2 e.1 ∧ ¬ ConsumingIn (K.along r) e.1
  related e e' := ∃ c, Participates (K.along r) e.1 c ∧ Participates (K.along r) e'.1 c
  own := own
  sig := sig

namespace Conditions

variable {F Cond : Type} {P : Process S A} (K : Conditions S F Cond) (r : Run P)
  (own sig : Pos → F × Nat → Prop)

/-- A condition in which every living formation participates connects the whole. -/
theorem connected_of_common (c₀ : Cond)
    (common : ∀ e, (K.valuation r own sig).living e → Participates (K.along r) e.1 c₀) :
    (K.valuation r own sig).Connected :=
  fun c d alive alive' =>
    Reach.of_step (a := ()) ⟨⟨c₀, common c alive, common d alive'⟩, alive'⟩

/-- With a condition in which every living formation participates, living significance for every
standpoint is exactly a seed with N_rel and N_std. Connection follows from
co-participation, given which conditions are counted. -/
theorem significant_iff_of_common (c₀ : Cond)
    (common : ∀ e, (K.valuation r own sig).living e → Participates (K.along r) e.1 c₀)
    (p₀ : Pos) {e₀ : F × Nat} (alive₀ : (K.valuation r own sig).living e₀) :
    (K.valuation r own sig).Significant ↔ (K.valuation r own sig).Grounds :=
  Valuation.significant_iff (connected_of_common K r own sig c₀ common) p₀ alive₀

/-- A consuming formation and a formation that loses its support from some step on
co-participate in the drawn condition, so their events are related. -/
theorem consumption_relates {f : F} (consuming : ConsumingIn (K.along r) f) :
    ∃ g T, (∀ t, T ≤ t → ¬ Supported (K.along r) t g) ∧
      ∀ t t', (K.valuation r own sig).related (f, t) (g, t') :=
  match consuming with
  | ⟨c, drawn, g, T, depends, lost⟩ =>
    ⟨g, T, fun t after supported => Nat.not_le_of_gt (lost t after) (supported c depends),
      fun _ _ => ⟨c, Or.inr drawn, Or.inl depends⟩⟩

/-- Under N_rel, a standpoint that values a consuming formation's activity holds
significant every living event of a formation that loses its support to the consumed
condition. The transmission runs along co-participation; it does not use the
consumption. Under the relational reading the consumer's own events are not living,
so S0 alone supplies no such valuation. N_rel's rival needs a boundary, or a narrower
account of which co-participation is a formed relation. -/
theorem valuing_consumption_reaches (transmit : Neutral (K.valuation r own sig).transmits)
    {f : F} (consuming : ConsumingIn (K.along r) f) :
    ∃ g T, (∀ t, T ≤ t → ¬ Supported (K.along r) t g) ∧
      ∀ p t t', (K.valuation r own sig).sig p (f, t) →
        (K.valuation r own sig).living (g, t') → (K.valuation r own sig).sig p (g, t') :=
  match consumption_relates K r own sig consuming with
  | ⟨g, T, lost, related⟩ =>
    ⟨g, T, lost, fun p t t' held alive => transmit (p, (f, t), (g, t')) held (related t t') alive⟩

end Conditions

/-! Two formations, each participating only in its own condition: both are living
and nothing consumes, yet no formed relation links them. -/

namespace Separate

def same : Bool → Bool → Prop
  | false, false => True
  | false, true => False
  | true, false => False
  | true, true => True

def frame : Process Unit Unit := ⟨fun _ _ _ => True⟩

def still : Run frame := ⟨fun _ => (), fun _ => (), fun _ => trivial⟩

def conditions : Conditions Unit Bool Bool :=
  ⟨fun _ _ => 0, fun _ _ => True, same, fun _ _ => 0, fun _ _ => False⟩

theorem stays (e e' : Bool × Nat)
    (related : ∃ c, (same e.1 c ∨ False) ∧ (same e'.1 c ∨ False)) :
    e.1 = false → e'.1 = false :=
  match e, e', related with
  | (false, _), (false, _), _ => fun _ => rfl
  | (true, _), _, _ => fun h => Bool.noConfusion h
  | (false, _), (true, _), ⟨false, _, .inl h⟩ => (nomatch h)
  | (false, _), (true, _), ⟨true, .inl h, _⟩ => (nomatch h)
  | (_, _), (_, _), ⟨_, .inr h, _⟩ => (nomatch h)
  | (_, _), (_, _), ⟨_, _, .inr h⟩ => (nomatch h)

theorem not_connected (own sig : Unit → Bool × Nat → Prop) :
    ¬ (conditions.valuation still own sig).Connected := fun connected =>
  Bool.noConfusion (Invariant.reach (P := (conditions.valuation still own sig).relations)
    (I := fun e => e.1 = false) (fun e _ e' step => stays e e' step.1)
    (connected (false, 0) (true, 0) ⟨trivial, fun ⟨_, drawn, _⟩ => drawn⟩
      ⟨trivial, fun ⟨_, drawn, _⟩ => drawn⟩) rfl)

end Separate

/-! ### The stepwise reading -/

/-- Formation events of a web read stepwise. An event is living when its formation is
active and it is not undermining: it does not draw on a condition at a step after which
the condition is below both the present need of a dependence on it and a need of that
dependence met while it held. Two events are related when their
formations participate in a common condition at their steps. Standpoints, their regions
and significance remain supplied. -/
def Web.valuation {F Cond : Type} (W : Web F Cond) (own sig : Pos → F × Nat → Prop) :
    Valuation Pos (F × Nat) where
  living e := W.active e.2 e.1 ∧ ¬ W.UnderminingAt e.2 e.1
  related e e' := ∃ c, W.Participates e.2 e.1 c ∧ W.Participates e'.2 e'.1 c
  own := own
  sig := sig

namespace Web

variable {F Cond : Type} (W : Web F Cond) (own sig : Pos → F × Nat → Prop)

/-- A condition in which every living event participates connects the whole. -/
theorem connected_of_common (c₀ : Cond)
    (common : ∀ e, (W.valuation own sig).living e → W.Participates e.2 e.1 c₀) :
    (W.valuation own sig).Connected :=
  fun c d alive alive' =>
    Reach.of_step (a := ()) ⟨⟨c₀, common c alive, common d alive'⟩, alive'⟩

/-- With a condition in which every living event participates, living significance for every standpoint
is exactly a seed with N_rel and N_std, on the stepwise reading as on the whole-run
one. -/
theorem significant_iff_of_common (c₀ : Cond)
    (common : ∀ e, (W.valuation own sig).living e → W.Participates e.2 e.1 c₀)
    (p₀ : Pos) {e₀ : F × Nat} (alive₀ : (W.valuation own sig).living e₀) :
    (W.valuation own sig).Significant ↔ (W.valuation own sig).Grounds :=
  Valuation.significant_iff (connected_of_common W own sig c₀ common) p₀ alive₀

/-- An event drawing on a condition at a step that breaks a dependence on it is not
living, and is related to every event of the broken formation that participates in the
condition. Other formations may take part in the breaking. -/
theorem breaking_relates {f g : F} {t : Nat} {c : Cond} (drawn : W.draws t f c)
    (broken : W.Broken t g c) :
    ¬ (W.valuation own sig).living (f, t) ∧
      ∀ t', W.Participates t' g c → (W.valuation own sig).related (f, t) (g, t') :=
  ⟨fun ⟨_, notUndermining⟩ =>
    notUndermining ⟨c, (show W.BreakingOn t f c from ⟨drawn, g, broken⟩).undermining⟩,
   fun _ joins => ⟨c, Or.inr drawn, joins⟩⟩

/-- Under N_rel, a standpoint that values an event drawing at a step that breaks a
dependence holds significant every living event of the broken formation that
participates in the condition, its event at that step included. The drawing event is
not living, so S0 alone supplies no such valuation. -/
theorem valuing_breaking_reaches (transmit : Neutral (W.valuation own sig).transmits)
    {f g : F} {t : Nat} {c : Cond} (drawn : W.draws t f c) (broken : W.Broken t g c)
    {p : Pos} (held : (W.valuation own sig).sig p (f, t)) {t' : Nat}
    (joins : W.Participates t' g c) (alive : (W.valuation own sig).living (g, t')) :
    (W.valuation own sig).sig p (g, t') :=
  transmit (p, (f, t), (g, t')) held ((breaking_relates W own sig drawn broken).2 t' joins) alive

end Web

/-- Relations read stepwise. A claim is a formation's relation to a condition at a step.
It is living when the formation is active and participates in the condition there, and
the relation is not undermining. Two relations are related when they concern one
condition or belong to one event. Standpoints, their regions and significance remain
supplied. -/
def Web.relations {F Cond : Type} (W : Web F Cond) (own sig : Pos → F × Cond × Nat → Prop) :
    Valuation Pos (F × Cond × Nat) where
  living e := W.active e.2.2 e.1 ∧ W.Participates e.2.2 e.1 e.2.1 ∧
    ¬ W.UnderminingOn e.2.2 e.1 e.2.1
  related e e' := e.2.1 = e'.2.1 ∨ (e.1 = e'.1 ∧ e.2.2 = e'.2.2)
  own := own
  sig := sig

/-- An event is living exactly when it is active and each of its relations to the
conditions it participates in is living: the stepwise reading of events is the
conjunction of the reading of relations. -/
theorem Web.living_iff_relations {F Cond : Type} (W : Web F Cond)
    (own sig : Pos → F × Nat → Prop) (own' sig' : Pos → F × Cond × Nat → Prop) (f : F)
    (t : Nat) :
    (W.valuation own sig).living (f, t) ↔
      W.active t f ∧ ∀ c, W.Participates t f c → (W.relations own' sig').living (f, c, t) :=
  ⟨fun ⟨active, notUndermining⟩ =>
    ⟨active, fun c joins => ⟨active, joins, fun undermining => notUndermining ⟨c, undermining⟩⟩⟩,
   fun ⟨active, all⟩ =>
    ⟨active, fun ⟨c, undermining⟩ => (all c (Or.inr undermining.1)).2.2 undermining⟩⟩

namespace Mixed

inductive Formation where
  | drawer
  | dependent

inductive Source where
  | kept
  | lost

/-- One event draws on two conditions; its step keeps the dependence on one and breaks
the dependence on the other. -/
def web : Web Formation Source where
  level t
    | .kept => 1
    | .lost => match t with
      | 0 => 1
      | _ + 1 => 0
  active t
    | .drawer => True
    | .dependent => match t with
      | 0 => True
      | _ + 1 => False
  requires _
    | .drawer => fun _ => False
    | .dependent => fun _ => True
  need _ _ _ := 1
  draws _
    | .drawer => fun _ => True
    | .dependent => fun _ => False

theorem dependent : web.Dependent
  | _, .drawer, _, _, depends => False.elim depends
  | 0, .dependent, _, .kept, _ => Nat.le_refl 1
  | 0, .dependent, _, .lost, _ => Nat.le_refl 1
  | _ + 1, .dependent, active, _, _ => False.elim active

/-- The event is not living, while one of its relations is: one activity takes part in
both generation and degeneration, and the reading of relations keeps them apart. -/
theorem one_event_two_relations (own sig : Pos → Formation × Nat → Prop)
    (own' sig' : Pos → Formation × Source × Nat → Prop) :
    ¬ (web.valuation own sig).living (.drawer, 0) ∧
    (web.relations own' sig').living (.drawer, .kept, 0) ∧
    ¬ (web.relations own' sig').living (.drawer, .lost, 0) :=
  have undermining : web.UnderminingOn 0 .drawer .lost :=
    ⟨trivial, .dependent, trivial,
      ⟨0, Nat.le_refl 0, fun _ _ _ => trivial, Nat.le_refl 1, Nat.le_refl _⟩, Nat.zero_lt_one⟩
  ⟨fun ⟨_, notUndermining⟩ => notUndermining ⟨.lost, undermining⟩,
   ⟨trivial, Or.inr trivial, fun ⟨_, _, _, _, unmet⟩ => Nat.lt_irrefl 1 unmet⟩,
   fun ⟨_, _, notUndermining⟩ => notUndermining undermining⟩

end Mixed

/-- On fixed dependences the stepwise reading relates exactly the events the whole-run
reading relates; the readings differ only in which events are living. -/
theorem Conditions.stepwise_related {F Cond : Type} {P : Process S A} (K : Conditions S F Cond)
    (r : Run P) (own sig : Pos → F × Nat → Prop) :
    ((K.dependence.along r).valuation own sig).related = (K.valuation r own sig).related :=
  rfl

/-- In one process the two readings include different events, in both directions. In
the escalating run the focal formation consumes, so the whole-run reading counts none
of its events as living, while the stepwise reading includes its first. In the dipping
run it does not consume, since the condition returns, so the whole-run reading counts
its first event as living, while the stepwise reading does not: it draws at a step
that breaks the sustaining formation's dependence. Both readings include the sustaining
formation's event at the step that breaks its dependence. -/
theorem Renewable.readings_differ (own sig : Pos → Renewable.Formation × Nat → Prop) :
    ((Renewable.conditions.dependence.along Renewable.escalating).valuation own sig).living
      (.focal, 0) ∧
    ¬ (Renewable.conditions.valuation Renewable.escalating own sig).living (.focal, 0) ∧
    (Renewable.conditions.valuation Renewable.dipping own sig).living (.focal, 0) ∧
    ¬ ((Renewable.conditions.dependence.along Renewable.dipping).valuation own sig).living
      (.focal, 0) ∧
    (Renewable.conditions.valuation Renewable.escalating own sig).living (.sustaining, 1) ∧
    ((Renewable.conditions.dependence.along Renewable.escalating).valuation own sig).living
      (.sustaining, 1) :=
  match Renewable.broken_formation with
  | ⟨active, _, _, victim⟩ =>
    ⟨⟨trivial, Renewable.stepwise_includes_before_escalation.2.1.not_undermining⟩,
     fun ⟨_, notConsuming⟩ => notConsuming
       ((Web.static_consumingIn _ _).mp Renewable.stepwise_includes_before_escalation.1),
     ⟨trivial, fun consuming => Renewable.dip_breaks_without_consuming.1
       ((Web.static_consumingIn _ _).mpr consuming)⟩,
     fun ⟨_, notUndermining⟩ => notUndermining
       ⟨(), trivial, .sustaining, trivial,
         ⟨0, Nat.le_refl 0, fun _ _ _ => trivial, Nat.le_refl 1, Nat.le_refl _⟩, Nat.zero_lt_one⟩,
     ⟨active, fun ⟨_, drawn, _⟩ => drawn⟩, ⟨active, victim⟩⟩

end Reading

/-! ## Minimality: each premise is needed, and each rival is a bounded rule -/

namespace Model

inductive Who where
  | evaluator | bystander

inductive Life where
  | self | other | beyond

-- Exhaustive, non-overlapping patterns keep these definitions free of `propext`.
def related : Life → Life → Prop
  | .self, .self => False
  | .self, .other => True
  | .self, .beyond => False
  | .other, .self => True
  | .other, .other => False
  | .other, .beyond => False
  | .beyond, _ => False

def own : Who → Life → Prop
  | .evaluator, .self => True
  | .evaluator, .other => False
  | .evaluator, .beyond => False
  | .bystander, _ => False

/-- `beyond` stands outside every formed relation of the others. -/
def linked : Life → Prop
  | .self => True
  | .other => True
  | .beyond => False

def valuation (living : Life → Prop) (sig : Who → Life → Prop) : Valuation Who Life :=
  ⟨living, related, own, sig⟩

theorem linked_connected (sig : Who → Life → Prop) : (valuation linked sig).Connected
  | .self, .self, _, _ => Reach.refl _ _
  | .other, .other, _, _ => Reach.refl _ _
  | .self, .other, _, _ => Reach.of_step (a := ()) ⟨trivial, trivial⟩
  | .other, .self, _, _ => Reach.of_step (a := ()) ⟨trivial, trivial⟩
  | .beyond, _, dead, _ => nomatch dead
  | _, .beyond, _, dead => nomatch dead

/-- Present aim: no seed. Both neutralities hold vacuously; nothing is significant. -/
theorem seed_is_needed :
    let V := valuation linked (fun _ _ => False)
    V.Connected ∧ ¬ V.Seed ∧ Neutral V.transmits ∧ Neutral V.shares ∧ ¬ V.Significant :=
  ⟨linked_connected _, fun ⟨_, _, _, held⟩ => held,
    fun ⟨_, _, _⟩ held => (nomatch held), fun ⟨_, _, _⟩ _ held => (nomatch held),
    fun all => all .evaluator .self trivial⟩

/-- Significance of the evaluator's own region only, from every standpoint. -/
def ownRegion : Who → Life → Prop
  | _, .self => True
  | _, .other => False
  | _, .beyond => False

/-- N_rel is needed. The rival holds S0, a seed and N_std, and transmits significance
only inside the evaluator's own region. -/
theorem relational_neutrality_is_needed :
    let V := valuation linked ownRegion
    V.Connected ∧ V.SelfGood .evaluator ∧ V.Seed ∧ Neutral V.shares ∧
    Within (fun i => own .evaluator i.2.2) V.transmits ∧
    ¬ Neutral V.transmits ∧ ¬ V.Significant :=
  ⟨linked_connected _,
    fun | .self, _, _ => trivial
        | .other, owned, _ => (nomatch owned)
        | .beyond, owned, _ => (nomatch owned),
    ⟨.evaluator, .self, trivial, trivial⟩,
    fun | (_, _, .self), _, _ => trivial
        | (_, _, .other), _, held => held
        | (_, _, .beyond), dead, _ => dead,
    fun | (_, _, .self), _, _, _, _ => trivial
        | (_, _, .other), bound, _, _, _ => (nomatch bound)
        | (_, _, .beyond), bound, _, _, _ => (nomatch bound),
    fun neutral => neutral (.evaluator, .self, .other) trivial trivial trivial,
    fun all => all .evaluator .other trivial⟩

/-- Significance from the evaluator's standpoint only. -/
def ownStandpoint : Who → Life → Prop
  | .evaluator, _ => True
  | .bystander, _ => False

/-- N_std is needed. The rival holds a seed and N_rel at every standpoint, and shares
significance only with its own standpoint. -/
theorem standpoint_neutrality_is_needed :
    let V := valuation linked ownStandpoint
    V.Connected ∧ V.Seed ∧ Neutral V.transmits ∧
    Within (fun i => i.1 = i.2.1) V.shares ∧
    ¬ Neutral V.shares ∧ ¬ V.Significant :=
  ⟨linked_connected _, ⟨.evaluator, .self, trivial, trivial⟩,
    fun | (.evaluator, _, _), _, _, _ => trivial
        | (.bystander, _, _), held, _, _ => held,
    fun | (_, _, _), rfl, _, held => held,
    fun neutral => neutral (.evaluator, .bystander, .self) trivial trivial,
    fun all => all .bystander .self trivial⟩

theorem no_relation_into_beyond : ∀ c, ¬ related c .beyond
  | .self => id
  | .other => id
  | .beyond => id

/-- No path of formed relations enters `beyond` from elsewhere. -/
theorem isolated {living : Life → Prop} {sig : Who → Life → Prop} :
    ∀ {c : Life} {word : List Unit},
      Trace (valuation living sig).relations c word .beyond → c = .beyond
  | _, _, .nil _ => rfl
  | _, _, .cons step rest => by
    have entered := isolated rest
    subst entered
    exact absurd step.1 (no_relation_into_beyond _)

/-- Connection is needed: with an unrelated living claim, every premise holds and
significance stops where formed relations stop. -/
theorem connection_is_needed :
    let V := valuation (fun _ => True) (fun _ c => linked c)
    V.Grounds ∧ ¬ V.Connected ∧ ¬ V.Significant :=
  ⟨⟨⟨.evaluator, .self, trivial, trivial⟩,
      fun | (_, _, .self), _, _, _ => trivial
          | (_, _, .other), _, _, _ => trivial
          | (_, c, .beyond), _, rel, _ => absurd rel (no_relation_into_beyond c),
      fun | (_, _, _), _, held => held⟩,
    fun connected => match connected .self .beyond trivial trivial with
      | ⟨_, path⟩ => Life.noConfusion (isolated path),
    fun all => all .evaluator .beyond trivial⟩

/-- Only the evaluator endorses. -/
def endorses : Who → Prop
  | .evaluator => True
  | .bystander => False

/-- A is needed for endorsement independence. Every living claim is significant from
every standpoint, yet a reason restricted to endorsers is consistent with that and
withholds the reason from a non-endorsing position with access. -/
theorem articulation_neutrality_is_needed :
    let V := valuation linked (fun _ _ => True)
    let Art := articulates (H := Unit) (R := Unit) V (fun _ _ => True) (fun _ _ => True)
      (fun _ _ => False) (fun p _ => endorses p)
    V.Significant ∧ Within (fun i => endorses i.1) Art ∧ ¬ Neutral Art :=
  ⟨fun _ _ _ => trivial,
    fun | (.evaluator, _), _, _, _ => trivial
        | (.bystander, _), bound, _, _ => (nomatch bound),
    fun neutral => neutral (.bystander, ()) trivial (fun _ _ => ⟨.self, trivial, id⟩)⟩

end Model

end Becoming
