import Becoming.Testing
import Becoming.Inquiry

/-!
# Probe C–E: refutation, models, pooled registration, the inquiry bridge, the horizon dual

Sixteenth review of P47.

* C1 `RefutesWithin`: refutation relative to a class of admissible histories (a model).
  `Refutes` is the case of every history; narrowing the model refutes more; soundness
  (`not_meets`) needs the actual history inside the model.
* C2 `tail_untested`: with every history admissible, a claim met by some history that agrees
  with the record up to `t` is not refuted at `t`; so both "the stock comes to zero" and "it never
  does after `t`" are unrefuted by every finite record. Trivial for `Refutes`.
* C3 `model_refutes_tail`: relative to a model fixing the exchange, a formation observing a
  stock refutes at the first step every false claim that the stock comes to zero.
* C4 `Stationary.model_error`: relative to a model the actual history violates, a true claim is
  refuted: crossing the horizon by a model is fallible.
* C5 `RefutesBy`, `Clearing.pooled`: a group refutes what each member refutes; in `Clearing`
  neither the clearer nor the dweller refutes a disjunctive claim that the pair refutes.
* D  `belief_*`: the bridge to `Becoming.Inquiry`. A formation's belief at `t` is the set of
  histories it registers alike with the actual; refutation is a claim disjoint from it; a judgment
  under it is a common response; later steps and more observation narrow it and keep every common
  response; a part beyond the registration closure cannot be judged from within.
* E  `Renewable.*`: `finite_reading_withholds_renewal` against `finite_reading_credits_consumption`.
-/

namespace Becoming.Review47

open Becoming Generative

variable {F C : Type}

/-! ## C1. Refutation relative to a model -/

/-- Refuted relative to the admissible histories. -/
def RefutesWithin (W : Web F C) (admissible : (Nat → C → Nat) → Prop) (obs : F → C → Prop)
    (claim : (Nat → C → Nat) → Prop) (g : F) (l : Nat → C → Nat) (t : Nat) : Prop :=
  ∀ l', admissible l' → claim l' → ¬ W.AlikeUpTo obs g l l' t

variable {W : Web F C} {obs : F → C → Prop} {claim : (Nat → C → Nat) → Prop} {g : F}
  {l : Nat → C → Nat} {t : Nat}

theorem refutes_iff_within_all :
    W.Refutes obs claim g l t ↔ RefutesWithin W (fun _ => True) obs claim g l t :=
  ⟨fun refutes l' _ meets => refutes l' meets, fun refutes l' meets => refutes l' trivial meets⟩

theorem RefutesWithin.narrow {adm adm' : (Nat → C → Nat) → Prop} (narrower : ∀ l, adm' l → adm l)
    (refutes : RefutesWithin W adm obs claim g l t) : RefutesWithin W adm' obs claim g l t :=
  fun l' inside meets => refutes l' (narrower l' inside) meets

theorem RefutesWithin.not_meets {adm : (Nat → C → Nat) → Prop} (actual : adm l)
    (refutes : RefutesWithin W adm obs claim g l t) : ¬ claim l :=
  fun meets => refutes l actual meets fun _ _ => Web.RegistersAlike.refl _

/-! ## C2. With every history admissible, a finite record leaves the tail open -/

theorem alike_of_agree {l' : Nat → C → Nat} (agree : ∀ s, s ≤ t → ∀ e, l' s e = l s e) :
    W.AlikeUpTo obs g l l' t :=
  fun s le => ⟨⟨fun admits c requires => Nat.le_trans (admits c requires)
      (Nat.le_of_eq (agree s le c).symm),
    fun admits c requires => Nat.le_trans (admits c requires) (Nat.le_of_eq (agree s le c))⟩,
   fun c _ => (agree s le c).symm⟩

theorem unrefuted_of_extension
    (extends_ : ∃ l', claim l' ∧ ∀ s, s ≤ t → ∀ e, l' s e = l s e) :
    ¬ W.Refutes obs claim g l t :=
  match extends_ with
  | ⟨l', meets, agree⟩ => Web.Refutes.not_of_alike meets (alike_of_agree agree)

/-- The record up to `t`, then a constant `k` on one condition. -/
def thenConst [DecidableEq C] (l : Nat → C → Nat) (t : Nat) (c : C) (k : Nat) :
    Nat → C → Nat :=
  fun s e => if s ≤ t then l s e else if e = c then k else l s e

/-- C2. For every finite record, both a claim about the whole run and its rival stay unrefuted. -/
theorem tail_untested [DecidableEq C] (c : C) :
    ¬ W.Refutes obs (fun l' => ∃ T, l' T c = 0) g l t ∧
      ¬ W.Refutes obs (fun l' => ∀ T, t < T → 0 < l' T c) g l t :=
  have agree : ∀ k, ∀ s, s ≤ t → ∀ e, thenConst l t c k s e = l s e := fun _ _ le _ =>
    if_pos le
  have after : ∀ k T, t < T → thenConst l t c k T c = k := fun _ _ later =>
    (if_neg (Nat.not_le_of_lt later)).trans (if_pos rfl)
  ⟨unrefuted_of_extension ⟨thenConst l t c 0, ⟨t + 1, after 0 (t + 1) (Nat.lt_succ_self t)⟩,
      agree 0⟩,
   unrefuted_of_extension ⟨thenConst l t c 1, fun T later =>
      Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq (after 1 T later).symm), agree 1⟩⟩

/-! ## C3. A model fixing the exchange crosses the horizon -/

/-- The histories balancing a fixed flow: a model of the exchange. -/
def Model (L : Flow F C) (l : Nat → C → Nat) : Prop :=
  ∀ s e, l (s + 1) e + L.taken s e = l s e + L.given s e

theorem Model.agree {L : Flow F C} {l l' : Nat → C → Nat} {c : C} (model : Model L l)
    (model' : Model L l') (start : l 0 c = l' 0 c) : ∀ s, l s c = l' s c
  | 0 => start
  | s + 1 => add_right_cancel (L.taken s c)
      ((model s c).trans ((congrArg (· + L.given s c) (Model.agree model model' start s)).trans
        (model' s c).symm))

/-- C3. Relative to a model of the exchange, a formation observing a stock refutes at the first
step every false claim that the stock comes to zero. -/
theorem model_refutes_tail {L : Flow F C} {c : C} (observed : obs g c) (model : Model L l)
    (never : ∀ T, ¬ l T c = 0) :
    RefutesWithin W (Model L) obs (fun l' => ∃ T, l' T c = 0) g l 0 :=
  fun l' model' ⟨T, zero⟩ alike =>
    never T ((Model.agree model model' ((alike 0 (Nat.le_refl 0)).2 c observed) T).trans zero)

namespace Stationary

/-- The model: nothing takes or gives. -/
def still : Flow Unit Unit := ⟨fun _ => [()], fun _ _ _ => 0, fun _ _ _ => 0⟩

/-- The actual history: the stock stands at two, then something the model omits takes it. -/
def actual : Nat → Unit → Nat
  | 0, _ => 2
  | _ + 1, _ => 0

def web : Web Unit Unit := ⟨actual, fun _ _ => True, fun _ _ _ => True, fun _ _ _ => 1,
  fun _ _ _ => True⟩

def gauge : Unit → Unit → Prop := fun _ _ => True

/-- C4. **Model error.** Relative to the stationary model, a formation gauging the stock refutes
at the first step the claim that the stock comes to zero, which holds of the actual history. -/
theorem model_error :
    (∃ T, actual T () = 0) ∧ ¬ Model still actual ∧
      RefutesWithin web (Model still) gauge (fun l' => ∃ T, l' T () = 0) () actual 0 :=
  ⟨⟨1, rfl⟩, fun model => Nat.noConfusion (model 0 ()),
   fun l' model' ⟨T, zero⟩ alike =>
     have same : ∀ s, l' s () = l' 0 () := fun s =>
       Nat.rec (motive := fun s => l' s () = l' 0 ()) rfl
         (fun s ih => (model' s ()).trans ih) s
     have two : l' 0 () = 2 := ((alike 0 (Nat.le_refl 0)).2 () trivial).symm
     Nat.noConfusion ((zero.symm.trans (same T)).trans two)⟩

/-- C4b. **The model is refuted.** At the second step no history the stationary model admits is
registered alike by the gauging formation: its belief within the model is empty, so the model
itself (the claim `True` within it) is refuted. -/
theorem model_refuted :
    RefutesWithin web (Model still) gauge (fun _ => True) () actual 1 :=
  fun l' model' _ alike =>
    have zero : l' 1 () = 0 := ((alike 1 (Nat.le_refl 1)).2 () trivial).symm
    have two : l' 0 () = 2 := ((alike 0 (Nat.zero_le 1)).2 () trivial).symm
    Nat.noConfusion (zero.symm.trans ((model' 0 ()).trans two))

end Stationary

/-- C6. Refutation within a model is refutation of the model and the claim together. -/
theorem refutesWithin_iff_conjunction {adm : (Nat → C → Nat) → Prop} :
    RefutesWithin W adm obs claim g l t ↔ W.Refutes obs (fun l' => adm l' ∧ claim l') g l t :=
  ⟨fun refutes l' ⟨inside, meets⟩ => refutes l' inside meets,
   fun refutes l' inside meets => refutes l' ⟨inside, meets⟩⟩

/-- C7. **Beyond the registration closure, only a model can judge.** Where a formation within the
closure refutes a claim relative to a model, the model and the claim together exclude the levels
without the part: the refutation rests on a model of the part's exchange, not on registration. -/
theorem beyond_needs_model {L : Flow F C} {part : F → Bool} (balances : L.Balances W)
    {l₀ : Nat → C → Nat} (without : L.WithheldLevels part W l₀) {f : F}
    (beyond : ∀ h, part h = true → ¬ L.WithinRegistration W obs f h)
    (within : L.WithinRegistration W obs f g) {adm : (Nat → C → Nat) → Prop}
    (refutes : RefutesWithin W adm obs claim g W.level t) : ¬ (adm l₀ ∧ claim l₀) :=
  fun ⟨inside, meets⟩ => refutes l₀ inside meets fun s _ =>
    balances.unregistered_beyond_registration without beyond s g within

namespace ClearingModel

open Becoming.Clearing

/-- A model fixing the start and the exchange. -/
def complete (l' : Nat → Place → Nat) : Prop :=
  Model flow l' ∧ ∀ c, l' 0 c = web.level 0 c

/-- C8. With a model fixing the start and the exchange, the clearer refutes at the first step,
registering nothing about the habitat, that the dweller is admitted at the third: the
registration does no work. -/
theorem model_idles_registration :
    RefutesWithin web complete supportOnly (fun l' => web.Admits (l' 2) 2 .dweller) .clearer
      web.level 0 :=
  fun l' ⟨model', start⟩ admits _ =>
    have same : l' 2 .habitat = web.level 2 .habitat :=
      (Model.agree model' balances (start .habitat) 2)
    Nat.not_succ_le_zero 0 (Nat.le_trans (admits .habitat trivial) (Nat.le_of_eq same))

end ClearingModel

/-! ## C5. Pooled registration -/

/-- Every member of a group registers alike up to `t`. -/
def AlikeUpToAll (W : Web F C) (obs : F → C → Prop) (group : F → Prop) (l l' : Nat → C → Nat)
    (t : Nat) : Prop :=
  ∀ g, group g → W.AlikeUpTo obs g l l' t

/-- A group refutes a claim when no history meeting it is registered alike by all its members. -/
def RefutesBy (W : Web F C) (obs : F → C → Prop) (claim : (Nat → C → Nat) → Prop)
    (group : F → Prop) (l : Nat → C → Nat) (t : Nat) : Prop :=
  ∀ l', claim l' → ¬ AlikeUpToAll W obs group l l' t

theorem RefutesBy.of_member {group : F → Prop} (member : group g)
    (refutes : W.Refutes obs claim g l t) : RefutesBy W obs claim group l t :=
  fun l' meets all => refutes l' meets (all g member)

namespace ClearingPooled

open Becoming.Clearing

/-- The resource gone at the third step, all else as spared. -/
def resourceGone (t : Nat) : Place → Nat
  | .resource => match t with
    | 2 => 0
    | _ => 1
  | .habitat => 2
  | .fuel n => sparedWeb.level t (.fuel n)

/-- The dweller is not admitted at the third step, or the clearer is not. -/
def EitherEnded (l : Nat → Place → Nat) : Prop :=
  ¬ web.Admits (l 2) 2 .dweller ∨ ¬ web.Admits (l 2) 2 .clearer

def pair : Formation → Prop
  | .clearer => True
  | .dweller => True
  | .source => False

/-- C5. **Pooled testing.** In the spared world, neither the clearer nor the dweller refutes, at
the third step, that one of them is not admitted there; the two together do. -/
theorem pooled :
    ¬ web.Refutes supportOnly EitherEnded .clearer sparedWeb.level 2 ∧
      ¬ web.Refutes supportOnly EitherEnded .dweller sparedWeb.level 2 ∧
      RefutesBy web supportOnly EitherEnded pair sparedWeb.level 2 :=
  ⟨fun refutes => refutes web.level (.inl fun admits =>
      Nat.not_succ_le_zero 0 (admits .habitat trivial))
     (alike_for_clearer 2).symm,
   fun refutes => refutes resourceGone (.inr fun admits =>
      Nat.not_succ_le_zero 0 (admits .resource trivial))
     (fun s _ => ⟨⟨fun admits c requires => (match c, requires with
          | .habitat, _ => admits .habitat trivial
          | .resource, no => nomatch no
          | .fuel _, no => nomatch no),
         fun admits c requires => (match c, requires with
          | .habitat, _ => admits .habitat trivial
          | .resource, no => nomatch no
          | .fuel _, no => nomatch no)⟩, fun _ no => False.elim no⟩),
   fun l' meets all => match meets with
    | .inl dweller => dweller (((all .dweller trivial) 2 (Nat.le_refl 2)).1.mp
        fun c requires => match c, requires with
          | .habitat, _ => Nat.le_succ 1
          | .resource, no => nomatch no
          | .fuel _, no => nomatch no)
    | .inr clearer => clearer (((all .clearer trivial) 2 (Nat.le_refl 2)).1.mp
        fun c requires => match c, requires with
          | .resource, _ => Nat.le_refl 1
          | .habitat, no => nomatch no
          | .fuel _, no => nomatch no)⟩

end ClearingPooled

/-! ## D. The bridge to `Becoming.Inquiry` -/

open Generative.InquirySufficiency

/-- A formation's belief at `t`: the histories it registers alike with the actual up to `t`. -/
def Belief (W : Web F C) (obs : F → C → Prop) (g : F) (l : Nat → C → Nat) (t : Nat) :
    (Nat → C → Nat) → Prop :=
  fun l' => W.AlikeUpTo obs g l l' t

theorem belief_refutes_iff :
    W.Refutes obs claim g l t ↔ ∀ l', Belief W obs g l t l' → ¬ claim l' :=
  ⟨fun refutes l' believed meets => refutes l' meets believed,
   fun disjoint l' meets believed => disjoint l' believed meets⟩

variable {H : Type} {admissible : (Nat → C → Nat) → H → Prop} {a : H}

/-- A judgment from the formation's registration is a common response over its belief. -/
theorem belief_judge_iff :
    CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True) (fun a => [a])
        (sees (Belief W obs g l t)) a ↔ ∀ l', W.AlikeUpTo obs g l l' t → admissible l' a :=
  commonResponse_judge_iff

theorem sees_mono {X : Type} {B B' : X → Prop} (narrower : ∀ x, B' x → B x) :
    ∀ s, sees B' s → sees B s
  | _, ⟨x, believed, same⟩ => ⟨x, narrower x believed, same⟩

/-- Later steps narrow the belief and keep every common response. -/
theorem belief_judge_later {t' : Nat} (le : t ≤ t')
    (common : CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True)
      (fun a => [a]) (sees (Belief W obs g l t)) a) :
    CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True) (fun a => [a])
      (sees (Belief W obs g l t')) a :=
  commonResponse_antitone (sees_mono fun _ alike => alike.earlier le) common

/-- More observation narrows the belief and keeps every common response. -/
theorem belief_judge_widen {obs' : F → C → Prop} (larger : ∀ g c, obs g c → obs' g c)
    (common : CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True)
      (fun a => [a]) (sees (Belief W obs g l t)) a) :
    CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True) (fun a => [a])
      (sees (Belief W obs' g l t)) a :=
  commonResponse_antitone (sees_mono fun _ alike => alike.of_obs larger) common

/-- A judgment from within the registration closure cannot tell a part beyond it: every response
common to the belief is admissible both with and without the part. -/
theorem belief_judge_beyond {L : Flow F C} {part : F → Bool} (balances : L.Balances W)
    {l₀ : Nat → C → Nat} (without : L.WithheldLevels part W l₀) {f : F}
    (beyond : ∀ h, part h = true → ¬ L.WithinRegistration W obs f h)
    (within : L.WithinRegistration W obs f g)
    (common : CommonResponse (judgeProcess admissible) (fun _ _ _ => True) (fun _ => True)
      (fun a => [a]) (sees (Belief W obs g W.level t)) a) :
    admissible W.level a ∧ admissible l₀ a :=
  ⟨belief_judge_iff.mp common W.level fun s _ => Web.RegistersAlike.refl s,
   belief_judge_iff.mp common l₀ fun s _ =>
     balances.unregistered_beyond_registration without beyond s g within⟩

end Becoming.Review47

/-! ## E. The horizon dual -/

namespace Becoming.Renewable

/-- From `finite_reading_credits_consumption` alone, a sound reading does not credit every
renewing run. -/
theorem sound_not_complete (h : Nat) (reading : Run process → Prop)
    (decided : ∀ r r', r.AgreeUpTo h r' → reading r → reading r')
    (sound : ∀ r, reading r → ¬ (conditions.dependence.along r).ConsumingIn .focal) :
    ¬ ∀ r, (conditions.dependence.along r).RenewingIn .focal → reading r :=
  fun credits => match finite_reading_credits_consumption h reading decided credits with
    | ⟨r, consumes, reads⟩ => sound r reads consumes

/-- From `finite_reading_credits_consumption` alone, the witness of the dual holds up to double
negation (apply it to the doubly negated reading). -/
theorem withholds_not_not (h : Nat) (reading : Run process → Prop)
    (decided : ∀ r r', r.AgreeUpTo h r' → reading r → reading r')
    (sound : ∀ r, reading r → ¬ (conditions.dependence.along r).ConsumingIn .focal) :
    ¬ ¬ ∃ r, (conditions.dependence.along r).RenewingIn .focal ∧ ¬ reading r :=
  fun none => match finite_reading_credits_consumption h (fun r => ¬ ¬ reading r)
      (fun r r' agree unread unread' => unread fun reads => unread' (decided r r' agree reads))
      (fun r renews unread => none ⟨r, renews, unread⟩) with
    | ⟨r, consumes, reads⟩ => reads fun read => sound r read consumes

/-- No reading decided by a finite prefix is exactly the whole-run classification. -/
theorem no_exact_finite_reading (h : Nat) (reading : Run process → Prop)
    (decided : ∀ r r', r.AgreeUpTo h r' → reading r → reading r') :
    ¬ ∀ r, reading r ↔ (conditions.dependence.along r).RenewingIn .focal :=
  fun exact => sound_not_complete h reading decided
    (fun r reads => Web.renewing_not_consuming ((exact r).mp reads)) fun r => (exact r).mpr

end Becoming.Renewable

open Becoming.Review47
#print axioms refutes_iff_within_all
#print axioms RefutesWithin.narrow
#print axioms RefutesWithin.not_meets
#print axioms unrefuted_of_extension
#print axioms tail_untested
#print axioms model_refutes_tail
#print axioms Stationary.model_error
#print axioms Stationary.model_refuted
#print axioms refutesWithin_iff_conjunction
#print axioms beyond_needs_model
#print axioms ClearingModel.model_idles_registration
#print axioms RefutesBy.of_member
#print axioms ClearingPooled.pooled
#print axioms belief_refutes_iff
#print axioms belief_judge_iff
#print axioms belief_judge_later
#print axioms belief_judge_widen
#print axioms belief_judge_beyond
#print axioms Becoming.Renewable.sound_not_complete
#print axioms Becoming.Renewable.withholds_not_not
#print axioms Becoming.Renewable.no_exact_finite_reading
