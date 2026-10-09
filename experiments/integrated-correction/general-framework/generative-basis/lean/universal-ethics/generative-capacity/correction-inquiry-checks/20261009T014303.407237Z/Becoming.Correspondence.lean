import Becoming.Metaethics

/-!
# Which conditions relate: a correspondence discipline

The readings of `Becoming.Metaethics` count co-participation in a condition as a
formed relation. Connection is then cheap: adjoining a condition that every formation
requires at level zero leaves `living` unchanged and connects any web (`inert_connects`;
Q4 of the independent review). A dependence at level zero is met at every level, and a
condition nothing draws on is changed by no formation's activity. Neither relates one
formation to another.

The discipline stated here relates two events through a condition only when one draws
on it and the other depends on it at a positive level, so that the first's drawing bears
on the second's support (`Interacts`). A condition that no activity draws on, or no
dependence on which can fail, is `Idle`. The living events are those of the stepwise
reading; only the relation changes (`Web.interaction`).

Results:
* An idle condition relates nothing and undermines nothing. Adjoining one leaves
  `living`, the relation and connection unchanged (`adjoin_connected_iff`), so the free
  connection of Q4 is excluded (`inert_connects`).
* Every undermining relation is an interaction (`UnderminingOn.interacts`): the stepwise
  reading of `living` withholds an event through this relation. Under N_rel, valuing an
  undermining event reaches the living events of the formation whose support it
  undermines (`valuing_undermining_reaches`).
* A condition on which every living event bears, with a living drawer and a living
  dependent, connects the whole in at most two interactions (`connected_of_commons`). G0
  there is exactly a seed with N_rel and N_std (`significant_iff_of_commons`).
* Connection through a condition is made by its living use (`Shared`): two formations
  depending on one condition are connected through its use while the use keeps their
  support, and not when the only use undermines it. Co-participation connects them in
  both runs.

Not settled:
* Adjoining a renewed condition that every formation draws on and depends on at a
  positive level still connects any web without changing `living`
  (`universal_connects`). Its content is the claim that every formation actually draws on
  and depends on it, which the web does not check. The discipline turns free connection
  into this claim; the correspondence remains an application duty.
* A coarse common condition whose dependence fails still withholds the events drawing on
  it at that step (Q10). The discipline changes relations, not `living`.
* Like co-participation, interaction does not order the two events in time.
* The discipline is stated with the stepwise reading of `living`. On fixed dependences
  it applies to `K.dependence.along r`; the whole-run reading could take the same
  relation, which is not done here.

The discipline is a disclosed correspondence choice, not a consequence of the
unfolding; no ethical predicate is added. Every declaration has an empty axiom report.
-/

namespace Becoming

/-- Connection carries over to a valuation with the same living claims and at least
the same relations. -/
theorem Valuation.Connected.transfer {Pos C : Type} {V V' : Valuation Pos C}
    (living : ∀ c, V.living c ↔ V'.living c) (related : ∀ c d, V.related c d → V'.related c d)
    (connected : V.Connected) : V'.Connected :=
  fun c d alive alive' =>
    Reach.map (P := V.relations) (Q := V'.relations) (f := id)
      (fun _ _ _ step => ⟨related _ _ step.1, (living _).mp step.2⟩)
      (connected c d ((living c).mpr alive) ((living d).mpr alive'))

namespace Web

variable {F C Pos : Type} (W : Web F C)

/-- `g` depends on `c` at `t` at a positive level, so the condition can fail it. A
dependence at level zero is met at every level. -/
def Bearing (t : Nat) (g : F) (c : C) : Prop :=
  W.requires t g c ∧ 0 < W.need t g c

/-- Two events interact through a condition when one draws on it and the other depends
on it at a positive level: the first's drawing bears on the second's support. -/
def Interacts (c : C) (e e' : F × Nat) : Prop :=
  (W.draws e.2 e.1 c ∧ W.Bearing e'.2 e'.1 c) ∨ (W.Bearing e.2 e.1 c ∧ W.draws e'.2 e'.1 c)

/-- No activity draws on the condition, or no dependence on it can fail: it carries no
interaction. -/
def Idle (c : C) : Prop :=
  (∀ t f, ¬ W.draws t f c) ∨ ∀ t g, ¬ W.Bearing t g c

/-- Formation events of a web read stepwise, related only through interaction. The
living events are those of `Web.valuation`: active and not undermining. Standpoints,
their regions and significance remain supplied. -/
def interaction (own sig : Pos → F × Nat → Prop) : Valuation Pos (F × Nat) where
  living e := W.active e.2 e.1 ∧ ¬ W.UnderminingAt e.2 e.1
  related e e' := ∃ c, W.Interacts c e e'
  own := own
  sig := sig

variable {W}

theorem Interacts.symm {c : C} {e e' : F × Nat} : W.Interacts c e e' → W.Interacts c e' e
  | .inl ⟨drawn, bearing⟩ => .inr ⟨bearing, drawn⟩
  | .inr ⟨bearing, drawn⟩ => .inl ⟨drawn, bearing⟩

/-- Interacting events co-participate in the condition. -/
theorem Interacts.participates {c : C} {e e' : F × Nat} :
    W.Interacts c e e' → W.Participates e.2 e.1 c ∧ W.Participates e'.2 e'.1 c
  | .inl ⟨drawn, bearing⟩ => ⟨.inr drawn, .inl bearing.1⟩
  | .inr ⟨bearing, drawn⟩ => ⟨.inl bearing.1, .inr drawn⟩

theorem Idle.not_interacts {c : C} (idle : W.Idle c) (e e' : F × Nat) :
    ¬ W.Interacts c e e' :=
  match idle with
  | .inl undrawn => fun
    | .inl ⟨drawn, _⟩ => undrawn _ _ drawn
    | .inr ⟨_, drawn⟩ => undrawn _ _ drawn
  | .inr unbearing => fun
    | .inl ⟨_, bearing⟩ => unbearing _ _ bearing
    | .inr ⟨bearing, _⟩ => unbearing _ _ bearing

/-- An undermining relation is an interaction: the drawing event interacts with the
event of a formation whose dependence it undermines. -/
theorem UnderminingOn.interacts {t : Nat} {f : F} {c : C} :
    W.UnderminingOn t f c → ∃ g, W.Bearing t g c ∧ W.Interacts c (f, t) (g, t)
  | ⟨drawn, g, depends, _, fell⟩ =>
    have bearing : W.Bearing t g c := ⟨depends, Nat.lt_of_le_of_lt (Nat.zero_le _) fell⟩
    ⟨g, bearing, .inl ⟨drawn, bearing⟩⟩

theorem Idle.not_undermining {c : C} (idle : W.Idle c) (t : Nat) (f : F) :
    ¬ W.UnderminingOn t f c :=
  fun undermining => match undermining.interacts with
    | ⟨g, _, interacts⟩ => idle.not_interacts (f, t) (g, t) interacts

variable (W) (own sig : Pos → F × Nat → Prop)

/-- The discipline narrows co-participation and keeps the living events. -/
theorem interaction_narrows (e e' : F × Nat) :
    ((W.interaction own sig).living e ↔ (W.valuation own sig).living e) ∧
      ((W.interaction own sig).related e e' → (W.valuation own sig).related e e') :=
  ⟨Iff.rfl, fun ⟨c, interacts⟩ => ⟨c, interacts.participates⟩⟩

theorem interacts_reach {c : C} {e e' : F × Nat} (interacts : W.Interacts c e e')
    (alive : (W.interaction own sig).living e') :
    Reach (W.interaction own sig).relations e e' :=
  Reach.of_step (a := ()) ⟨⟨c, interacts⟩, alive⟩

/-- A condition on which every living event bears, with a living event drawing on it
and a living event depending on it at a positive level, connects the whole: every two
living events are linked in at most two interactions. -/
theorem connected_of_commons (c₀ : C)
    (bears : ∀ e, (W.interaction own sig).living e →
      W.draws e.2 e.1 c₀ ∨ W.Bearing e.2 e.1 c₀)
    {d g : F × Nat} (aliveD : (W.interaction own sig).living d) (drawn : W.draws d.2 d.1 c₀)
    (aliveG : (W.interaction own sig).living g) (bearing : W.Bearing g.2 g.1 c₀) :
    (W.interaction own sig).Connected :=
  fun e e' alive alive' => match bears e alive, bears e' alive' with
    | .inl drawsE, .inr bearsE' => interacts_reach W own sig (.inl ⟨drawsE, bearsE'⟩) alive'
    | .inr bearsE, .inl drawsE' => interacts_reach W own sig (.inr ⟨bearsE, drawsE'⟩) alive'
    | .inl drawsE, .inl drawsE' =>
      (interacts_reach W own sig (.inl ⟨drawsE, bearing⟩) aliveG).trans
        (interacts_reach W own sig (.inr ⟨bearing, drawsE'⟩) alive')
    | .inr bearsE, .inr bearsE' =>
      (interacts_reach W own sig (.inr ⟨bearsE, drawn⟩) aliveD).trans
        (interacts_reach W own sig (.inl ⟨drawn, bearsE'⟩) alive')

/-- With such a condition, G0 for every standpoint is exactly a seed with N_rel and
N_std under the discipline. -/
theorem significant_iff_of_commons (c₀ : C)
    (bears : ∀ e, (W.interaction own sig).living e →
      W.draws e.2 e.1 c₀ ∨ W.Bearing e.2 e.1 c₀)
    {d g : F × Nat} (aliveD : (W.interaction own sig).living d) (drawn : W.draws d.2 d.1 c₀)
    (aliveG : (W.interaction own sig).living g) (bearing : W.Bearing g.2 g.1 c₀) (p₀ : Pos) :
    (W.interaction own sig).Significant ↔ (W.interaction own sig).Grounds :=
  Valuation.significant_iff (connected_of_commons W own sig c₀ bears aliveD drawn aliveG bearing)
    p₀ aliveD

/-- Under N_rel, a standpoint that values an undermining event holds significant every
living event of a formation it undermines, at every step where that formation depends
on the condition at a positive level. The undermining event is not living, so S0 alone
supplies no such valuation. -/
theorem valuing_undermining_reaches (transmit : Neutral (W.interaction own sig).transmits)
    {t : Nat} {f : F} {c : C} (undermining : W.UnderminingOn t f c) :
    ∃ g, W.Bearing t g c ∧ ∀ p, (W.interaction own sig).sig p (f, t) →
      ∀ t', W.Bearing t' g c → (W.interaction own sig).living (g, t') →
        (W.interaction own sig).sig p (g, t') :=
  match undermining with
  | ⟨drawn, g, depends, _, fell⟩ =>
    ⟨g, ⟨depends, Nat.lt_of_le_of_lt (Nat.zero_le _) fell⟩, fun p held t' bearing alive =>
      transmit (p, (f, t), (g, t')) held ⟨c, .inl ⟨drawn, bearing⟩⟩ alive⟩

/-! ## Adjoining a condition -/

/-- One condition read along the steps: its levels, and the formations depending on it
(at what level) and drawing on it. -/
structure Condition (F : Type) where
  level : Nat → Nat
  requires : Nat → F → Prop
  need : Nat → F → Nat
  draws : Nat → F → Prop

/-- The web with one more condition; the formations and their activity are unchanged. -/
def adjoin (k : Condition F) : Web F (Option C) where
  level t c := match c with
    | none => k.level t
    | some c => W.level t c
  active := W.active
  requires t f c := match c with
    | none => k.requires t f
    | some c => W.requires t f c
  need t f c := match c with
    | none => k.need t f
    | some c => W.need t f c
  draws t f c := match c with
    | none => k.draws t f
    | some c => W.draws t f c

variable {W own sig}

/-- Adjoining a condition that is never undermined leaves the living events unchanged. -/
theorem adjoin_living {k : Condition F}
    (never : ∀ t f, ¬ (W.adjoin k).UnderminingOn t f none) (e : F × Nat) :
    ((W.adjoin k).interaction own sig).living e ↔ (W.interaction own sig).living e :=
  ⟨fun ⟨active, notUndermining⟩ => ⟨active, fun ⟨c, undermining⟩ =>
      notUndermining ⟨some c, undermining⟩⟩,
   fun ⟨active, notUndermining⟩ => ⟨active, fun ⟨c, undermining⟩ => match c, undermining with
      | none, undermining => never e.2 e.1 undermining
      | some c, undermining => notUndermining ⟨c, undermining⟩⟩⟩

/-- Adjoining an idle condition changes neither the living events nor the relation, so
neither connection. -/
theorem adjoin_connected_iff {k : Condition F} (idle : (W.adjoin k).Idle none) :
    ((W.adjoin k).interaction own sig).Connected ↔ (W.interaction own sig).Connected :=
  have living := adjoin_living (own := own) (sig := sig) (idle.not_undermining · ·)
  ⟨Valuation.Connected.transfer living fun _ _ ⟨c, interacts⟩ => match c, interacts with
      | none, interacts => absurd interacts (idle.not_interacts _ _)
      | some c, interacts => ⟨c, interacts⟩,
   Valuation.Connected.transfer (fun e => (living e).symm) fun _ _ ⟨c, interacts⟩ =>
      ⟨some c, interacts⟩⟩

/-- A condition every formation requires at level zero, which nothing draws on. -/
def Condition.inert : Condition F :=
  ⟨fun _ => 0, fun _ _ => True, fun _ _ => 0, fun _ _ => False⟩

/-- A condition held at level one, which every formation draws on and depends on at
level one. -/
def Condition.universal : Condition F :=
  ⟨fun _ => 1, fun _ _ => True, fun _ _ => 1, fun _ _ => True⟩

variable (W own sig)

/-- Q4 under the discipline. Adjoining the inert condition leaves the living events
unchanged and connects every web through co-participation; through interaction,
connection is unchanged. -/
theorem inert_connects :
    (∀ e, ((W.adjoin .inert).valuation own sig).living e ↔ (W.valuation own sig).living e) ∧
    ((W.adjoin .inert).valuation own sig).Connected ∧
    (((W.adjoin .inert).interaction own sig).Connected ↔ (W.interaction own sig).Connected) :=
  have idle : (W.adjoin .inert).Idle none := .inl fun _ _ drawn => drawn
  ⟨adjoin_living (own := own) (sig := sig) (idle.not_undermining · ·),
   Web.connected_of_common (W.adjoin .inert) own sig none fun _ _ => .inl trivial,
   adjoin_connected_iff idle⟩

/-- What the discipline does not settle. Adjoining a renewed condition that every
formation draws on and depends on at a positive level leaves the living events
unchanged and connects every web through interaction. Its content is that every
formation draws on and depends on it. -/
theorem universal_connects :
    (W.adjoin .universal).Renewed none ∧
    (∀ e, ((W.adjoin .universal).interaction own sig).living e ↔
      (W.interaction own sig).living e) ∧
    ((W.adjoin .universal).interaction own sig).Connected :=
  ⟨fun _ _ _ => ⟨Nat.le_refl 1, Nat.le_refl 1⟩,
   adjoin_living fun _ _ ⟨_, _, _, _, fell⟩ => Nat.lt_irrefl 1 fell,
   fun _ _ _ alive' =>
     interacts_reach (W.adjoin .universal) own sig (c := none)
       (.inl ⟨trivial, trivial, Nat.zero_lt_one⟩) alive'⟩

end Web

/-! ## Connection is made by living use -/

namespace Shared

inductive Formation where
  | user
  | first
  | second

/-- The user is active at the first step only. -/
def atStart : Nat → Prop
  | 0 => True
  | _ + 1 => False

/-- The condition stays at level one. -/
def steady : Nat → Nat := fun _ => 1

/-- The condition falls to zero after the first step. -/
def falling : Nat → Nat
  | 0 => 1
  | _ + 1 => 0

/-- Two formations depend on one condition at level one and are active while it meets
their need; a third draws on it at the first step. -/
def web (level : Nat → Nat) : Web Formation Unit where
  level t _ := level t
  active t f := match f with
    | .user => atStart t
    | .first => 1 ≤ level t
    | .second => 1 ≤ level t
  requires _ f _ := match f with
    | .user => False
    | .first => True
    | .second => True
  need _ _ _ := 1
  draws t f _ := match f with
    | .user => atStart t
    | .first => False
    | .second => False

theorem dependent (level : Nat → Nat) : (web level).Dependent
  | _, .user, _, _, depends => False.elim depends
  | _, .first, active, _, _ => active
  | _, .second, active, _, _ => active

/-- Every active event takes part in the condition. -/
theorem participates (level : Nat → Nat) :
    ∀ e : Formation × Nat, (web level).active e.2 e.1 → (web level).Participates e.2 e.1 ()
  | (.user, _), active => .inr active
  | (.first, _), _ => .inl trivial
  | (.second, _), _ => .inl trivial

/-- The user's drawing breaks the dependents' support in the falling run. -/
theorem user_undermines : (web falling).UnderminingAt 0 .user :=
  ⟨(), trivial, .first, trivial, ⟨0, Nat.le_refl 0, fun _ _ _ => trivial, Nat.le_refl 1⟩,
    Nat.zero_lt_one⟩

/-- In the falling run no living event draws on the condition: the only drawing event
undermines. -/
theorem no_living_drawer (own sig : Unit → Formation × Nat → Prop) :
    ∀ e : Formation × Nat, ((web falling).interaction own sig).living e →
      ¬ (web falling).draws e.2 e.1 ()
  | (.user, 0), alive, _ => alive.2 user_undermines
  | (.user, _ + 1), _, drawn => drawn
  | (.first, _), _, drawn => drawn
  | (.second, _), _, drawn => drawn

/-- No event of the first formation interacts with a living event: it draws on nothing,
and no living event draws. -/
theorem first_isolated (own sig : Unit → Formation × Nat → Prop) :
    Invariant ((web falling).interaction own sig).relations (fun e => e.1 = .first) :=
  fun x _ y ⟨⟨_, interacts⟩, alive⟩ isFirst => match interacts with
    | .inl ⟨drawn, _⟩ => False.elim (isFirst ▸ drawn : (web falling).draws x.2 .first ())
    | .inr ⟨_, drawn⟩ => absurd drawn (no_living_drawer own sig y alive)

/-- The two dependents are connected through the condition's use while the use keeps
their support, and not when the only use undermines it; co-participation connects them
in both runs. -/
theorem connection_by_living_use (own sig : Unit → Formation × Nat → Prop) :
    ((web steady).interaction own sig).Connected ∧
    ((web falling).interaction own sig).living (.first, 0) ∧
    ((web falling).interaction own sig).living (.second, 0) ∧
    ¬ ((web falling).interaction own sig).Connected ∧
    ((web steady).valuation own sig).Connected ∧
    ((web falling).valuation own sig).Connected :=
  have bears : ∀ e, ((web steady).interaction own sig).living e →
      (web steady).draws e.2 e.1 () ∨ (web steady).Bearing e.2 e.1 ()
    | (.user, _), alive => .inl alive.1
    | (.first, _), _ => .inr ⟨trivial, Nat.zero_lt_one⟩
    | (.second, _), _ => .inr ⟨trivial, Nat.zero_lt_one⟩
  have aliveUser : ((web steady).interaction own sig).living (.user, 0) :=
    ⟨trivial, fun ⟨_, _, _, _, _, fell⟩ => Nat.lt_irrefl 1 fell⟩
  have aliveFirst : ((web steady).interaction own sig).living (.first, 0) :=
    ⟨Nat.le_refl 1, fun ⟨_, drawn, _⟩ => drawn⟩
  have aliveFalling : ∀ f, f ≠ Formation.user →
      ((web falling).interaction own sig).living (f, 0)
    | .user, notUser => absurd rfl notUser
    | .first, _ => ⟨Nat.le_refl 1, fun ⟨_, drawn, _⟩ => drawn⟩
    | .second, _ => ⟨Nat.le_refl 1, fun ⟨_, drawn, _⟩ => drawn⟩
  ⟨Web.connected_of_commons _ own sig () bears aliveUser trivial aliveFirst
      ⟨trivial, Nat.zero_lt_one⟩,
   aliveFalling .first Formation.noConfusion,
   aliveFalling .second Formation.noConfusion,
   fun connected => Formation.noConfusion ((first_isolated own sig).reach
      (connected (.first, 0) (.second, 0) (aliveFalling .first Formation.noConfusion)
        (aliveFalling .second Formation.noConfusion)) rfl),
   Web.connected_of_common _ own sig () fun e alive => participates steady e alive.1,
   Web.connected_of_common _ own sig () fun e alive => participates falling e alive.1⟩

end Shared

end Becoming
