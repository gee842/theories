import Becoming.Weighted

/-!
# Chance floors: what pointwise continuation of a due protection gives under a law of chance

The entries of a listed domain pair implementations under the same support conditions, failures
and seeds; a weighting of the entries is one finite law of chance, its total positive where it
is a probability (`total`). The core's mass (`mass`) follows inclusion under every weighting
(`mass_mono`), rises where a weighted entry is added (`mass_lt_of_added`), and every weighting
agrees exactly on inclusion (`every_weighting_iff`), the weightings counting one entry telling
events apart (`mass_dirac_pos_iff`).

A due protection is the demand together with the old support that still works (`target`); a new
route fulfils it where it works at every entry where the protection was due (`Fulfilled`), a
pointwise condition, not a comparison of chances.

* **Fulfilment gives a chance floor**: the protection's mass is at most the new route's, and that
  at most the total (`fulfillment_gives_chance_floor`), through `mass_mono`.
* **Repair as an event**: the due protection or a candidate (`repair`) fulfils the protection
  and covers the candidate (`repair_covers_target_and_candidate`); a candidate working at a
  weighted entry where the protection was not due raises the mass (`repair_adds_new_protection`,
  through `mass_lt_of_added`). Its timely, permitted implementation is a separate condition.
* **Positive chance can miss a due protection**: a route of positive chance and the same total
  success as the old one can fail exactly where the protection was due
  (`positive_chance_can_miss_due_protection`).

Coupling of the entries, coverage, the window of support and the protection due are supplied.
This states `ChanceAdequacy` (8 October) in the core (board item F3C, 18 October 2026); its mass,
inclusion, monotonicity, strict rise and all-weightings laws were already the core's. No premise;
every declaration has an empty axiom report.
-/

namespace Becoming

namespace ChanceFloors

variable {Ω : Type}

/-- The total weight of a listed domain. -/
def total (domain : List Ω) (weight : Ω → Nat) : Nat := mass domain weight (fun _ => true)

/-- **The weighting counting one entry gives an event positive mass exactly where the entry is
listed and the event holds there.** -/
theorem mass_dirac_pos_iff [DecidableEq Ω] (domain : List Ω) (h : Ω) (event : Ω → Bool) :
    0 < mass domain (dirac h) event ↔ h ∈ domain ∧ event h = true :=
  ⟨mem_of_mass_dirac_pos, fun ⟨member, occurs⟩ => mass_dirac_pos occurs member⟩

/-- The due protection: demanded, with the old support still working. -/
def target (demand oldWorks : Ω → Bool) (h : Ω) : Bool := demand h && oldWorks h

/-- A new route fulfils the protection where it works at every entry where it was due. -/
def Fulfilled (domain : List Ω) (demand oldWorks newWorks : Ω → Bool) : Prop :=
  IncludedOn domain (target demand oldWorks) newWorks

/-- **Fulfilment gives a chance floor**, with one positive total as common denominator. Meeting
the floor alone does not fulfil the protection. -/
theorem fulfillment_gives_chance_floor (domain : List Ω)
    (weight : Ω → Nat) (demand oldWorks newWorks : Ω → Bool)
    (positive : 0 < total domain weight)
    (fulfilled : Fulfilled domain demand oldWorks newWorks) :
    0 < total domain weight ∧
    mass domain weight (target demand oldWorks) ≤ mass domain weight newWorks ∧
    mass domain weight newWorks ≤ total domain weight :=
  ⟨positive, mass_mono weight fulfilled, mass_mono weight fun _ _ _ => rfl⟩

/-- Repair: the due protection or a candidate. -/
def repair (demand oldWorks candidate : Ω → Bool) (h : Ω) : Bool :=
  target demand oldWorks h || candidate h

theorem or_true (b : Bool) : (b || true) = true := match b with | true => rfl | false => rfl

/-- **Repair fulfils the protection and covers the candidate.** -/
theorem repair_covers_target_and_candidate (domain : List Ω)
    (demand oldWorks candidate : Ω → Bool) :
    Fulfilled domain demand oldWorks (repair demand oldWorks candidate) ∧
    IncludedOn domain candidate (repair demand oldWorks candidate) :=
  ⟨fun h _ occurs => by
      show (target demand oldWorks h || candidate h) = true
      rw [occurs]
      rfl,
   fun h _ occurs => by
      show (target demand oldWorks h || candidate h) = true
      rw [occurs]
      exact or_true _⟩

/-- **A candidate working at a weighted entry where the protection was not due raises the
mass.** -/
theorem repair_adds_new_protection (domain : List Ω)
    (weight : Ω → Nat) (demand oldWorks candidate : Ω → Bool)
    (h : Ω) (member : h ∈ domain) (positive : 0 < weight h)
    (notOldTarget : target demand oldWorks h = false) (added : candidate h = true) :
    mass domain weight (target demand oldWorks) <
      mass domain weight (repair demand oldWorks candidate) :=
  mass_lt_of_added weight positive notOldTarget
    (show (target demand oldWorks h || candidate h) = true by rw [added]; exact or_true _)
    (repair_covers_target_and_candidate domain demand oldWorks candidate).1 member

/-- **Positive chance can miss a due protection**: both conditions have positive mass, the new
route has the old one's total success, yet it fails where the protection was due. -/
theorem positive_chance_can_miss_due_protection :
    total [false, true] (fun _ => 1) = 2 ∧
    mass [false, true] (fun _ => 1) (target (fun _ => true) Bool.not) = 1 ∧
    mass [false, true] (fun _ => 1) (fun h => h) = 1 ∧
    ¬ Fulfilled [false, true] (fun _ => true) Bool.not (fun h => h) ∧
    target (fun _ => true) Bool.not false = true ∧
    (fun h : Bool => h) false = false ∧ 0 < (fun _ : Bool => 1) false :=
  ⟨rfl, rfl, rfl, fun fulfilled => (nomatch fulfilled false (.head _) rfl), rfl, rfl,
    Nat.zero_lt_one⟩

end ChanceFloors

end Becoming
