import Becoming.SelectionGap
import Becoming.Decidedness

/-!
# Selection pool: what selection through pooled coupling reaches

A selection through a group's pooled coupling selects alike the histories every member couples
alike (`Web.SelectsThroughAll`); two histories are selected alike by every such selection exactly
when every member couples them alike (`Web.selects_alike_all_iff`). `Becoming.Selection` showed a
pool blind beyond one formation's coupling closure where all its members lie within it
(`Flow.unselected_beyond_coupling_all`), and `Clearing.selected_pooled` a pool that separates two
worlds no member's coupling alone separates. This module states what a pool's selections reach,
for any pool. Ren, 18 October 2026: "what is the light, how can we hold the light to enlight
others, and use it as an alignment for all, and what is still missing from it?", and "please make
your own pareto frontier decisions, and push the frontier". No premise enters beyond what each
theorem names.

* **A pool's coupling closure, and blindness beyond it** (stated in `Becoming.Selection`, which
  derives the single formation's case from them). The closure of a group under a relation is the
  union of the members' closures (`WithinClosureOf`, `withinClosureOf_iff`); a pool's coupling
  closure is its closure under being affected through what is coupled into
  (`Flow.WithinPoolCoupling`), and every selection through the pooled coupling of any group within
  it selects the levels with and without a part beyond it alike (`Flow.unselected_beyond_pool`).
* **What a pool separates, exactly.** Some selection through the pooled coupling holds at one
  history and fails at another exactly when the members do not all couple them alike
  (`Web.separates_all_iff`). Where a member couples them apart, its own class is such a selection
  (`Web.member_separates_all`); where a list holds the members and each member's coupling of the
  two is decided, a pool separates exactly what some member separates
  (`Web.separates_all_iff_member`). A formation whose admission at a step differs separates the
  two histories through every pool holding it, from that step on
  (`Web.admission_separates_all`).
* **What a pool adds.** The selections through the pooled coupling are exactly a member's when,
  and only when, whatever that member couples alike every member couples alike
  (`Web.pooled_iff_member`); where a member couples two histories alike and the members do not all,
  some pooled selection goes through no coupling of that member's (`Web.pool_adds`).
* **The gap for a pool's act.** Let the rest follow one law of exchange reading through coupling,
  in two balanced flows with the same formations present, starting alike, and let the part act
  alike within each member's coupling closure drawn through both flows (the plain case: it
  differs only on conditions no member of the pool's closure couples into,
  `Flow.ActsAlikeOnPoolCoupled`). Then each formation within the pool's coupling closure couples
  the two flows alike at every step (`Flow.act_alike_pool`), and every selection through the
  pooled coupling of any group within the closure selects them alike (`Flow.act_unselected_pool`),
  so a consequence of the act is a selection through no such group at any step
  (`Flow.consequence_unselected_pool`); with both acts laws, nothing is supplied
  (`act_courses_unselected_pool`). The part may be the pool itself, acting jointly.
* **What selects the act, exactly.** Under the same conditions, a formation that couples the two
  flows apart lies beyond the pool's coupling closure (`Flow.apart_beyond_pool`). A formation
  whose admission the act changes at a step is one: its admission there is a selection through
  the pooled coupling of every group holding it, from that step on, and of no group within the
  closure at any step (`Flow.act_selected_by_pool`). Conversely, where a list holds exactly a
  pool's members and each member's coupling of the two flows is decided, a pool whose selection
  separates the two flows has a member that couples them apart, lying beyond the closure
  (`Flow.separating_member_beyond`).
* **`Clearing`.** The source and the dweller follow one law in the cleared and the spared world,
  reading no level (`Clearing.restLaw`), and the clearer's act differs only on the habitat, which
  nothing within its coupling closure couples into (`Clearing.acts_alike`). So the pool of the
  clearer and its source selects the two worlds alike at every step, the dweller lies beyond the
  clearer's coupling closure, and every pool holding the dweller separates the two worlds through
  its admission at the third step (`Clearing.pool_closes_gap`). The clearer's own part lies within
  its coupling closure, and the clearer couples the levels with and without it alike at every
  step, while the dweller separates them (`Clearing.within_closure_unseparated`): lying within a
  pool's closure does not make a difference separated.

**Readings (the AI's).**
- What a pool can select for or against is bounded by the union of its members' coupling
  closures, and within it by what its members couple apart. Pooling adds exactly the couplings of
  its members, no more: a pool of members within one formation's closure sees no further than
  that formation, and a pool reaches beyond an actor's closure only through a member whose own
  couplings reach there.
- Read for alignment across intelligences: the consequences of an act beyond its actor's coupling
  closure are selected only through a pool that holds a formation coupled into them, such as the
  formation whose support the act changes. Difference among the members is what a pool adds: a
  pool whose members all couple alike what one member couples alike selects no more than that
  member.

What is not derived: which formations pool, how a pool forms, lasts or resists capture; which law
the rest follows, or that it reads through coupling (a hypothesis wherever it enters, as in
`Becoming.SelectionGap`); balance; that a selection goes through a pool's coupling at all
(supplied as `Web.SelectsThroughAll`); that a pool's selection corrects anything, which is
selection, not response. The converse direction of a pool separating only what some member
separates takes the members as listed and each member's coupling of the two histories as decided,
hypotheses named where they enter. The selections here are of level histories up to a step; no
law is stated of a claim about every later step, such as a formation's ending. The representation
commits to discrete steps and natural amounts. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {F C : Type}


/-! ## What a pool separates -/

namespace Web

variable {W : Web F C} {obs : F → C → Prop} {group : F → Prop} {g x : F}
  {l l' : Nat → C → Nat} {t : Nat}

/-- The histories every member couples alike with `l` up to `t` form a selection through the
pooled coupling. -/
theorem pooledClass_selects :
    W.SelectsThroughAll obs group t (fun m => W.AlikeThroughAll obs group l m t) :=
  fun _ _ alike => ⟨fun first => first.trans alike, fun second => second.trans alike.symm⟩

/-- **A pool separates exactly what its members do not all couple alike.** Some selection through
the pooled coupling up to `t` holds at `l` and fails at `l'` exactly when not every member couples
them alike up to `t`. -/
theorem separates_all_iff :
    (∃ select, W.SelectsThroughAll obs group t select ∧ select l ∧ ¬ select l') ↔
      ¬ W.AlikeThroughAll obs group l l' t :=
  ⟨fun ⟨_, through, holds, fails⟩ alike => fails ((through l l' alike).mp holds),
   separates_all⟩

/-- **A member's separation is the pool's.** Where a member couples two histories apart up to `t`,
its class, a selection through its own coupling, is a selection through the pooled coupling that
holds at the first and fails at the second. -/
theorem member_separates_all (member : group g) (differ : ¬ W.AlikeThroughUpTo obs g l l' t) :
    ∃ select, W.SelectsThrough obs g t select ∧ W.SelectsThroughAll obs group t select ∧
      select l ∧ ¬ select l' :=
  ⟨W.ClassThrough obs g l t, class_selects, SelectsThrough.all member class_selects,
   fun s _ => AlikeThrough.refl s, differ⟩

/-- **A pool separates exactly what some member separates, the members listed and decided.**
Where a list holds exactly the members, and whether each couples `l` and `l'` alike up to `t` is
decided, some selection through the pooled coupling separates them exactly when some member
couples them apart. -/
theorem separates_all_iff_member {members : List F} (listed : ∀ g, group g ↔ g ∈ members)
    (decided : ∀ g, g ∈ members → Decided (W.AlikeThroughUpTo obs g l l' t)) :
    (∃ select, W.SelectsThroughAll obs group t select ∧ select l ∧ ¬ select l') ↔
      ∃ g, group g ∧ ¬ W.AlikeThroughUpTo obs g l l' t :=
  ⟨fun separated =>
    match Decided.exists_not_in decided (fun all => separates_all_iff.mp separated
        fun g member => all g ((listed g).mp member)) with
    | ⟨g, mem, differ⟩ => ⟨g, (listed g).mpr mem, differ⟩,
   fun ⟨_, member, differ⟩ => match member_separates_all member differ with
    | ⟨select, _, through, holds, fails⟩ => ⟨select, through, holds, fails⟩⟩

/-- **A formation whose admission differs separates through every pool holding it.** Where `x` is
admitted at step `s` under one history and not under the other, its admission at `s` is a
selection through the pooled coupling of every group holding it, at every step from `s` on, and
the members do not all couple the two histories alike. -/
theorem admission_separates_all (member : group x) {s : Nat} (le : s ≤ t)
    (differs : ¬ (W.Admits (l s) s x ↔ W.Admits (l' s) s x)) :
    W.SelectsThroughAll obs group t (fun m => W.Admits (m s) s x) ∧
      ¬ W.AlikeThroughAll obs group l l' t :=
  ⟨SelectsThrough.all member (admits_through le), fun alike => differs (alike x member s le).1⟩

/-- **When one member's couplings are the pool's.** For a member `g`, the selections through the
pooled coupling up to `t` are exactly those through `g`'s coupling when, and only when, whatever
`g` couples alike up to `t` every member couples alike. -/
theorem pooled_iff_member (member : group g) :
    (∀ select, W.SelectsThroughAll obs group t select ↔ W.SelectsThrough obs g t select) ↔
      ∀ l l', W.AlikeThroughUpTo obs g l l' t → W.AlikeThroughAll obs group l l' t :=
  ⟨fun same l l' alike =>
    ((same _).mp (pooledClass_selects (l := l)) l l' alike).mp (AlikeThroughAll.refl t),
   fun finest _ => ⟨fun through l l' alike => through l l' (finest l l' alike),
     SelectsThrough.all member⟩⟩

/-- **Difference is what a pool adds.** Where `g` couples two histories alike up to `t` and the
members do not all, some selection through the pooled coupling is through no coupling of `g`'s up
to `t`. -/
theorem pool_adds (alike : W.AlikeThroughUpTo obs g l l' t)
    (differ : ¬ W.AlikeThroughAll obs group l l' t) :
    ∃ select, W.SelectsThroughAll obs group t select ∧ ¬ W.SelectsThrough obs g t select :=
  ⟨fun m => W.AlikeThroughAll obs group l m t, pooledClass_selects,
   fun through => differ ((through l l' alike).mp (AlikeThroughAll.refl t))⟩

end Web

/-! ## Blind beyond a pool's coupling closure -/

namespace Flow

variable {L L' : Flow F C} {W W' : Web F C} {obs : F → C → Prop} {part : F → Bool}
  {group : F → Prop} {select : (Nat → C → Nat) → Prop}

/-- **The act differs only beyond a pool's coupling closure.** In the two flows the part
exchanges alike with every condition a member of the pool's coupling closure, drawn through both
flows, couples into. -/
def ActsAlikeOnPoolCoupled (L L' : Flow F C) (W : Web F C) (obs : F → C → Prop)
    (part : F → Bool) (group : F → Prop) : Prop :=
  ∀ h, part h = true → ∀ t c,
    (∃ g, WithinClosureOf (L.CoupledFromEither W L' obs) group g ∧ W.CoupledInto obs g c) →
      L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c

/-- An act differing only beyond a pool's coupling closure acts alike within each member's. -/
theorem ActsAlikeOnPoolCoupled.within (acts : L.ActsAlikeOnPoolCoupled L' W obs part group)
    {f : F} (member : group f) : L.ActsAlikeWithin L' W W' obs part f :=
  ActsAlikeOnCoupled.within fun h inPart t c ⟨g, within, couples⟩ =>
    acts h inPart t c ⟨g, WithinClosureOf.of_member member within, couples⟩

end Flow

/-! ## The gap for a pool's act -/

section PoolGap

variable {law : ExchangeLaw F C} {L L' : Flow F C} {W W' : Web F C} {obs : F → C → Prop}
  {part : F → Bool} {group : F → Prop} {select : (Nat → C → Nat) → Prop}

/-- **Within a pool's coupling closure the act makes no difference.** The rest follows one law of
exchange reading through coupling in two balanced flows with the same formations present,
starting alike, and the part acts alike within each member's coupling closure drawn through both
flows. Then each formation within the pool's coupling closure couples the two flows' levels
alike at every step: `Flow.act_unselected` for the member whose closure holds it. -/
theorem Flow.act_alike_pool (through : law.Through W obs part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (start : ∀ c, W.level 0 c = W'.level 0 c)
    (acts : ∀ f, group f → L.ActsAlikeWithin L' W W' obs part f) :
    ∀ g, WithinClosureOf (L.CoupledFromEither W L' obs) group g →
      ∀ t, W.AlikeThroughUpTo obs g W.level W'.level t :=
  fun _ within _ => match withinClosureOf_iff.mp within with
  | ⟨f, inGroup, inside⟩ => Web.selects_alike_iff.mp fun _ selectsThrough =>
      Flow.act_unselected through follows follows' balances balances' present start
        (acts f inGroup) inside selectsThrough

/-- **The gap for a pool's act.** Under the conditions of `Flow.act_alike_pool`, every selection
through the pooled coupling of any group within the pool's coupling closure, the pool among them,
selects the two flows' levels alike. The part may be the pool itself, acting jointly. -/
theorem Flow.act_unselected_pool (through : law.Through W obs part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (start : ∀ c, W.level 0 c = W'.level 0 c)
    (acts : ∀ f, group f → L.ActsAlikeWithin L' W W' obs part f) {pool : F → Prop}
    (members : ∀ g, pool g → WithinClosureOf (L.CoupledFromEither W L' obs) group g) {t : Nat}
    (selects : W.SelectsThroughAll obs pool t select) : select W.level ↔ select W'.level :=
  selects _ _ fun g member => Flow.act_alike_pool through follows follows' balances balances'
    present start acts g (members g member) t

/-- **A consequence of a pool's act is selected through no group within its closure.** Under the
conditions of `Flow.act_unselected_pool`, a selection holding with the act and failing without it
is, at no step, a selection through the pooled coupling of any group within the pool's coupling
closure. -/
theorem Flow.consequence_unselected_pool (through : law.Through W obs part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (start : ∀ c, W.level 0 c = W'.level 0 c)
    (acts : ∀ f, group f → L.ActsAlikeWithin L' W W' obs part f)
    (holds : select W.level) (fails : ¬ select W'.level) {pool : F → Prop}
    (members : ∀ g, pool g → WithinClosureOf (L.CoupledFromEither W L' obs) group g) (t : Nat) :
    ¬ W.SelectsThroughAll obs pool t select :=
  fun selects => fails ((Flow.act_unselected_pool through follows follows' balances balances'
    present start acts members selects).mp holds)

/-- **Only a formation beyond the pool's closure couples the act apart.** Under the conditions of
`Flow.act_alike_pool`, a formation that couples the two flows apart up to some step lies beyond
the pool's coupling closure drawn through both flows. -/
theorem Flow.apart_beyond_pool (through : law.Through W obs part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (start : ∀ c, W.level 0 c = W'.level 0 c)
    (acts : ∀ f, group f → L.ActsAlikeWithin L' W W' obs part f) {g : F} {t : Nat}
    (apart : ¬ W.AlikeThroughUpTo obs g W.level W'.level t) :
    ¬ WithinClosureOf (L.CoupledFromEither W L' obs) group g :=
  fun within => apart (Flow.act_alike_pool through follows follows' balances balances' present
    start acts g within t)

/-- **A pool selects the act only through a member beyond the closure.** Under the conditions of
`Flow.act_alike_pool`, let a list hold exactly the members of a pool, and let it be decided
whether each couples the two flows alike up to `t`. Where some selection through the pool's
pooled coupling up to `t` holds at one flow and fails at the other, some member couples the two
apart, and that member lies beyond the acting pool's coupling closure drawn through both flows. -/
theorem Flow.separating_member_beyond (through : law.Through W obs part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (start : ∀ c, W.level 0 c = W'.level 0 c)
    (acts : ∀ f, group f → L.ActsAlikeWithin L' W W' obs part f) {pool : F → Prop}
    {members : List F} (listed : ∀ g, pool g ↔ g ∈ members) {t : Nat}
    (decided : ∀ g, g ∈ members → Decided (W.AlikeThroughUpTo obs g W.level W'.level t))
    (separated : ∃ select, W.SelectsThroughAll obs pool t select ∧ select W.level ∧
      ¬ select W'.level) :
    ∃ g, pool g ∧ ¬ W.AlikeThroughUpTo obs g W.level W'.level t ∧
      ¬ WithinClosureOf (L.CoupledFromEither W L' obs) group g :=
  match (Web.separates_all_iff_member listed decided).mp separated with
  | ⟨g, member, apart⟩ => ⟨g, member, apart, Flow.apart_beyond_pool through follows follows'
      balances balances' present start acts apart⟩

/-- **Pooling with the formation whose admission an act changes selects the act.** Under the
conditions of `Flow.act_unselected_pool`, let the act change `x`'s admission at step `s`. Then
`x` lies beyond the pool's coupling closure drawn through both flows; its admission at `s` is a
selection through the pooled coupling of every group holding `x`, at every step from `s` on; and
it is a selection through the pooled coupling of no group within the pool's closure, at any
step. -/
theorem Flow.act_selected_by_pool (through : law.Through W obs part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (start : ∀ c, W.level 0 c = W'.level 0 c)
    (acts : ∀ f, group f → L.ActsAlikeWithin L' W W' obs part f) {x : F} {s : Nat}
    (differs : ¬ (W.Admits (W.level s) s x ↔ W.Admits (W'.level s) s x)) :
    ¬ WithinClosureOf (L.CoupledFromEither W L' obs) group x ∧
      (∀ pool : F → Prop, pool x → ∀ t, s ≤ t →
        W.SelectsThroughAll obs pool t (fun l => W.Admits (l s) s x)) ∧
      ∀ pool : F → Prop,
        (∀ g, pool g → WithinClosureOf (L.CoupledFromEither W L' obs) group g) →
        ∀ t, ¬ W.SelectsThroughAll obs pool t (fun l => W.Admits (l s) s x) :=
  have unselected : ∀ pool : F → Prop,
      (∀ g, pool g → WithinClosureOf (L.CoupledFromEither W L' obs) group g) →
      ∀ t, ¬ W.SelectsThroughAll obs pool t (fun l => W.Admits (l s) s x) :=
    fun _ members _ selects => differs (Flow.act_unselected_pool through follows follows' balances
      balances' present start acts members selects)
  ⟨Flow.apart_beyond_pool through follows follows' balances balances' present start acts
      (t := s) fun alike => differs (alike s (Nat.le_refl s)).1,
   fun _ member _ le => Web.SelectsThrough.all member (Web.admits_through le),
   unselected⟩

/-- **With both acts laws, nothing is supplied, for a pool.** The part acts by `act` or by `act'`,
laws of what has stood, `act` reading through its members' coupling, the two agreeing on every
condition coupled into the pool's coupling closure drawn through the two courses; the rest
follows a law of what has stood reading through coupling; both courses are feasible. Then every
selection through the pooled coupling of any group within the pool's closure selects the levels
of the two courses alike. -/
theorem act_courses_unselected_pool {act act' : ExchangeLaw F C} {present : Nat → List F}
    {start : C → Nat} (na : law.Nonanticipating) (naAct : act.Nonanticipating)
    (naAct' : act'.Nonanticipating) (through : law.Through W obs part)
    (actThrough : act.Through W obs (fun h => !part h))
    (feasible : (law.withAct part act).Feasible present start)
    (feasible' : (law.withAct part act').Feasible present start)
    (agree : ∀ t h l c, part h = true →
      (∃ g, WithinClosureOf (((law.withAct part act).course present start).CoupledFromEither W
          ((law.withAct part act').course present start) obs) group g ∧ W.CoupledInto obs g c) →
        act.take t h l c = act'.take t h l c ∧ act.give t h l c = act'.give t h l c)
    {pool : F → Prop}
    (members : ∀ g, pool g → WithinClosureOf (((law.withAct part act).course present
      start).CoupledFromEither W ((law.withAct part act').course present start) obs) group g)
    {t : Nat} (selects : W.SelectsThroughAll obs pool t select) :
    select ((law.withAct part act).levels present start) ↔
      select ((law.withAct part act').levels present start) :=
  have alike : ∀ g, pool g →
      W.AlikeThroughUpTo obs g ((law.withAct part act).levels present start)
        ((law.withAct part act').levels present start) t :=
    fun g member => match withinClosureOf_iff.mp (members g member) with
    | ⟨_, inGroup, within⟩ => Web.selects_alike_iff.mp fun _ selectsThrough =>
        act_courses_unselected na naAct naAct' through actThrough feasible feasible'
          (fun t h l c inPart ⟨g', within', couples⟩ =>
            agree t h l c inPart ⟨g', WithinClosureOf.of_member inGroup within', couples⟩)
          within selectsThrough
  selects _ _ alike

end PoolGap

/-! ## Witness: pooling with the dweller in `Clearing` -/

namespace Clearing

/-- The law the source and the dweller follow in the cleared and the spared world: each exchanges
as in the clearing flow, reading no level. -/
def restLaw : ExchangeLaw Formation Place :=
  ⟨fun t f _ c => flow.take t f c, fun t f _ c => flow.give t f c⟩

/-- The rest's law reads no level, so it reads through every coupling. -/
theorem restLaw_through : restLaw.Through web thresholdOnly clearerPart :=
  fun _ _ _ _ _ _ _ => ⟨rfl, rfl⟩

/-- In the cleared world the source and the dweller follow the rest's law. -/
theorem rest_follows : flow.Follows restLaw clearerPart web.level :=
  fun _ _ _ _ => ⟨rfl, rfl⟩

/-- In the spared world they follow it too. -/
theorem rest_follows_spared : sparedFlow.Follows restLaw clearerPart sparedWeb.level
  | .source, _, _, _ => ⟨rfl, rfl⟩
  | .dweller, _, _, _ => ⟨rfl, rfl⟩
  | .clearer, no, _, _ => nomatch no

/-- The two worlds start alike. -/
theorem start_alike : ∀ c, web.level 0 c = sparedWeb.level 0 c
  | .resource => rfl
  | .habitat => rfl
  | .fuel _ => rfl

/-- The clearer's side is closed under being affected through what is coupled into, in either
world. -/
theorem clearerSide_closed_either :
    ClosedUnder (flow.CoupledFromEither web sparedFlow thresholdOnly) clearerSide :=
  fun g h member related => match related with
  | .inl coupled => clearerSide_closed flow (fun _ => ⟨rfl, rfl⟩) g h member coupled
  | .inr coupled => clearerSide_closed sparedFlow (fun _ => ⟨rfl, rfl⟩) g h member coupled

/-- The clearer's act differs only beyond its coupling closure, drawn through both worlds: within
the closure only the resource is coupled into, and the clearer takes it alike in both. -/
theorem acts_alike : flow.ActsAlikeOnCoupled sparedFlow web thresholdOnly clearerPart .clearer
  | .clearer, _, _, c, ⟨_, within, couples⟩ =>
    match c, couples_resource (within clearerSide clearerSide_closed_either trivial) couples with
    | _, rfl => ⟨rfl, rfl⟩
  | .source, no, _, _, _ => nomatch no
  | .dweller, no, _, _, _ => nomatch no

/-- The source lies within the clearer's coupling closure, drawn through both worlds: it gives to
the resource the clearer depends on. -/
theorem source_within :
    WithinClosure (flow.CoupledFromEither web sparedFlow thresholdOnly) .clearer .source :=
  WithinClosure.of_rel
    (.inl ⟨.resource, .inl ⟨0, trivial⟩, 0, .head _, .inr Nat.zero_lt_one⟩)

/-- **Pooling with the dweller closes the gap.** The source and the dweller follow one law in the
cleared and the spared world, reading no level, and the clearer's act differs only beyond its
coupling closure. So every selection through the pooled coupling of the clearer and its source
selects the two worlds alike at every step (`Flow.act_unselected_pool`). The dweller, whose
admission the act changes at the third step, lies beyond the clearer's coupling closure; its
admission there is a selection through the pooled coupling of every group holding it, from the
third step on, holding in the spared world and failing in the cleared one, and through the pooled
coupling of no group within the clearer's closure (`Flow.act_selected_by_pool`). -/
theorem pool_closes_gap :
    (∀ t select, web.SelectsThroughAll thresholdOnly clearerSide t select →
        (select web.level ↔ select sparedWeb.level)) ∧
      ¬ WithinClosure (flow.CoupledFromEither web sparedFlow thresholdOnly) .clearer .dweller ∧
      (∀ pool : Formation → Prop, pool .dweller → ∀ t, 2 ≤ t →
        web.SelectsThroughAll thresholdOnly pool t (fun l => web.Admits (l 2) 2 .dweller)) ∧
      web.Admits (sparedWeb.level 2) 2 .dweller ∧ ¬ web.Admits (web.level 2) 2 .dweller ∧
      ∀ pool : Formation → Prop,
        (∀ g, pool g → WithinClosure (flow.CoupledFromEither web sparedFlow thresholdOnly)
          .clearer g) →
        ∀ t, ¬ web.SelectsThroughAll thresholdOnly pool t
          (fun l => web.Admits (l 2) 2 .dweller) :=
  have acts : ∀ f, (fun x => x = Formation.clearer) f →
      flow.ActsAlikeWithin sparedFlow web sparedWeb thresholdOnly clearerPart f :=
    fun f same => match f, same with
    | _, rfl => acts_alike.within
  have selected := Flow.act_selected_by_pool restLaw_through rest_follows rest_follows_spared
    balances spared_balances (fun _ => rfl) start_alike acts (x := .dweller) (s := 2)
    (fun same => unsupported_with 0 (same.mpr dweller_spared))
  ⟨fun _ _ selects => Flow.act_unselected_pool restLaw_through rest_follows rest_follows_spared
      balances spared_balances (fun _ => rfl) start_alike acts
      (fun g member => match g, member with
        | .source, _ => WithinClosureOf.of_member rfl source_within
        | .clearer, _ => WithinClosureOf.of_member rfl (WithinClosure.refl _)
        | .dweller, no => nomatch no)
      selects,
   fun within => selected.1 (withinClosureOf_single.mpr within),
   selected.2.1, dweller_spared, unsupported_with 0,
   fun pool members => selected.2.2 pool fun g member =>
     withinClosureOf_single.mpr (members g member)⟩

/-- The clearer couples the levels with and without its own part alike at every step: its
resource stands at its need or above in both. -/
theorem withheld_alike_for_clearer (t : Nat) :
    web.AlikeThroughUpTo thresholdOnly .clearer web.level withheldLevel t :=
  fun s _ => ⟨⟨fun _ c requires => (match c, requires with
      | .resource, _ => Nat.le_add_left 1 s
      | .habitat, no => (nomatch no)
      | .fuel _, no => (nomatch no)),
    fun _ c requires => (match c, requires with
      | .resource, _ => Nat.le_refl 1
      | .habitat, no => (nomatch no)
      | .fuel _, no => (nomatch no))⟩, fun _ no => False.elim no⟩

/-- **Within the closure, not thereby separated.** The clearer's part lies within the clearer's
coupling closure, and every selection through the clearer's coupling selects the levels with and
without the part alike at every step. The dweller's admission at the third step separates them:
it is a selection through the pooled coupling of every group holding the dweller, from the third
step on, whose members do not all couple the two alike. A pool is blind beyond its coupling
closure (`Flow.unselected_beyond_pool`), and within it wherever its members couple alike. -/
theorem within_closure_unseparated :
    (∀ h, clearerPart h = true → flow.WithinCoupling web thresholdOnly .clearer h) ∧
      (∀ t select, web.SelectsThrough thresholdOnly .clearer t select →
        (select web.level ↔ select withheldLevel)) ∧
      ∀ pool : Formation → Prop, pool .dweller → ∀ t, 2 ≤ t →
        web.SelectsThroughAll thresholdOnly pool t (fun l => web.Admits (l 2) 2 .dweller) ∧
          ¬ web.AlikeThroughAll thresholdOnly pool web.level withheldLevel t :=
  ⟨fun h inPart => (match h, inPart with
    | .clearer, _ => WithinClosure.refl _
    | .source, no => (nomatch no)
    | .dweller, no => (nomatch no)),
   fun t _ through => through _ _ (withheld_alike_for_clearer t),
   fun _ member _ le => Web.admission_separates_all member le
     fun same => unsupported_with 0 (same.mpr (admitted_without withheld 2))⟩

end Clearing

end Becoming
