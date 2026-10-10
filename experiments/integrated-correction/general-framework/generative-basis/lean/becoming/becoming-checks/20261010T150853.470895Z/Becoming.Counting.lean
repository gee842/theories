import Becoming.Openness

/-!
# Counting: what the premises add to the laws of counting

`Becoming.Population` shows that the tally is the whole law of counting: a property of the
counts, how many hold at each step and how many cease and come to hold across it, holds
wherever what holds is listed exactly when it holds of every tally (`counting_laws`). This
module states what the premises of `Becoming.Premises` add to that law for the counts of a
census, how many relata are active at each step and how many cease and arise across it:
under all eight, under each of their 256 selections, with every step from some step on
enclosed, in finite worlds, and where every premise binds. Each law of counting is an
equivalence: a property of the counts holds of every census of every world meeting the
premises exactly when it holds of every tally meeting the added conditions, queues and
rings counting each such tally being the witnesses.

* **Counting under the premises.** Relata queuing with nothing flowing meet every premise
  but embodiment, and relata queuing that stand exactly while active meet every premise but
  balance (`World.queue_premised`, `World.embodiedQueue_premised`). So a property of the
  counts of a census holds in every world meeting either seven exactly when it holds of
  every tally (`World.counting_free`): premises lacking balance or embodiment leave counting
  free. Together, with only active relata giving, they bind it: what arises is given by a
  relatum active at the step, so under a census nothing arises across a step at which
  nothing is active, which is no law of tallies (`World.counting_binds_jointly`). That is
  all the eight premises add. An open queue, whose front gives to each relatum joining,
  takes from each leaving and, while active, exchanges a unit each way with every ground
  relatum, meets all eight wherever nothing joins an empty queue
  (`World.openQueue_premised`). So a property of the counts holds in every world meeting the
  eight exactly when it holds of every tally in which nothing arises across a step at which
  nothing is active (`World.premised_counting`). Three of the eight hold vacuously in the
  open queue: nothing taking part takes from a closed family, and nothing depends on
  anything (`World.openQueue_not_binds`). No step at which the front is active is enclosed;
  with enclosure from some step on change is bounded as well.
* **Counting under each selection.** Under each of the 256 selections of the premises
  (`World.Meets`) the laws of counting are of two kinds: the tally alone, or the tally with
  nothing arising across a step at which nothing is active, the second exactly where the
  selection binds counting (`World.counting_under`, `World.counting_binds_iff`): balance and
  embodiment, with only active relata giving, or with only active relata taking and
  dissipation. The second route needs no premise on giving: at a step at which nothing is
  active nothing is taken, whatever is given comes to stand and so is active after the step,
  the relata active after it form a closed family, and dissipation lets nothing be given to
  it (`World.taking_binds_counting`). At an enclosed step balance, dissipation and
  embodiment suffice (`World.enclosed_binds_counting`). Every other selection leaves every
  tally counted: a queue driven by an inactive ground relatum, exchanging a unit each way
  with every ground relatum, meets every premise but only active relata giving and taking
  (`World.drivenQueue_holds`), and the open queue, whatever its counts, every premise but
  only active relata giving and dissipation (`World.openQueue_holds`).
* **Enclosure bounds change.** In a world with a census whose relata are embodied, with a
  balanced, dissipative flow and every step from `T` on enclosed, the relata active at any
  later step, with the steps since `T` at which something arose or ceased, number at most
  the total standing at `T`: that total bounds change (`World.enclosure_bounds_change`,
  `ChangeBound`). A bound from some step is one from the first step
  (`changeBound_iff_zero`). An enclosed queue, whose front exchanges only within the queue
  and whose standing falls by one at each step at which a member joins or leaves, has every
  step enclosed (`World.enclosedQueue_enclosed`), and meets all eight premises wherever a
  bound from the first step holds of its counts and nothing joins an empty queue
  (`World.enclosedQueue_premised`); activity needing support and bounded transmission hold
  there vacuously, nothing depending on anything. So under the eight, with every step from
  some step on enclosed, the laws of counting are the tally, that nothing arises across a
  step at which nothing is active, and a change bound from the first step
  (`World.enclosed_counting`). On the finitely many places its members ever take, the queue
  is a finite world meeting the eight (`World.finiteQueue_premised`), in which dissipation
  binds and the bound of `World.enclosure_bounds_change` is attained
  (`World.finite_dissipation_binds`, `World.replaced_attains`); so finite worlds have the
  same laws of counting (`World.finite_counting`, `World.enclosed_iff_finite_counting`).
  Change then does not recur (`ChangeBound.not_recurring`), but a step after which nothing
  arises in every finite world meeting the eight would give `LPO`
  (`World.lpo_of_finite_ends`).
* **Counting under each selection, with enclosure.** In worlds enclosed from some step on,
  the laws of counting under each selection of the premises add one condition to those of
  `World.counting_under`, exactly where balance, embodiment and dissipation are selected:
  from some step on change stays within a bound and nothing arises across a step at which
  nothing is active (`World.enclosed_counting_under`). A change bound from some step is a
  law there exactly where the three are selected (`World.enclosed_change_bound_iff`), so
  enclosure adds no law exactly where they are not all selected. Where neither only active
  relata giving nor only active relata taking is selected, the witness is an enclosed queue
  closing at that step, every relatum exchanging a unit each way with the front before it
  (`World.closingQueue_dissipative`). The enclosed queue takes only while active whatever
  its counts (`World.enclosedQueue_taking`) and dissipates step by step
  (`World.enclosedQueue_dissipatesOn`).
* **Counting under each selection, in finite worlds.** Every step of a finite world is
  enclosed (`World.Finite.enclosed`), so there dissipation with balance and embodiment
  binds counting by itself. Under each selection the laws of counting in finite worlds are
  those of a tally with at most some number active at each step, and two more where
  selected (`World.finite_counting_under`): nothing arising across a step at which nothing
  is active, exactly where balance and embodiment are selected with only active relata
  giving or with dissipation (`World.finite_counting_binds_iff`), and a change bound from
  the first step, exactly where balance, embodiment and dissipation are selected
  (`World.finite_change_bound_iff`). So the 256 selections give three kinds of law. Finite
  worlds and worlds enclosed from some step on have the same laws under a selection exactly
  when it bounds change and binds counting (`World.enclosed_iff_finite_counting_under`).
  The witnesses seat a queue round a ring of places, each member at the next place in turn
  (`Ring.slot`), so that those in the queue before or after any step hold distinct places
  and the ring counts what the queue counts (`Ring.slot_inj`, `Ring.counts`). With nothing
  standing, a ring meets every premise but embodiment (`World.ring_meets`); with each place
  standing while held, every premise but balance (`World.embodiedRing_meets`); with the
  front's place also taking what each place's standing loses and giving what it gains, every
  premise but dissipation, only active relata giving where nothing joins an empty queue
  (`World.balancedRing_meets`).
* **Counting where every premise binds.** A premise binds where its condition has an
  instance (`World.Binds`). Where every premise binds, every census counts something arising
  (`World.binds_arising`), which is no law under the eight alone (`World.binds_adds`), and
  that is all binding adds. A queue closed once is open across every step but one, `T`, at
  which its front stands `E` more: across `T` it exchanges only within the queue and loses
  that excess, so dissipation binds there. Every relatum depends on every relatum, needing
  what it stands at, so the conditions of activity needing support and bounded transmission
  have instances wherever something joins; but these two premises hold there whatever is
  active and whatever flows (`OnceClosedQueue.dependent_any_activity`,
  `OnceClosedQueue.transmits_any_flow`): they bind only as instances, and only dissipation
  excludes anything. With nothing joining an empty queue, something joining across `T` and
  `E` more than join there, it meets the eight and every premise binds
  (`World.onceClosedQueue_premised`, `World.onceClosedQueue_binds`). So where every premise
  binds, the laws of counting under the eight are the tally, that nothing arises across a
  step at which nothing is active, and that something arises (`World.binding_counting`). A
  census binds only where the world is not finite, so no finite world binds every premise
  (`World.Finite.not_binds`), though in a finite world every other premise can bind
  (`World.finiteHatch_binds_but_census`). Every premise binding decides neither rest nor
  change without end: `hatch` comes to rest, and in a queue closed once in which one member
  replaces another at every step arising and ceasing recur (`World.binding_contingent`).

The counts are of activity; what the premises add to the counts of standing and of
dependence is not stated, nor are the laws where the premises of each selection bind, or
those of finite worlds in which every premise but the census binds. Binding here is an
instance of each condition; a sense of binding in which each premise excludes something the
representation allows would be a further reading. A property of the counts respects their
values at each step (`Pointwise`), as function extensionality would give and the pure core
does not assume. Activity is supposed decidable where a theorem needs it, a logical
commitment of the representation. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {α : Type}

/-! ## Lists -/

/-- What a mapped list holds is the value of some member. -/
theorem exists_of_mem_map {β : Type} {g : α → β} {b : β} :
    ∀ {l : List α}, b ∈ l.map g → ∃ a, a ∈ l ∧ g a = b
  | [], mem => nomatch mem
  | a :: _, mem => match mem_cons_cases mem with
    | .inl same => ⟨a, .head _, same.symm⟩
    | .inr mem => match exists_of_mem_map mem with
      | ⟨x, listed, same⟩ => ⟨x, .tail a listed, same⟩

/-- Mapping a list one to one on its members keeps it without repetition. -/
theorem distinct_map_on {β : Type} {g : α → β} :
    ∀ {l : List α}, (∀ a b, a ∈ l → b ∈ l → g a = g b → a = b) → Distinct l →
      Distinct (l.map g)
  | [], _, _ => trivial
  | a :: l, inj, ⟨fresh, distinct⟩ =>
    ⟨fun mem => match exists_of_mem_map mem with
      | ⟨b, listed, same⟩ => fresh (Eq.subst (motive := (· ∈ l))
          (inj b a (.tail a listed) (.head l) same) listed),
     distinct_map_on (fun x y first second => inj x y (.tail a first) (.tail a second))
       distinct⟩

namespace World

variable {w : World}

/-! ## Counting under the premises -/

/-- `Q` holds of the counts of every census of the world: how many are active at each step,
how many cease and how many arise across it. -/
def CountsObey (w : World) [∀ t x, Decidable (w.web.active t x)]
    (Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop) : Prop :=
  ∀ alive, w.web.Census alive → Q (fun t => (alive t).length)
    (fun t => ceasings (alive t) (fun x s => w.web.active s x) t)
    (fun t => comings (alive (t + 1)) (fun x s => w.web.active s x) t)

end World

namespace Queue

/-- Relata in a queue, each active from the step it joins to the step it leaves; nothing
stands, depends or draws. -/
def web (n c : Nat → Nat) : Web Nat Nat where
  level _ _ := 0
  active t k := holds n c k t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- The same queue, each relatum standing exactly while it is active. -/
def embodied (n c : Nat → Nat) : Web Nat Nat :=
  { web n c with level := fun t k => mark (holds n c k t) }

/-- None at the first step, one from then on. -/
def lone : Nat → Nat
  | 0 => 0
  | _ + 1 => 1

/-- One joins across the first step and none after. -/
def joins : Nat → Nat
  | 0 => 1
  | _ + 1 => 0

/-- One relatum comes to be across the first step, from none, and stays. -/
theorem lone_tally : Tally lone (fun _ => 0) joins
  | 0 => ⟨0, rfl, rfl⟩
  | _ + 1 => ⟨1, rfl, rfl⟩

end Queue

namespace World

/-- Relata queue, with nothing flowing. -/
def queue (n c : Nat → Nat) : World :=
  ⟨Nat, Flow.still, Queue.web n c⟩

/-- Relata queue, each standing exactly while it is active, with nothing flowing. -/
def embodiedQueue (n c : Nat → Nat) : World :=
  ⟨Nat, Flow.still, Queue.embodied n c⟩

instance queue_decided (n c : Nat → Nat) : ∀ t x, Decidable ((queue n c).web.active t x) :=
  fun t x => inferInstanceAs (Decidable (Queue.holds n c x t))

instance embodiedQueue_decided (n c : Nat → Nat) :
    ∀ t x, Decidable ((embodiedQueue n c).web.active t x) :=
  fun t x => inferInstanceAs (Decidable (Queue.holds n c x t))

/-- A queue meets every premise but embodiment: nothing depends, stands or flows. -/
theorem queue_premised (n c : Nat → Nat) :
    (queue n c).Dependent ∧ (queue n c).Balanced ∧ (queue n c).Acting ∧
      (queue n c).Taking ∧ (queue n c).Dissipative ∧ (queue n c).Counted ∧
      (queue n c).Transmitting :=
  ⟨fun _ _ _ _ no => (nomatch no), fun _ _ => rfl, (still_vacuous _).1, (still_vacuous _).2.1,
   (still_vacuous _).2.2.1, ⟨_, Queue.listed⟩, (still_vacuous _).2.2.2⟩

/-- A queue standing while active meets every premise but balance: its standing changes
with nothing flowing. -/
theorem embodiedQueue_premised (n c : Nat → Nat) :
    (embodiedQueue n c).Dependent ∧ (embodiedQueue n c).Acting ∧
      (embodiedQueue n c).Taking ∧ (embodiedQueue n c).Dissipative ∧
      (embodiedQueue n c).Embodied ∧ (embodiedQueue n c).Counted ∧
      (embodiedQueue n c).Transmitting :=
  ⟨fun _ _ _ _ no => (nomatch no), (still_vacuous _).1, (still_vacuous _).2.1,
   (still_vacuous _).2.2.1, fun _ _ => mark_pos.symm, ⟨_, Queue.listed⟩,
   (still_vacuous _).2.2.2⟩

/-- The premises leave counting free. A property of the counts holds of every tally exactly
when it holds of the census of every world; and already when it holds of the census of
every world meeting every premise but embodiment, or of every world meeting every premise
but balance. -/
theorem counting_free {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop}
    (pointwise : Pointwise Q) :
    ((∀ n c a, Tally n c a → Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.CountsObey Q) ∧
    ((∀ n c a, Tally n c a → Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Dependent → w.Balanced →
        w.Acting → w.Taking → w.Dissipative → w.Transmitting → w.CountsObey Q) ∧
    ((∀ n c a, Tally n c a → Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Dependent → w.Acting →
        w.Taking → w.Dissipative → w.Embodied → w.Transmitting → w.CountsObey Q) :=
  have every : (∀ n c a, Tally n c a → Q n c a) →
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.CountsObey Q :=
    fun law _ _ _ census => law _ _ _ census.tally
  ⟨⟨every, fun law n c _ tally => pointwise (fun t => Queue.counts tally t)
      (law (queue n c) _ Queue.listed)⟩,
   ⟨fun law w _ _ _ _ _ _ _ => every law w, fun law n c _ tally =>
      match queue_premised n c with
      | ⟨dependent, balanced, acting, taking, dissipative, _, transmitting⟩ =>
        pointwise (fun t => Queue.counts tally t) (law (queue n c) dependent balanced acting
          taking dissipative transmitting _ Queue.listed)⟩,
   ⟨fun law w _ _ _ _ _ _ _ => every law w, fun law n c _ tally =>
      match embodiedQueue_premised n c with
      | ⟨dependent, acting, taking, dissipative, embodied, _, transmitting⟩ =>
        pointwise (fun t => Queue.counts tally t) (law (embodiedQueue n c) dependent acting
          taking dissipative embodied transmitting _ Queue.listed)⟩⟩

/-- Together, balance and embodiment bind the counts. Where the flow balances, only active
relata give and whatever arises is embodied, what arises is given by a relatum active at
the step (`Web.Embodied.arises_given`), so under a census nothing arises across a step at
which nothing is active. This is no law of tallies: one relatum arising from none is
counted by a queue meeting every premise but embodiment, and by one meeting every premise
but balance. -/
theorem counting_binds_jointly :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Balanced → w.Acting →
      w.ArisingEmbodied → w.CountsObey fun n _ a => ∀ t, 0 < a t → 0 < n t) ∧
    ¬ (queue Queue.lone fun _ => 0).CountsObey (fun n _ a => ∀ t, 0 < a t → 0 < n t) ∧
    ¬ (embodiedQueue Queue.lone fun _ => 0).CountsObey
      (fun n _ a => ∀ t, 0 < a t → 0 < n t) :=
  ⟨fun _ _ balanced acting embodied alive census t arising =>
    match total_pos _ arising with
    | ⟨x, _, comes⟩ => match Web.Embodied.arises_given balanced acting
        (embodied t x (mark_pos.mp comes)) (mark_pos.mp comes) with
      | ⟨f, active, _⟩ => Nat.lt_of_lt_of_le (total_pos_of_mem (((census t).2 f).mp active)
          Nat.zero_lt_one) (Nat.le_of_eq (total_ones (alive t))),
   fun obeys => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (obeys _ Queue.listed 0
      (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq
        (Queue.comings_eq Queue.lone_tally 0).symm)))
      (Nat.le_of_eq (Queue.counts Queue.lone_tally 0).1)),
   fun obeys => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (obeys _ Queue.listed 0
      (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq
        (Queue.comings_eq Queue.lone_tally 0).symm)))
      (Nat.le_of_eq (Queue.counts Queue.lone_tally 0).1))⟩


end World

/-! ## Counting under all the premises -/

namespace OpenQueue

/-- The members of a queue, and ground relata. -/
inductive Relatum
  | member (k : Nat)
  | ground (k : Nat)

variable (n c : Nat → Nat)

/-- Members stand and are active exactly while in the queue; ground relata stand at nothing
and are never active. -/
def web : Web Relatum Relatum where
  level t x := match x with
    | .member k => mark (Queue.holds n c k t)
    | .ground _ => 0
  active t x := match x with
    | .member k => Queue.holds n c k t
    | .ground _ => False
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

/-- The front of the queue takes part at every step. It gives one unit to each member
joining and takes one from each member leaving; while active it also gives one unit to every
ground relatum and takes one from each. -/
def flow : Flow Relatum Relatum where
  present t := [.member (Queue.gone c t)]
  take t _ x := match x with
    | .member k => mark (CeasesToBe (Queue.holds n c k) t)
    | .ground _ => mark (Queue.holds n c (Queue.gone c t) t)
  give t _ x := match x with
    | .member k => mark (ComesToBe (Queue.holds n c k) t)
    | .ground _ => mark (Queue.holds n c (Queue.gone c t) t)

def index : Relatum → Nat
  | .member k => k
  | .ground k => k

/-- No finite family holds every ground relatum. -/
theorem outside (cs : List Relatum) : ¬ Relatum.ground (beyond (cs.map index)) ∈ cs :=
  fun mem => beyond_not_mem _ (mem_map_of (g := index) mem)

theorem member_inj : ∀ a b : Nat, Relatum.member a = Relatum.member b → a = b :=
  fun _ _ same => Relatum.noConfusion same id

theorem ground_not_member {g : Nat} : ∀ {l : List Nat}, ¬ Relatum.ground g ∈ l.map .member
  | [], no => nomatch no
  | _ :: _, .tail _ mem => ground_not_member mem

variable {n c}

/-- The front of the queue is in it exactly while the queue is not empty. -/
theorem front {t : Nat} : Queue.holds n c (Queue.gone c t) t ↔ 0 < n t :=
  ⟨fun holds => Nat.lt_of_add_lt_add_left (n := Queue.gone c t) (k := 0) holds.2,
   fun pos => ⟨Nat.le_refl _, Nat.lt_add_of_pos_right pos⟩⟩

/-- A member in the queue means the queue is not empty. -/
theorem occupied {k t : Nat} (holds : Queue.holds n c k t) : 0 < n t :=
  Nat.lt_of_add_lt_add_left (n := Queue.gone c t) (k := 0) (Nat.lt_of_le_of_lt holds.1 holds.2)

/-- Where something joins only across a step at which the queue is not empty, a member
joining means the queue was not empty. -/
theorem joined {a : Nat → Nat} (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    {k t : Nat} (comes : ComesToBe (Queue.holds n c k) t) : 0 < n t :=
  company t (Nat.lt_of_lt_of_le (total_pos_of_mem (q := fun j => mark (ComesToBe
    (Queue.holds n c j) t)) (steps_of_within comes.2.1 comes.2.2) (mark_pos.mpr comes))
    (Nat.le_of_eq (Queue.comings_eq tally t)))

end OpenQueue

namespace World

/-- An open queue: its front gives to each relatum joining, takes from each
leaving, and while active exchanges one unit each way with every ground relatum. -/
def openQueue (n c : Nat → Nat) : World :=
  ⟨OpenQueue.Relatum, OpenQueue.flow n c, OpenQueue.web n c⟩

instance openQueue_decided (n c : Nat → Nat) :
    ∀ t x, Decidable ((openQueue n c).web.active t x)
  | t, .member k => inferInstanceAs (Decidable (Queue.holds n c k t))
  | _, .ground _ => isFalse id

/-- The census of an open queue is its members, listed as the queue lists them. -/
theorem openQueue_census (n c : Nat → Nat) :
    (openQueue n c).web.Census fun t => (Queue.line n c t).map .member :=
  fun _ => ⟨distinct_map OpenQueue.member_inj (steps_distinct _ _), fun x => match x with
    | .member _ => ⟨fun holds => mem_map_of (steps_of_within holds.1 holds.2),
        fun mem => match mem_of_map OpenQueue.member_inj mem with
          | listed => ⟨steps_mem listed, steps_within listed⟩⟩
    | .ground _ => ⟨False.elim, fun mem => OpenQueue.ground_not_member mem⟩⟩

/-- Its census counts what the queue counts. -/
theorem openQueue_counts {n c a : Nat → Nat} (tally : Tally n c a) (t : Nat) :
    ((Queue.line n c t).map OpenQueue.Relatum.member).length = n t ∧
      ceasings ((Queue.line n c t).map .member)
        (fun x s => (openQueue n c).web.active s x) t = c t ∧
      comings ((Queue.line n c (t + 1)).map .member)
        (fun x s => (openQueue n c).web.active s x) t = a t :=
  ⟨(total_ones _).symm.trans ((total_map _ _ _).trans ((total_ones _).trans (steps_length _ _))),
   (total_map OpenQueue.Relatum.member _ (Queue.line n c t)).trans (Queue.ceasings_eq tally t),
   (total_map OpenQueue.Relatum.member _ (Queue.line n c (t + 1))).trans
     (Queue.comings_eq tally t)⟩

/-- Whatever its counts, an open queue balances, only active relata take there and only from
what they draw on, every relatum is embodied, it has a census, and nothing depends on
anything. Only active relata giving and dissipation can fail: where something joins an
empty queue, its front gives while inactive. -/
theorem openQueue_holds (n c : Nat → Nat) :
    (openQueue n c).Dependent ∧ (openQueue n c).Balanced ∧ (openQueue n c).Taking ∧
      (openQueue n c).Embodied ∧ (openQueue n c).Counted ∧ (openQueue n c).Transmitting :=
  ⟨fun _ _ _ _ no => (nomatch no),
   fun t x => match x with
    | .member k => mark_turn (Queue.holds n c k t) (Queue.holds n c k (t + 1))
    | .ground _ => rfl,
   fun _ f x present takes => match f, present, x, takes with
    | _, .head _, .member _, takes => ⟨OpenQueue.front.mpr (OpenQueue.occupied
        (mark_pos.mp takes).1), trivial⟩
    | _, .head _, .ground _, takes => ⟨mark_pos.mp takes, trivial⟩
    | _, .tail _ no, _, _ => (nomatch no),
   fun x => match x with
    | .member _ => fun _ => mark_pos.symm
    | .ground _ => fun _ => ⟨False.elim, fun no => absurd no (Nat.lt_irrefl 0)⟩,
   ⟨_, openQueue_census n c⟩,
   ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩⟩

/-- Where something arises only across a step at which something is active, an open queue
meets all eight premises. Not all of them bind: no step at which the front is active is
enclosed, and nothing depends on anything (`openQueue_not_binds`). -/
theorem openQueue_premised {n c a : Nat → Nat} (tally : Tally n c a)
    (company : ∀ t, 0 < a t → 0 < n t) : (openQueue n c).Premised :=
  match openQueue_holds n c with
  | ⟨dependent, balanced, taking, embodied, counted, transmitting⟩ =>
    .of dependent balanced
      (fun _ f x present gives => match f, present, x, gives with
        | _, .head _, .member _, gives => OpenQueue.front.mpr (OpenQueue.joined tally company
            (mark_pos.mp gives))
        | _, .head _, .ground _, gives => mark_pos.mp gives
        | _, .tail _ no, _, _ => (nomatch no))
      taking
      (fun cs t _ closed _ _ => match Nat.eq_zero_or_pos (n t) with
        | .inr pos => absurd ((mark_one (OpenQueue.front.mpr pos)).symm.trans
            (closed _ (.head _) _ (OpenQueue.outside cs)).2) (fun no => Nat.noConfusion no)
        | .inl empty => gives_nothing ((total_congr_on (g := fun _ => 0) fun x _ => match x with
            | .member _ => mark_zero fun comes => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le
                (OpenQueue.joined tally company comes) (Nat.le_of_eq empty))
            | .ground _ => mark_zero fun holds => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le
                (OpenQueue.front.mp holds) (Nat.le_of_eq empty))).trans (total_zero cs)))
      embodied counted transmitting

/-- Under all eight premises the laws of counting are the tally and that nothing arises
across a step at which nothing is active: a property of the counts holds of every census of
every world meeting the eight exactly when it holds of every tally in which something arises
only across a step at which something is active. -/
theorem premised_counting {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop}
    (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.CountsObey Q :=
  ⟨fun law w _ premised alive census =>
    law _ _ _ census.tally (counting_binds_jointly.1 w (premised _ (.tail _ (.head _)))
      (premised _ (.tail _ (.tail _ (.head _))))
      (Embodied.arising (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _
        (.head _))))))))
      alive census),
   fun law n c _ tally company => pointwise (openQueue_counts tally)
      (law (openQueue n c) (openQueue_premised tally company) _
        (openQueue_census n c))⟩

/-- In an open queue dissipation, activity needing support and bounded transmission hold
vacuously. Nothing taking part takes from a closed family: where something is taken the
front is active, and then it gives to a ground relatum beyond every finite family. Nothing
depends on anything. So not every premise binds there (the thirteenth review's probe). -/
theorem openQueue_not_binds {n c : Nat → Nat} :
    (¬ ∃ cs t f, Distinct cs ∧ (openQueue n c).flow.ClosedAt cs t ∧
      f ∈ (openQueue n c).flow.present t ∧ 0 < total cs ((openQueue n c).flow.take t f)) ∧
    (¬ ∃ t f x, (openQueue n c).web.active t f ∧ (openQueue n c).web.requires t f x ∧
      0 < (openQueue n c).web.need t f x) ∧
    (¬ ∃ t x g y, (openQueue n c).flow.DescendsAt (openQueue n c).web t x g ∧
      (openQueue n c).web.requires (t + 1) x y) ∧
    ¬ (openQueue n c).Binds :=
  have idle : ¬ ∃ cs t f, Distinct cs ∧ (openQueue n c).flow.ClosedAt cs t ∧
      f ∈ (openQueue n c).flow.present t ∧ 0 < total cs ((openQueue n c).flow.take t f) :=
    fun ⟨cs, t, f, _, closed, present, takes⟩ => match total_pos cs takes with
      | ⟨x, _, positive⟩ =>
        have occupied : 0 < n t := match x, positive with
          | .member _, positive => OpenQueue.occupied (mark_pos.mp positive).1
          | .ground _, positive => OpenQueue.front.mp (mark_pos.mp positive)
        Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq
          ((mark_one (OpenQueue.front.mpr occupied)).symm.trans
            (closed f present _ (OpenQueue.outside cs)).2)))
  ⟨idle, fun ⟨_, _, _, _, no, _⟩ => no, fun ⟨_, _, _, _, _, no⟩ => no,
   fun binds => idle binds.dissipative⟩

/-- Where every premise binds, every census counts something arising: embodiment binds only
where something arises (the thirteenth review's probe). -/
theorem binds_arising (w : World) [∀ t x, Decidable (w.web.active t x)] (binds : w.Binds) :
    w.CountsObey fun _ _ a => ∃ t, 0 < a t := fun _ census =>
  match binds.embodied with
  | ⟨t, x, arises⟩ =>
    ⟨t, Nat.lt_of_lt_of_le (mark_pos.mpr arises)
      (le_total_of_mem (q := fun y => mark (ComesToBe (fun s => w.web.active s y) t))
        (((census (t + 1)).2 x).mp arises.2))⟩

/-- Under the eight premises something arising is no law of counting, as the empty tally
shows; where every premise binds it is one (`binds_arising`). The laws of
`premised_counting` hold of worlds in which some premises hold vacuously (the thirteenth
review's probe). -/
theorem binds_adds :
    ¬ ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised →
      w.CountsObey fun _ _ a => ∃ t, 0 < a t :=
  fun law => match (premised_counting (Q := fun _ _ a => ∃ t, 0 < a t)
      (fun same ⟨t, pos⟩ => ⟨t, Nat.lt_of_lt_of_le pos (Nat.le_of_eq (same t).2.2)⟩)).mpr
      law (fun _ => 0) (fun _ => 0) (fun _ => 0) (fun _ => ⟨0, rfl, rfl⟩) (fun _ no => no) with
    | ⟨_, no⟩ => Nat.lt_irrefl 0 no

end World

/-! ## Counting under each selection -/

namespace OpenQueue

/-- An inactive ground relatum drives the queue: at every step it gives one unit to each member
joining, takes one from each member leaving, and exchanges one unit each way with every
ground relatum, so no family is closed across any step. -/
def driven (n c : Nat → Nat) : Flow Relatum Relatum where
  present _ := [.ground 0]
  take t _ x := match x with
    | .member k => mark (CeasesToBe (Queue.holds n c k) t)
    | .ground _ => 1
  give t _ x := match x with
    | .member k => mark (ComesToBe (Queue.holds n c k) t)
    | .ground _ => 1

end OpenQueue

namespace World

/-- A queue driven by an inactive relatum: the members of an open queue, the exchange driven
from a ground relatum never active. -/
def drivenQueue (n c : Nat → Nat) : World :=
  ⟨OpenQueue.Relatum, OpenQueue.driven n c, OpenQueue.web n c⟩

instance drivenQueue_decided (n c : Nat → Nat) :
    ∀ t x, Decidable ((drivenQueue n c).web.active t x) :=
  openQueue_decided n c

/-- Whatever its counts, a driven queue balances, dissipates, since no family is closed
across any step, has every relatum embodied and a census, and nothing depends on anything.
Only active relata giving and only active relata taking fail. -/
theorem drivenQueue_holds (n c : Nat → Nat) :
    (drivenQueue n c).Dependent ∧ (drivenQueue n c).Balanced ∧
      (drivenQueue n c).Dissipative ∧ (drivenQueue n c).Embodied ∧
      (drivenQueue n c).Counted ∧ (drivenQueue n c).Transmitting :=
  match openQueue_holds n c with
  | ⟨dependent, _, _, embodied, counted, _⟩ =>
    ⟨dependent,
     fun t x => match x with
      | .member k => mark_turn (Queue.holds n c k t) (Queue.holds n c k (t + 1))
      | .ground _ => rfl,
     fun cs _ _ closed => absurd (closed _ (.head _) _ (OpenQueue.outside cs)).2
       (fun no => Nat.noConfusion no),
     embodied, counted, ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩⟩

/-- Taking and dissipation can stand in for only active relata giving. Where the flow
balances, only active relata take and only from what they draw on, the flow dissipates and
every relatum is embodied, then under a census nothing arises across a step at which nothing
is active, whoever gives. At such a step nothing is taken and nothing stands; whatever is
given comes to stand, so it is active after the step, and the relata active after it form
a closed family, to which dissipation lets nothing be given. -/
theorem taking_binds_counting (w : World) [∀ t x, Decidable (w.web.active t x)]
    (balanced : w.Balanced) (taking : w.Taking) (dissipative : w.Dissipative)
    (embodied : w.Embodied) : w.CountsObey fun n _ a => ∀ t, 0 < a t → 0 < n t :=
  fun alive census t arising => match Nat.eq_zero_or_pos (alive t).length with
    | .inr pos => pos
    | .inl empty =>
      have idle : ∀ f, ¬ w.web.active t f := fun f active =>
        Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le
          (total_pos_of_mem (((census t).2 f).mp active) Nat.zero_lt_one)
          (Nat.le_of_eq (total_ones (alive t)))) (Nat.le_of_eq empty))
      have untaken : ∀ f c, f ∈ w.flow.present t → w.flow.take t f c = 0 :=
        fun f c present => eq_zero_of_not_pos fun takes => idle f (taking t f c present takes).1
      have flows : ∀ c, w.web.level (t + 1) c = w.flow.given t c := fun c =>
        (congrArg (w.web.level (t + 1) c + ·)
            ((total_congr_on (g := fun _ => 0) fun f present => untaken f c present).trans
              (total_zero _)).symm).trans
          ((balanced t c).trans ((congrArg (· + w.flow.given t c)
            (eq_zero_of_not_pos fun stands => idle c ((embodied c t).mpr stands))).trans
            (Nat.zero_add _)))
      have closed : w.flow.ClosedAt (alive (t + 1)) t := fun f present c outside =>
        ⟨untaken f c present, eq_zero_of_not_pos fun gives => outside
          (((census (t + 1)).2 c).mp ((embodied c (t + 1)).mpr (Nat.lt_of_lt_of_le
            (Nat.lt_of_lt_of_le gives (le_total_of_mem (q := fun g => w.flow.give t g c)
              present)) (Nat.le_of_eq (flows c).symm))))⟩
      match total_pos _ arising with
      | ⟨x, listed, comes⟩ =>
        match total_pos _ (Nat.lt_of_lt_of_le ((embodied x (t + 1)).mp (mark_pos.mp comes).2)
            (Nat.le_of_eq (flows x))) with
        | ⟨f, present, gives⟩ =>
          have nothing : total (alive (t + 1)) (w.flow.take t f) = 0 :=
            (total_congr_on (g := fun _ => 0) fun c _ => untaken f c present).trans (total_zero _)
          absurd (Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le gives
              (le_total_of_mem (q := w.flow.give t f) listed))
              (Nat.le_trans (Nat.le_add_right _ _)
                (dissipative _ t (census (t + 1)).1 closed f present)))
            fun pos => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le pos (Nat.le_of_eq nothing))

/-- Enclosure lets dissipation stand in for only active relata giving, too. Where the flow
balances and dissipates and every relatum is embodied, under a census nothing arises across
an enclosed step at which nothing is active, whoever gives and whoever takes: nothing stands
there, so a closed family's stock is nothing, and a member coming to stand would lower it
(`Flow.standing_lowers`). -/
theorem enclosed_binds_counting (w : World) [∀ t x, Decidable (w.web.active t x)]
    (balanced : w.Balanced) (dissipative : w.Dissipative) (embodied : w.Embodied)
    {alive : Nat → List w.Relatum} (census : w.web.Census alive) {t : Nat}
    (enclosed : w.flow.Enclosed t)
    (arising : 0 < comings (alive (t + 1)) (fun x s => w.web.active s x) t) :
    0 < (alive t).length :=
  match Nat.eq_zero_or_pos (alive t).length, enclosed, total_pos _ arising with
  | .inr pos, _, _ => pos
  | .inl empty, ⟨cs, distinct, closed⟩, ⟨x, _, comes⟩ =>
    have idle : ∀ f, ¬ w.web.active t f := fun f active =>
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le
        (total_pos_of_mem (((census t).2 f).mp active) Nat.zero_lt_one)
        (Nat.le_of_eq (total_ones (alive t)))) (Nat.le_of_eq empty))
    have nothing : w.web.stock cs t = 0 :=
      total_eq_zero fun c _ => eq_zero_of_not_pos fun stands => idle c ((embodied c t).mpr stands)
    have comes : w.web.ComesToStand t x :=
      ⟨fun stands => idle x ((embodied x t).mpr stands),
       (embodied x (t + 1)).mp (mark_pos.mp comes).2⟩
    match total_pos _ (Flow.Balances.rise_given balanced comes.rises) with
    | ⟨f, present, gives⟩ =>
      absurd (fun mem => Nat.not_lt_zero _ (Nat.lt_of_lt_of_le
          (Flow.standing_lowers balanced dissipative distinct closed mem comes)
          (Nat.le_of_eq nothing)))
        fun out => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le gives
          (Nat.le_of_eq (closed f present x out).2))

/-- A selection binds counting when it selects balance and embodiment, and either only
active relata giving or both only active relata taking and dissipation. -/
def BindsCounting (S : Premise → Bool) : Prop :=
  S .balanced = true ∧ S .embodied = true ∧
    (S .acting = true ∨ S .taking = true ∧ S .dissipative = true)

/-- A queue meets every selection without embodiment. -/
theorem queue_meets (n c : Nat → Nat) {S : Premise → Bool} (free : S .embodied = false) :
    (queue n c).Meets S :=
  match queue_premised n c with
  | ⟨dependent, balanced, acting, taking, dissipative, counted, transmitting⟩ => fun
    | .dependent, _ => dependent
    | .balanced, _ => balanced
    | .acting, _ => acting
    | .taking, _ => taking
    | .dissipative, _ => dissipative
    | .embodied, selected => nomatch free.symm.trans selected
    | .counted, _ => counted
    | .transmitting, _ => transmitting

/-- A queue standing while active meets every selection without balance. -/
theorem embodiedQueue_meets (n c : Nat → Nat) {S : Premise → Bool}
    (free : S .balanced = false) : (embodiedQueue n c).Meets S :=
  match embodiedQueue_premised n c with
  | ⟨dependent, acting, taking, dissipative, embodied, counted, transmitting⟩ => fun
    | .dependent, _ => dependent
    | .balanced, selected => nomatch free.symm.trans selected
    | .acting, _ => acting
    | .taking, _ => taking
    | .dissipative, _ => dissipative
    | .embodied, _ => embodied
    | .counted, _ => counted
    | .transmitting, _ => transmitting

/-- An open queue meets every selection without only active relata giving and without
dissipation. -/
theorem openQueue_meets (n c : Nat → Nat) {S : Premise → Bool} (giving : S .acting = false)
    (dissipating : S .dissipative = false) : (openQueue n c).Meets S :=
  match openQueue_holds n c with
  | ⟨dependent, balanced, taking, embodied, counted, transmitting⟩ => fun
    | .dependent, _ => dependent
    | .balanced, _ => balanced
    | .acting, selected => nomatch giving.symm.trans selected
    | .taking, _ => taking
    | .dissipative, selected => nomatch dissipating.symm.trans selected
    | .embodied, _ => embodied
    | .counted, _ => counted
    | .transmitting, _ => transmitting

/-- A driven queue meets every selection without only active relata giving and without
only active relata taking. -/
theorem drivenQueue_meets (n c : Nat → Nat) {S : Premise → Bool} (giving : S .acting = false)
    (taking : S .taking = false) : (drivenQueue n c).Meets S :=
  match drivenQueue_holds n c with
  | ⟨dependent, balanced, dissipative, embodied, counted, transmitting⟩ => fun
    | .dependent, _ => dependent
    | .balanced, _ => balanced
    | .acting, selected => nomatch giving.symm.trans selected
    | .taking, selected => nomatch taking.symm.trans selected
    | .dissipative, _ => dissipative
    | .embodied, _ => embodied
    | .counted, _ => counted
    | .transmitting, _ => transmitting

/-- The laws of counting under each selection of the premises. A property of the counts
holds of every census of every world meeting the selection exactly when it holds of every
tally, and, where the selection binds counting, of every tally in which nothing arises across
a step at which nothing is active. So the laws of counting under the 256 selections are of
two kinds: the tally alone, or the tally and nothing arising at a step at which nothing is
active, the second exactly where balance, embodiment, and only active relata giving or
taking with dissipation are selected. -/
theorem counting_under (S : Premise → Bool)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (BindsCounting S → ∀ t, 0 < a t → 0 < n t) → Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.CountsObey Q :=
  ⟨fun law w _ meets alive census => law _ _ _ census.tally fun ⟨balanced, embodied, giving⟩ =>
    match giving with
    | .inl acting => counting_binds_jointly.1 w (meets _ balanced) (meets _ acting)
        (Embodied.arising (meets _ embodied)) alive census
    | .inr ⟨taking, dissipative⟩ => taking_binds_counting w (meets _ balanced)
        (meets _ taking) (meets _ dissipative) (meets _ embodied) alive census,
   fun law n c _ tally quiet =>
    match hb : S .balanced, he : S .embodied with
    | false, _ => pointwise (fun t => Queue.counts tally t)
        (law (embodiedQueue n c) (embodiedQueue_meets n c hb) _ Queue.listed)
    | true, false => pointwise (fun t => Queue.counts tally t)
        (law (queue n c) (queue_meets n c he) _ Queue.listed)
    | true, true => match ha : S .acting, ht : S .taking, hd : S .dissipative with
      | true, _, _ => pointwise (openQueue_counts tally) (law (openQueue n c)
          ((openQueue_premised tally (quiet ⟨hb, he, .inl ha⟩)).meets S) _
          (openQueue_census n c))
      | false, true, true => pointwise (openQueue_counts tally) (law (openQueue n c)
          ((openQueue_premised tally (quiet ⟨hb, he, .inr ⟨ht, hd⟩⟩)).meets S) _
          (openQueue_census n c))
      | false, false, _ => pointwise (openQueue_counts tally) (law (drivenQueue n c)
          (drivenQueue_meets n c ha ht) _ (openQueue_census n c))
      | false, true, false => pointwise (openQueue_counts tally) (law (openQueue n c)
          (openQueue_meets n c ha hd) _ (openQueue_census n c))⟩

/-- Nothing arising across a step at which nothing is active is a law of counting under a
selection exactly when the selection binds counting. -/
theorem counting_binds_iff (S : Premise → Bool) :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S →
      w.CountsObey fun n _ a => ∀ t, 0 < a t → 0 < n t) ↔ BindsCounting S :=
  have pointwise : Pointwise fun n (_ : Nat → Nat) a => ∀ t, 0 < a t → 0 < n t :=
    fun same law t pos => Nat.lt_of_lt_of_le (law t (Nat.lt_of_lt_of_le pos
      (Nat.le_of_eq (same t).2.2.symm))) (Nat.le_of_eq (same t).1)
  have unbound : ¬ BindsCounting S → ¬ ∀ (w : World) [∀ t x, Decidable (w.web.active t x)],
      w.Meets S → w.CountsObey fun n _ a => ∀ t, 0 < a t → 0 < n t := fun free law =>
    Nat.lt_irrefl 0 ((counting_under S pointwise).mpr law _ _ _ Queue.lone_tally
      (fun binds => absurd binds free) 0 Nat.zero_lt_one)
  ⟨fun law => match hb : S .balanced, he : S .embodied, ha : S .acting, ht : S .taking,
      hd : S .dissipative with
    | true, true, true, _, _ => ⟨hb, he, .inl ha⟩
    | true, true, false, true, true => ⟨hb, he, .inr ⟨ht, hd⟩⟩
    | false, _, _, _, _ => absurd law (unbound fun binds => nomatch hb.symm.trans binds.1)
    | true, false, _, _, _ => absurd law (unbound fun binds => nomatch he.symm.trans binds.2.1)
    | true, true, false, false, _ => absurd law (unbound fun binds => match binds.2.2 with
        | .inl acting => nomatch ha.symm.trans acting
        | .inr ⟨taking, _⟩ => nomatch ht.symm.trans taking)
    | true, true, false, true, false => absurd law (unbound fun binds => match binds.2.2 with
        | .inl acting => nomatch ha.symm.trans acting
        | .inr ⟨_, dissipative⟩ => nomatch hd.symm.trans dissipative),
   fun binds => (counting_under S pointwise).mp fun _ _ _ _ quiet => quiet binds⟩

end World

/-! ## Counting under enclosure -/

namespace World

variable {w : World}

/-- Under a census of embodied relata, each relatum active at a step stands there, so they
number at most the total standing. -/
theorem length_le_stock {alive : Nat → List w.Relatum} (census : w.web.Census alive)
    (embodied : w.Embodied) (t : Nat) : (alive t).length ≤ w.web.stock (alive t) t :=
  Nat.le_trans (Nat.le_of_eq (total_ones (alive t)).symm) (total_le (alive t) fun x mem =>
    (embodied x t).mp (((census t).2 x).mpr mem))

/-- Enclosure bounds change. In a world with a census whose relata are embodied, with a
balanced, dissipative flow, in which every step from `T` on is enclosed, the total standing
at `T` bounds the change of the census from `T`: the relata active at any
later step, with the steps since `T` at which something arose or ceased, number at most
that total. -/
theorem enclosure_bounds_change [∀ t x, Decidable (w.web.active t x)]
    {alive : Nat → List w.Relatum} (census : w.web.Census alive) (embodied : w.Embodied)
    (balanced : w.Balanced) (dissipative : w.Dissipative) {T : Nat}
    (enclosed : ∀ t, T ≤ t → w.flow.Enclosed t) :
    ChangeBound T (w.web.stock (alive T) T) (fun t => (alive t).length)
      (fun t => ceasings (alive t) (fun x s => w.web.active s x) t)
      (fun t => comings (alive (t + 1)) (fun x s => w.web.active s x) t) :=
  have standing := standingCensus census embodied
  fun _ later => Nat.le_trans (Nat.add_le_add_right (length_le_stock census embodied _) _)
    (falls_by_occurrences (fun t => w.web.stock (alive t) t) _ (fun t later =>
      Decidable.of_not_not fun no => (enclosed t later).aroundStanding_not_not alive
        fun around => no (match Nat.eq_zero_or_pos (ceasings (alive t)
            (fun x s => w.web.active s x) t + comings (alive (t + 1))
            (fun x s => w.web.active s x) t) with
          | .inl quiet => Nat.le_trans (Nat.le_of_eq (congrArg (_ + ·) (mark_zero
              fun positive => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le positive
                (Nat.le_of_eq quiet)))))
              (Flow.standing_never_rises balanced dissipative standing around)
          | .inr changes =>
            have lowers : ∃ x, w.web.Rises t x ∨ w.web.Falls t x :=
              match Nat.eq_zero_or_pos (ceasings (alive t) (fun x s => w.web.active s x) t) with
              | .inr ceasing => match total_pos _ ceasing with
                | ⟨x, _, ceases⟩ => ⟨x, .inr (falls_of_ceases embodied (mark_pos.mp ceases))⟩
              | .inl still => match total_pos _ (Nat.lt_of_lt_of_le changes (Nat.le_of_eq
                  ((congrArg (· + _) still).trans (Nat.zero_add _)))) with
                | ⟨x, _, comes⟩ => ⟨x, .inl (rises_of_arises embodied (mark_pos.mp comes))⟩
            match lowers with
            | ⟨_, change⟩ => Nat.le_trans (Nat.le_of_eq (congrArg (_ + ·) (mark_one changes)))
                (Flow.change_lowers balanced dissipative standing around change)))
      later)

end World

namespace EnclosedQueue

variable (n c a : Nat → Nat) (B : Nat)

/-- What stands: `B`, less one for each step at which something ceased or arose. -/
def store (t : Nat) : Nat :=
  B - occurrences 0 (fun s => c s + a s) t

/-- Standing in a queue whose front is `g` and which holds `m`: one, and `s` more at the
front. -/
def place (g m s k : Nat) : Nat :=
  if g ≤ k ∧ k < g + m then 1 + (if k = g then s else 0) else 0

/-- Members stand by their place in the queue, the front holding what the store holds
beyond one for each member. -/
def level (t k : Nat) : Nat :=
  place (Queue.gone c t) (n t) (store c a B t - n t) k

/-- Members stand and are active exactly while in the queue. -/
def web : Web Nat Nat where
  level := level n c a B
  active t k := Queue.holds n c k t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

/-- The front takes part at every step. It takes from each member what that member's
standing loses across the step and gives each what it gains. -/
def flow : Flow Nat Nat where
  present t := [Queue.gone c t]
  take t _ k := level n c a B t k - level n c a B (t + 1) k
  give t _ k := level n c a B (t + 1) k - level n c a B t k

/-- The members in the queue before or after the step from `t`. -/
def span (t : Nat) : List Nat :=
  steps (Queue.gone c t) (n t + a t)

variable {n c a : Nat → Nat} {B : Nat}

theorem place_pos {g m s k : Nat} : (g ≤ k ∧ k < g + m) ↔ 0 < place g m s k :=
  if h : g ≤ k ∧ k < g + m then
    ⟨fun _ => Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_add_right 1 _))
      (Nat.le_of_eq (if_pos h).symm), fun _ => h⟩
  else
    ⟨fun holds => absurd holds h,
     fun pos => absurd (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (if_neg h))) (Nat.lt_irrefl 0)⟩

theorem place_zero {g m s k : Nat} (out : ¬ (g ≤ k ∧ k < g + m)) : place g m s k = 0 :=
  if_neg out

/-- A queue of `m + 1` stands at `m + 1`, and `s` more at its front. -/
theorem total_place (g m s : Nat) : total (steps g (m + 1)) (place g (m + 1) s) = m + 1 + s :=
  have front : place g (m + 1) s g = 1 + s :=
    (if_pos ⟨Nat.le_refl g, Nat.lt_add_of_pos_right (Nat.succ_pos m)⟩).trans
      (congrArg (1 + ·) (if_pos rfl))
  have rest : total (steps (g + 1) m) (place g (m + 1) s) = m :=
    (total_congr_on (g := fun _ => 1) fun _ mem =>
      (if_pos ⟨Nat.le_of_succ_le (steps_mem mem), Nat.lt_of_lt_of_le (steps_within mem)
        (Nat.le_of_eq (Nat.add_right_comm g 1 m))⟩).trans
        (congrArg (1 + ·) (if_neg fun same => Nat.lt_irrefl g (Nat.lt_of_lt_of_le
          (Nat.lt_succ_self g) (Nat.le_trans (steps_mem mem) (Nat.le_of_eq same)))))).trans
      ((total_ones _).trans (steps_length _ _))
  (congrArg (· + _) front).trans ((congrArg (1 + s + ·) rest).trans
    ((Nat.add_right_comm 1 s m).trans ((congrArg (· + s) (Nat.add_comm 1 m)))))

/-- Where a member's standing does not change, the front neither takes from nor gives to
it. -/
theorem still_flows {t k f : Nat} (same : level n c a B (t + 1) k = level n c a B t k) :
    (flow n c a B).take t f k = 0 ∧ (flow n c a B).give t f k = 0 :=
  ⟨(congrArg (level n c a B t k - ·) same).trans (Nat.sub_self _),
   (congrArg (· - level n c a B t k) same).trans (Nat.sub_self _)⟩

theorem still {t k f : Nat}
    (flows : (flow n c a B).take t f k = 0 ∧ (flow n c a B).give t f k = 0) :
    ¬ (0 < (flow n c a B).take t f k ∨ 0 < (flow n c a B).give t f k)
  | .inl takes => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le takes (Nat.le_of_eq flows.1))
  | .inr gives => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le gives (Nat.le_of_eq flows.2))

/-- An empty queue stays empty where nothing joins an empty queue. -/
theorem empty_stays (tally : Tally n c a) {t : Nat} (company : 0 < a t → 0 < n t)
    (empty : n t = 0) : n (t + 1) = 0 :=
  match tally t with
  | ⟨k, before, after⟩ =>
    have kept : k = 0 := Nat.eq_zero_of_le_zero
      (Nat.le_trans (Nat.le_add_right k (c t)) (Nat.le_of_eq (before.symm.trans empty)))
    have joined : a t = 0 := eq_zero_of_not_pos fun joins =>
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (company joins) (Nat.le_of_eq empty))
    after.trans ((congrArg (· + a t) kept).trans ((Nat.zero_add _).trans joined))

theorem outside_empty {k t : Nat} (empty : n t = 0) : ¬ Queue.holds n c k t :=
  fun holds => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (OpenQueue.occupied holds) (Nat.le_of_eq empty))

/-- Across a step from an empty queue nothing is taken or given. -/
theorem idle (tally : Tally n c a) {t : Nat} (company : 0 < a t → 0 < n t)
    (empty : n t = 0) (k f : Nat) :
    (flow n c a B).take t f k = 0 ∧ (flow n c a B).give t f k = 0 :=
  still_flows ((place_zero (outside_empty (empty_stays tally company empty))).trans
    (place_zero (outside_empty empty)).symm)

/-- Across a step at which nothing ceases or arises nothing changes. -/
theorem quiet_same (tally : Tally n c a) {t : Nat} (quiet : c t + a t = 0) (k : Nat) :
    level n c a B (t + 1) k = level n c a B t k :=
  have ceased : c t = 0 :=
    Nat.eq_zero_of_le_zero (Nat.le_trans (Nat.le_add_right _ _) (Nat.le_of_eq quiet))
  have joined : a t = 0 :=
    Nat.eq_zero_of_le_zero (Nat.le_trans (Nat.le_add_left _ _) (Nat.le_of_eq quiet))
  have front : Queue.gone c (t + 1) = Queue.gone c t :=
    (Queue.gone_succ t).trans (congrArg (_ + ·) ceased)
  have size : n (t + 1) = n t := match tally t with
    | ⟨_, before, after⟩ => after.trans ((congrArg (_ + ·) joined).trans
        ((congrArg (_ + ·) ceased).symm.trans before.symm))
  have kept : store c a B (t + 1) = store c a B t :=
    congrArg (B - ·) ((occurrences_succ _ (Nat.zero_le t)).trans (congrArg (_ + ·)
      (mark_zero fun changes => Nat.lt_irrefl 0
        (Nat.lt_of_lt_of_le changes (Nat.le_of_eq quiet)))))
  (congrArg (fun g => place g (n (t + 1)) (store c a B (t + 1) - n (t + 1)) k) front).trans
    ((congrArg (fun m => place (Queue.gone c t) m (store c a B (t + 1) - m) k) size).trans
      (congrArg (fun s => place (Queue.gone c t) (n t) (s - n t) k) kept))

/-- What is in the queue before or after a step lies in its span. -/
theorem within_span (tally : Tally n c a) {t k : Nat}
    (holds : Queue.holds n c k t ∨ Queue.holds n c k (t + 1)) : k ∈ span n c a t :=
  match tally t, holds with
  | _, .inl now => steps_of_within now.1
      (Nat.lt_of_lt_of_le now.2 (Nat.add_le_add_left (Nat.le_add_right _ _) _))
  | ⟨_, before, after⟩, .inr next => steps_of_within
      (Nat.le_trans (Nat.le_trans (Nat.le_add_right _ (c t))
        (Nat.le_of_eq (Queue.gone_succ t).symm)) next.1)
      (Nat.lt_of_lt_of_le next.2 (Nat.le_of_eq ((congrArg (_ + ·) after).trans
        ((Nat.add_assoc _ _ _).symm.trans ((congrArg (· + a t) (Queue.kept_end before).symm).trans
          (Nat.add_assoc _ _ _))))))

/-- Whatever the front takes from or gives to lies in the span. -/
theorem moving_within (tally : Tally n c a) {t k f : Nat}
    (moves : 0 < (flow n c a B).take t f k ∨ 0 < (flow n c a B).give t f k) :
    k ∈ span n c a t :=
  if now : Queue.holds n c k t then within_span tally (.inl now)
  else if next : Queue.holds n c k (t + 1) then within_span tally (.inr next)
  else absurd moves (still (still_flows ((place_zero next).trans (place_zero now).symm)))

/-- Each step is enclosed by its span. -/
theorem closed (tally : Tally n c a) (t : Nat) : (flow n c a B).ClosedAt (span n c a t) t :=
  fun _ _ _ out => ⟨eq_zero_of_not_pos fun takes => out (moving_within tally (.inl takes)),
    eq_zero_of_not_pos fun gives => out (moving_within tally (.inr gives))⟩

theorem span_distinct (t : Nat) : Distinct (span n c a t) :=
  steps_distinct _ _

/-- Something taken or given means the queue is not empty. -/
theorem busy (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) {t k f : Nat}
    (moves : 0 < (flow n c a B).take t f k ∨ 0 < (flow n c a B).give t f k) : 0 < n t :=
  match Nat.eq_zero_or_pos (n t) with
  | .inl empty => absurd moves (still (idle tally (company t) empty k f))
  | .inr occupied => occupied

end EnclosedQueue

namespace World

/-- An enclosed queue: its front exchanges only within the queue, and what stands falls
by one at each step at which a member joins or leaves. -/
def enclosedQueue (n c a : Nat → Nat) (B : Nat) : World :=
  ⟨Nat, EnclosedQueue.flow n c a B, EnclosedQueue.web n c a B⟩

instance enclosedQueue_decided (n c a : Nat → Nat) (B : Nat) :
    ∀ t x, Decidable ((enclosedQueue n c a B).web.active t x) :=
  fun t k => inferInstanceAs (Decidable (Queue.holds n c k t))

/-- The census of an enclosed queue is the queue. -/
theorem enclosedQueue_census (n c a : Nat → Nat) (B : Nat) :
    (enclosedQueue n c a B).web.Census (Queue.line n c) :=
  Queue.listed

theorem enclosedQueue_embodied (n c a : Nat → Nat) (B : Nat) :
    (enclosedQueue n c a B).Embodied :=
  fun _ _ => EnclosedQueue.place_pos

theorem enclosedQueue_balanced (n c a : Nat → Nat) (B : Nat) :
    (enclosedQueue n c a B).Balanced :=
  fun t k => add_sub_turn (EnclosedQueue.level n c a B t k) (EnclosedQueue.level n c a B (t + 1) k)

variable {n c a : Nat → Nat} {B : Nat}

theorem enclosedQueue_acting (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) :
    (enclosedQueue n c a B).Acting :=
  fun _ f _ present gives => match f, present, gives with
    | _, .head _, gives => OpenQueue.front.mpr (EnclosedQueue.busy tally company (.inr gives))
    | _, .tail _ no, _ => (nomatch no)

/-- Only the front takes, and only from a member in the queue, so only while it is active,
whatever the counts. -/
theorem enclosedQueue_taking (n c a : Nat → Nat) (B : Nat) : (enclosedQueue n c a B).Taking :=
  fun _ f _ present takes => match f, present, takes with
    | _, .head _, takes => ⟨OpenQueue.front.mpr (OpenQueue.occupied (EnclosedQueue.place_pos.mpr
        (Nat.lt_of_lt_of_le takes (Nat.sub_le _ _)))), trivial⟩
    | _, .tail _ no, _ => (nomatch no)

/-- Where the queue fits its store, what stands is at most the store, and is the store
while the queue is not empty. -/
theorem enclosedQueue_stock {t : Nat} (fits : n t ≤ EnclosedQueue.store c a B t) :
    (enclosedQueue n c a B).web.stock (Queue.line n c t) t ≤ EnclosedQueue.store c a B t ∧
      (0 < n t → (enclosedQueue n c a B).web.stock (Queue.line n c t) t =
        EnclosedQueue.store c a B t) :=
  have whole : ∀ m, n t = m + 1 →
      (enclosedQueue n c a B).web.stock (Queue.line n c t) t = EnclosedQueue.store c a B t :=
    fun m size =>
      (congrArg (fun k => total (steps (Queue.gone c t) k)
        (EnclosedQueue.place (Queue.gone c t) k (EnclosedQueue.store c a B t - n t))) size).trans
        ((EnclosedQueue.total_place _ m _).trans ((congrArg (· + _) size.symm).trans
          (add_sub_of_le fits)))
  match Nat.eq_zero_or_pos (n t) with
  | .inl empty => ⟨Nat.le_trans (Nat.le_of_eq
      (congrArg (fun k => total (steps (Queue.gone c t) k)
        (EnclosedQueue.place (Queue.gone c t) k (EnclosedQueue.store c a B t - n t))) empty))
      (Nat.zero_le _), fun occupied => absurd (empty ▸ occupied) (Nat.lt_irrefl 0)⟩
  | .inr occupied => ⟨Nat.le_of_eq (whole _ (Nat.succ_pred_eq_of_pos occupied).symm),
      fun _ => whole _ (Nat.succ_pred_eq_of_pos occupied).symm⟩

/-- Across a step at which nothing joins an empty queue, with the queue within its store
before and after, the enclosed queue dissipates on every closed family: where something joins
or leaves, what stands falls by one, so the front takes more than it gives. -/
theorem enclosedQueue_dissipatesOn (tally : Tally n c a) {t : Nat}
    (company : 0 < a t → 0 < n t) (fits : n t ≤ EnclosedQueue.store c a B t)
    (fits' : n (t + 1) ≤ EnclosedQueue.store c a B (t + 1)) {cs : List Nat}
    (distinct : Distinct cs) (closed : (EnclosedQueue.flow n c a B).ClosedAt cs t) :
    (EnclosedQueue.flow n c a B).DissipatesOn cs t :=
  fun f present =>
    have still : (∀ k, (EnclosedQueue.flow n c a B).take t f k = 0 ∧
        (EnclosedQueue.flow n c a B).give t f k = 0) →
        total cs ((EnclosedQueue.flow n c a B).give t f) +
          sign (total cs ((EnclosedQueue.flow n c a B).take t f)) ≤
            total cs ((EnclosedQueue.flow n c a B).take t f) := fun flows =>
      Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) (total_eq_zero fun k _ => (flows k).2)).trans
        ((Nat.zero_add _).trans (congrArg sign (total_eq_zero fun k _ => (flows k).1)))))
        (Nat.zero_le _)
    match Nat.eq_zero_or_pos (n t), Nat.eq_zero_or_pos (c t + a t) with
    | .inl empty, _ => still fun k => EnclosedQueue.idle tally company empty k f
    | .inr _, .inl quiet => still fun k =>
      EnclosedQueue.still_flows (EnclosedQueue.quiet_same tally quiet k)
    | .inr occupied, .inr changes =>
      have census := enclosedQueue_census n c a B
      have standing := standingCensus census (enclosedQueue_embodied n c a B)
      have before := standing.stock_eq (EnclosedQueue.span_distinct t) fun k mem =>
        EnclosedQueue.within_span tally (.inl (((census t).2 k).mpr mem))
      have after := standing.stock_eq (t := t + 1) (EnclosedQueue.span_distinct t) fun k mem =>
        EnclosedQueue.within_span tally (.inr (((census (t + 1)).2 k).mpr mem))
      have spent : EnclosedQueue.store c a B (t + 1) + 1 ≤ EnclosedQueue.store c a B t :=
        Nat.le_of_eq ((congrArg (fun u => B - u + 1) ((occurrences_succ _ (Nat.zero_le t)).trans
          (congrArg (_ + ·) (mark_one changes)))).trans (Nat.succ_pred_eq_of_pos
            (Nat.lt_of_lt_of_le occupied fits)))
      have lowered := Nat.le_trans (Nat.add_le_add_right (Nat.le_trans (Nat.le_of_eq after.symm)
          (enclosedQueue_stock fits').1) 1)
        (Nat.le_trans spent (Nat.le_of_eq (((enclosedQueue_stock fits).2
          occupied).symm.trans before)))
      have over := (enclosedQueue_balanced n c a B).over (EnclosedQueue.span n c a t) t
      have exceeds :
          total (EnclosedQueue.span n c a t) ((EnclosedQueue.flow n c a B).give t f) + 1 ≤
            total (EnclosedQueue.span n c a t) ((EnclosedQueue.flow n c a B).take t f) :=
        le_of_add_le_add_right _ (Nat.le_trans (Nat.le_of_eq ((Nat.add_assoc _ _ _).trans
          (congrArg (_ + ·) (Nat.add_comm _ _)))) (Nat.le_trans (Nat.add_le_add_left lowered _)
            (Nat.le_of_eq ((Nat.add_comm _ _).trans (over.symm.trans (Nat.add_comm _ _))))))
      Nat.le_trans (Nat.add_le_add (total_le_of_support distinct fun _ _ gives =>
          EnclosedQueue.moving_within tally (.inr gives)) (sign_le_one _))
        (Nat.le_trans exceeds (total_le_of_support (EnclosedQueue.span_distinct t) fun k _ takes =>
          match decideMem k cs with
          | .isTrue mem => mem
          | .isFalse out => absurd (Nat.lt_of_lt_of_le takes
              (Nat.le_of_eq (closed f present k out).1)) (Nat.lt_irrefl 0)))

/-- Under a change bound from the first step the enclosed queue dissipates. -/
theorem enclosedQueue_dissipative (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    (bound : ChangeBound 0 B n c a) : (enclosedQueue n c a B).Dissipative :=
  fun _ t distinct closed => enclosedQueue_dissipatesOn tally (company t)
    (RelationalRenewal.le_sub_from_add (bound t (Nat.zero_le t)))
    (RelationalRenewal.le_sub_from_add (bound (t + 1) (Nat.zero_le _))) distinct closed

/-- Under a change bound from the first step, with nothing joining an empty queue, an
enclosed queue meets all eight premises. -/
theorem enclosedQueue_premised (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    (bound : ChangeBound 0 B n c a) : (enclosedQueue n c a B).Premised :=
  .of (fun _ _ _ _ no => (nomatch no)) (enclosedQueue_balanced n c a B)
    (enclosedQueue_acting tally company) (enclosedQueue_taking n c a B)
    (enclosedQueue_dissipative tally company bound) (enclosedQueue_embodied n c a B)
    ⟨_, enclosedQueue_census n c a B⟩ ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩

/-- Every step of an enclosed queue is enclosed. -/
theorem enclosedQueue_enclosed (tally : Tally n c a) (t : Nat) :
    (enclosedQueue n c a B).flow.Enclosed t :=
  ⟨EnclosedQueue.span n c a t, EnclosedQueue.span_distinct t, EnclosedQueue.closed tally t⟩

/-- Under all eight premises, with every step from some step on enclosed, the laws of
counting are the tally, that nothing arises across a step at which nothing is active, and a
change bound from the first step: a property of the counts holds of every census of every such
world exactly when it holds of every tally of this kind. -/
theorem enclosed_counting {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop}
    (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ B, ChangeBound 0 B n c a) →
      Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised →
        (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q :=
  ⟨fun law w _ premised ⟨_, enclosed⟩ alive census =>
    law _ _ _ census.tally
      (counting_binds_jointly.1 w (premised _ (.tail _ (.head _)))
        (premised _ (.tail _ (.tail _ (.head _))))
        (Embodied.arising (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _
          (.head _))))))))
        alive census)
      ⟨_, (enclosure_bounds_change census
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))))
        (premised _ (.tail _ (.head _)))
        (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))) enclosed).from_zero⟩,
   fun law _ _ _ tally company ⟨_, bound⟩ => pointwise (Queue.counts tally)
      (law (enclosedQueue _ _ _ _) (enclosedQueue_premised tally company bound)
        ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩ _ (enclosedQueue_census _ _ _ _))⟩

end World

/-! ## Counting in finite worlds -/

/-- The numbers of a list that are below `K`, as places among `K`. -/
def placesBelow (K : Nat) : List Nat → List (Fin K)
  | [] => []
  | k :: l => if h : k < K then ⟨k, h⟩ :: placesBelow K l else placesBelow K l

theorem mem_placesBelow {K : Nat} {i : Fin K} :
    ∀ {l : List Nat}, i ∈ placesBelow K l ↔ i.val ∈ l
  | [] => ⟨fun no => (nomatch no), fun no => (nomatch no)⟩
  | k :: l =>
    if h : k < K then
      have unfold : placesBelow K (k :: l) = ⟨k, h⟩ :: placesBelow K l := dif_pos h
      ⟨fun mem => match mem_cons_cases (Eq.mp (congrArg (i ∈ ·) unfold) mem) with
        | .inl same => Eq.subst (motive := fun v => v ∈ k :: l) (congrArg Fin.val same).symm
            (.head l)
        | .inr mem => .tail k (mem_placesBelow.mp mem),
       fun mem => Eq.mpr (congrArg (i ∈ ·) unfold) (match mem_cons_cases mem with
        | .inl same => Eq.subst (motive := fun j => j ∈ (⟨k, h⟩ : Fin K) :: placesBelow K l)
            (Fin.eq_of_val_eq (i := ⟨k, h⟩) (j := i) same.symm) (.head _)
        | .inr mem => .tail _ (mem_placesBelow.mpr mem))⟩
    else
      have unfold : placesBelow K (k :: l) = placesBelow K l := dif_neg h
      ⟨fun mem => .tail k (mem_placesBelow.mp (Eq.mp (congrArg (i ∈ ·) unfold) mem)),
       fun mem => Eq.mpr (congrArg (i ∈ ·) unfold) (match mem_cons_cases mem with
        | .inl same => absurd (Eq.subst (motive := fun v => v < K) same i.isLt) h
        | .inr mem => mem_placesBelow.mpr mem)⟩

theorem placesBelow_distinct {K : Nat} :
    ∀ {l : List Nat}, Distinct l → Distinct (placesBelow K l)
  | [], _ => trivial
  | k :: _, ⟨fresh, distinct⟩ =>
    if h : k < K then
      Eq.mpr (congrArg Distinct (dif_pos h))
        ⟨fun mem => fresh (mem_placesBelow.mp mem), placesBelow_distinct distinct⟩
    else Eq.mpr (congrArg Distinct (dif_neg h)) (placesBelow_distinct distinct)

/-- Over a list of numbers below `K`, a quantity on places totals what it totals on the
numbers. -/
theorem total_placesBelow {K : Nat} {q : Fin K → Nat} {g : Nat → Nat}
    (same : ∀ i, q i = g i.val) :
    ∀ {l : List Nat}, (∀ k, k ∈ l → k < K) → total (placesBelow K l) q = total l g
  | [], _ => rfl
  | k :: l, within =>
    (congrArg (fun m => total m q) (dif_pos (within k (.head l)))).trans
      ((congrArg (· + total (placesBelow K l) q) (same ⟨k, within k (.head l)⟩)).trans
        (congrArg (g k + ·) (total_placesBelow same fun j mem => within j (.tail k mem))))

/-- The `K` places, each listed once. -/
theorem places_listed (K : Nat) : ∃ all : List (Fin K), Distinct all ∧ ∀ i, i ∈ all :=
  ⟨placesBelow _ (steps 0 K), placesBelow_distinct (steps_distinct _ _),
   fun i => mem_placesBelow.mpr (steps_of_within (Nat.zero_le _)
     (Nat.lt_of_lt_of_le i.isLt (Nat.le_of_eq (Nat.zero_add _).symm)))⟩

namespace FiniteQueue

variable (n c a : Nat → Nat) (B : Nat)

/-- Room for every member a queue counting a tally whose change `B` bounds ever holds
(`ChangeBound.reach`). -/
def size : Nat := B + B * B + 1

/-- The front of the queue where it lies within the room, the first place otherwise. -/
def front (t : Nat) : Fin (size B) :=
  if h : Queue.gone c t < size B then ⟨_, h⟩ else ⟨0, Nat.succ_pos _⟩

/-- The enclosed queue's web, on the places of the room. -/
def web : Web (Fin (size B)) (Fin (size B)) where
  level t i := EnclosedQueue.level n c a B t i.val
  active t i := Queue.holds n c i.val t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

/-- The enclosed queue's flow, on the places of the room. -/
def flow : Flow (Fin (size B)) (Fin (size B)) where
  present t := [front c B t]
  take t _ i := (EnclosedQueue.flow n c a B).take t (Queue.gone c t) i.val
  give t _ i := (EnclosedQueue.flow n c a B).give t (Queue.gone c t) i.val

/-- The members in the queue at each step, as places. -/
def alive (t : Nat) : List (Fin (size B)) :=
  placesBelow (size B) (Queue.line n c t)

variable {n c a : Nat → Nat} {B : Nat}

/-- Every member the queue holds has a place. -/
theorem placed (tally : Tally n c a) (bound : ChangeBound 0 B n c a) {k t : Nat}
    (holds : Queue.holds n c k t) : k < size B :=
  Nat.lt_of_lt_of_le holds.2 (Nat.le_succ_of_le (ChangeBound.reach tally bound t))

theorem front_val (tally : Tally n c a) (bound : ChangeBound 0 B n c a) (t : Nat) :
    (front c B t).val = Queue.gone c t :=
  congrArg Fin.val (dif_pos (Nat.lt_of_le_of_lt (Nat.le_add_right _ (n t))
    (Nat.lt_succ_of_le (ChangeBound.reach tally bound t))))

end FiniteQueue

namespace World

/-- An enclosed queue on the finitely many places its members ever take. -/
def finiteQueue (n c a : Nat → Nat) (B : Nat) : World :=
  ⟨Fin (FiniteQueue.size B), FiniteQueue.flow n c a B, FiniteQueue.web n c a B⟩

instance finiteQueue_decided (n c a : Nat → Nat) (B : Nat) :
    ∀ t x, Decidable ((finiteQueue n c a B).web.active t x) :=
  fun t i => inferInstanceAs (Decidable (Queue.holds n c i.val t))

theorem finiteQueue_finite (n c a : Nat → Nat) (B : Nat) : (finiteQueue n c a B).Finite :=
  places_listed _

theorem finiteQueue_census (n c a : Nat → Nat) (B : Nat) :
    (finiteQueue n c a B).web.Census (FiniteQueue.alive n c B) :=
  fun _ => ⟨placesBelow_distinct (steps_distinct _ _), fun _ =>
    ⟨fun holds => mem_placesBelow.mpr (steps_of_within holds.1 holds.2),
     fun mem => ⟨steps_mem (mem_placesBelow.mp mem), steps_within (mem_placesBelow.mp mem)⟩⟩⟩

variable {n c a : Nat → Nat} {B : Nat}

/-- Under a change bound from the first step, its census counts what the queue counts. -/
theorem finiteQueue_counts (tally : Tally n c a) (bound : ChangeBound 0 B n c a) (t : Nat) :
    (FiniteQueue.alive n c B t).length = n t ∧
      ceasings (FiniteQueue.alive n c B t)
        (fun x s => (finiteQueue n c a B).web.active s x) t = c t ∧
      comings (FiniteQueue.alive n c B (t + 1))
        (fun x s => (finiteQueue n c a B).web.active s x) t = a t :=
  have within : ∀ s k, k ∈ Queue.line n c s → k < FiniteQueue.size B := fun _ _ mem =>
    FiniteQueue.placed tally bound ⟨steps_mem mem, steps_within mem⟩
  ⟨(total_ones _).symm.trans ((total_placesBelow (g := fun _ => 1) (fun _ => rfl)
      (within t)).trans ((total_ones _).trans (steps_length _ _))),
   (total_placesBelow (fun _ => rfl) (within t)).trans (Queue.ceasings_eq tally t),
   (total_placesBelow (fun _ => rfl) (within (t + 1))).trans (Queue.comings_eq tally t)⟩

/-- Under a change bound from the first step, with nothing joining an empty queue, the
finite queue meets all eight premises: it dissipates as the enclosed queue does. -/
theorem finiteQueue_premised (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    (bound : ChangeBound 0 B n c a) : (finiteQueue n c a B).Premised :=
  have active : ∀ {t : Nat}, 0 < n t →
      (finiteQueue n c a B).web.active t (FiniteQueue.front c B t) :=
    fun occupied => Eq.subst (motive := fun v => Queue.holds n c v _)
      (FiniteQueue.front_val tally bound _).symm (OpenQueue.front.mpr occupied)
  .of (fun _ _ _ _ no => (nomatch no))
    (fun t i => enclosedQueue_balanced n c a B t i.val)
    (fun _ f _ present gives => match f, present, gives with
      | _, .head _, gives => active (EnclosedQueue.busy (f := 0) tally company (.inr gives))
      | _, .tail _ no, _ => (nomatch no))
    (fun _ f _ present takes => match f, present, takes with
      | _, .head _, takes => ⟨active (EnclosedQueue.busy (f := 0) tally company (.inl takes)),
          trivial⟩
      | _, .tail _ no, _ => (nomatch no))
    (fun cs t distinct closed f present =>
      have dissipates := enclosedQueue_dissipative tally company bound
        (cs.map Fin.val) t (distinct_map (fun _ _ same => Fin.eq_of_val_eq same) distinct)
        (fun _ _ (k : Nat) out =>
          if h : k < FiniteQueue.size B then
            closed f present ⟨k, h⟩ fun mem => out (mem_map_of (g := Fin.val) mem)
          else EnclosedQueue.still_flows
            ((EnclosedQueue.place_zero fun holds => h (FiniteQueue.placed tally bound holds)).trans
              (EnclosedQueue.place_zero fun holds =>
                h (FiniteQueue.placed tally bound holds)).symm))
        (Queue.gone c t) (.head _)
      have gives : total (cs.map Fin.val) ((EnclosedQueue.flow n c a B).give t (Queue.gone c t)) =
          total cs ((FiniteQueue.flow n c a B).give t f) := total_map _ _ cs
      have takes : total (cs.map Fin.val) ((EnclosedQueue.flow n c a B).take t (Queue.gone c t)) =
          total cs ((FiniteQueue.flow n c a B).take t f) := total_map _ _ cs
      Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) gives.symm).trans
          (congrArg (fun k => _ + sign k) takes.symm)))
        (Nat.le_trans dissipates (Nat.le_of_eq takes)))
    (fun _ _ => EnclosedQueue.place_pos)
    ⟨_, finiteQueue_census _ _ _ _⟩
    ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩

/-- Under all eight premises, in a finite world, the laws of counting are those under
enclosure from some step on: the tally, that nothing arises across a step at which nothing
is active, and a change bound from the first step. -/
theorem finite_counting {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop}
    (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ B, ChangeBound 0 B n c a) →
      Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.Finite →
        w.CountsObey Q :=
  ⟨fun law w _ premised finite => (enclosed_counting pointwise).mp law w premised
      ⟨0, fun t _ => finite.enclosed t⟩,
   fun law _ _ _ tally company ⟨_, bound⟩ => pointwise (finiteQueue_counts tally bound)
      (law (finiteQueue _ _ _ _) (finiteQueue_premised tally company bound)
        (finiteQueue_finite _ _ _ _) _ (finiteQueue_census _ _ _ _))⟩

/-- So under the eight premises, worlds enclosed from some step on and finite worlds have
the same laws of counting (the thirteenth review's probe). -/
theorem enclosed_iff_finite_counting {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop}
    (pointwise : Pointwise Q) :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised →
      (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.Finite →
        w.CountsObey Q :=
  (enclosed_counting pointwise).symm.trans (finite_counting pointwise)

/-- One member replaced across the first step, in a finite queue. -/
abbrev replaced : World :=
  finiteQueue (fun _ => 1) (Swap.change fun _ => true) (Swap.change fun _ => true) 2

/-- In the finite queue dissipation binds: where one member is replaced across the first
step, the front takes two units from the family of all places. -/
theorem finite_dissipation_binds :
    ∃ cs t f, Distinct cs ∧ replaced.flow.ClosedAt cs t ∧ f ∈ replaced.flow.present t ∧
      0 < total cs (replaced.flow.take t f) :=
  have takes : replaced.flow.take 0 (FiniteQueue.front (Swap.change fun _ => true) 2 0)
      ⟨0, Nat.succ_pos _⟩ = 2 := rfl
  match finiteQueue_finite (fun _ => 1) (Swap.change fun _ => true)
      (Swap.change fun _ => true) 2 with
  | ⟨all, distinct, every⟩ =>
    ⟨all, 0, FiniteQueue.front (Swap.change fun _ => true) 2 0, distinct,
     fun _ _ x out => absurd (every x) out, .head _,
     Nat.lt_of_lt_of_le Nat.zero_lt_two (Nat.le_trans (Nat.le_of_eq takes.symm)
       (le_total_of_mem (every ⟨0, Nat.succ_pos _⟩)))⟩

/-- And the bound of `enclosure_bounds_change` is attained there: what stands at the first step
totals two, and from the next step on one member is active with one step of change behind
it. -/
theorem replaced_attains :
    replaced.web.stock (FiniteQueue.alive (fun _ => 1) (Swap.change fun _ => true) 2 0) 0 = 2 ∧
      ∀ t, (FiniteQueue.alive (fun _ => 1) (Swap.change fun _ => true) 2 (t + 1)).length +
        occurrences 0 (fun u => Swap.change (fun _ => true) u + Swap.change (fun _ => true) u)
          (t + 1) = 2 :=
  ⟨rfl, fun t => (congrArg (· + _) (finiteQueue_counts (Swap.tally fun _ => true)
      (Swap.change_bound fun _ => true) (t + 1)).1).trans (congrArg (1 + ·)
        ((congrArg (_ + ·) (mark_zero fun c => Bool.noConfusion (Clear.and_right c))).symm.trans
          (Swap.counted (fun _ => true) (t + 1))))⟩

/-- That arising does not recur in a finite world meeting the eight premises
(`premised_rests`) cannot be strengthened to a step after which nothing arises without
omniscience: if every such world whose activity is decided had one, `LPO` would hold, even
where one member is active throughout and replaced at most once (`Swap`; the thirteenth
review's probe). -/
theorem lpo_of_finite_ends
    (ends : ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.Finite →
      ∃ E, ∀ t x, E ≤ t → ¬ w.web.Arises t x) : LPO := fun s =>
  match ends (finiteQueue (fun _ => 1) (Swap.change s) (Swap.change s) 2)
      (finiteQueue_premised (Swap.tally s) (fun _ _ => Nat.zero_lt_one) (Swap.change_bound s))
      (finiteQueue_finite _ _ _ _) with
  | ⟨E, quiet⟩ => Swap.decide_of_end s (E := E) fun m ge c yes =>
    match total_pos _ (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq
        ((Swap.at_first s c yes).symm.trans
          (finiteQueue_counts (Swap.tally s) (Swap.change_bound s) m).2.2.symm))) with
    | ⟨x, _, arises⟩ => quiet m x ge (mark_pos.mp arises)

end World

/-! ## Counting under each selection, with enclosure -/

/-- The enclosed queue's flow opened before step `T`: there every relatum also exchanges one
unit each way with the front, so no family is closed across a step before `T`. -/
def EnclosedQueue.closing (n c a : Nat → Nat) (B T : Nat) : Flow Nat Nat where
  present t := [Queue.gone c t]
  take t f k := (EnclosedQueue.flow n c a B).take t f k + mark (t < T)
  give t f k := (EnclosedQueue.flow n c a B).give t f k + mark (t < T)

namespace World

/-- An enclosed queue closing at step `T`: before `T` every relatum also exchanges one unit
each way with the front. -/
def closingQueue (n c a : Nat → Nat) (B T : Nat) : World :=
  ⟨Nat, EnclosedQueue.closing n c a B T, EnclosedQueue.web n c a B⟩

instance closingQueue_decided (n c a : Nat → Nat) (B T : Nat) :
    ∀ t x, Decidable ((closingQueue n c a B T).web.active t x) :=
  enclosedQueue_decided n c a B

variable {n c a : Nat → Nat} {B T : Nat}

theorem closingQueue_balanced (n c a : Nat → Nat) (B T : Nat) :
    (closingQueue n c a B T).Balanced :=
  fun t k =>
    show EnclosedQueue.level n c a B (t + 1) k + (EnclosedQueue.level n c a B t k -
        EnclosedQueue.level n c a B (t + 1) k + mark (t < T)) =
      EnclosedQueue.level n c a B t k + (EnclosedQueue.level n c a B (t + 1) k -
        EnclosedQueue.level n c a B t k + mark (t < T)) from
    (Nat.add_assoc _ _ _).symm.trans ((congrArg (· + mark (t < T))
      (add_sub_turn (EnclosedQueue.level n c a B t k)
        (EnclosedQueue.level n c a B (t + 1) k))).trans (Nat.add_assoc _ _ _))

/-- From step `T` on, the closing queue's flow is the enclosed queue's. -/
theorem closing_flows {t : Nat} (later : T ≤ t) (f k : Nat) :
    (EnclosedQueue.closing n c a B T).take t f k = (EnclosedQueue.flow n c a B).take t f k ∧
      (EnclosedQueue.closing n c a B T).give t f k = (EnclosedQueue.flow n c a B).give t f k :=
  have opened : mark (t < T) = 0 := mark_zero (Nat.not_lt_of_le later)
  ⟨congrArg (_ + ·) opened, congrArg (_ + ·) opened⟩

/-- Every step from `T` on is enclosed by its span. -/
theorem closingQueue_enclosed (tally : Tally n c a) {t : Nat} (later : T ≤ t) :
    (closingQueue n c a B T).flow.Enclosed t :=
  ⟨EnclosedQueue.span n c a t, EnclosedQueue.span_distinct t, fun f present k out =>
    match EnclosedQueue.closed (B := B) tally t f present k out with
    | ⟨takes, gives⟩ => ⟨(closing_flows later f k).1.trans takes,
        (closing_flows later f k).2.trans gives⟩⟩

/-- With a change bound from step `T`, nothing joining an empty queue from `T` on, the
closing queue dissipates: before `T` no family is closed, and from `T` on it dissipates as
the enclosed queue does, its store larger by `T`. -/
theorem closingQueue_dissipative (tally : Tally n c a) {K : Nat} (bound : ChangeBound T K n c a)
    (company : ∀ t, T ≤ t → 0 < a t → 0 < n t) : (closingQueue n c a (K + T) T).Dissipative :=
  fun cs t distinct closed f present => match Nat.lt_or_ge t T with
  | .inl early => absurd (closed f present (beyond cs) (beyond_not_mem cs)).2
      fun nothing => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le
        (mark_pos.mpr early) (Nat.le_add_left _ _)) (Nat.le_of_eq nothing))
  | .inr later =>
    have fits : ∀ s, T ≤ s → n s ≤ EnclosedQueue.store c a (K + T) s := fun s later =>
      RelationalRenewal.le_sub_from_add (Nat.le_trans (Nat.add_le_add_left
        (occurrences_zero_le _ s) _) (Nat.le_trans (Nat.le_of_eq (Nat.add_assoc _ _ _).symm)
          (Nat.add_le_add_right (bound s later) T)))
    have takes : total cs ((EnclosedQueue.closing n c a (K + T) T).take t f) =
        total cs ((EnclosedQueue.flow n c a (K + T)).take t f) :=
      total_congr (fun k => (closing_flows later f k).1) cs
    have gives : total cs ((EnclosedQueue.closing n c a (K + T) T).give t f) =
        total cs ((EnclosedQueue.flow n c a (K + T)).give t f) :=
      total_congr (fun k => (closing_flows later f k).2) cs
    Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) gives).trans
        (congrArg (fun u => _ + sign u) takes)))
      (Nat.le_trans (enclosedQueue_dissipatesOn tally (company t later) (fits t later)
          (fits (t + 1) (Nat.le_succ_of_le later)) distinct
          (fun g present k out => match closed g present k out with
            | ⟨took, gave⟩ => ⟨(closing_flows later g k).1.symm.trans took,
                (closing_flows later g k).2.symm.trans gave⟩) f present)
        (Nat.le_of_eq takes.symm))

/-- A selection bounds change under enclosure when it selects balance, embodiment and
dissipation. -/
def BoundsChange (S : Premise → Bool) : Prop :=
  S .balanced = true ∧ S .embodied = true ∧ S .dissipative = true

/-- Where nothing takes part, every step is enclosed. -/
theorem still_enclosed (w : World) (still : ∀ t, w.flow.present t = []) (t : Nat) :
    w.flow.Enclosed t :=
  ⟨[], trivial, fun _ present => nomatch (still t) ▸ present⟩

/-- The laws of counting under each selection of the premises, in worlds enclosed from some
step on. A property of the counts holds of every census of every such world meeting the
selection exactly when it holds of every tally that meets two conditions: where the selection
binds counting, nothing arises across a step at which nothing is active; where it bounds
change, from some step `T` on change stays within a bound and nothing arises across a step at
which nothing is active. The second condition carries its step: that change does not recur
within the bound (`ChangeBound.not_recurring`) gives no such step by itself. -/
theorem enclosed_counting_under (S : Premise → Bool)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (BindsCounting S → ∀ t, 0 < a t → 0 < n t) →
      (BoundsChange S → ∃ T B, ChangeBound T B n c a ∧ ∀ t, T ≤ t → 0 < a t → 0 < n t) →
        Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S →
        (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q :=
  ⟨fun law w _ meets ⟨T, enclosed⟩ alive census => law _ _ _ census.tally
    (fun ⟨balanced, embodied, giving⟩ => match giving with
      | .inl acting => counting_binds_jointly.1 w (meets _ balanced) (meets _ acting)
          (Embodied.arising (meets _ embodied)) alive census
      | .inr ⟨taking, dissipative⟩ => taking_binds_counting w (meets _ balanced)
          (meets _ taking) (meets _ dissipative) (meets _ embodied) alive census)
    (fun ⟨balanced, embodied, dissipative⟩ => ⟨T, _, enclosure_bounds_change census
      (meets _ embodied) (meets _ balanced) (meets _ dissipative) enclosed,
      fun t later arising => enclosed_binds_counting w (meets _ balanced) (meets _ dissipative)
        (meets _ embodied) census (enclosed t later) arising⟩),
   fun law n c a tally quiet bounded =>
    match hb : S .balanced, he : S .embodied with
    | false, _ => pointwise (Queue.counts tally) (law (embodiedQueue n c)
        (embodiedQueue_meets n c hb) ⟨0, fun t _ => still_enclosed _ (fun _ => rfl) t⟩ _
        Queue.listed)
    | true, false => pointwise (Queue.counts tally) (law (queue n c) (queue_meets n c he)
        ⟨0, fun t _ => still_enclosed _ (fun _ => rfl) t⟩ _ Queue.listed)
    | true, true => match hd : S .dissipative, ha : S .acting, ht : S .taking with
      | false, _, _ => pointwise (Queue.counts tally) (law (enclosedQueue n c a 0)
          (fun
            | .dependent, _ => fun _ _ _ _ no => (nomatch no)
            | .balanced, _ => enclosedQueue_balanced n c a 0
            | .acting, selected => enclosedQueue_acting tally (quiet ⟨hb, he, .inl selected⟩)
            | .taking, _ => enclosedQueue_taking n c a 0
            | .dissipative, selected => nomatch hd.symm.trans selected
            | .embodied, _ => enclosedQueue_embodied n c a 0
            | .counted, _ => ⟨_, enclosedQueue_census n c a 0⟩
            | .transmitting, _ => ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩)
          ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩ _ (enclosedQueue_census n c a 0))
      | true, true, _ => match bounded ⟨hb, he, hd⟩ with
        | ⟨_, _, bound, _⟩ => pointwise (Queue.counts tally) (law (enclosedQueue n c a _)
            ((enclosedQueue_premised tally (quiet ⟨hb, he, .inl ha⟩) bound.from_zero).meets S)
            ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩ _ (enclosedQueue_census n c a _))
      | true, false, true => match bounded ⟨hb, he, hd⟩ with
        | ⟨_, _, bound, _⟩ => pointwise (Queue.counts tally) (law (enclosedQueue n c a _)
            ((enclosedQueue_premised tally (quiet ⟨hb, he, .inr ⟨ht, hd⟩⟩)
              bound.from_zero).meets S)
            ⟨0, fun t _ => enclosedQueue_enclosed tally t⟩ _ (enclosedQueue_census n c a _))
      | true, false, false => match bounded ⟨hb, he, hd⟩ with
        | ⟨T, K, bound, company⟩ => pointwise (Queue.counts tally)
            (law (closingQueue n c a (K + T) T)
              (fun
                | .dependent, _ => fun _ _ _ _ no => (nomatch no)
                | .balanced, _ => closingQueue_balanced n c a (K + T) T
                | .acting, selected => nomatch ha.symm.trans selected
                | .taking, selected => nomatch ht.symm.trans selected
                | .dissipative, _ => closingQueue_dissipative tally bound company
                | .embodied, _ => enclosedQueue_embodied n c a (K + T)
                | .counted, _ => ⟨_, enclosedQueue_census n c a (K + T)⟩
                | .transmitting, _ => ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩)
              ⟨T, fun _ later => closingQueue_enclosed tally later⟩ _
              (enclosedQueue_census n c a (K + T)))⟩

/-- So in worlds enclosed from some step on, a change bound from some step is a law of
counting under a selection exactly when the selection bounds change: a count growing by one
at each step is counted by an enclosed world meeting any other selection, and stays within
no bound (the fourteenth review's probe). -/
theorem enclosed_change_bound_iff (S : Premise → Bool) :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S →
      (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) →
        w.CountsObey fun n c a => ∃ T B, ChangeBound T B n c a) ↔ BoundsChange S :=
  have pointwise : Pointwise fun n (_ _ : Nat → Nat) => ∃ T B, ∀ t, T ≤ t → n t ≤ B :=
    fun same ⟨T, B, bounded⟩ => ⟨T, B, fun t later =>
      Nat.le_trans (Nat.le_of_eq (same t).1.symm) (bounded t later)⟩
  have growing : Tally (fun t => t + 1) (fun _ => 0) (fun _ => 1) := fun t => ⟨t + 1, rfl, rfl⟩
  ⟨fun law => if bounds : S .balanced = true ∧ S .embodied = true ∧ S .dissipative = true
      then bounds else
      match (enclosed_counting_under S pointwise).mpr
          (fun w _ meets enclosed alive census => match law w meets enclosed alive census with
            | ⟨T, B, bound⟩ => ⟨T, B, fun t later =>
                Nat.le_trans (Nat.le_add_right _ _) (bound t later)⟩)
          _ _ _ growing (fun _ t _ => Nat.zero_lt_succ t) (fun bound => absurd bound bounds) with
      | ⟨T, B, bounded⟩ => (Nat.not_succ_le_self B (Nat.le_trans
          (Nat.succ_le_succ (Nat.le_add_right B T)) (bounded (B + T) (Nat.le_add_left T B)))).elim,
   fun ⟨balanced, embodied, dissipative⟩ _ _ meets ⟨T, enclosed⟩ _ census =>
     ⟨T, _, enclosure_bounds_change census (meets _ embodied) (meets _ balanced)
       (meets _ dissipative) enclosed⟩⟩

end World

/-! ## Counting under each selection, in finite worlds -/

/-- Coming to be respects agreement at the step and after it. -/
theorem comesToBe_congr {p q : Nat → Prop} {t : Nat} (now : p t ↔ q t)
    (next : p (t + 1) ↔ q (t + 1)) : ComesToBe p t ↔ ComesToBe q t :=
  ⟨fun comes => ⟨fun holds => comes.1 (now.mpr holds), next.mp comes.2⟩,
   fun comes => ⟨fun holds => comes.1 (now.mp holds), next.mpr comes.2⟩⟩

/-- So does ceasing to be. -/
theorem ceasesToBe_congr {p q : Nat → Prop} {t : Nat} (now : p t ↔ q t)
    (next : p (t + 1) ↔ q (t + 1)) : CeasesToBe p t ↔ CeasesToBe q t :=
  ⟨fun ceases => ⟨now.mp ceases.1, fun holds => ceases.2 (next.mpr holds)⟩,
   fun ceases => ⟨now.mpr ceases.1, fun holds => ceases.2 (next.mp holds)⟩⟩

namespace Ring

/-- Members seated round a ring of `N` places in turn, the first at place `0`: the place of
the `k`th. -/
def slot (N : Nat) : Nat → Nat
  | 0 => 0
  | k + 1 => if slot N k + 1 < N then slot N k + 1 else 0

variable {N : Nat}

/-- The next member sits at the next place, or at the first once the ring is full. -/
theorem slot_step (N k : Nat) :
    (slot N (k + 1) = slot N k + 1 ∧ slot N k + 1 < N) ∨
      (slot N (k + 1) = 0 ∧ ¬ slot N k + 1 < N) :=
  if h : slot N k + 1 < N then .inl ⟨if_pos h, h⟩ else .inr ⟨if_neg h, h⟩

theorem slot_lt (pos : 0 < N) : ∀ k, slot N k < N
  | 0 => pos
  | k + 1 => match slot_step N k with
    | .inl ⟨same, below⟩ => Nat.lt_of_le_of_lt (Nat.le_of_eq same) below
    | .inr ⟨same, _⟩ => Nat.lt_of_le_of_lt (Nat.le_of_eq same) pos

/-- Fewer than `N` members on, the place is as many places on, or as many less a full
turn. -/
theorem slot_add (k : Nat) : ∀ {d : Nat}, d < N →
    slot N (k + d) = slot N k + d ∨ slot N (k + d) + N = slot N k + d
  | 0, _ => .inl rfl
  | d + 1, short =>
    have pos : 0 < N := Nat.lt_of_le_of_lt (Nat.zero_le _) short
    match slot_step N (k + d), slot_add k (Nat.lt_of_succ_lt short) with
    | .inl ⟨same, _⟩, .inl on => .inl (same.trans (congrArg (· + 1) on))
    | .inl ⟨same, _⟩, .inr round => .inr ((congrArg (· + N) same).trans
        ((Nat.add_right_comm _ 1 N).trans (congrArg (· + 1) round)))
    | .inr ⟨same, full⟩, on =>
      have turned : slot N (k + d) + 1 = N :=
        Nat.le_antisymm (slot_lt pos (k + d)) ((Nat.lt_or_ge _ _).resolve_left full)
      match on with
      | .inl on => .inr ((congrArg (· + N) same).trans ((Nat.zero_add N).trans
          (turned.symm.trans (congrArg (· + 1) on))))
      | .inr round => absurd (Nat.add_lt_add (slot_lt pos k) short)
          (Nat.not_lt_of_le (Nat.le_of_eq ((congrArg (· + N) turned).symm.trans
            ((Nat.add_right_comm _ 1 N).trans (congrArg (· + 1) round)))))

/-- Members fewer than a full turn apart sit at different places. -/
theorem slot_ne (k : Nat) {d : Nat} (pos : 0 < d) (short : d < N) :
    slot N (k + d) ≠ slot N k :=
  fun same => match slot_add k short with
  | .inl on => Nat.lt_irrefl (slot N k) (Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right pos)
      (Nat.le_of_eq (on.symm.trans same)))
  | .inr round => Nat.lt_irrefl (slot N k + d) (Nat.lt_of_lt_of_le
      (Nat.add_lt_add_left short _) (Nat.le_of_eq ((congrArg (· + N) same).symm.trans round)))

/-- A member later than another, both within `L ≤ N` members from `g`, sits apart from
it. -/
theorem slot_apart {g L j k : Nat} (fits : L ≤ N) (start : g ≤ j) (before : j < k)
    (within : k < g + L) : slot N k ≠ slot N j :=
  match le_dest (Nat.le_of_lt before) with
  | ⟨_, split⟩ =>
    have ahead : j + _ < j + L := Eq.subst (motive := (· < j + L)) split
      (Nat.lt_of_lt_of_le within (Nat.add_le_add_right start L))
    fun same => slot_ne j (Nat.lt_of_add_lt_add_left (n := j)
        (Eq.subst (motive := (j + 0 < ·)) split before))
      (Nat.lt_of_lt_of_le (Nat.lt_of_add_lt_add_left ahead) fits)
      (Eq.subst (motive := fun x => slot N x = slot N j) split same)

/-- Among at most `N` members in turn, members at one place are one. -/
theorem slot_inj {g L j k : Nat} (fits : L ≤ N) (first : g ≤ j ∧ j < g + L)
    (second : g ≤ k ∧ k < g + L) (same : slot N j = slot N k) : j = k :=
  match Nat.lt_or_ge j k with
  | .inl before => absurd same.symm (slot_apart fits first.1 before second.2)
  | .inr after => match Nat.lt_or_ge k j with
    | .inl before => absurd same (slot_apart fits second.1 before first.2)
    | .inr after' => Nat.le_antisymm after' after

/-- Room for the members in a queue before or after any step, where at most `M` are in it
at each. -/
def size (M : Nat) : Nat := M + M + 1

/-- The `k`th member's place on the ring. -/
def seat (M k : Nat) : Fin (size M) :=
  ⟨slot (size M) k, slot_lt (Nat.succ_pos _) k⟩

variable (n c : Nat → Nat) (M : Nat)

/-- The places held at step `t`: the queue's members, each at its place. -/
def seated (t : Nat) : List (Fin (size M)) :=
  (Queue.line n c t).map (seat M)

/-- Place `i` is held at step `t`. -/
def holds (i : Fin (size M)) (t : Nat) : Prop :=
  i ∈ seated n c M t

instance (i : Fin (size M)) (t : Nat) : Decidable (holds n c M i t) :=
  decideMem i _

/-- The queue seated round the ring, each place standing at `level` and active while
held. -/
def web (level : Nat → Fin (size M) → Nat) : Web (Fin (size M)) (Fin (size M)) where
  level := level
  active t i := holds n c M i t
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

/-- Each place stands exactly while it is held. -/
def stands (t : Nat) (i : Fin (size M)) : Nat :=
  mark (holds n c M i t)

/-- The front's place takes part at every step. It takes from each place what that place's
standing loses across the step and gives each what it gains. -/
def flow : Flow (Fin (size M)) (Fin (size M)) where
  present t := [seat M (Queue.gone c t)]
  take t _ i := stands n c M t i - stands n c M (t + 1) i
  give t _ i := stands n c M (t + 1) i - stands n c M t i

variable {n c M} {a : Nat → Nat}

/-- A place held means the queue is not empty. -/
theorem occupied {i : Fin (size M)} {t : Nat} (held : holds n c M i t) : 0 < n t :=
  match exists_of_mem_map held with
  | ⟨_, listed, _⟩ => OpenQueue.occupied ⟨steps_mem listed, steps_within listed⟩

/-- The front's place is held while the queue is not empty. -/
theorem front_holds {t : Nat} (pos : 0 < n t) : holds n c M (seat M (Queue.gone c t)) t :=
  mem_map_of (steps_of_within (OpenQueue.front.mpr pos).1 (OpenQueue.front.mpr pos).2)

/-- Where at most `M` are in the queue at each step, those in it before or after a step fit
on the ring. -/
theorem span_fits (tally : Tally n c a) (bounded : ∀ t, n t ≤ M) (t : Nat) :
    n t + a t ≤ size M :=
  match tally t with
  | ⟨_, _, after⟩ => Nat.le_succ_of_le (Nat.add_le_add (bounded t) (Nat.le_trans
      (Nat.le_add_left _ _) (Nat.le_trans (Nat.le_of_eq after.symm) (bounded (t + 1)))))

/-- A member in the span of the step from `t` holds its place at a step whose queue lies in
the span exactly when it is in the queue then. -/
theorem holds_iff (tally : Tally n c a) (bounded : ∀ t, n t ≤ M) {t k s : Nat}
    (spanned : k ∈ EnclosedQueue.span n c a t)
    (inside : ∀ j, Queue.holds n c j s → j ∈ EnclosedQueue.span n c a t) :
    holds n c M (seat M k) s ↔ Queue.holds n c k s :=
  ⟨fun held => match exists_of_mem_map held with
    | ⟨j, listed, same⟩ =>
      have member : Queue.holds n c j s := ⟨steps_mem listed, steps_within listed⟩
      have there := inside j member
      Eq.subst (motive := fun x => Queue.holds n c x s)
        (slot_inj (span_fits tally bounded t) ⟨steps_mem there, steps_within there⟩
          ⟨steps_mem spanned, steps_within spanned⟩ (congrArg Fin.val same)) member,
   fun holds => mem_map_of (steps_of_within holds.1 holds.2)⟩

/-- The ring lists the places held at each step, each once. -/
theorem census (bounded : ∀ t, n t ≤ M) (level : Nat → Fin (size M) → Nat) :
    (web n c M level).Census (seated n c M) :=
  fun t => ⟨distinct_map_on (fun _ _ first second same =>
      slot_inj (Nat.le_succ_of_le (Nat.le_trans (bounded t) (Nat.le_add_right M M)))
        ⟨steps_mem first, steps_within first⟩ ⟨steps_mem second, steps_within second⟩
        (congrArg Fin.val same)) (steps_distinct _ _), fun _ => Iff.rfl⟩

/-- Where at most `M` are in the queue at each step, the ring counts what the queue
counts. -/
theorem counts (tally : Tally n c a) (bounded : ∀ t, n t ≤ M) (t : Nat) :
    (seated n c M t).length = n t ∧ ceasings (seated n c M t) (holds n c M) t = c t ∧
      comings (seated n c M (t + 1)) (holds n c M) t = a t :=
  have now : ∀ j, Queue.holds n c j t → j ∈ EnclosedQueue.span n c a t :=
    fun _ holds => EnclosedQueue.within_span tally (.inl holds)
  have next : ∀ j, Queue.holds n c j (t + 1) → j ∈ EnclosedQueue.span n c a t :=
    fun _ holds => EnclosedQueue.within_span tally (.inr holds)
  ⟨(total_ones _).symm.trans ((total_map _ _ _).trans ((total_ones _).trans (steps_length _ _))),
   (total_map _ _ _).trans ((total_congr_on fun k listed =>
      have spanned := now k ⟨steps_mem listed, steps_within listed⟩
      mark_iff (ceasesToBe_congr (holds_iff tally bounded spanned now)
        (holds_iff tally bounded spanned next))).trans (Queue.ceasings_eq tally t)),
   (total_map _ _ _).trans ((total_congr_on fun k listed =>
      have spanned := next k ⟨steps_mem listed, steps_within listed⟩
      mark_iff (comesToBe_congr (holds_iff tally bounded spanned now)
        (holds_iff tally bounded spanned next))).trans (Queue.comings_eq tally t))⟩

/-- What the front takes from a place, the place held before the step. -/
theorem taken_held {t : Nat} {f i : Fin (size M)} (takes : 0 < (flow n c M).take t f i) :
    holds n c M i t :=
  mark_pos.mp (Nat.lt_of_lt_of_le takes (Nat.sub_le _ _))

/-- What the front gives to a place, the place held after the step. -/
theorem given_held {t : Nat} {f i : Fin (size M)} (gives : 0 < (flow n c M).give t f i) :
    holds n c M i (t + 1) :=
  mark_pos.mp (Nat.lt_of_lt_of_le gives (Nat.sub_le _ _))

end Ring

/-- From the step after it arises, the lone relatum is all there is and nothing changes. -/
theorem Queue.lone_settles : ChangeBound 1 1 Queue.lone (fun _ => 0) Queue.joins :=
  have still : ∀ t, occurrences 1 (fun s => 0 + Queue.joins s) t = 0 := fun t =>
    Nat.rec (motive := fun t => occurrences 1 (fun s => 0 + Queue.joins s) t = 0) rfl
      (fun t same => (congrArg (· + _) same).trans ((Nat.zero_add _).trans
        (mark_zero (p := 1 ≤ t ∧ 0 < 0 + Queue.joins t) fun ⟨later, pos⟩ =>
          match t, later, pos with
          | 0, later, _ => Nat.not_succ_le_zero 0 later
          | _ + 1, _, pos => Nat.lt_irrefl 0 pos))) t
  fun t later => match t, later with
  | 0, later => absurd later (Nat.not_succ_le_zero 0)
  | t + 1, _ => Nat.le_of_eq (congrArg (1 + ·) (still (t + 1)))

namespace World

/-- A queue seated round a ring of places, with nothing standing or flowing. -/
def ring (n c : Nat → Nat) (M : Nat) : World :=
  ⟨Fin (Ring.size M), Flow.still, Ring.web n c M fun _ _ => 0⟩

/-- The same ring, each place standing exactly while it is held, with nothing flowing. -/
def embodiedRing (n c : Nat → Nat) (M : Nat) : World :=
  ⟨Fin (Ring.size M), Flow.still, Ring.web n c M (Ring.stands n c M)⟩

/-- The same ring, its front's place taking what each place's standing loses and giving what
it gains. -/
def balancedRing (n c : Nat → Nat) (M : Nat) : World :=
  ⟨Fin (Ring.size M), Ring.flow n c M, Ring.web n c M (Ring.stands n c M)⟩

instance ring_decided (n c : Nat → Nat) (M : Nat) :
    ∀ t x, Decidable ((ring n c M).web.active t x) :=
  fun t i => inferInstanceAs (Decidable (Ring.holds n c M i t))

instance embodiedRing_decided (n c : Nat → Nat) (M : Nat) :
    ∀ t x, Decidable ((embodiedRing n c M).web.active t x) :=
  fun t i => inferInstanceAs (Decidable (Ring.holds n c M i t))

instance balancedRing_decided (n c : Nat → Nat) (M : Nat) :
    ∀ t x, Decidable ((balancedRing n c M).web.active t x) :=
  fun t i => inferInstanceAs (Decidable (Ring.holds n c M i t))

variable {n c a : Nat → Nat} {M : Nat}

/-- Where at most `M` are in the queue at each step, the ring meets every premise but
embodiment. -/
theorem ring_premised (bounded : ∀ t, n t ≤ M) :
    (ring n c M).Dependent ∧ (ring n c M).Balanced ∧ (ring n c M).Acting ∧
      (ring n c M).Taking ∧ (ring n c M).Dissipative ∧ (ring n c M).Counted ∧
      (ring n c M).Transmitting :=
  ⟨fun _ _ _ _ no => (nomatch no), fun _ _ => rfl, (still_vacuous _).1, (still_vacuous _).2.1,
   (still_vacuous _).2.2.1, ⟨_, Ring.census bounded _⟩, (still_vacuous _).2.2.2⟩

/-- And the embodied ring every premise but balance. -/
theorem embodiedRing_premised (bounded : ∀ t, n t ≤ M) :
    (embodiedRing n c M).Dependent ∧ (embodiedRing n c M).Acting ∧
      (embodiedRing n c M).Taking ∧ (embodiedRing n c M).Dissipative ∧
      (embodiedRing n c M).Embodied ∧ (embodiedRing n c M).Counted ∧
      (embodiedRing n c M).Transmitting :=
  ⟨fun _ _ _ _ no => (nomatch no), (still_vacuous _).1, (still_vacuous _).2.1,
   (still_vacuous _).2.2.1, fun _ _ => mark_pos.symm, ⟨_, Ring.census bounded _⟩,
   (still_vacuous _).2.2.2⟩

/-- The balanced ring meets every premise but dissipation and only active relata giving. -/
theorem balancedRing_holds (bounded : ∀ t, n t ≤ M) :
    (balancedRing n c M).Dependent ∧ (balancedRing n c M).Balanced ∧
      (balancedRing n c M).Taking ∧ (balancedRing n c M).Embodied ∧
      (balancedRing n c M).Counted ∧ (balancedRing n c M).Transmitting :=
  ⟨fun _ _ _ _ no => (nomatch no),
   fun t i => add_sub_turn (Ring.stands n c M t i) (Ring.stands n c M (t + 1) i),
   fun _ f _ present takes => match f, present, takes with
    | _, .head _, takes => ⟨Ring.front_holds (Ring.occupied
        (Ring.taken_held takes)), trivial⟩
    | _, .tail _ no, _ => (nomatch no),
   fun _ _ => mark_pos.symm, ⟨_, Ring.census bounded _⟩,
   ⟨0, fun _ _ _ _ _ no => (nomatch no)⟩⟩

/-- Where nothing joins an empty queue, only active relata give in the balanced ring. -/
theorem balancedRing_acting (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) :
    (balancedRing n c M).Acting :=
  fun t f _ present gives => match f, present, gives with
    | _, .head _, gives => Ring.front_holds (match Nat.eq_zero_or_pos (n t) with
      | .inl empty => absurd (Ring.occupied (Ring.given_held gives)) fun pos =>
          Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le pos (Nat.le_of_eq
            (EnclosedQueue.empty_stays tally (company t) empty)))
      | .inr pos => pos)
    | _, .tail _ no, _ => (nomatch no)

/-- A ring meets every selection without embodiment. -/
theorem ring_meets (bounded : ∀ t, n t ≤ M) {S : Premise → Bool} (free : S .embodied = false) :
    (ring n c M).Meets S :=
  match ring_premised bounded with
  | ⟨dependent, balanced, acting, taking, dissipative, counted, transmitting⟩ => fun
    | .dependent, _ => dependent
    | .balanced, _ => balanced
    | .acting, _ => acting
    | .taking, _ => taking
    | .dissipative, _ => dissipative
    | .embodied, selected => nomatch free.symm.trans selected
    | .counted, _ => counted
    | .transmitting, _ => transmitting

/-- An embodied ring meets every selection without balance. -/
theorem embodiedRing_meets (bounded : ∀ t, n t ≤ M) {S : Premise → Bool}
    (free : S .balanced = false) : (embodiedRing n c M).Meets S :=
  match embodiedRing_premised bounded with
  | ⟨dependent, acting, taking, dissipative, embodied, counted, transmitting⟩ => fun
    | .dependent, _ => dependent
    | .balanced, selected => nomatch free.symm.trans selected
    | .acting, _ => acting
    | .taking, _ => taking
    | .dissipative, _ => dissipative
    | .embodied, _ => embodied
    | .counted, _ => counted
    | .transmitting, _ => transmitting

/-- A balanced ring meets every selection without dissipation, where it selects only active
relata giving only if nothing joins an empty queue. -/
theorem balancedRing_meets (tally : Tally n c a) (bounded : ∀ t, n t ≤ M) {S : Premise → Bool}
    (giving : S .acting = true → ∀ t, 0 < a t → 0 < n t) (free : S .dissipative = false) :
    (balancedRing n c M).Meets S :=
  match balancedRing_holds (c := c) bounded with
  | ⟨dependent, balanced, taking, embodied, counted, transmitting⟩ => fun
    | .dependent, _ => dependent
    | .balanced, _ => balanced
    | .acting, selected => balancedRing_acting tally (giving selected)
    | .taking, _ => taking
    | .dissipative, selected => nomatch free.symm.trans selected
    | .embodied, _ => embodied
    | .counted, _ => counted
    | .transmitting, _ => transmitting

/-- The laws of counting under each selection of the premises, in finite worlds. A property
of the counts holds of every census of every finite world meeting the selection exactly when
it holds of every tally that meets three conditions: at most some number are active at each
step; where the selection binds counting or bounds change, nothing arises across a step at
which nothing is active; where it bounds change, change stays within a bound from the first
step. Every step of a finite world is enclosed (`Finite.enclosed`), so dissipation with
balance and embodiment binds counting there by itself (`enclosed_binds_counting`). -/
theorem finite_counting_under (S : Premise → Bool)
    {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop} (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (∃ M, ∀ t, n t ≤ M) →
      (BindsCounting S ∨ BoundsChange S → ∀ t, 0 < a t → 0 < n t) →
      (BoundsChange S → ∃ B, ChangeBound 0 B n c a) → Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
        w.CountsObey Q :=
  ⟨fun law w _ meets finite alive census => law _ _ _ census.tally
    (match finite.census_bounded with
      | ⟨M, bounded⟩ => ⟨M, bounded alive census⟩)
    (fun
      | .inl ⟨balanced, embodied, .inl acting⟩ => counting_binds_jointly.1 w (meets _ balanced)
          (meets _ acting) (Embodied.arising (meets _ embodied)) alive census
      | .inl ⟨balanced, embodied, .inr ⟨_, dissipative⟩⟩ | .inr ⟨balanced, embodied, dissipative⟩ =>
          fun t arising => enclosed_binds_counting w (meets _ balanced) (meets _ dissipative)
            (meets _ embodied) census (finite.enclosed t) arising)
    (fun ⟨balanced, embodied, dissipative⟩ => ⟨_, enclosure_bounds_change census
      (meets _ embodied) (meets _ balanced) (meets _ dissipative) fun t _ => finite.enclosed t⟩),
   fun law n c _ tally ⟨M, bounded⟩ quiet bounds =>
    match hb : S .balanced, he : S .embodied with
    | false, _ => pointwise (Ring.counts tally bounded) (law (embodiedRing n c M)
        (embodiedRing_meets bounded hb) (places_listed _) _ (Ring.census bounded _))
    | true, false => pointwise (Ring.counts tally bounded) (law (ring n c M)
        (ring_meets bounded he) (places_listed _) _ (Ring.census bounded _))
    | true, true => match hd : S .dissipative with
      | false => pointwise (Ring.counts tally bounded) (law (balancedRing n c M)
          (balancedRing_meets tally bounded (fun ha => quiet (.inl ⟨hb, he, .inl ha⟩)) hd)
          (places_listed _) _ (Ring.census bounded _))
      | true => match bounds ⟨hb, he, hd⟩ with
        | ⟨_, bound⟩ => pointwise (finiteQueue_counts tally bound) (law (finiteQueue _ _ _ _)
            ((finiteQueue_premised tally (quiet (.inr ⟨hb, he, hd⟩)) bound).meets S)
            (finiteQueue_finite _ _ _ _) _ (finiteQueue_census _ _ _ _))⟩

/-- So in finite worlds, nothing arising across a step at which nothing is active is a law of
counting under a selection exactly when the selection selects balance and embodiment, and
only active relata giving or dissipation. -/
theorem finite_counting_binds_iff (S : Premise → Bool) :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
      w.CountsObey fun n _ a => ∀ t, 0 < a t → 0 < n t) ↔ BindsCounting S ∨ BoundsChange S :=
  have pointwise : Pointwise fun n (_ : Nat → Nat) a => ∀ t, 0 < a t → 0 < n t :=
    fun same law t pos => Nat.lt_of_lt_of_le (law t (Nat.lt_of_lt_of_le pos
      (Nat.le_of_eq (same t).2.2.symm))) (Nat.le_of_eq (same t).1)
  have unbound : ¬ (BindsCounting S ∨ BoundsChange S) → ¬ ∀ (w : World)
      [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
        w.CountsObey fun n _ a => ∀ t, 0 < a t → 0 < n t := fun free law =>
    Nat.lt_irrefl 0 ((finite_counting_under S pointwise).mpr law _ _ _ Queue.lone_tally
      ⟨1, fun | 0 => Nat.zero_le 1 | _ + 1 => Nat.le_refl 1⟩
      (fun binds => absurd binds free) (fun bounds => absurd (.inr bounds) free)
      0 Nat.zero_lt_one)
  ⟨fun law => match hb : S .balanced, he : S .embodied, ha : S .acting,
      hd : S .dissipative with
    | true, true, true, _ => .inl ⟨hb, he, .inl ha⟩
    | true, true, false, true => .inr ⟨hb, he, hd⟩
    | false, _, _, _ => absurd law (unbound fun
        | .inl binds => nomatch hb.symm.trans binds.1
        | .inr bounds => nomatch hb.symm.trans bounds.1)
    | true, false, _, _ => absurd law (unbound fun
        | .inl binds => nomatch he.symm.trans binds.2.1
        | .inr bounds => nomatch he.symm.trans bounds.2.1)
    | true, true, false, false => absurd law (unbound fun
        | .inl ⟨_, _, .inl acting⟩ => nomatch ha.symm.trans acting
        | .inl ⟨_, _, .inr ⟨_, dissipative⟩⟩ => nomatch hd.symm.trans dissipative
        | .inr ⟨_, _, dissipative⟩ => nomatch hd.symm.trans dissipative),
   fun binds => (finite_counting_under S pointwise).mp fun _ _ _ _ _ quiet _ => quiet binds⟩

/-- And a change bound from the first step is a law of counting in finite worlds under a
selection exactly when the selection bounds change: one member replaced at every step is
counted by a finite world meeting any other selection. -/
theorem finite_change_bound_iff (S : Premise → Bool) :
    (∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
      w.CountsObey fun n c a => ∃ B, ChangeBound 0 B n c a) ↔ BoundsChange S :=
  have replaced : Tally (fun _ => 1) (fun _ => 1) (fun _ => 1) := fun _ => ⟨0, rfl, rfl⟩
  have bounded : ∀ t, (fun _ => 1 : Nat → Nat) t ≤ 1 := fun _ => Nat.le_refl 1
  have recurring : ¬ ∃ B, ChangeBound 0 B
      (fun t => (Ring.seated (fun _ => 1) (fun _ => 1) 1 t).length)
      (fun t => ceasings (Ring.seated (fun _ => 1) (fun _ => 1) 1 t)
        (Ring.holds (fun _ => 1) (fun _ => 1) 1) t)
      (fun t => comings (Ring.seated (fun _ => 1) (fun _ => 1) 1 (t + 1))
        (Ring.holds (fun _ => 1) (fun _ => 1) 1) t) :=
    fun ⟨_, bound⟩ => bound.not_recurring fun N => ⟨N, Nat.le_refl N,
      Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_trans
        (Nat.le_of_eq (Ring.counts replaced bounded N).2.1.symm) (Nat.le_add_right _ _))⟩
  ⟨fun law => match hb : S .balanced, he : S .embodied, hd : S .dissipative with
    | true, true, true => ⟨hb, he, hd⟩
    | false, _, _ => absurd (law (embodiedRing _ _ 1) (embodiedRing_meets bounded hb)
        (places_listed _) _ (Ring.census bounded _)) recurring
    | true, false, _ => absurd (law (ring _ _ 1) (ring_meets bounded he)
        (places_listed _) _ (Ring.census bounded _)) recurring
    | true, true, false => absurd (law (balancedRing _ _ 1)
        (balancedRing_meets replaced bounded (fun _ _ _ => Nat.zero_lt_one) hd)
        (places_listed _) _ (Ring.census bounded _)) recurring,
   fun ⟨balanced, embodied, dissipative⟩ _ _ meets finite _ census =>
    ⟨_, enclosure_bounds_change census (meets _ embodied) (meets _ balanced)
      (meets _ dissipative) fun t _ => finite.enclosed t⟩⟩

/-- Finite worlds and worlds enclosed from some step on have the same laws of counting under a
selection exactly when it bounds change and binds counting: there a change bound from some
step is one from the first step (`ChangeBound.from_zero`) and bounds the count. Where the
selection does not bound change, a count growing without end is counted in a world enclosed
at every step and in no finite world; where it bounds change without binding counting, one
relatum arising from none before enclosure is counted in an enclosed world and in no finite
world. -/
theorem enclosed_iff_finite_counting_under (S : Premise → Bool) :
    (∀ Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop, Pointwise Q →
      ((∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S →
          (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q) ↔
        ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
          w.CountsObey Q)) ↔
      BoundsChange S ∧ BindsCounting S :=
  have growing : ¬ BoundsChange S → ¬ ∀ Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop,
      Pointwise Q → ((∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S →
          (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q) ↔
        ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
          w.CountsObey Q) := fun free law =>
    have pointwise : Pointwise fun n (_ _ : Nat → Nat) => ∃ M, ∀ t, n t ≤ M :=
      fun same ⟨M, bounded⟩ => ⟨M, fun t => Nat.le_trans (Nat.le_of_eq (same t).1.symm)
        (bounded t)⟩
    match (enclosed_counting_under S pointwise).mpr ((law _ pointwise).mpr
        fun _ _ _ finite alive census => match finite.census_bounded with
          | ⟨M, bounded⟩ => ⟨M, bounded alive census⟩)
        (fun t => t + 1) (fun _ => 0) (fun _ => 1) (fun t => ⟨t + 1, rfl, rfl⟩)
        (fun _ _ _ => Nat.succ_pos _) (fun bounds => absurd bounds free) with
    | ⟨M, bounded⟩ => Nat.lt_irrefl M (bounded M)
  have arising : BoundsChange S → ¬ BindsCounting S → ¬ ∀ Q : (Nat → Nat) → (Nat → Nat) →
      (Nat → Nat) → Prop, Pointwise Q →
      ((∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S →
          (∃ T, ∀ t, T ≤ t → w.flow.Enclosed t) → w.CountsObey Q) ↔
        ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Meets S → w.Finite →
          w.CountsObey Q) := fun bounds free law =>
    have pointwise : Pointwise fun n (_ : Nat → Nat) a => ∀ t, 0 < a t → 0 < n t :=
      fun same law t pos => Nat.lt_of_lt_of_le (law t (Nat.lt_of_lt_of_le pos
        (Nat.le_of_eq (same t).2.2.symm))) (Nat.le_of_eq (same t).1)
    Nat.lt_irrefl 0 ((enclosed_counting_under S pointwise).mpr ((law _ pointwise).mpr
        ((finite_counting_binds_iff S).mpr (.inr bounds))) _ _ _ Queue.lone_tally
      (fun binds => absurd binds free)
      (fun _ => ⟨1, 1, Queue.lone_settles, fun t later pos => match t, later, pos with
        | 0, later, _ => absurd later (Nat.not_succ_le_zero 0)
        | _ + 1, _, pos => absurd pos (Nat.lt_irrefl 0)⟩)
      0 Nat.zero_lt_one)
  ⟨fun law => match hb : S .balanced, he : S .embodied, hd : S .dissipative, ha : S .acting,
      ht : S .taking with
    | true, true, true, true, _ => ⟨⟨hb, he, hd⟩, ⟨hb, he, .inl ha⟩⟩
    | true, true, true, false, true => ⟨⟨hb, he, hd⟩, ⟨hb, he, .inr ⟨ht, hd⟩⟩⟩
    | true, true, true, false, false => absurd law (arising ⟨hb, he, hd⟩ fun
        | ⟨_, _, .inl acting⟩ => nomatch ha.symm.trans acting
        | ⟨_, _, .inr ⟨taking, _⟩⟩ => nomatch ht.symm.trans taking)
    | false, _, _, _, _ => absurd law (growing fun bounds => nomatch hb.symm.trans bounds.1)
    | true, false, _, _, _ => absurd law (growing fun bounds => nomatch he.symm.trans bounds.2.1)
    | true, true, false, _, _ =>
      absurd law (growing fun bounds => nomatch hd.symm.trans bounds.2.2),
   fun ⟨bounds, binds⟩ _ pointwise => (enclosed_counting_under S pointwise).symm.trans
    (Iff.trans ⟨fun law n c a tally _ quiet bounded => law n c a tally (fun _ => quiet (.inl binds))
        fun _ => match bounded bounds with
          | ⟨_, bound⟩ => ⟨0, _, bound, fun t _ => quiet (.inl binds) t⟩,
      fun law n c a tally quiet bounded => match bounded bounds with
        | ⟨_, _, bound, _⟩ => law n c a tally ⟨_, fun t => Nat.le_trans (Nat.le_add_right _ _)
            (bound.from_zero t (Nat.zero_le t))⟩ (fun _ => quiet binds)
            (fun _ => ⟨_, bound.from_zero⟩)⟩
      (finite_counting_under S pointwise))⟩

end World

/-! ## Counting where every premise binds -/

namespace EnclosedQueue

/-- A member stands at one, and at most `s` more. -/
theorem place_le (g m s k : Nat) : place g m s k ≤ 1 + s :=
  if h : g ≤ k ∧ k < g + m then
    Nat.le_trans (Nat.le_of_eq (if_pos h)) (Nat.add_le_add_left
      (if front : k = g then Nat.le_of_eq (if_pos front)
       else Nat.le_trans (Nat.le_of_eq (if_neg front)) (Nat.zero_le s)) 1)
  else Nat.le_trans (Nat.le_of_eq (if_neg h)) (Nat.zero_le _)

/-- A queue stands at most at its length, and `s` more. -/
theorem total_place_le (g m s : Nat) : total (steps g m) (place g m s) ≤ m + s :=
  match m with
  | 0 => Nat.zero_le _
  | _ + 1 => Nat.le_of_eq (total_place g _ s)

/-- A queue not empty stands at its length, and `s` more at its front. -/
theorem total_place_pos {g m : Nat} (s : Nat) (occupied : 0 < m) :
    total (steps g m) (place g m s) = m + s :=
  match m, occupied with
  | _ + 1, _ => total_place g _ s

end EnclosedQueue

namespace OnceClosedQueue

variable (n c : Nat → Nat) (T E : Nat)

/-- What the front stands at beyond one: `E` at step `T`, nothing at any other step. -/
def excess (t : Nat) : Nat :=
  if t = T then E else 0

/-- Members stand by their place in the queue, the front `E` more at step `T`. -/
def level (t k : Nat) : Nat :=
  EnclosedQueue.place (Queue.gone c t) (n t) (excess T E t) k

/-- Across every step but `T` at which the queue is not empty, one unit is exchanged each
way. -/
def exchange (t : Nat) : Nat :=
  mark (0 < n t ∧ ¬ t = T)

/-- Members are active exactly while in the queue. Every relatum depends on every relatum,
needing what it stands at. -/
def web : Web Nat Nat where
  level := level n c T E
  active t k := Queue.holds n c k t
  requires _ _ _ := True
  need t _ k := level n c T E t k
  draws _ _ _ := True

/-- The front takes part at every step. It takes from each member what that member's
standing loses across the step and gives each what it gains, and across every step but `T` at
which the queue is not empty it exchanges one unit more each way with every relatum. -/
def flow : Flow Nat Nat where
  present t := [Queue.gone c t]
  take t _ k := level n c T E t k - level n c T E (t + 1) k + exchange n T t
  give t _ k := level n c T E (t + 1) k - level n c T E t k + exchange n T t

variable {n c a : Nat → Nat} {T E : Nat}

theorem excess_le (t : Nat) : excess T E t ≤ E :=
  if same : t = T then Nat.le_of_eq (if_pos same)
  else Nat.le_trans (Nat.le_of_eq (if_neg same)) (Nat.zero_le E)

/-- No member stands at more than one and the excess. -/
theorem level_le (t k : Nat) : level n c T E t k ≤ 1 + E :=
  Nat.le_trans (EnclosedQueue.place_le _ _ _ k) (Nat.add_le_add_left (excess_le t) 1)

/-- Where a member's standing does not change and nothing is exchanged, the front neither
takes from nor gives to it. -/
theorem still_flows {t k f : Nat} (same : level n c T E (t + 1) k = level n c T E t k)
    (shut : exchange n T t = 0) :
    (flow n c T E).take t f k = 0 ∧ (flow n c T E).give t f k = 0 :=
  ⟨((congrArg (level n c T E t k - · + exchange n T t) same).trans
      (congrArg (level n c T E t k - level n c T E t k + ·) shut)).trans (Nat.sub_self _),
   ((congrArg (· - level n c T E t k + exchange n T t) same).trans
      (congrArg (level n c T E t k - level n c T E t k + ·) shut)).trans (Nat.sub_self _)⟩

theorem still {t k f : Nat}
    (flows : (flow n c T E).take t f k = 0 ∧ (flow n c T E).give t f k = 0) :
    ¬ (0 < (flow n c T E).take t f k ∨ 0 < (flow n c T E).give t f k)
  | .inl takes => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le takes (Nat.le_of_eq flows.1))
  | .inr gives => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le gives (Nat.le_of_eq flows.2))

/-- Across a step from an empty queue nothing is taken or given. -/
theorem idle (tally : Tally n c a) {t : Nat} (company : 0 < a t → 0 < n t)
    (empty : n t = 0) (k f : Nat) :
    (flow n c T E).take t f k = 0 ∧ (flow n c T E).give t f k = 0 :=
  still_flows ((EnclosedQueue.place_zero (EnclosedQueue.outside_empty
      (EnclosedQueue.empty_stays tally company empty))).trans
      (EnclosedQueue.place_zero (EnclosedQueue.outside_empty empty)).symm)
    (mark_zero fun ⟨occupied, _⟩ =>
      Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le occupied (Nat.le_of_eq empty)))

/-- Something taken or given means the queue is not empty. -/
theorem busy (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) {t k f : Nat}
    (moves : 0 < (flow n c T E).take t f k ∨ 0 < (flow n c T E).give t f k) : 0 < n t :=
  match Nat.eq_zero_or_pos (n t) with
  | .inl empty => absurd moves (still (idle tally (company t) empty k f))
  | .inr occupied => occupied

/-- Across a step at which nothing is exchanged, whatever the front takes from or gives to
lies in the span. -/
theorem moving_within (tally : Tally n c a) {t k f : Nat} (shut : exchange n T t = 0)
    (moves : 0 < (flow n c T E).take t f k ∨ 0 < (flow n c T E).give t f k) :
    k ∈ EnclosedQueue.span n c a t :=
  if now : Queue.holds n c k t then EnclosedQueue.within_span tally (.inl now)
  else if next : Queue.holds n c k (t + 1) then EnclosedQueue.within_span tally (.inr next)
  else absurd moves (still (still_flows ((EnclosedQueue.place_zero next).trans
    (EnclosedQueue.place_zero now).symm) shut))

/-- Such a step is enclosed by its span. -/
theorem closed (tally : Tally n c a) {t : Nat} (shut : exchange n T t = 0) :
    (flow n c T E).ClosedAt (EnclosedQueue.span n c a t) t :=
  fun _ _ _ out => ⟨eq_zero_of_not_pos fun takes => out (moving_within tally shut (.inl takes)),
    eq_zero_of_not_pos fun gives => out (moving_within tally shut (.inr gives))⟩

/-- Activity needing support holds in its web whatever is active: each need is the level of
what is needed (the fourteenth review's probe). -/
theorem dependent_any_activity (active : Nat → Nat → Prop) :
    ({ web n c T E with active } : Web Nat Nat).Dependent :=
  fun _ _ _ _ _ => Nat.le_refl _

/-- And every flow transmits each dependence within one and the excess, the levels being
bounded by it. So in this witness activity needing support and bounded transmission bind
only in that their conditions have instances: they exclude no activity and no exchange. -/
theorem transmits_any_flow (L : Flow Nat Nat) (k : Nat) :
    L.TransmitsWithin (web n c T E) k (1 + E) :=
  fun t _ _ _ _ => ⟨trivial, Nat.le_trans (level_le (t + 1) k) (Nat.le_add_left _ _)⟩

/-- Across every other step at which the queue is not empty, no family is closed. -/
theorem not_closed {t : Nat} (occupied : 0 < n t) (other : ¬ t = T) (cs : List Nat) :
    ¬ (flow n c T E).ClosedAt cs t :=
  fun closed => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le Nat.zero_lt_one
    (Nat.le_trans (Nat.le_of_eq (mark_one ⟨occupied, other⟩).symm) (Nat.le_add_left _ _)))
    (Nat.le_of_eq (closed _ (.head _) (beyond cs) (beyond_not_mem cs)).1))

end OnceClosedQueue

namespace World

/-- A queue closed once: open across every step but `T` at which it is not empty; across
`T` its front, standing `E` more, exchanges only within the queue and loses that excess. -/
def onceClosedQueue (n c : Nat → Nat) (T E : Nat) : World :=
  ⟨Nat, OnceClosedQueue.flow n c T E, OnceClosedQueue.web n c T E⟩

instance onceClosedQueue_decided (n c : Nat → Nat) (T E : Nat) :
    ∀ t x, Decidable ((onceClosedQueue n c T E).web.active t x) :=
  fun t k => inferInstanceAs (Decidable (Queue.holds n c k t))

/-- The census of a queue closed once is the queue. -/
theorem onceClosedQueue_census (n c : Nat → Nat) (T E : Nat) :
    (onceClosedQueue n c T E).web.Census (Queue.line n c) :=
  Queue.listed

theorem onceClosedQueue_embodied (n c : Nat → Nat) (T E : Nat) :
    (onceClosedQueue n c T E).Embodied :=
  fun _ _ => EnclosedQueue.place_pos

theorem onceClosedQueue_balanced (n c : Nat → Nat) (T E : Nat) :
    (onceClosedQueue n c T E).Balanced :=
  fun t k => add_sub_turn_add (OnceClosedQueue.level n c T E t k)
    (OnceClosedQueue.level n c T E (t + 1) k) (OnceClosedQueue.exchange n T t)

variable {n c a : Nat → Nat} {T E : Nat}

theorem onceClosedQueue_acting (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) :
    (onceClosedQueue n c T E).Acting :=
  fun _ f _ present gives => match f, present, gives with
    | _, .head _, gives => OpenQueue.front.mpr (OnceClosedQueue.busy tally company (.inr gives))
    | _, .tail _ no, _ => (nomatch no)

theorem onceClosedQueue_taking (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t) :
    (onceClosedQueue n c T E).Taking :=
  fun _ f _ present takes => match f, present, takes with
    | _, .head _, takes =>
      ⟨OpenQueue.front.mpr (OnceClosedQueue.busy tally company (.inl takes)), trivial⟩
    | _, .tail _ no, _ => (nomatch no)

/-- Across step `T`, with the queue not empty and its front standing more than join across
the step, the front takes from the span more than it gives: what stands falls. -/
theorem onceClosedQueue_exceeds (tally : Tally n c a) {t : Nat} (same : t = T)
    (occupied : 0 < n t) (excess : a t < E) (f : Nat) :
    total (EnclosedQueue.span n c a t) ((onceClosedQueue n c T E).flow.give t f) + 1 ≤
      total (EnclosedQueue.span n c a t) ((onceClosedQueue n c T E).flow.take t f) :=
  have census := onceClosedQueue_census n c T E
  have standing := standingCensus census (onceClosedQueue_embodied n c T E)
  have before := standing.stock_eq (EnclosedQueue.span_distinct t) fun k mem =>
    EnclosedQueue.within_span tally (.inl (((census t).2 k).mpr mem))
  have after := standing.stock_eq (t := t + 1) (EnclosedQueue.span_distinct t) fun k mem =>
    EnclosedQueue.within_span tally (.inr (((census (t + 1)).2 k).mpr mem))
  have full : (onceClosedQueue n c T E).web.stock (Queue.line n c t) t = n t + E :=
    (EnclosedQueue.total_place_pos _ occupied).trans (congrArg (n t + ·) (if_pos same))
  have spent : (onceClosedQueue n c T E).web.stock (Queue.line n c (t + 1)) (t + 1) ≤ n (t + 1) :=
    Nat.le_trans (EnclosedQueue.total_place_le _ _ _) (Nat.le_of_eq (congrArg (n (t + 1) + ·)
      (if_neg fun later => Nat.succ_ne_self t (later.trans same.symm))))
  have grows : n (t + 1) + 1 ≤ n t + E :=
    Nat.le_trans (Nat.add_le_add_right (Nat.le_trans (Nat.le_add_right _ (c t))
      (Nat.le_of_eq (tally.balance t))) 1)
      (Nat.le_trans (Nat.le_of_eq (Nat.add_assoc _ _ _)) (Nat.add_le_add_left excess _))
  have lowered := Nat.le_trans (Nat.add_le_add_right (Nat.le_trans (Nat.le_of_eq after.symm)
      spent) 1) (Nat.le_trans grows (Nat.le_of_eq (full.symm.trans before)))
  have over := (onceClosedQueue_balanced n c T E).over (EnclosedQueue.span n c a t) t
  le_of_add_le_add_right _ (Nat.le_trans (Nat.le_of_eq ((Nat.add_assoc _ _ _).trans
    (congrArg (_ + ·) (Nat.add_comm _ _)))) (Nat.le_trans (Nat.add_le_add_left lowered _)
      (Nat.le_of_eq ((Nat.add_comm _ _).trans (over.symm.trans (Nat.add_comm _ _))))))

/-- Where the front stands more than join across `T`, a queue closed once dissipates: no family
is closed across a step at which one unit is exchanged each way, nothing moves across a step
from an empty queue, and across `T` what stands falls. -/
theorem onceClosedQueue_dissipative (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    (excess : a T < E) : (onceClosedQueue n c T E).Dissipative :=
  fun cs t distinct closed f present => match Nat.eq_zero_or_pos (n t) with
    | .inl empty => Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) (total_eq_zero fun k _ =>
        (OnceClosedQueue.idle tally (company t) empty k f).2)).trans ((Nat.zero_add _).trans
          (congrArg sign (total_eq_zero fun k _ =>
            (OnceClosedQueue.idle tally (company t) empty k f).1))))) (Nat.zero_le _)
    | .inr occupied => if same : t = T then
        have shut : OnceClosedQueue.exchange n T t = 0 := mark_zero fun ⟨_, other⟩ => other same
        Nat.le_trans (Nat.add_le_add (total_le_of_support distinct fun _ _ gives =>
            OnceClosedQueue.moving_within tally shut (.inr gives)) (sign_le_one _))
          (Nat.le_trans (onceClosedQueue_exceeds tally same occupied
              (Nat.lt_of_le_of_lt (Nat.le_of_eq (congrArg a same)) excess) f)
            (total_le_of_support (EnclosedQueue.span_distinct t) fun k _ takes =>
              match decideMem k cs with
              | .isTrue mem => mem
              | .isFalse out => absurd (Nat.lt_of_lt_of_le takes
                  (Nat.le_of_eq (closed f present k out).1)) (Nat.lt_irrefl 0)))
      else absurd closed (OnceClosedQueue.not_closed occupied same cs)

/-- With nothing joining an empty queue and the front standing more than join across `T`, a
queue closed once meets all eight premises. -/
theorem onceClosedQueue_premised (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    (excess : a T < E) : (onceClosedQueue n c T E).Premised :=
  .of (OnceClosedQueue.dependent_any_activity (n := n) (c := c) (T := T) (E := E) _)
    (onceClosedQueue_balanced n c T E)
    (onceClosedQueue_acting tally company) (onceClosedQueue_taking tally company)
    (onceClosedQueue_dissipative tally company excess) (onceClosedQueue_embodied n c T E)
    ⟨_, onceClosedQueue_census n c T E⟩
    ⟨1 + E, OnceClosedQueue.transmits_any_flow (n := n) (c := c) (T := T) (E := E) _⟩

/-- Where moreover something joins across `T`, every premise binds there: the front is
active and depends on its own standing, gives to a member joining, which comes to stand
depending on what it stands at, and takes from the span more than it gives, the span
closed; and no finite list holds every relatum. -/
theorem onceClosedQueue_binds (tally : Tally n c a) (company : ∀ t, 0 < a t → 0 < n t)
    (excess : a T < E) (joins : 0 < a T) : (onceClosedQueue n c T E).Binds :=
  have front : Queue.holds n c (Queue.gone c T) T := OpenQueue.front.mpr (company T joins)
  have shut : OnceClosedQueue.exchange n T T = 0 := mark_zero fun ⟨_, other⟩ => other rfl
  have takes := Nat.lt_of_lt_of_le (Nat.zero_lt_succ _)
    (onceClosedQueue_exceeds tally rfl (company T joins) excess (Queue.gone c T))
  match total_pos _ (Nat.lt_of_lt_of_le joins (Nat.le_of_eq (Queue.comings_eq tally T).symm)),
      total_pos _ takes with
  | ⟨x, _, comes⟩, ⟨k, _, taken⟩ =>
    have comes := mark_pos.mp comes
    have stands : 0 < OnceClosedQueue.level n c T E (T + 1) x := EnclosedQueue.place_pos.mp comes.2
    have gives : 0 < (onceClosedQueue n c T E).flow.give T (Queue.gone c T) x :=
      Nat.lt_of_lt_of_le stands (Nat.le_trans (Nat.le_of_eq (congrArg
        (OnceClosedQueue.level n c T E (T + 1) x - ·) (EnclosedQueue.place_zero comes.1).symm))
        (Nat.le_add_right _ _))
    { dependent := ⟨T, _, _, front, trivial, EnclosedQueue.place_pos.mp front⟩
      balanced := ⟨T, x, fun same => Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le stands
        (Nat.le_of_eq (same.trans (EnclosedQueue.place_zero comes.1))))⟩
      acting := ⟨T, _, x, .head _, gives⟩
      taking := ⟨T, _, k, .head _, taken⟩
      dissipative := ⟨_, T, _, EnclosedQueue.span_distinct T, OnceClosedQueue.closed tally shut,
        .head _, takes⟩
      embodied := ⟨T, x, comes⟩
      counted := fun ⟨all, _, every⟩ => beyond_not_mem all (every _)
      transmitting := ⟨T, x, _, x, ⟨.head _, gives, fun standing =>
        comes.1 (EnclosedQueue.place_pos.mpr standing), stands⟩, trivial⟩ }

/-- Where every premise binds, the laws of counting under the eight are the tally, that
nothing arises across a step at which nothing is active, and that something arises: a
property of the counts holds of every census of every world meeting the eight and binding
each exactly when it holds of every tally of this kind. Binding adds one law, which binding
embodiment gives by itself (`binds_arising`, `binds_adds`). Binding is `Binds`: each
condition has an instance. -/
theorem binding_counting {Q : (Nat → Nat) → (Nat → Nat) → (Nat → Nat) → Prop}
    (pointwise : Pointwise Q) :
    (∀ n c a, Tally n c a → (∀ t, 0 < a t → 0 < n t) → (∃ t, 0 < a t) → Q n c a) ↔
      ∀ (w : World) [∀ t x, Decidable (w.web.active t x)], w.Premised → w.Binds →
        w.CountsObey Q :=
  ⟨fun law w _ premised binds alive census =>
    law _ _ _ census.tally
      (counting_binds_jointly.1 w (premised _ (.tail _ (.head _)))
        (premised _ (.tail _ (.tail _ (.head _))))
        (Embodied.arising (premised _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _
          (.head _))))))))
        alive census)
      (binds_arising w binds alive census),
   fun law n c a tally company ⟨T, joins⟩ => pointwise (Queue.counts tally)
      (law (onceClosedQueue n c T (a T + 1))
        (onceClosedQueue_premised tally company (Nat.lt_succ_self _))
        (onceClosedQueue_binds tally company (Nat.lt_succ_self _) joins) _
        (onceClosedQueue_census _ _ _ _))⟩

/-- Every premise binding decides neither rest nor change without end: in `hatch` every
premise binds and arising stops (`hatch_rests`); in a queue closed once in which one member
replaces another at every step every premise binds and arising and ceasing recur. -/
theorem binding_contingent :
    (hatch.Premised ∧ hatch.Binds ∧ ¬ hatch.ArisingRecurs) ∧
      ((onceClosedQueue (fun _ => 1) (fun _ => 1) 0 2).Premised ∧
        (onceClosedQueue (fun _ => 1) (fun _ => 1) 0 2).Binds ∧
        (onceClosedQueue (fun _ => 1) (fun _ => 1) 0 2).ArisingRecurs ∧
        (onceClosedQueue (fun _ => 1) (fun _ => 1) 0 2).CeasingRecurs) :=
  have tally : Tally (fun _ => 1) (fun _ => 1) (fun _ => 1) := fun _ => ⟨0, rfl, rfl⟩
  have company : ∀ t, 0 < (fun _ => 1 : Nat → Nat) t → 0 < (fun _ => 1 : Nat → Nat) t :=
    fun _ pos => pos
  ⟨⟨hatch_binds.1, hatch_binds.2, hatch_rests.2.2.1⟩,
   ⟨onceClosedQueue_premised tally company (Nat.lt_succ_self 1),
    onceClosedQueue_binds tally company (Nat.lt_succ_self 1) Nat.zero_lt_one,
    fun N => match total_pos _ (Nat.lt_of_lt_of_le Nat.zero_lt_one
        (Nat.le_of_eq (Queue.comings_eq tally N).symm)) with
      | ⟨x, _, comes⟩ => ⟨N, x, Nat.le_refl N, mark_pos.mp comes⟩,
    fun N => match total_pos _ (Nat.lt_of_lt_of_le Nat.zero_lt_one
        (Nat.le_of_eq (Queue.ceasings_eq tally N).symm)) with
      | ⟨x, _, ceases⟩ => ⟨N, x, Nat.le_refl N, mark_pos.mp ceases⟩⟩⟩

end World

end Becoming
