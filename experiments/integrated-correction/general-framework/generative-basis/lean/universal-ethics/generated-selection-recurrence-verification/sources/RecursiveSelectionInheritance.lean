import RecursiveGenerativeSelection

/-!
# Reconstructing a coupling arrangement and operating its actual successor

This explicitly supplied finite mechanism extends the previous one-round law.
The weak/strong arrangement is an eight-carrier organization: two collectives
with compositions 3:1 and 1:3, using strength 1 or 3. A daughter is assembled
from four carriers of each response, rather than assigned a free group label.

Precursor material and activity support are distinct, finite initial stocks.
Every new carrier consumes one precursor and one activity-support unit. Every
assembled daughter uses existing carriers and one activity-support unit. Old
arrangements become retained inactive material; leftovers are retained too.
These conversion recipes are inputs, not derived biology or universal costs.

Actual successor operation invokes `RecursiveGenerativeSelection.pooled`
again, using the coupling actually reconstructed. Neither inheritance table,
regrouping recipe nor their origin is selected or explained by this extension.
No self-sustaining recursion, long-run convergence or ethical predicate occurs.
-/

namespace RecursiveSelectionInheritance

structure State where
  precursor : Nat
  available : Nat
  spent : Nat
  weak : Nat
  strong : Nat
  retired : Nat
  weakA : Nat
  weakH : Nat
  strongA : Nat
  strongH : Nat
  deriving DecidableEq

structure Transfer where
  weakToWeak : Nat
  weakToStrong : Nat
  strongToWeak : Nat
  strongToStrong : Nat
  deriving DecidableEq

/-- Carrier count, including free precursor, assembled and retired carriers. -/
def material (s : State) : Nat :=
  s.precursor + 8 * (s.weak + s.strong + s.retired) +
    s.weakA + s.weakH + s.strongA + s.strongH

/-- No productive run occurs without active arrangements and both sources.
    Descendants are tagged by the arrangement that actually produced them. -/
def operate (s : State) : Option State :=
  let w := RecursiveGenerativeSelection.pooled 1 1
  let g := RecursiveGenerativeSelection.pooled 1 3
  let cost := s.weak * (w.1 + w.2) + s.strong * (g.1 + g.2)
  if 0 < s.weak + s.strong ∧ cost ≤ s.precursor ∧ cost ≤ s.available then
    some { s with
      precursor := s.precursor - cost
      available := s.available - cost
      spent := s.spent + cost
      weak := 0
      strong := 0
      retired := s.retired + s.weak + s.strong
      weakA := s.weakA + s.weak * w.1
      weakH := s.weakH + s.weak * w.2
      strongA := s.strongA + s.strong * g.1
      strongH := s.strongH + s.strong * g.2 }
  else none

/-- The rows identify source arrangements; columns identify the reconstructed
    coupling. Four carriers of each response are transferred into each daughter.
    Pool origin is retained here; free cross-origin mixing is not supplied. -/
def assemble (s : State) (t : Transfer) : Option State :=
  let w := t.weakToWeak + t.weakToStrong
  let g := t.strongToWeak + t.strongToStrong
  let count := w + g
  if 0 < count ∧ count ≤ s.available ∧
      4 * w ≤ s.weakA ∧ 4 * w ≤ s.weakH ∧
      4 * g ≤ s.strongA ∧ 4 * g ≤ s.strongH then
    some { s with
      available := s.available - count
      spent := s.spent + count
      weak := s.weak + t.weakToWeak + t.strongToWeak
      strong := s.strong + t.weakToStrong + t.strongToStrong
      weakA := s.weakA - 4 * w
      weakH := s.weakH - 4 * w
      strongA := s.strongA - 4 * g
      strongH := s.strongH - 4 * g }
  else none

/-- Every admitted operation conserves carrier material and accounts for all
    activity support drawn, with no source reset at a generation boundary. -/
theorem operation_accounts {s next : State} (actual : operate s = some next) :
    material next = material s ∧ next.available + next.spent = s.available + s.spent := by
  unfold operate at actual
  dsimp [RecursiveGenerativeSelection.pooled, RecursiveGenerativeSelection.descendants,
    RecursiveGenerativeSelection.support] at actual
  split at actual
  · rename_i enabled
    cases Option.some.inj actual
    dsimp [material]
    constructor <;> omega
  · cases actual

/-- Assembly moves existing carriers into organized activity; it does not
    destroy them or count them again as free carriers. -/
theorem assembly_accounts {s next : State} {t : Transfer}
    (actual : assemble s t = some next) :
    material next = material s ∧ next.available + next.spent = s.available + s.spent := by
  unfold assemble at actual
  dsimp at actual
  split at actual
  · rename_i enabled
    cases Option.some.inj actual
    dsimp [material]
    constructor <;> omega
  · cases actual

/-- A generic connected history, not three independently funded comparisons. -/
theorem connected_two_generation_accounts {seed produced daughter finalState : State}
    {t : Transfer} (firstRun : operate seed = some produced)
    (formed : assemble produced t = some daughter)
    (secondRun : operate daughter = some finalState) :
    material finalState = material seed ∧
      finalState.available + finalState.spent = seed.available + seed.spent := by
  obtain ⟨firstMaterial, firstSupport⟩ := operation_accounts firstRun
  obtain ⟨formedMaterial, formedSupport⟩ := assembly_accounts formed
  obtain ⟨lastMaterial, lastSupport⟩ := operation_accounts secondRun
  exact ⟨lastMaterial.trans (formedMaterial.trans firstMaterial),
    lastSupport.trans (formedSupport.trans firstSupport)⟩

/-- The limiting response counts in the actual first output restrict every
    admissible table, not just the selected faithful and conversion examples. -/
theorem assembly_row_limits {produced daughter : State} {t : Transfer}
    (formed : assemble produced t = some daughter)
    (weakSource : produced.weakA = 28) (strongSource : produced.strongH = 66) :
    t.weakToWeak + t.weakToStrong ≤ 7 ∧
      t.strongToWeak + t.strongToStrong ≤ 16 := by
  unfold assemble at formed
  dsimp at formed
  split at formed
  · rename_i enabled
    omega
  · cases formed

/-- Actual successful assembly with row capacities 7 and 16 gives an exact
    condition for increasing strong-arrangement share from an initial 1:1.
    More daughters of a source is not enough when their coupling changes. -/
theorem fully_assembled_strong_share_rises_iff {produced daughter : State} {t : Transfer}
    (formed : assemble produced t = some daughter)
    (noActiveWeak : produced.weak = 0) (noActiveStrong : produced.strong = 0)
    (weakRow : t.weakToWeak + t.weakToStrong = 7)
    (strongRow : t.strongToWeak + t.strongToStrong = 16) :
    daughter.weak < daughter.strong ↔ t.strongToWeak ≤ t.weakToStrong + 4 := by
  unfold assemble at formed
  dsimp at formed
  split at formed
  · cases Option.some.inj formed
    dsimp
    omega
  · cases formed

/-- Full faithful reconstruction followed by operation of the actual daughters.
    All residual precursor, support, inactive structures and loose carriers are
    retained in the final state. The coupling law really executes twice. -/
theorem faithful_two_generation_history :
    let seed : State := ⟨3000, 3000, 0, 1, 1, 0, 0, 0, 0, 0⟩
    let produced : State := ⟨2808, 2808, 192, 0, 0, 2, 28, 30, 68, 66⟩
    let daughter : State := ⟨2808, 2785, 215, 7, 16, 2, 0, 2, 4, 2⟩
    let finalState : State := ⟨258, 235, 2765, 0, 0, 25, 196, 212, 1092, 1058⟩
    operate seed = some produced ∧
    assemble produced ⟨7, 0, 0, 16⟩ = some daughter ∧
    operate daughter = some finalState ∧
    daughter.weak < daughter.strong ∧
    material finalState = material seed ∧
    finalState.available + finalState.spent = 3000 := by
  decide

/-- All four transfer channels are positive and use the same output and assembly
    limits. The higher-output source mostly reconstructs weak arrangements. -/
theorem converted_two_generation_history :
    let seed : State := ⟨3000, 3000, 0, 1, 1, 0, 0, 0, 0, 0⟩
    let produced : State := ⟨2808, 2808, 192, 0, 0, 2, 28, 30, 68, 66⟩
    let daughter : State := ⟨2808, 2785, 215, 21, 2, 2, 0, 2, 4, 2⟩
    let finalState : State := ⟨1322, 1299, 1701, 0, 0, 25, 588, 632, 140, 134⟩
    let transfer : Transfer := ⟨6, 1, 15, 1⟩
    operate seed = some produced ∧
    assemble produced transfer = some daughter ∧
    operate daughter = some finalState ∧
    0 < transfer.weakToWeak ∧ 0 < transfer.weakToStrong ∧
    0 < transfer.strongToWeak ∧ 0 < transfer.strongToStrong ∧
    daughter.strong < daughter.weak ∧
    material finalState = material seed ∧
    finalState.available + finalState.spent = 3000 := by
  decide

/-- The finite source and actual carrier guards are effective: none of these
    failures can be bypassed by naming a stronger coupling or a successor. -/
theorem insufficient_source_or_excess_assembly_fails :
    let seed : State := ⟨3000, 3000, 0, 1, 1, 0, 0, 0, 0, 0⟩
    let produced : State := ⟨2808, 2808, 192, 0, 0, 2, 28, 30, 68, 66⟩
    operate { seed with available := 191 } = none ∧
    operate { seed with precursor := 191 } = none ∧
    assemble produced ⟨8, 0, 0, 16⟩ = none ∧
    assemble produced ⟨7, 0, 0, 17⟩ = none ∧
    assemble { produced with available := 22 } ⟨7, 0, 0, 16⟩ = none := by
  decide

end RecursiveSelectionInheritance
