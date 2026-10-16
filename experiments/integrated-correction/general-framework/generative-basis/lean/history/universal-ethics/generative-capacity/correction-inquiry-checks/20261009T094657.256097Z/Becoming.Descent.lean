import Becoming.Correspondence
import Becoming.Reserve

/-!
# Descent: relata related through what they live on and what they give

`Becoming.Correspondence` relates two events only through a condition they share. Read
with one kind of relatum, that leaves unrelated relata whose relations run to each other
directly: a bee and a flower each depending only on the other
(`Mutualism.apart_not_connected`), and generations each given by the one before
(`Brood.descended`). `Becoming.Metaethics` counts conditioning and descent among formed
relations. This module states two readings of `related` that the one-kind reading
supplies, each added to interaction; the living events stay those of the stepwise
reading.

* **Living on a relatum.** A formation lives on a relatum at a step when it draws on it
  and depends on it at a positive need there (`Web.LivesOn`); an event living on a
  relatum is related to that relatum's events (`Web.sustenance`). Like interaction, this is not
  free: under `Dependent` an active formation lives only on an embodied relatum active
  at that step (`LivesOn.active`). The reading relates the bee and the flower that
  depend only on each other (`Mutualism.apart_sustenance_connected`). Under N_rel,
  valuing an event that lives on a relatum reaches every living event of that relatum,
  and valuing any event of the relatum reaches the living events that live on it
  (`living_on_reaches`, `lived_on_reaches`): valuing the fox's eating reaches the hare's
  living.
* **Descent.** A relatum descends from a formation that gives to it at a step across
  which it comes to stand (`Flow.Descends`). Descent relates relata whole, every event
  of the one to every event of the other (`Flow.descent`). In a balanced flow in which only
  active formations give, an embodied relatum that arises descends from another
  formation active at that step (`Embodied.descends`), which need not be embodied.
  Under N_rel, valuing any event of a formation then reaches every living event of the
  relata descending from it, and conversely (`descent_reaches`, `ancestry_reaches`,
  `arisen_reached`). Generations each given by the one before are connected by descent,
  and by neither co-participation nor interaction; G0 there is exactly a seed with N_rel
  and N_std (`Brood.descended`). Descent follows coming to stand, not arising: a seed
  descends from the parent that provisioned it while dormant (`Provisioned.descends`),
  and waking from dormancy descends from nothing (`Sleeper.no_descent`).
* **Where the identification enters.** Both readings use which condition is which
  relatum. Relabelling the conditions of the bee and the flower that depend only on each
  other, each onto the other, keeps co-participation and interaction, which do not
  connect them, and disconnects living on, which does (`Mutualism.relabel_sustenance`).

Whether living on a relatum and descent count as formed relations for N_rel, so that
valuing the fox's eating reaches the hare and valuing a parent reaches its offspring, is
a correspondence choice and Ren's. Descent relates relata that come to stand; it does not
make bringing them about better, which is the question of C. No axiom occurs.
-/

namespace Becoming

variable {X Pos : Type}

/-! ## Living on a relatum -/

namespace Web

variable (W : Web X X) (own sig : Pos → X × Nat → Prop)

/-- The formation of `e` *lives on* the relatum of `e'`: at its step it draws on that
relatum and depends on it at a positive need. -/
def LivesOn (e e' : X × Nat) : Prop :=
  W.draws e.2 e.1 e'.1 ∧ W.Bearing e.2 e.1 e'.1

/-- Events read stepwise, related by interaction or by living on a relatum, in either
direction. -/
def sustenance : Valuation Pos (X × Nat) where
  living e := W.active e.2 e.1 ∧ ¬ W.UnderminingAt e.2 e.1
  related e e' := (∃ c, W.Interacts c e e') ∨ W.LivesOn e e' ∨ W.LivesOn e' e
  own := own
  sig := sig

variable {W own sig}

/-- Living on extends interaction. -/
theorem interaction_sustenance :
    (W.interaction own sig).Connected → (W.sustenance own sig).Connected :=
  Valuation.Connected.transfer (fun _ => Iff.rfl) fun _ _ => .inl

/-- Living on is not free: under `Dependent`, an active formation lives only on an
embodied relatum active at that step. -/
theorem LivesOn.active (dependent : W.Dependent) {e e' : X × Nat} (lives : W.LivesOn e e')
    (embodied : W.Embodied e'.1) (active : W.active e.2 e.1) : W.active e.2 e'.1 :=
  embodied.active_of_bearing dependent active lives.2

/-- Under N_rel, valuing an event that lives on a relatum reaches every living event of
that relatum. -/
theorem living_on_reaches (transmit : Neutral (W.sustenance own sig).transmits) {p : Pos}
    {e d : X × Nat} (lives : W.LivesOn e d) (held : (W.sustenance own sig).sig p e)
    (alive : (W.sustenance own sig).living d) : (W.sustenance own sig).sig p d :=
  transmit (p, e, d) held (.inr (.inl lives)) alive

/-- Under N_rel, valuing any event of a relatum reaches every living event that lives on
it. -/
theorem lived_on_reaches (transmit : Neutral (W.sustenance own sig).transmits) {p : Pos}
    {e d : X × Nat} (lives : W.LivesOn e d) (held : (W.sustenance own sig).sig p d)
    (alive : (W.sustenance own sig).living e) : (W.sustenance own sig).sig p e :=
  transmit (p, d, e) held (.inr (.inr lives)) alive

end Web

/-! ## Descent -/

namespace Flow

variable (L : Flow X X) (W : Web X X) (own sig : Pos → X × Nat → Prop)

/-- `x` descends from `g`: `g` gives to `x` at some step across which `x` comes to
stand. -/
def Descends (x g : X) : Prop :=
  ∃ t, 0 < L.give t g x ∧ W.ComesToStand t x

/-- Events read stepwise, related by interaction or by descent between their relata, in
either direction. -/
def descent : Valuation Pos (X × Nat) where
  living e := W.active e.2 e.1 ∧ ¬ W.UnderminingAt e.2 e.1
  related e e' := (∃ c, W.Interacts c e e') ∨ L.Descends W e'.1 e.1 ∨ L.Descends W e.1 e'.1
  own := own
  sig := sig

variable {L W own sig}

/-- Descent extends interaction. -/
theorem interaction_descent :
    (W.interaction own sig).Connected → (L.descent W own sig).Connected :=
  Valuation.Connected.transfer (fun _ => Iff.rfl) fun _ _ => .inl

/-- Under N_rel, valuing any event of a formation reaches every living event of a relatum
descending from it. -/
theorem descent_reaches (transmit : Neutral (L.descent W own sig).transmits) {p : Pos}
    {x g : X} (descends : L.Descends W x g) {t s : Nat}
    (held : (L.descent W own sig).sig p (g, t)) (alive : (L.descent W own sig).living (x, s)) :
    (L.descent W own sig).sig p (x, s) :=
  transmit (p, (g, t), (x, s)) held (.inr (.inl descends)) alive

/-- Under N_rel, valuing any event of a relatum reaches every living event of a formation
it descends from. -/
theorem ancestry_reaches (transmit : Neutral (L.descent W own sig).transmits) {p : Pos}
    {x g : X} (descends : L.Descends W x g) {t s : Nat}
    (held : (L.descent W own sig).sig p (x, s)) (alive : (L.descent W own sig).living (g, t)) :
    (L.descent W own sig).sig p (g, t) :=
  transmit (p, (x, s), (g, t)) held (.inr (.inr descends)) alive

end Flow

namespace Web

variable {W : Web X X} {L : Flow X X}

/-- In a balanced flow in which only active formations give, an embodied relatum that
arises descends from another formation active at that step. -/
theorem Embodied.descends (balances : L.Balances W) (acting : L.Acting W) {x : X}
    (embodied : W.Embodied x) {t : Nat} (arises : W.Arises t x) :
    ∃ g, W.active t g ∧ g ≠ x ∧ L.Descends W x g :=
  match embodied.arises_given balances acting arises with
  | ⟨g, active, _, gives, other⟩ => ⟨g, active, other, t, gives, embodied.comesToStand arises⟩

/-- Every embodied relatum that arises is reached from a formation that gives to it:
under N_rel for descent, valuing any event of some formation active at its arising reaches
every living event of the arisen relatum. -/
theorem arisen_reached {own sig : Pos → X × Nat → Prop} (balances : L.Balances W)
    (acting : L.Acting W) (transmit : Neutral (L.descent W own sig).transmits) {x : X}
    (embodied : W.Embodied x) {t : Nat} (arises : W.Arises t x) :
    ∃ g, W.active t g ∧ g ≠ x ∧ ∀ p s s', (L.descent W own sig).sig p (g, s) →
      (L.descent W own sig).living (x, s') → (L.descent W own sig).sig p (x, s') :=
  match embodied.descends balances acting arises with
  | ⟨g, active, other, descends⟩ =>
    ⟨g, active, other, fun _ _ _ held alive => Flow.descent_reaches transmit descends held alive⟩

end Web

/-! ## Witnesses -/

namespace Brood

variable (own sig : Pos → Nat × Nat → Prop)

/-- Generation `t + 1` is given one unit across step `t`. -/
theorem birth_next : ∀ t, birth (t + 1) t = 1
  | 0 => rfl
  | t + 1 => birth_next t

/-- Each generation descends from the one before. -/
theorem descends (t : Nat) : flow.Descends web (t + 1) t :=
  ⟨t, Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq (birth_next t).symm), arises t⟩

/-- Nothing draws, so nothing undermines: a generation's event is living exactly while it
stands. -/
theorem alive_of_stands {e : Nat × Nat} (stands : 0 < standing e.1 e.2) :
    (flow.descent web own sig).living e :=
  ⟨stands, fun ⟨_, drawn, _⟩ => drawn⟩

theorem self_alive (t : Nat) : (flow.descent web own sig).living (t, t) :=
  alive_of_stands own sig (Nat.lt_of_lt_of_le Nat.zero_lt_one (Nat.le_of_eq (standing_self t).symm))

/-- Every living event reaches the first generation's first event through descent. -/
theorem down : ∀ x s, (flow.descent web own sig).living (x, s) →
    Reach (flow.descent web own sig).relations (x, s) (0, 0)
  | 0, _, _ => Reach.trans
      (Reach.of_step (a := ()) ⟨.inr (.inl (descends 0)), self_alive own sig 1⟩)
      (Reach.of_step (a := ()) ⟨.inr (.inr (descends 0)), self_alive own sig 0⟩)
  | x + 1, _, _ => Reach.trans
      (Reach.of_step (a := ()) ⟨.inr (.inr (descends x)), self_alive own sig x⟩)
      (down x x (self_alive own sig x))

/-- The first generation's first event reaches every living event through descent. -/
theorem up : ∀ y s, (flow.descent web own sig).living (y, s) →
    Reach (flow.descent web own sig).relations (0, 0) (y, s)
  | 0, _, alive => Reach.trans
      (Reach.of_step (a := ()) ⟨.inr (.inl (descends 0)), self_alive own sig 1⟩)
      (Reach.of_step (a := ()) ⟨.inr (.inr (descends 0)), alive⟩)
  | y + 1, _, alive => Reach.trans (up y y (self_alive own sig y))
      (Reach.of_step (a := ()) ⟨.inr (.inl (descends y)), alive⟩)

/-- Generations each given by the one before are connected by descent. -/
theorem descent_connected : (flow.descent web own sig).Connected :=
  fun c d alive alive' => Reach.trans (down own sig c.1 c.2 alive) (up own sig d.1 d.2 alive')

/-- A generation takes part only in itself. -/
theorem participates {t x c : Nat} : web.Participates t x c → c = x :=
  fun joins => joins.elim (fun depends => depends.1) False.elim

/-- Co-participation relates only events of one generation. -/
theorem not_coparticipating : ¬ (web.valuation own sig).Connected := fun connected =>
  Nat.noConfusion (Invariant.reach (P := (web.valuation own sig).relations)
    (I := fun e => e.1 = 0)
    (fun _ _ _ ⟨⟨_, joins, joins'⟩, _⟩ held =>
      (participates joins').symm.trans ((participates joins).trans held))
    (connected (0, 0) (1, 1) (self_alive own sig 0) (self_alive own sig 1)) rfl)

/-- Nothing draws, so nothing interacts. -/
theorem not_interacting : ¬ (web.interaction own sig).Connected := fun connected =>
  Nat.noConfusion (Invariant.reach (P := (web.interaction own sig).relations)
    (I := fun e => e.1 = 0)
    (fun _ _ _ ⟨⟨_, interacts⟩, _⟩ _ => match interacts with
      | .inl ⟨drawn, _⟩ => False.elim drawn
      | .inr ⟨_, drawn⟩ => False.elim drawn)
    (connected (0, 0) (1, 1) (self_alive own sig 0) (self_alive own sig 1)) rfl)

/-- Generations given each by the one before are connected by descent, and by neither
co-participation nor interaction; G0 there is exactly a seed with N_rel and N_std. -/
theorem descended (p₀ : Pos) :
    (flow.descent web own sig).Connected ∧ ¬ (web.valuation own sig).Connected ∧
      ¬ (web.interaction own sig).Connected ∧
      ((flow.descent web own sig).Significant ↔ (flow.descent web own sig).Grounds) :=
  ⟨descent_connected own sig, not_coparticipating own sig, not_interacting own sig,
   Valuation.significant_iff (descent_connected own sig) p₀ (self_alive own sig 0)⟩

end Brood

namespace Mutualism

variable (own sig : Pos → Relatum × Nat → Prop)

/-- The bee and the flower that depend only on each other are connected by living on:
each lives on the other. -/
theorem apart_sustenance_connected : (apart.sustenance own sig).Connected
  | (.bee, _), (.bee, _), _, alive' => Reach.trans
      (Reach.of_step (a := ()) (t := (Relatum.flower, 0))
        ⟨.inr (.inl ⟨rfl, rfl, Nat.zero_lt_one⟩), apart_alive (.flower, 0)⟩)
      (Reach.of_step (a := ()) ⟨.inr (.inl ⟨rfl, rfl, Nat.zero_lt_one⟩), alive'⟩)
  | (.flower, _), (.flower, _), _, alive' => Reach.trans
      (Reach.of_step (a := ()) (t := (Relatum.bee, 0))
        ⟨.inr (.inl ⟨rfl, rfl, Nat.zero_lt_one⟩), apart_alive (.bee, 0)⟩)
      (Reach.of_step (a := ()) ⟨.inr (.inl ⟨rfl, rfl, Nat.zero_lt_one⟩), alive'⟩)
  | (.bee, _), (.flower, _), _, alive' =>
      Reach.of_step (a := ()) ⟨.inr (.inl ⟨rfl, rfl, Nat.zero_lt_one⟩), alive'⟩
  | (.flower, _), (.bee, _), _, alive' =>
      Reach.of_step (a := ()) ⟨.inr (.inl ⟨rfl, rfl, Nat.zero_lt_one⟩), alive'⟩

/-- The other of the other is the relatum itself. -/
theorem other_other : ∀ x : Relatum, other (other x) = x
  | .bee => rfl
  | .flower => rfl

/-- Where the identification enters: relabelling the conditions of the bee and the flower
each onto the other keeps co-participation and interaction, which do not connect them,
and disconnects living on, which does. -/
theorem relabel_sustenance :
    (((apart.relabel other).valuation own sig).Connected ↔ (apart.valuation own sig).Connected) ∧
    (((apart.relabel other).interaction own sig).Connected ↔
      (apart.interaction own sig).Connected) ∧
    (apart.sustenance own sig).Connected ∧
      ¬ ((apart.relabel other).sustenance own sig).Connected :=
  have onto (c : Relatum) : ∃ y, other y = c := ⟨other c, other_other c⟩
  ⟨Web.relabel_valuation_connected onto own sig, Web.relabel_interaction_connected onto own sig,
   apart_sustenance_connected own sig, fun connected =>
    Relatum.noConfusion (Invariant.reach
      (P := ((apart.relabel other).sustenance own sig).relations)
      (I := fun e => e.1 = .bee)
      (fun _ _ _ ⟨related, _⟩ held => match related with
        | .inl ⟨_, .inl ⟨drawn, depends, _⟩⟩ =>
            (other_cancel depends).symm.trans ((other_cancel drawn).trans held)
        | .inl ⟨_, .inr ⟨⟨depends, _⟩, drawn⟩⟩ =>
            (other_cancel drawn).symm.trans ((other_cancel depends).trans held)
        | .inr (.inl ⟨drawn, _⟩) => (other_cancel drawn).trans held
        | .inr (.inr ⟨drawn, _⟩) => (other_cancel drawn).symm.trans held)
      (connected (.bee, 0) (.flower, 0)
        ((Web.relabel_alive onto 0 .bee).mpr (apart_alive (.bee, 0)))
        ((Web.relabel_alive onto 0 .flower).mpr (apart_alive (.flower, 0)))) rfl)⟩

end Mutualism

namespace Provisioned

/-- The seed descends from the parent that provisioned it while dormant, though it arises
only at the next step, when nothing is given to it. -/
theorem descends :
    flow.Descends web .seed .parent ∧ web.Arises 1 .seed ∧ flow.given 1 .seed = 0 :=
  ⟨⟨0, Nat.zero_lt_one, ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩⟩,
   ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩, rfl⟩

end Provisioned

namespace Sleeper

/-- Waking from dormancy descends from nothing, though generation is unceasing. -/
theorem no_descent : web.Unceasing ∧ ∀ x g, ¬ flow.Descends web x g :=
  ⟨sleeper.2.2.2.1, fun _ _ ⟨_, gives, _⟩ => Nat.lt_irrefl 0 gives⟩

end Sleeper

end Becoming
