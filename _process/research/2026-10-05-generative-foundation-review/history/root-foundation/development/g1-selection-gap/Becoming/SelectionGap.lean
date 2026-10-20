import Becoming.Selection
import Becoming.Counterfactual

/-!
# Selection gap: an act whose difference stays beyond the coupling closure is not selected

Chapter §8.2 listed as open "the gap for one's own act as a general theorem": where an act
differs only on conditions no member of the actor's coupling closure couples into, every selection
through it misses the act. `Becoming.Selection` showed the gap in one world (`Clearing`), and
showed selection blind beyond the closure where the second flow and the rest's response are
supplied (`Flow.unselected_beyond_coupling_responsive`). This module states the law for any act,
with the rest following a law of exchange (`Becoming.Counterfactual`), so that the response is
derived, not supplied. Ren, 18 October 2026: "please see what else is there to do - keep pushing
the frontier till finishing". No premise enters beyond what each theorem names.

* **The act's difference stays beyond the closure.** Two flows in which the part acts are
  compared. The part acts alike within `f`'s coupling closure, drawn through both flows, when
  each of its members within the closure that is coupled alike up to a step exchanges alike, in
  the two flows, with every condition a member of the closure couples into
  (`Flow.ActsAlikeWithin`). The plain case: the two acts differ only on conditions no member of
  the closure couples into (`Flow.ActsAlikeOnCoupled`, `Flow.ActsAlikeOnCoupled.within`).
* **Every selection through the closure misses the act.** Where the rest follows one law of
  exchange reading through coupling in both flows, both balance, the same formations are present
  and they start alike: every selection through the coupling of any formation within the closure,
  `f` among them, selects the two flows' levels alike at every step (`Flow.act_unselected`,
  `Flow.act_unselected_of_coupled`). So a consequence of the act, a selection holding with it and
  failing without it (a formation beyond ending, say), is a selection through no member of the
  closure at any step (`Flow.consequence_unselected`). The rest's response is derived from the law
  (`ExchangeLaw.Through.responds`), not supplied.
* **With both acts laws, nothing is supplied.** Where the part acts by laws of what has stood,
  the first reading through its members' coupling and the two agreeing on every condition coupled
  into the closure, the courses the law generates with each act, feasible, are selected alike
  through every member of the closure (`act_courses_unselected`): neither the second flow, nor
  the response, nor the levels are supplied.
* **The gap is exact.** Conversely, where two courses come apart through a formation's coupling up
  to a step, some selection through it separates them (`Web.separates`), and two histories are
  selected alike by every selection through it exactly when it couples them alike
  (`Web.selects_alike_iff`). So an act is selected through a formation exactly where its
  difference reaches what couples into that formation, and the theorems above give the dynamic
  condition under which it never does. `Clearing` is a world in which such an act ends a
  formation within the actor's reach (`Clearing.unselected`).

**Reading (the AI's).** What a formation can select for or against is bounded by its coupling
closure, not by its reach. An act's consequences beyond the closure, however large, never enter
any selection made through the members of the closure, the actor's own included, unless they
come back through a condition some member couples into. Correcting such an act takes a coupling
that reaches the consequence: widening what couples into the actor, or pooling with a formation
that couples into it (`Clearing.selected_pooled`). This is the formal form of the gap for one's
own act. It does not say which acts are taken, or that any is wrong.

What is not derived: which law the rest follows, or that it reads through coupling (a hypothesis
wherever it enters, as in `Becoming.Counterfactual`); balance and feasibility; how large an act's
consequences beyond the closure are; which acts are taken. A difference cannot come back into the
closure through a formation outside it: nothing beyond the closure exchanges with a condition
coupled into it (`Flow.beyond_coupling`). The representation commits to discrete steps and natural
amounts. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {F C : Type}

namespace Flow

variable (L L' : Flow F C) (W W' : Web F C) (obs : F → C → Prop) (part : F → Bool) (f : F)

/-- **The part acts alike within `f`'s coupling closure.** Each member of the part within the
closure, drawn through both flows, coupled alike up to `t`, exchanges alike in the two flows across
the step from `t` with every condition a member of the closure couples into. -/
def ActsAlikeWithin : Prop :=
  ∀ h, part h = true → WithinClosure (L.CoupledFromEither W L' obs) f h →
    ∀ t, W.AlikeThroughUpTo obs h W.level W'.level t →
    ∀ g c, WithinClosure (L.CoupledFromEither W L' obs) f g → W.CoupledInto obs g c →
      L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c

/-- **The act differs only beyond the closure.** In the two flows the part exchanges alike with
every condition a member of `f`'s coupling closure couples into. -/
def ActsAlikeOnCoupled : Prop :=
  ∀ h, part h = true → ∀ t c,
    (∃ g, WithinClosure (L.CoupledFromEither W L' obs) f g ∧ W.CoupledInto obs g c) →
      L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c

variable {L L' W W' obs part f}

/-- An act differing only beyond the closure acts alike within it. -/
theorem ActsAlikeOnCoupled.within (acts : L.ActsAlikeOnCoupled L' W obs part f) :
    L.ActsAlikeWithin L' W W' obs part f :=
  fun h member _ t _ g c within couples => acts h member t c ⟨g, within, couples⟩

end Flow

section Gap

variable {law : ExchangeLaw F C} {L L' : Flow F C} {W W' : Web F C} {obs : F → C → Prop}
  {part : F → Bool} {f : F} {select : (Nat → C → Nat) → Prop}

/-- **Every selection through the closure misses the act.** The rest follows one law of exchange
reading through coupling in two balanced flows with the same formations present, starting alike,
and the part acts alike within `f`'s coupling closure. Then every selection through the coupling
of a formation within the closure, `f` among them, selects the two flows' levels alike. The rest's
response is derived from the law. -/
theorem Flow.act_unselected (through : law.Through W obs part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (start : ∀ c, W.level 0 c = W'.level 0 c)
    (acts : L.ActsAlikeWithin L' W W' obs part f)
    {g : F} (within : WithinClosure (L.CoupledFromEither W L' obs) f g) {t : Nat}
    (selects : W.SelectsThrough obs g t select) : select W.level ↔ select W'.level :=
  Flow.unselected_beyond_coupling_responsive
    (fun t _ c _ _ => balances.on [c] t) (fun t _ c _ _ => balances'.on [c] t) present
    (fun _ _ c _ => start c)
    (fun h within_h t alike g c within_g couples =>
      match q : part h with
      | false => (through.responds follows follows') h q t alike c
      | true => acts h q within_h t alike g c within_g couples)
    within selects

/-- **An act differing only beyond the closure is not selected.** -/
theorem Flow.act_unselected_of_coupled (through : law.Through W obs part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (start : ∀ c, W.level 0 c = W'.level 0 c)
    (acts : L.ActsAlikeOnCoupled L' W obs part f)
    {g : F} (within : WithinClosure (L.CoupledFromEither W L' obs) f g) {t : Nat}
    (selects : W.SelectsThrough obs g t select) : select W.level ↔ select W'.level :=
  Flow.act_unselected through follows follows' balances balances' present start acts.within
    within selects

/-- **A consequence of the act is selected through no member of the closure.** Under the
conditions of `Flow.act_unselected`, a selection holding with the act and failing without it is,
at no step, a selection through the coupling of any formation within the closure. -/
theorem Flow.consequence_unselected (through : law.Through W obs part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (start : ∀ c, W.level 0 c = W'.level 0 c)
    (acts : L.ActsAlikeWithin L' W W' obs part f)
    (holds : select W.level) (fails : ¬ select W'.level)
    {g : F} (within : WithinClosure (L.CoupledFromEither W L' obs) f g) (t : Nat) :
    ¬ W.SelectsThrough obs g t select :=
  fun selects => fails ((Flow.act_unselected through follows follows' balances balances' present
    start acts within selects).mp holds)

/-- The law with the part acting takes, for a member of the part, as the act does. -/
theorem ExchangeLaw.withAct_take_of_part {act : ExchangeLaw F C} {h : F} (member : part h = true)
    (t : Nat) (l : Nat → C → Nat) (c : C) : (law.withAct part act).take t h l c = act.take t h l c :=
  congrArg (fun b => bif b then act.take t h l c else law.take t h l c) member

/-- And gives as the act does. -/
theorem ExchangeLaw.withAct_give_of_part {act : ExchangeLaw F C} {h : F} (member : part h = true)
    (t : Nat) (l : Nat → C → Nat) (c : C) : (law.withAct part act).give t h l c = act.give t h l c :=
  congrArg (fun b => bif b then act.give t h l c else law.give t h l c) member

/-- **With both acts laws, nothing is supplied.** The part acts by `act` or by `act'`, laws of
what has stood, `act` reading through its members' coupling, the two agreeing on every condition
coupled into `f`'s coupling closure drawn through the two courses; the rest follows a law of what
has stood reading through coupling; both courses are feasible. Then every selection through the
coupling of a formation within the closure selects the levels of the two courses alike. -/
theorem act_courses_unselected {act act' : ExchangeLaw F C} {present : Nat → List F}
    {start : C → Nat} (na : law.Nonanticipating) (naAct : act.Nonanticipating)
    (naAct' : act'.Nonanticipating) (through : law.Through W obs part)
    (actThrough : act.Through W obs (fun h => !part h))
    (feasible : (law.withAct part act).Feasible present start)
    (feasible' : (law.withAct part act').Feasible present start)
    (agree : ∀ t h l c, part h = true →
      (∃ g, WithinClosure (((law.withAct part act).course present start).CoupledFromEither W
          ((law.withAct part act').course present start) obs) f g ∧ W.CoupledInto obs g c) →
        act.take t h l c = act'.take t h l c ∧ act.give t h l c = act'.give t h l c)
    {g : F} (within : WithinClosure (((law.withAct part act).course present start).CoupledFromEither
      W ((law.withAct part act').course present start) obs) f g) {t : Nat}
    (selects : W.SelectsThrough obs g t select) :
    select ((law.withAct part act).levels present start) ↔
      select ((law.withAct part act').levels present start) :=
  Flow.act_unselected (law := law) (W := W.withLevel ((law.withAct part act).levels present start))
    (W' := W.withLevel ((law.withAct part act').levels present start)) through
    (ExchangeLaw.withAct_follows present start) (ExchangeLaw.withAct_follows present start)
    ((ExchangeLaw.course_balances_iff (ExchangeLaw.withAct_nonanticipating na naAct) W).mpr feasible)
    ((ExchangeLaw.course_balances_iff (ExchangeLaw.withAct_nonanticipating na naAct') W).mpr
      feasible')
    (fun _ => rfl) (fun _ => rfl)
    (fun h member _ t alike g' c within' couples =>
      have same := actThrough h (congrArg Bool.not member) t _ _ alike c
      have both := agree t h ((law.withAct part act').levels present start) c member
        ⟨g', within', couples⟩
      ⟨(ExchangeLaw.withAct_take_of_part member t _ c).trans (same.1.trans
          (both.1.trans (ExchangeLaw.withAct_take_of_part member t _ c).symm)),
       (ExchangeLaw.withAct_give_of_part member t _ c).trans (same.2.trans
          (both.2.trans (ExchangeLaw.withAct_give_of_part member t _ c).symm))⟩)
    within selects

end Gap

end Becoming
