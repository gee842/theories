import Becoming.Return

/-!
# Generation: arising, unceasing generation and renewal

The readings of `living` in `Becoming.Dependence` and `Becoming.Metaethics` read what an
event does not harm. None of them reads further generation. This module states the
second 生 of 生生 on webs of dependence and relates it to renewal.

* A formation *arises* across a step when it is not active before the step and is
  active after it (`Arises`). Generation is *unceasing* when some formation arises at
  arbitrarily late steps (`Unceasing`). The same formation may arise again: what does
  not cease is arising, not any particular form.
* A condition *rises* or *falls* across a step with its level. Every rise is *made by*
  some active formation renewing the condition when the unfolding has no source of
  renewal outside its formations (`RenewedBy`). A sun or a river is then one of the
  formations, not an outside.

Results:
* A finite family of conditions none of which rises from some step on pays for only
  finitely many events, when each such event at a step where none of them rises lowers
  one of them (`paid_finitely`). This is the descent principle of `Becoming.Renewal`
  applied to the family's total level.
* Unceasing generation needs renewal. If each arising at a step where no condition of a
  finite family rises lowers one of them, unceasing generation makes some condition of
  the family rise at arbitrarily late steps (`Unceasing.rises`). When every rise is made
  by a formation renewing it, renewing activity recurs (`Unceasing.regeneration_recurs`).
* Substitution defers the end and does not escape it. A formation that at each of its
  active steps lowers some condition of a finite family, none of which rises any more,
  is active only finitely often, however it moves its dependence among them
  (`substitution_defers`, witness `Relay`).
* A finite family whose total level never rises, every renewal within it being paid
  within it, cannot sustain unceasing generation that lowers that total
  (`conserved_ceases`).
* Renewal does not imply generation: drawing exactly what is renewed keeps every
  dependence and nothing ever arises (`Commons.renewal_without_generation`).
* Generation by consumption ceases: formations arise while drawing an unrenewed
  condition down, consume it, and generation stops (`Growth.ceases`).
* Unceasing generation is consistent with these premises: a formation arises again and
  again on a condition that another formation renews (`Bloom.unceasing`). The working
  stepwise reading withholds every bloom, which draws its condition below its own need
  until the next renewal, while the reading over cycles of two credits it
  (`Bloom.readings`).

So, under the premises stated, unceasing generation is strictly stronger than recurring
renewal. The premises are correspondence claims about an application: that every rise
is made by some formation within the unfolding, that arising is paid by a fall at steps
without renewal, and that the conditions concerned are finitely many. No ethical
predicate, ranking or axiom occurs. "More" generation, diversity and complexity are not
stated here.
-/

namespace Becoming

/-- The total of a quantity over a finite list. -/
def total {α : Type} : List α → (α → Nat) → Nat
  | [], _ => 0
  | a :: as, q => q a + total as q

variable {F C : Type}

namespace Web

variable (W : Web F C)

/-- A formation arises across the step from `t`: not active at `t`, active after it. -/
def Arises (t : Nat) (f : F) : Prop :=
  ¬ W.active t f ∧ W.active (t + 1) f

/-- Generation does not cease: some formation arises at arbitrarily late steps. -/
def Unceasing : Prop :=
  ∀ N, ∃ t f, N ≤ t ∧ W.Arises t f

/-- The condition rises across the step from `t`. -/
def Rises (t : Nat) (c : C) : Prop :=
  W.level t c < W.level (t + 1) c

/-- The condition falls across the step from `t`. -/
def Falls (t : Nat) (c : C) : Prop :=
  W.level (t + 1) c < W.level t c

/-- No condition of the family rises across the step from `t`. -/
def Still (cs : List C) (t : Nat) : Prop :=
  ∀ c, c ∈ cs → ¬ W.Rises t c

/-- At a step where no condition of the family rises, the event lowers one of them. -/
def Paid (cs : List C) (event : Nat → Prop) : Prop :=
  ∀ t, event t → W.Still cs t → ∃ c, c ∈ cs ∧ W.Falls t c

/-- Every rise of a condition is made by some active formation renewing it. -/
def RenewedBy (renews : Nat → F → C → Prop) : Prop :=
  ∀ t c, W.Rises t c → ∃ f, W.active t f ∧ renews t f c

/-- An active formation renews a condition of the family. -/
def Regenerating (renews : Nat → F → C → Prop) (cs : List C) (t : Nat) (f : F) : Prop :=
  W.active t f ∧ ∃ c, c ∈ cs ∧ renews t f c

/-- The total level of a finite family of conditions. -/
def stock (cs : List C) (t : Nat) : Nat :=
  total cs (W.level t)

/-- When no condition of the family rises, the total does not rise. -/
theorem stock_le {t : Nat} : ∀ cs : List C, W.Still cs t → W.stock cs (t + 1) ≤ W.stock cs t
  | [], _ => Nat.le_refl 0
  | c :: cs, still =>
    Nat.add_le_add (Nat.ge_of_not_lt (still c (.head cs)))
      (stock_le cs fun d mem => still d (.tail c mem))

/-- When no condition of the family rises and one falls, the total falls. -/
theorem stock_lt {t : Nat} : ∀ cs : List C, W.Still cs t → (∃ c, c ∈ cs ∧ W.Falls t c) →
    W.stock cs (t + 1) < W.stock cs t
  | c :: cs, still, ⟨_, .head _, falls⟩ =>
    Nat.add_lt_add_of_lt_of_le falls (W.stock_le cs fun d mem => still d (.tail c mem))
  | c :: cs, still, ⟨d, .tail _ mem, falls⟩ =>
    Nat.add_lt_add_of_le_of_lt (Nat.ge_of_not_lt (still c (.head cs)))
      (stock_lt cs (fun e mem => still e (.tail c mem)) ⟨d, mem, falls⟩)

/-- A finite family of conditions none of which rises from step `T` on pays for only
finitely many events. -/
theorem paid_finitely (cs : List C) (T : Nat) (event : Nat → Prop)
    (still : ∀ t, T ≤ t → W.Still cs t) (paid : W.Paid cs event) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ event t :=
  fun recurs => falls_finitely (W.stock cs) T (fun t after => W.stock_le cs (still t after))
    fun N => match recurs (N + T) with
      | ⟨t, later, happens⟩ =>
        have after : T ≤ t := Nat.le_trans (Nat.le_add_left T N) later
        ⟨t, Nat.le_trans (Nat.le_add_right N T) later,
          W.stock_lt cs (still t after) (paid t happens (still t after))⟩

/-- Unceasing generation needs renewal: when arising is paid by a finite family of
conditions, some condition of the family rises at arbitrarily late steps. -/
theorem Unceasing.rises {cs : List C} (paid : W.Paid cs fun t => ∃ f, W.Arises t f)
    (unceasing : W.Unceasing) (T : Nat) : ¬ ∀ t, T ≤ t → W.Still cs t :=
  fun still => W.paid_finitely cs T _ still paid
    fun N => match unceasing N with
      | ⟨t, f, later, arises⟩ => ⟨t, later, f, arises⟩

/-- When every rise is made by a formation renewing the condition, unceasing generation
paid by a finite family makes renewing activity recur. -/
theorem Unceasing.regeneration_recurs {renews : Nat → F → C → Prop} {cs : List C}
    (made : W.RenewedBy renews) (paid : W.Paid cs fun t => ∃ f, W.Arises t f)
    (unceasing : W.Unceasing) (T : Nat) :
    ¬ ∀ t, T ≤ t → ∀ f, ¬ W.Regenerating renews cs t f :=
  fun none => Unceasing.rises W paid unceasing T fun t after c mem rises =>
    match made t c rises with
    | ⟨f, active, renewing⟩ => none t after f ⟨active, c, mem, renewing⟩

/-- Substitution defers the end and does not escape it: a formation lowering some
condition of a finite family at each of its active steps, while none of them rises, is
active only finitely often. -/
theorem substitution_defers (cs : List C) (f : F) (T : Nat)
    (still : ∀ t, T ≤ t → W.Still cs t) (draws_down : W.Paid cs fun t => W.active t f) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ W.active t f :=
  W.paid_finitely cs T _ still draws_down

/-- A finite family whose total never rises cannot sustain unceasing generation that
lowers its total. -/
theorem conserved_ceases (cs : List C) (conserved : ∀ t, W.stock cs (t + 1) ≤ W.stock cs t)
    (costly : ∀ t f, W.Arises t f → W.stock cs (t + 1) < W.stock cs t) : ¬ W.Unceasing :=
  fun unceasing => falls_finitely (W.stock cs) 0 (fun t _ => conserved t)
    fun N => match unceasing N with
      | ⟨t, f, later, arises⟩ => ⟨t, later, costly t f arises⟩

end Web

/-! ## Renewal does not imply generation -/

namespace Commons

/-- Drawing exactly what is renewed keeps every dependence, and nothing ever arises. -/
theorem renewal_without_generation :
    (conditions.dependence.along sharing).Renewed () ∧
    ∀ t f, ¬ (conditions.dependence.along sharing).Arises t f :=
  ⟨fun _ g depends => match g, depends with
    | .sustaining, _ => ⟨Nat.le_refl 1, Nat.le_refl 1⟩,
   fun _ f ⟨inactive, _⟩ => match f with
    | .focal => inactive trivial
    | .sustaining => inactive (Nat.le_refl 1)⟩

end Commons

/-! ## Generation by consumption ceases -/

namespace Growth

/-- Three units, no renewal; each step takes one until none is left. -/
def left : Nat → Nat
  | 0 => 3
  | 1 => 2
  | 2 => 1
  | _ + 3 => 0

/-- Cell `n` is active after step `n` while the condition supports it: cells 0 and 1
arise, and the condition is gone before cell 2 can. -/
def web : Web Nat Unit where
  level t _ := left t
  active t n := n < t ∧ 1 ≤ left t
  requires _ _ _ := True
  need _ _ _ := 1
  draws t n _ := n < t ∧ 1 ≤ left t

theorem left_succ_le : ∀ t, left (t + 1) ≤ left t
  | 0 => Nat.le_succ 2
  | 1 => Nat.le_succ 1
  | 2 => Nat.le_succ 0
  | _ + 3 => Nat.le_refl 0

theorem left_late : ∀ t, 3 ≤ t → left t = 0
  | _ + 3, _ => rfl

/-- Cells arise while drawing the condition down; the condition is consumed and
generation stops. -/
theorem ceases :
    web.Dependent ∧ web.Arises 0 0 ∧ web.Arises 1 1 ∧ web.ConsumingIn 0 ∧
    (∀ t, ¬ web.Rises t ()) ∧ ¬ web.Unceasing :=
  have still : ∀ t, web.Still [()] t := fun t _ _ rises =>
    Nat.not_le_of_gt rises (left_succ_le t)
  have paid : web.Paid [()] fun t => ∃ n, web.Arises t n :=
    fun t ⟨_, _, active⟩ _ => ⟨(), .head [], match t, active with
      | 0, _ => Nat.lt_succ_self 2
      | 1, _ => Nat.lt_succ_self 1
      | 2, ⟨_, one⟩ => absurd one (Nat.not_succ_le_zero 0)
      | _ + 3, ⟨_, one⟩ => absurd one (Nat.not_succ_le_zero 0)⟩
  ⟨fun _ _ ⟨_, supported⟩ _ _ => supported,
   ⟨Nat.lt_irrefl 0 ∘ And.left, Nat.zero_lt_one, Nat.le_succ 1⟩,
   ⟨Nat.lt_irrefl 1 ∘ And.left, Nat.lt_succ_self 1, Nat.le_refl 1⟩,
   ⟨1, (), ⟨Nat.zero_lt_one, Nat.le_succ 1⟩, 0, 3, trivial,
     fun t later => (left_late t (Nat.le_of_lt later)).symm ▸ Nat.zero_lt_one⟩,
   fun t rises => still t () (.head []) rises,
   fun unceasing => Web.Unceasing.rises web paid unceasing 0 fun t _ => still t⟩

end Growth

/-! ## Substitution among costly conditions ends -/

namespace Relay

inductive Source where
  | first
  | second

/-- One unit in each source: the first is drawn at step 0, the second at step 1. -/
def reserve : Nat → Source → Nat
  | 0, _ => 1
  | 1, .first => 0
  | 1, .second => 1
  | _ + 2, _ => 0

/-- The consumer depends on the first source at step 0 and on the second afterwards. -/
def dependsOn : Nat → Source → Prop
  | 0, .first => True
  | 0, .second => False
  | _ + 1, .first => False
  | _ + 1, .second => True

/-- The source the consumer depends on at each step. -/
def source : Nat → Source
  | 0 => .first
  | _ + 1 => .second

/-- The consumer is active while the source it depends on supports it, and draws on it. -/
def web : Web Unit Source where
  level := reserve
  active t _ := 1 ≤ reserve t (source t)
  requires t _ c := dependsOn t c
  need _ _ _ := 1
  draws t _ c := dependsOn t c ∧ 1 ≤ reserve t (source t)

theorem reserve_succ_le : ∀ t c, reserve (t + 1) c ≤ reserve t c
  | 0, .first => Nat.zero_le 1
  | 0, .second => Nat.le_refl 1
  | 1, _ => Nat.zero_le _
  | _ + 2, _ => Nat.le_refl 0

/-- The consumer transforms its dependence from the first source to the second, and
ends: with no renewal of either, substitution defers the end and does not escape it. -/
theorem defers :
    web.Dependent ∧ web.active 0 () ∧ web.active 1 () ∧
    web.Dissolves 0 () .first ∧ web.Forms 0 () .second ∧ web.ConsumingIn () ∧
    (∀ t, 2 ≤ t → ¬ web.active t ()) ∧ ¬ ∀ N, ∃ t, N ≤ t ∧ web.active t () :=
  have still : ∀ t, web.Still [.first, .second] t := fun t c _ rises =>
    Nat.not_le_of_gt rises (reserve_succ_le t c)
  have paid : web.Paid [.first, .second] fun t => web.active t () := fun t active _ =>
    match t, active with
    | 0, _ => ⟨.first, .head _, Nat.zero_lt_one⟩
    | 1, _ => ⟨.second, .tail _ (.head _), Nat.zero_lt_one⟩
    | _ + 2, active => absurd active (Nat.not_succ_le_zero 0)
  ⟨fun t _ active c depends => match t, c, depends with
    | 0, .first, _ => active
    | _ + 1, .second, _ => active,
   Nat.le_refl 1, Nat.le_refl 1, ⟨trivial, id⟩, ⟨id, trivial⟩,
   ⟨0, .first, ⟨trivial, Nat.le_refl 1⟩, (), 0, trivial, fun t later => match t, later with
     | 1, _ => Nat.zero_lt_one
     | _ + 2, _ => Nat.zero_lt_one⟩,
   fun t late active => match t, late with
     | _ + 2, _ => Nat.not_succ_le_zero 0 active,
   web.substitution_defers [.first, .second] () 0 (fun t _ => still t) paid⟩

end Relay

/-! ## Unceasing generation on a renewed condition -/

namespace Bloom

inductive Formation where
  | sun
  | bloom

/-- Two at even steps and one at odd steps: the bloom takes two when it is active, and
the sun gives one at every step. -/
def glow : Nat → Nat
  | 0 => 2
  | 1 => 1
  | n + 2 => glow n

theorem glow_even : ∀ n, glow (2 * n) = 2
  | 0 => rfl
  | n + 1 => glow_even n

theorem glow_odd : ∀ n, glow (2 * n + 1) = 1
  | 0 => rfl
  | n + 1 => glow_odd n

/-- The sun is always active and depends on nothing here. The bloom is active where the
condition reaches its need of two, depends on it, and draws on it when active. -/
def web : Web Formation Unit where
  level t _ := glow t
  active t f := match f with
    | .sun => True
    | .bloom => 2 ≤ glow t
  requires _ f _ := match f with
    | .sun => False
    | .bloom => True
  need _ _ _ := 2
  draws t f _ := match f with
    | .sun => False
    | .bloom => 2 ≤ glow t

/-- Within two steps the condition is back at two. -/
theorem back : ∀ t, 2 ≤ glow (t + 1) ∨ 2 ≤ glow (t + 2)
  | 0 => .inr (Nat.le_refl 2)
  | 1 => .inl (Nat.le_refl 2)
  | t + 2 => back t

/-- The sun renews the condition. -/
def renews (_ : Nat) (f : Formation) (_ : Unit) : Prop :=
  match f with
  | .sun => True
  | .bloom => False

/-- Every premise of `Unceasing.regeneration_recurs` holds, and the bloom arises at every
odd step: generation does not cease, and the sun's renewing recurs. -/
theorem unceasing :
    web.Dependent ∧ web.RenewedBy renews ∧ web.Paid [()] (fun t => ∃ f, web.Arises t f) ∧
    web.Unceasing ∧ ∀ T, ¬ ∀ t, T ≤ t → ∀ f, ¬ web.Regenerating renews [()] t f :=
  have paid : web.Paid [()] fun t => ∃ f, web.Arises t f :=
    fun _ ⟨f, inactive, active⟩ still => match f, inactive, active with
    | .sun, inactive, _ => absurd trivial inactive
    | .bloom, inactive, active =>
      absurd (Nat.lt_of_lt_of_le (Nat.gt_of_not_le inactive) active) (still () (.head []))
  have made : web.RenewedBy renews := fun _ _ _ => ⟨.sun, trivial, trivial⟩
  have unceasing : web.Unceasing := fun N =>
    ⟨2 * N + 1, .bloom, Nat.le_succ_of_le (Nat.le_mul_of_pos_left N Nat.zero_lt_two),
      fun two => Nat.not_succ_le_self 1
        (Nat.le_trans (show 2 ≤ glow (2 * N + 1) from two) (Nat.le_of_eq (glow_odd N))),
      show 2 ≤ glow (2 * (N + 1)) from (glow_even (N + 1)).symm ▸ Nat.le_refl 2⟩
  ⟨fun _ f active _ depends => match f, active, depends with
    | .bloom, active, _ => active,
   made, paid, unceasing, Web.Unceasing.regeneration_recurs web made paid unceasing⟩

/-- The working stepwise reading withholds every bloom: each draws its condition below
its own need, which the sun restores by the next bloom. The reading over cycles of two
credits the bloom. -/
theorem readings :
    (∀ n, web.UnderminingAt (2 * n) .bloom) ∧ web.RenewingInWithin 2 .bloom :=
  ⟨fun n => have two : 2 ≤ glow (2 * n) := (glow_even n).symm ▸ Nat.le_refl 2
    ⟨(), two, .bloom, trivial, Web.MetSince.now trivial two,
      show glow (2 * n + 1) < 2 from Nat.lt_of_le_of_lt (Nat.le_of_eq (glow_odd n))
        (Nat.lt_succ_self 1)⟩,
   fun _ _ _ t g depends => match g, depends, back t with
    | .bloom, _, .inl one => ⟨1, Nat.zero_lt_one, Nat.le_succ 1, one⟩
    | .bloom, _, .inr two => ⟨2, Nat.zero_lt_two, Nat.le_refl 2, two⟩⟩

end Bloom

end Becoming
