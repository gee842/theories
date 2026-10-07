import InductiveDomain

/-!
The universal mapping property is exactly generation plus constructor
separation for a supplied carrier. The target range includes its generated
subtype and a universe-lifted Nat. This equivalence does not independently
justify that universal range or the source carrier's existence.
-/
namespace Initiality
open InductiveDomain
universe u
variable {A : Type u}

def Initial (z : A) (s : A → A) : Prop :=
  ∀ (B : Type u) (b : B) (t : B → B),
    ∃ f : A → B, Hom z s b t f ∧ ∀ g, Hom z s b t g → g = f

def generatedZero (z : A) (s : A → A) : {a : A // Generated z s a} :=
  ⟨z, (generated_closed z s).1⟩

def generatedSuccessor (z : A) (s : A → A)
    (a : {a : A // Generated z s a}) : {a : A // Generated z s a} :=
  ⟨s a.val, (generated_closed z s).2 a.val a.property⟩

theorem initial_noJunk (z : A) (s : A → A) (hi : Initial z s) : NoJunk z s := by
  obtain ⟨f, hf, _⟩ := hi {a : A // Generated z s a} (generatedZero z s) (generatedSuccessor z s)
  obtain ⟨g, _, hg⟩ := hi A z s
  have hp : Hom z s z s (fun a => (f a).val) := by
    constructor
    · exact congrArg Subtype.val hf.1
    · intro a
      exact congrArg Subtype.val (hf.2 a)
  have hid : Hom z s z s id := ⟨rfl, fun _ => rfl⟩
  have he : (fun a => (f a).val) = id := (hg _ hp).trans (hg id hid).symm
  intro a
  have ha := (f a).property
  have hv := congrFun he a
  change (f a).val = a at hv
  exact hv ▸ ha

def liftedZero : ULift.{u} Nat := ⟨0⟩

def liftedSuccessor (n : ULift.{u} Nat) : ULift.{u} Nat := ⟨n.down + 1⟩

theorem initial_nat_hom (z : A) (s : A → A) (hi : Initial z s) :
    ∃ f : A → Nat, Hom z s 0 Nat.succ f := by
  obtain ⟨f, hf, _⟩ := hi (ULift.{u} Nat) liftedZero liftedSuccessor
  refine ⟨fun a => (f a).down, ?_, ?_⟩
  · exact congrArg ULift.down hf.1
  · intro a
    exact congrArg ULift.down (hf.2 a)

theorem separated_of_noJunk_nat_hom (z : A) (s : A → A) (hn : NoJunk z s)
    (f : A → Nat) (hf : Hom z s 0 Nat.succ f) : Separated z s := by
  have he : ∀ n, f (iterate z s n) = n := fun n =>
    (hom_iterate z s 0 Nat.succ f hf n).trans (nat_iterate n)
  constructor
  · intro a b hab
    obtain ⟨n, rfl⟩ := hn a
    obtain ⟨m, rfl⟩ := hn b
    have hnm := congrArg f hab
    rw [hf.2, hf.2, he, he] at hnm
    exact congrArg (iterate z s) (Nat.succ.inj hnm)
  · intro a haz
    have h := congrArg f haz
    rw [hf.2, hf.1] at h
    exact Nat.noConfusion h

theorem initial_iff_generated_separated (z : A) (s : A → A) :
    Initial z s ↔ NoJunk z s ∧ Separated z s := by
  constructor
  · intro hi
    have hn := initial_noJunk z s hi
    obtain ⟨f, hf⟩ := initial_nat_hom z s hi
    exact ⟨hn, separated_of_noJunk_nat_hom z s hn f hf⟩
  · rintro ⟨hn, hs⟩ B b t
    exact unique_recursion z s hn hs b t

end Initiality
