import Becoming.Boundaries
import Becoming.Ranking

/-!
# Relevance: G0's uses under the axiom

`Becoming.Significance` shows that Ren's one axiom gives G0. Before Ren decided whether the axiom
replaces G0, every use of G0 in the core and in the periphery's
generative-capacity modules was audited for what it needs of positive relevance and of
`living`. This module states what the audit found.

* **G0 from the axiom on every frame.** Read positive relevance from significance: realized
  living content whose continuation has significance from every standpoint
  (`Frame.relevance`). Under the axiom G0 holds on every frame for every reading of `living`
  (`g0_of_unrestricted`), and this relevance is the least satisfying G0, exactly the realized
  living content (`relevance_least`). Every use of G0 takes it as a hypothesis for an arbitrary
  positive relevance, so each is discharged by this one; `Becoming.Bridge` does so for the
  periphery's interface. With no axiom, G0 with this relevance holds exactly where every
  realized living claim's continuation has significance from every standpoint
  (`g0_relevance_iff`): it is the axiom's condition on realized living content.
* **The axiom is G0 for anything.** On a frame whose claims are formations at steps, each
  realized at some configuration, the axiom holds exactly when G0 holds with every claim living
  and positive relevance read as significance from every standpoint (`unrestricted_iff_g0`).
  The level paths of every web are such a frame (`Web.unrestricted_iff_paths_g0`). Replacing G0
  by the axiom widens its scope from living content to anything and weakens “positive” to “has
  significance”.
* **The reason premises keep their scope only on living content.** Where everything has
  significance, A read with bare significance supplies a reason for every response with access
  that yields any new content, living or not; read on living content it supplies one for every
  response securing new living content (`articulates_total`). In a witness the first forces a
  reason the second does not (`Widening.bare_forces_reason`). Read on living content, A gives D
  on living content (`positioned_articulation_of_articulatesLiving`), and the universal reason
  follows from the axiom with no seed, neutrality or connection premise
  (`universal_reason_of_unrestricted`).
* **C read on possibilities.** The possibility reading credits a formation at a step when the
  course's levels admit it there. Under the axiom, extension under this reading is the axiom's
  comparison, retaining and adding what has significance (`Ranking.possible_extends_iff`). In
  every law of the support-gated family it ranks the course without an overdrawing formation
  above the course with it (`Ranking.possible_ranks`), restraint above overdraw
  (`Ranking.possible_restraint`), also with a third formation where the stepwise reading leaves
  them unranked (`Ranking.ThirdParty.possible_extends`), and sharing above winning by
  consumption (`Ranking.possible_contest`). It withholds no event: in a dependent course it
  credits every active formation (`Ranking.possible_of_active`), the malignant formation's
  first event included, which the whole-run reading withholds (`Ranking.malignant_possible`).
* **What it does not rank.** A formation drawing within renewal adds no possibility. Its course
  and the course without it admit the same formations, and neither extends the other
  (`Ranking.possible_tie`), while both readings of `living` rank its presence higher
  (`Ranking.readings_rank_presence`); sharing is an instance (`Ranking.sharing_presence`).
  Generally a level path nowhere lower is never ranked below (`Web.not_added_of_le`), so rest
  and restraint that leave the levels no lower are never worse.
* **Possibilities first.** Ranking by possibilities first and then by a reading's credited
  events satisfies C under the possibility reading and is a strict order
  (`Ranking.possibleFirst_order`). Whatever the reading, it ranks the absence of an overdrawing
  formation above its occurrence (`Ranking.possibleFirst_overdraw`); with either reading of
  `living` second, it ranks the presence of a formation drawing within renewal above its absence
  (`Ranking.possibleFirst_presence`). It also ranks a rest that adds no possibility below
  uninterrupted activity (`Ranking.Rest.rest_ranked_below`): counting continuations beyond
  possibilities counts a pause as a loss. The order is a further premise; the axiom gives the
  possibility reading alone.

**Ren's decisions, 11 October 2026.** Positive relevance is folded into significance (“Positive
relevance - yes, let's fold”): it is the significance of realized living content. Ren left the
comparison of courses to the AI (“Comparing courses - you decide”), which compares courses on
possibilities; the theorems of the other comparisons stay.

**AI reading, pending Ren.**
- Significance need not be positive, and what is positive is the living, 生生: so the AI reads
  Ren's “doesn't have to be positive”.
- The possibility reading of C reads “what has significance is what can form”
  (`Becoming.Significance`) and Ren's “more possibilities of becoming”. It counts what can form,
  not what does: a course in which a formation lives without adding a possibility is neither
  better nor worse than one in which it could live and does not.

What is not derived: the warrant of the axiom; the step from significance to a reason (A), which
stays a premise. After the audit Ren folded G0 (11 October 2026): it is no longer an axiom.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

/-! ## Positive relevance read from significance -/

section Relevance

variable {S A Q F Pos : Type}

/-- Positive relevance read from significance: realized living content whose continuation has
significance from every standpoint, a claim being some formation's continuation at some step. -/
def Frame.relevance (M : Frame S A Q) (living : Q → Prop) (sig : Pos → Nat → F → Prop)
    (formation : Q → F) (step : Q → Nat) (s : S) (c : Q) : Prop :=
  living c ∧ M.realized s c ∧ ∀ p, sig p (step c) (formation c)

/-- Under the axiom G0 holds on every frame for every reading of `living`, with positive
relevance read from significance. -/
theorem g0_of_unrestricted (M : Frame S A Q) (living : Q → Prop) {sig : Pos → Nat → F → Prop}
    (unrestricted : Unrestricted sig) (formation : Q → F) (step : Q → Nat) :
    G0 M living (M.relevance living sig formation step) :=
  fun _ c alive realized => ⟨alive, realized, fun p => unrestricted (p, step c, formation c)⟩

/-- It is the least positive relevance satisfying G0: under the axiom it holds of exactly the
realized living content, and every positive relevance satisfying G0 holds wherever it does. -/
theorem relevance_least (M : Frame S A Q) (living : Q → Prop) {sig : Pos → Nat → F → Prop}
    (unrestricted : Unrestricted sig) (formation : Q → F) (step : Q → Nat) :
    (∀ s c, M.relevance living sig formation step s c ↔ living c ∧ M.realized s c) ∧
      ∀ positive, G0 M living positive →
        ∀ s c, M.relevance living sig formation step s c → positive s c :=
  ⟨fun _ c => ⟨fun ⟨alive, realized, _⟩ => ⟨alive, realized⟩,
     fun ⟨alive, realized⟩ => ⟨alive, realized, fun p => unrestricted (p, step c, formation c)⟩⟩,
   fun _ g0 s c ⟨alive, realized, _⟩ => g0 s c alive realized⟩

/-- Positive relevance folded into significance (Ren, 11 October 2026). Read from significance, G0
holds exactly where the continuation of every realized living claim has significance from every
standpoint: it is the axiom's condition on realized living content, with no axiom. -/
theorem g0_relevance_iff (M : Frame S A Q) (living : Q → Prop) (sig : Pos → Nat → F → Prop)
    (formation : Q → F) (step : Q → Nat) :
    G0 M living (M.relevance living sig formation step) ↔
      ∀ s c, living c → M.realized s c → ∀ p, sig p (step c) (formation c) :=
  ⟨fun g0 s c alive realized => (g0 s c alive realized).2.2,
   fun all s c alive realized => ⟨alive, realized, all s c alive realized⟩⟩

/-- The axiom is G0 for anything. On a frame whose claims are formations at steps, each realized
at some configuration, the axiom holds exactly when G0 holds with every claim living and
positive relevance read as significance from every standpoint. -/
theorem unrestricted_iff_g0 (M : Frame S A (F × Nat)) (somewhere : ∀ e, ∃ s, M.realized s e)
    {sig : Pos → Nat → F → Prop} :
    Unrestricted sig ↔ G0 M (fun _ => True) (fun _ e => ∀ p, sig p e.2 e.1) :=
  ⟨fun unrestricted _ e _ _ p => unrestricted (p, e.2, e.1),
   fun g0 ⟨p, t, f⟩ => match somewhere (f, t) with
    | ⟨s, realized⟩ => g0 s (f, t) trivial realized p⟩

end Relevance

section Paths

variable {F C Pos : Type}

/-- Every formation at every step is admitted along some level path: the one meeting its needs
there. -/
theorem Web.paths_somewhere (W : Web F C) (e : F × Nat) : ∃ l, W.paths.realized l e :=
  ⟨fun _ c => W.need e.2 e.1 c, fun _ _ => Nat.le_refl _⟩

/-- So on the level paths of every web the axiom is G0 for anything. -/
theorem Web.unrestricted_iff_paths_g0 (W : Web F C) {sig : Pos → Nat → F → Prop} :
    Unrestricted sig ↔ G0 W.paths (fun _ => True) (fun _ e => ∀ p, sig p e.2 e.1) :=
  unrestricted_iff_g0 W.paths W.paths_somewhere

end Paths

/-! ## The reason premises keep their scope on living content -/

section Reasons

variable {S A Q F Pos : Type}

/-- Where everything has significance, securing ground with bare significance is securing any
new content. -/
theorem securesPositiveGround_total {H R : Type} {admitted : R → H → Prop}
    {before : H → Q → Prop} {sig : H → Q → Prop} (total : ∀ h c, sig h c) (r : R) :
    SecuresPositiveGround admitted before sig r ↔ ∀ h, admitted r h → ∃ c, ¬ before h c :=
  ⟨fun secured h inScope => match secured h inScope with
    | ⟨c, _, fresh⟩ => ⟨c, fresh⟩,
   fun novel h inScope => match novel h inScope with
    | ⟨c, fresh⟩ => ⟨c, total h c, fresh⟩⟩

/-- A read on living content: securing living content with significance from one's own
standpoint, with access, supplies a contributory reason. -/
def articulatesLiving {H R : Type} (V : Valuation Pos Q) (access : Pos → R → Prop)
    (admitted : R → H → Prop) (before : H → Q → Prop) (Reason : Pos → R → Prop) :
    Pos × R → Prop
  | (p, r) => access p r →
      SecuresPositiveGround admitted before (fun _ c => V.living c ∧ V.sig p c) r → Reason p r

/-- Where everything has significance, A read with bare significance supplies a reason for every
response with access that yields any new content, living or not; read on living content it
supplies one for every response securing new living content. -/
theorem articulates_total {H R : Type} {V : Valuation Pos Q} {access : Pos → R → Prop}
    {admitted : R → H → Prop} {before : H → Q → Prop} {Reason : Pos → R → Prop}
    (total : ∀ p c, V.sig p c) :
    (Neutral (articulates V access admitted before Reason) ↔
      ∀ p r, access p r → (∀ h, admitted r h → ∃ c, ¬ before h c) → Reason p r) ∧
    (Neutral (articulatesLiving V access admitted before Reason) ↔
      ∀ p r, access p r → SecuresPositiveGround admitted before (fun _ c => V.living c) r →
        Reason p r) :=
  ⟨⟨fun articulate p r available novel =>
      articulate (p, r) available ((securesPositiveGround_total (fun _ c => total p c) r).2 novel),
    fun all ⟨p, r⟩ available secured =>
      all p r available ((securesPositiveGround_total (fun _ c => total p c) r).1 secured)⟩,
   ⟨fun articulate p r available secured =>
      articulate (p, r) available fun h inScope => match secured h inScope with
        | ⟨c, alive, fresh⟩ => ⟨c, ⟨alive, total p c⟩, fresh⟩,
    fun all ⟨p, r⟩ available secured =>
      all p r available fun h inScope => match secured h inScope with
        | ⟨c, ⟨alive, _⟩, fresh⟩ => ⟨c, alive, fresh⟩⟩⟩

/-- D on living content follows from A read on living content, with G0's unindexed
significance. -/
theorem positioned_articulation_of_articulatesLiving {H R : Type} {V : Valuation Pos Q}
    {access : Pos → R → Prop} {admitted : R → H → Prop} {before : H → Q → Prop}
    {Reason : Pos → R → Prop}
    (articulate : Neutral (articulatesLiving V access admitted before Reason)) :
    PositionedArticulation access admitted before (fun _ c => V.living c ∧ ∀ p, V.sig p c)
      Reason :=
  fun p r available secured => articulate (p, r) available fun h inScope =>
    match secured h inScope with
    | ⟨c, ⟨alive, all⟩, fresh⟩ => ⟨c, ⟨alive, all p⟩, fresh⟩

/-- A sound inquiry whose goal is new living content gives every position with access to it a
contributory reason, from G0 at the level of claims and A read on living content. -/
theorem universal_reason_living {R : Type} {k : Nat} (M : Frame S A Q) (V : Valuation Pos Q)
    (before : S → Q → Prop) {safe : S → A → S → Prop} {sense : S → A → S → Fin k}
    {response : R → List A} {B : S → Prop}
    (access : Pos → Policy A R k → Prop) (Reason : Pos → Policy A R k → Prop)
    (all : V.Significant)
    (articulate : Neutral (articulatesLiving V access (Scope M.P sense response B) before Reason))
    (policy : Policy A R k)
    (sound : Sound M.P safe (Novel M V.living before) sense response policy B) :
    ∀ p, access p policy → Reason p policy :=
  fun p available => articulate (p, policy) available fun t reached =>
    match Scope.secures sound t reached with
    | ⟨c, alive, _, fresh⟩ => ⟨c, ⟨alive, all p c alive⟩, fresh⟩

/-- Under the axiom the universal reason needs no seed, neutrality or connection premise: on
every reading in which a claim's significance from a standpoint is that of some formation's
continuation at some step, a sound inquiry whose goal is new living content gives every
position with access to it a contributory reason, from A read on living content. -/
theorem universal_reason_of_unrestricted {R : Type} {k : Nat} (M : Frame S A Q)
    (V : Valuation Pos Q) (before : S → Q → Prop) {safe : S → A → S → Prop}
    {sense : S → A → S → Fin k} {response : R → List A} {B : S → Prop}
    (access : Pos → Policy A R k → Prop) (Reason : Pos → Policy A R k → Prop)
    {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig) (formation : Q → F)
    (step : Q → Nat) (reads : ∀ p c, sig p (step c) (formation c) → V.sig p c)
    (articulate : Neutral (articulatesLiving V access (Scope M.P sense response B) before Reason))
    (policy : Policy A R k)
    (sound : Sound M.P safe (Novel M V.living before) sense response policy B) :
    ∀ p, access p policy → Reason p policy :=
  universal_reason_living M V before access Reason
    (Valuation.premises_of_unrestricted unrestricted formation step reads).1 articulate policy sound

end Reasons

/-! ### Bare significance widens A

One position and one response with one outcome. Of two claims, `true` is living and held before;
`false` is new and not living. -/

namespace Widening

def valuation : Valuation Unit Bool :=
  ⟨fun c => c = true, fun _ _ => False, fun _ _ => True, fun _ _ => True⟩

def admitted : Unit → Unit → Prop := fun _ _ => True

def before : Unit → Bool → Prop := fun _ c => c = true

/-- Everything has significance. A read with bare significance forces a reason for the response,
whose only new content is not living; read on living content it forces none, for the empty
reason satisfies it. -/
theorem bare_forces_reason :
    (∀ p c, valuation.sig p c) ∧
    (∀ Reason : Unit → Unit → Prop,
      Neutral (articulates valuation (fun _ _ => True) admitted before Reason) → Reason () ()) ∧
    Neutral (articulatesLiving valuation (fun _ _ => True) admitted before fun _ _ => False) :=
  ⟨fun _ _ => trivial,
   fun _ articulate => articulate ((), ()) trivial fun _ _ => ⟨false, trivial, Bool.noConfusion⟩,
   fun ⟨_, _⟩ _ secured => match secured () trivial with
    | ⟨_, ⟨alive, _⟩, fresh⟩ => fresh alive⟩

end Widening

/-! ## Levels nowhere lower are never ranked below -/

namespace Web

variable {F C : Type} {W : Web F C}

/-- A level path at least as high at every step and condition includes the other: it admits
whatever the other admits. -/
theorem Includes.of_le {l l' : Nat → C → Nat} (le : ∀ t c, l' t c ≤ l t c) : W.Includes l l' :=
  fun t _ admits => Admits.mono (le t) admits

/-- A level path nowhere lower is never ranked below by retaining and adding: a path whose levels
are nowhere higher adds nothing against it, whatever has significance. -/
theorem not_added_of_le {Pos : Type} {sig : Pos → Nat → F → Prop} {p : Pos}
    {l l' : Nat → C → Nat} (le : ∀ t c, l' t c ≤ l t c) : ¬ W.Adds sig p l' l :=
  ((Includes.of_le le).retains sig p).not_added

end Web

/-! ## C read on possibilities -/

namespace Ranking

open RelationalRenewal RelationalRenewal.Law

variable {W F C : Type}

/-- The possibility reading: a course credits a formation at a step when the course's levels
admit it there, active or not. -/
def possible (U : W → Unfolding F C) (w : W) (e : F × Nat) : Prop :=
  (Web.static (U w)).Admits ((U w).level e.2) e.2 e.1

/-- In a dependent course the possibility reading credits every active formation, so every event
that either reading of `living` credits. -/
theorem possible_of_active {U : W → Unfolding F C} {w : W} (dependent : Dependent (U w))
    {e : F × Nat} (active : (U w).active e.2 e.1) : possible U w e :=
  dependent e.2 e.1 active

/-- The course without the focal formation admits every formation at every step. -/
theorem absent_admits_all (L : Law) (fWithin : L.needF ≤ L.needG) (gStart : L.needG ≤ L.start) :
    ∀ e, possible (course L) .absent e
  | (.focal, t), _, _ =>
    Nat.le_trans fWithin (Nat.le_trans gStart (undisturbed_sustains L gStart t))
  | (.sustaining, t), _, _ => Nat.le_trans gStart (undisturbed_sustains L gStart t)

/-- For every law of the family in which the focal formation draws beyond renewal from some step
on, the course without it extends the course with it under the possibility reading. -/
theorem possible_extends (L : Law) (positive : 0 < L.needG) (fWithin : L.needF ≤ L.needG)
    (gStart : L.needG ≤ L.start) {T0 : Nat}
    (over : ∀ t, T0 ≤ t → L.renew + L.contrib t < L.draw t) :
    ExtendsUnder (possible (course L)) .occurs .absent :=
  match overdraw_consuming L positive fWithin over with
  | ⟨_, T, lost⟩ =>
    ⟨fun e _ => absent_admits_all L fWithin gStart e, (.sustaining, T), trivial,
     absent_admits_all L fWithin gStart (.sustaining, T),
     fun admitted => lost T (Nat.le_refl T) (admitted () trivial)⟩

/-- So every comparison satisfying C under the possibility reading ranks the course without the
overdrawing formation strictly higher. -/
theorem possible_ranks (L : Law) (positive : 0 < L.needG) (fWithin : L.needF ≤ L.needG)
    (gStart : L.needG ≤ L.start) {T0 : Nat}
    (over : ∀ t, T0 ≤ t → L.renew + L.contrib t < L.draw t)
    {Better : Course → Course → Prop} (ranks : ComparisonUnder (possible (course L)) Better) :
    Better .occurs .absent :=
  ranks _ _ (possible_extends L positive fWithin gStart over)

/-- Both courses of a law have the law's requirements and needs, so the possibility reading of
either is admission on the law's web. -/
theorem possible_course_iff (L : Law) : ∀ w e, possible (course L) w e ↔
    (Web.static L.unfolding).Admits ((course L w).level e.2) e.2 e.1
  | .occurs, _ => Iff.rfl
  | .absent, _ => Iff.rfl

/-- Under the axiom, extension under the possibility reading is the axiom's comparison: one
course extends another exactly when, on the law's web, its levels retain what has significance
along the other's and add to it. -/
theorem possible_extends_iff (L : Law) {Pos : Type} {sig : Pos → Nat → Part → Prop}
    (unrestricted : Unrestricted sig) (p : Pos) (w w' : Course) :
    ExtendsUnder (possible (course L)) w w' ↔
      (Web.static L.unfolding).Retains sig p (course L w').level (course L w).level ∧
        (Web.static L.unfolding).Adds sig p (course L w').level (course L w).level :=
  have conv := possible_course_iff L
  ⟨fun ⟨keeps, e, _, credited, fresh⟩ =>
    ⟨fun t f _ admits => (conv w' (f, t)).1 (keeps (f, t) ((conv w (f, t)).2 admits)),
     e.2, e.1, unrestricted (p, e.2, e.1), (conv w' e).1 credited,
     fun admits => fresh ((conv w e).2 admits)⟩,
   fun ⟨retains, t, f, _, admits, ended⟩ =>
    ⟨fun e credited =>
      (conv w' e).2 (retains e.2 e.1 (unrestricted (p, e.2, e.1)) ((conv w e).1 credited)),
     (f, t), trivial, (conv w' (f, t)).2 admits,
     fun credited => ended ((conv w (f, t)).1 credited)⟩⟩

/-- Malignant growth under the possibility reading: the course without the formation extends the
course with it, while the formation's first event is credited, as the stepwise reading credits
it and the whole-run reading withholds it. -/
theorem malignant_possible :
    ExtendsUnder (possible (course malignant)) .occurs .absent ∧
      possible (course malignant) .occurs (.focal, 0) ∧
      stepwise (course malignant) .occurs (.focal, 0) ∧
      ¬ wholeRun (course malignant) .occurs (.focal, 0) :=
  have over : ∀ t, 0 ≤ t → malignant.renew + malignant.contrib t < malignant.draw t :=
    fun _ _ => Nat.lt_succ_of_le (Nat.le_succ 1)
  ⟨possible_extends malignant Nat.zero_lt_two (Nat.le_succ 1)
     (Nat.le_succ_of_le (Nat.le_succ 2)) over,
   fun _ _ => Nat.le_succ_of_le (Nat.le_succ_of_le (Nat.le_succ 1)),
   credited_before_loss malignant (t := 0)
     (Nat.le_succ_of_le (Nat.le_succ_of_le (Nat.le_succ 1))) (Nat.le_refl 2) (Nat.le_succ 1),
   fun ⟨_, notConsuming⟩ =>
     notConsuming (overdraw_consuming malignant Nat.zero_lt_two (Nat.le_succ 1) over).1⟩

/-- Under the possibility reading sharing extends winning by consumption. -/
theorem possible_contest : ExtendsUnder (possible contest) .wins .shares :=
  match overdraw_consuming winning Nat.zero_lt_one (Nat.zero_le 1) (T0 := 0)
      (fun _ _ => Nat.lt_succ_self 1) with
  | ⟨_, T, lost⟩ =>
    have shares : ∀ e, possible contest .shares e := fun e =>
      possible_of_active (U := contest) (w := .shares) (unfolding_dependent sharing)
        (sharing_credited e).1
    ⟨fun e _ => shares e, (.sustaining, T), trivial, shares (.sustaining, T),
     fun admitted => lost T (Nat.le_refl T) (admitted () trivial)⟩

/-- In the two-part family, a course in which every need stays met extends, under the
possibility reading, any course in which overdraw ends the sustaining formation's support. -/
theorem possible_restraint {stopping overdrawing : Law}
    (met : ∀ t, stopping.needG ≤ stopping.level t ∧ stopping.needF ≤ stopping.level t)
    (positive : 0 < overdrawing.needG) (fWithin : overdrawing.needF ≤ overdrawing.needG)
    {T0 : Nat}
    (over : ∀ t, T0 ≤ t → overdrawing.renew + overdrawing.contrib t < overdrawing.draw t) :
    ExtendsUnder (possible (restraint stopping overdrawing)) .overdraws .stops :=
  match overdraw_consuming overdrawing positive fWithin over with
  | ⟨_, T, lost⟩ =>
    have stops : ∀ e, possible (restraint stopping overdrawing) .stops e
      | (.focal, t), _, _ => (met t).2
      | (.sustaining, t), _, _ => (met t).1
    ⟨fun e _ => stops e, (.sustaining, T), trivial, stops (.sustaining, T),
     fun admitted => lost T (Nat.le_refl T) (admitted () trivial)⟩

namespace ThirdParty

/-- With a third formation sharing the condition, restraint still extends overdraw under the
possibility reading: every formation the overdrawing course admits, the restrained course admits,
and the sustaining formation is admitted only there from step 6. -/
theorem possible_extends : ExtendsUnder (possible courses) .overdraws .stops :=
  ⟨fun e admitted => match e, admitted with
    | (.focal, _), _ => fun _ no => False.elim no
    | (.sustaining, t), _ => fun _ _ => stops_supports t
    | (.third, t), admitted =>
      absurd (admitted () trivial) (Nat.not_le_of_gt (over_below_seven t)),
   (.sustaining, 6), trivial, fun _ _ => stops_supports 6,
   fun admitted => Nat.not_succ_le_zero 0 (admitted () trivial)⟩

end ThirdParty

/-- A formation drawing within renewal adds no possibility: its course and the course without it
admit every formation at every step, and neither extends the other. -/
theorem possible_tie (L : Law) (within : ∀ t, L.draw t ≤ L.renew + L.contrib t)
    (gStart : L.needG ≤ L.start) (fStart : L.needF ≤ L.start) :
    (∀ w e, possible (course L) w e) ∧ ¬ ExtendsUnder (possible (course L)) .occurs .absent ∧
      ¬ ExtendsUnder (possible (course L)) .absent .occurs :=
  have kept := within_renewal_sustains L within gStart fStart
  have all : ∀ w e, possible (course L) w e
    | .occurs, (.focal, t), _, _ => Nat.le_trans fStart (kept t)
    | .occurs, (.sustaining, t), _, _ => Nat.le_trans gStart (kept t)
    | .absent, (.focal, t), _, _ => Nat.le_trans fStart (undisturbed_sustains L gStart t)
    | .absent, (.sustaining, t), _, _ => Nat.le_trans gStart (undisturbed_sustains L gStart t)
  ⟨all, fun ⟨_, _, _, _, fresh⟩ => fresh (all _ _), fun ⟨_, _, _, _, fresh⟩ => fresh (all _ _)⟩

/-- Both readings of `living` rank the course of a formation drawing within renewal above the
course without it: they credit its events, which the course without it lacks. -/
theorem readings_rank_presence (L : Law) (within : ∀ t, L.draw t ≤ L.renew + L.contrib t)
    (gStart : L.needG ≤ L.start) (fStart : L.needF ≤ L.start) :
    ExtendsUnder (wholeRun (course L)) .absent .occurs ∧
      ExtendsUnder (stepwise (course L)) .absent .occurs :=
  have kept := within_renewal_sustains L within gStart fStart
  have credited := stops_credited (stopping := L) (overdrawing := L)
    (fun t => ⟨Nat.le_trans gStart (kept t), Nat.le_trans fStart (kept t)⟩)
  ⟨⟨fun e _ => (credited e).1, (.focal, 0), trivial, (credited (.focal, 0)).1,
     fun ⟨active, _⟩ => active⟩,
   ⟨fun e _ => (credited e).2, (.focal, 0), trivial, (credited (.focal, 0)).2,
     fun ⟨active, _⟩ => active⟩⟩

/-- In sharing, whose formation draws only the renewal, the possibility reading leaves the course
with the formation and the course without it unranked, while both readings of `living` rank the
course with it higher. -/
theorem sharing_presence :
    ¬ ExtendsUnder (possible (course sharing)) .absent .occurs ∧
      ¬ ExtendsUnder (possible (course sharing)) .occurs .absent ∧
      ExtendsUnder (wholeRun (course sharing)) .absent .occurs ∧
      ExtendsUnder (stepwise (course sharing)) .absent .occurs :=
  have within : ∀ t, sharing.draw t ≤ sharing.renew + sharing.contrib t := fun _ => Nat.le_refl 1
  have tie := possible_tie sharing within (Nat.le_succ_of_le (Nat.le_succ 1)) (Nat.zero_le 3)
  have ranks :=
    readings_rank_presence sharing within (Nat.le_succ_of_le (Nat.le_succ 1)) (Nat.zero_le 3)
  ⟨tie.2.2, tie.2.1, ranks.1, ranks.2⟩

/-! ### Possibilities first, then a reading -/

/-- Possibilities first, then a reading's credited events: the second course is better when it
extends the first under the possibility reading, or admits the same formations and extends it
under the reading. -/
def possibleFirst (U : W → Unfolding F C) (reading : W → F × Nat → Prop) (w w' : W) : Prop :=
  ExtendsUnder (possible U) w w' ∨
    ((∀ e, possible U w e ↔ possible U w' e) ∧ ExtendsUnder reading w w')

/-- It satisfies C under the possibility reading, and it is irreflexive and transitive. -/
theorem possibleFirst_order (U : W → Unfolding F C) (reading : W → F × Nat → Prop) :
    ComparisonUnder (possible U) (possibleFirst U reading) ∧
      (∀ w, ¬ possibleFirst U reading w w) ∧
      ∀ w w' w'', possibleFirst U reading w w' → possibleFirst U reading w' w'' →
        possibleFirst U reading w w'' :=
  ⟨fun _ _ ext => .inl ext,
   fun _ better => match better with
    | .inl ⟨_, _, _, credited, fresh⟩ => fresh credited
    | .inr ⟨_, _, _, _, credited, fresh⟩ => fresh credited,
   fun _ _ _ first second => match first, second with
    | .inl ⟨keeps, _, _, _, _⟩, .inl ⟨keeps', e, _, credited, fresh⟩ =>
      .inl ⟨fun e held => keeps' e (keeps e held), e, trivial, credited,
        fun held => fresh (keeps e held)⟩
    | .inl ⟨keeps, e, _, credited, fresh⟩, .inr ⟨same, _⟩ =>
      .inl ⟨fun e held => (same e).1 (keeps e held), e, trivial, (same e).1 credited, fresh⟩
    | .inr ⟨same, _⟩, .inl ⟨keeps, e, _, credited, fresh⟩ =>
      .inl ⟨fun e held => keeps e ((same e).1 held), e, trivial, credited,
        fun held => fresh ((same e).1 held)⟩
    | .inr ⟨same, keeps, _, _, _, _⟩, .inr ⟨same', keeps', e, _, credited, fresh⟩ =>
      .inr ⟨fun e => (same e).trans (same' e),
        fun e held => keeps' e (keeps e held), e, trivial, credited,
        fun held => fresh (keeps e held)⟩⟩

/-- In every law of the family, possibilities first ranks the absence of an overdrawing formation
above its occurrence, whatever the reading. -/
theorem possibleFirst_overdraw (L : Law) (reading : Course → Part × Nat → Prop)
    (positive : 0 < L.needG) (fWithin : L.needF ≤ L.needG) (gStart : L.needG ≤ L.start)
    {T0 : Nat} (over : ∀ t, T0 ≤ t → L.renew + L.contrib t < L.draw t) :
    possibleFirst (course L) reading .occurs .absent :=
  .inl (possible_extends L positive fWithin gStart over)

/-- With either reading of `living` second, it ranks the presence of a formation drawing within
renewal above its absence. -/
theorem possibleFirst_presence (L : Law) (within : ∀ t, L.draw t ≤ L.renew + L.contrib t)
    (gStart : L.needG ≤ L.start) (fStart : L.needF ≤ L.start) :
    possibleFirst (course L) (wholeRun (course L)) .absent .occurs ∧
      possibleFirst (course L) (stepwise (course L)) .absent .occurs :=
  have all := (possible_tie L within gStart fStart).1
  have same : ∀ e, possible (course L) .absent e ↔ possible (course L) .occurs e :=
    fun e => ⟨fun _ => all .occurs e, fun _ => all .absent e⟩
  have ranks := readings_rank_presence L within gStart fStart
  ⟨.inr ⟨same, ranks.1⟩, .inr ⟨same, ranks.2⟩⟩

/-! ### A rest

One formation needing one unit of a condition held at one. In the course `true` it rests at
step 0, though supported; in the course `false` it is active at every step. -/

namespace Rest

def courses (rests : Bool) : Unfolding Unit Unit where
  level _ _ := 1
  active t _ := rests = true → t ≠ 0
  requires _ _ := True
  need _ _ := 1
  draws _ _ := False

/-- The two courses admit the same formations, so neither extends the other under the
possibility reading; with either reading of `living` second, possibilities first ranks the
rest below uninterrupted activity. -/
theorem rest_ranked_below :
    (∀ w e, possible courses w e) ∧ ¬ ExtendsUnder (possible courses) true false ∧
      ¬ ExtendsUnder (possible courses) false true ∧
      possibleFirst courses (wholeRun courses) true false ∧
      possibleFirst courses (stepwise courses) true false :=
  have all : ∀ w e, possible courses w e := fun _ _ _ _ => Nat.le_refl 1
  have same : ∀ e, possible courses true e ↔ possible courses false e :=
    fun e => ⟨fun _ => all false e, fun _ => all true e⟩
  have notConsuming : ∀ w f, ¬ ConsumingIn (courses w) f := fun _ _ ⟨_, drawn, _⟩ => drawn
  have notUndermining : ∀ w t f, ¬ (Web.static (courses w)).UnderminingAt t f :=
    fun _ _ _ ⟨_, drawn, _⟩ => drawn
  have active : ∀ e : Unit × Nat, (courses false).active e.2 e.1 := fun _ no => Bool.noConfusion no
  have resting : ¬ (courses true).active 0 () := fun rests => rests rfl rfl
  ⟨all, fun ⟨_, _, _, _, fresh⟩ => fresh (all _ _), fun ⟨_, _, _, _, fresh⟩ => fresh (all _ _),
   .inr ⟨same, fun e _ => ⟨active e, notConsuming false e.1⟩, ((), 0), trivial,
     ⟨active ((), 0), notConsuming false ()⟩, fun ⟨rests, _⟩ => resting rests⟩,
   .inr ⟨same, fun e _ => ⟨active e, notUndermining false e.2 e.1⟩, ((), 0), trivial,
     ⟨active ((), 0), notUndermining false 0 ()⟩, fun ⟨rests, _⟩ => resting rests⟩⟩

end Rest

end Ranking

end Becoming
