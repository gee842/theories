import DevelopmentalReconstruction

/-!
An explicitly authored conventional network-and-stock comparator. The fields
encode exactly the supplied biological mechanism, not a neural learning law.
The operational definitions never call the old transition functions. Equality
is a result about this particular matched mechanism, not all connectionism.
-/
namespace EvolutionNetworkComparison

structure Graph where
  nodes : Nat
  substrate : Nat
  fuel : Nat
  used : Nat
  inherited : Nat → Bool
  origin : Nat → Nat
  edges : List (Nat × Nat)

structure Network where
  graph : Graph
  substrateStore : Nat
  fuelStore : Nat
  discardedSubstrate : Nat
  discardedFuel : Nat

def encodeGraph (s : DevelopmentalAssociation.State) : Graph :=
  ⟨s.count, s.precursor, s.available, s.spent, s.retains, s.founder, s.bonds⟩

def encode (w : DevelopmentalReconstruction.World) : Network :=
  ⟨encodeGraph w.culture, w.materialReserve, w.supportReserve,
    w.removedMaterial, w.removedSupport⟩

def decodeGraph (g : Graph) : DevelopmentalAssociation.State :=
  ⟨g.nodes, g.substrate, g.fuel, g.used, g.inherited, g.origin, g.edges⟩

def decode (n : Network) : DevelopmentalReconstruction.World :=
  ⟨decodeGraph n.graph, n.substrateStore, n.fuelStore,
    n.discardedSubstrate, n.discardedFuel⟩

theorem decode_encode (w : DevelopmentalReconstruction.World) :
    decode (encode w) = w := by cases w; rfl

theorem encode_decode (n : Network) : encode (decode n) = n := by
  cases n with
  | mk g a b c d => cases g; rfl

def reaction (e : DevelopmentalAssociation.Event) (g : Graph) : Option Graph :=
  match e with
  | .divide p =>
    if p < g.nodes ∧ 0 < g.substrate ∧ 0 < g.fuel then
      some { g with
        nodes := g.nodes + 1, substrate := g.substrate - 1,
        fuel := g.fuel - 1, used := g.used + 1,
        inherited := fun i => if i = g.nodes then g.inherited p else g.inherited i,
        origin := fun i => if i = g.nodes then g.origin p else g.origin i,
        edges := if g.inherited p then (p, g.nodes) :: g.edges else g.edges }
    else none
  | .changeRetention p v =>
    if p < g.nodes ∧ g.inherited p ≠ v ∧ 0 < g.fuel then
      some { g with
        fuel := g.fuel - 1
        used := g.used + 1
        inherited := fun i => if i = p then v else g.inherited i }
    else none
  | .detach a b =>
    if (a, b) ∈ g.edges ∧ 0 < g.fuel then
      some { g with
        fuel := g.fuel - 1
        used := g.used + 1
        edges := g.edges.filter (fun edge => edge != (a, b)) }
    else none
  | .aggregate a b =>
    if a < g.nodes ∧ b < g.nodes ∧ a ≠ b ∧ 0 < g.fuel then
      some { g with
        fuel := g.fuel - 1
        used := g.used + 1
        edges := (a, b) :: g.edges }
    else none

def developmentalRun : List DevelopmentalAssociation.Event → Graph → Option Graph
  | [], g => some g
  | e :: es, g => (reaction e g).bind (developmentalRun es)

def sample (n : Network) (r : DevelopmentalReconstruction.Requirement)
    (p substrate fuel : Nat) : Option Network :=
  let attached := n.graph.edges.any (fun edge => edge.1 == p || edge.2 == p)
  let permitted := decide (p < n.graph.nodes) && match r with
    | .anyCell => true
    | .attachedCell => attached
  if permitted = true ∧ p < n.graph.nodes ∧
      substrate ≤ n.substrateStore ∧ fuel ≤ n.fuelStore then
    some {
      graph := ⟨1, substrate, fuel, 0,
        fun _ => n.graph.inherited p, fun _ => n.graph.origin p, []⟩
      substrateStore := n.substrateStore - substrate
      fuelStore := n.fuelStore - fuel
      discardedSubstrate := n.discardedSubstrate + (n.graph.nodes - 1) + n.graph.substrate
      discardedFuel := n.discardedFuel + n.graph.fuel + n.graph.used }
  else none

def transition (e : DevelopmentalReconstruction.Event) (n : Network) : Option Network :=
  match e with
  | .develop es => (developmentalRun es n.graph).map (fun g => { n with graph := g })
  | .transfer r p substrate fuel => sample n r p substrate fuel

def history : List DevelopmentalReconstruction.Event → Network → Option Network
  | [], n => some n
  | e :: es, n => (transition e n).bind (history es)

theorem reaction_correspondence (e : DevelopmentalAssociation.Event)
    (s : DevelopmentalAssociation.State) :
    reaction e (encodeGraph s) = (DevelopmentalAssociation.step e s).map encodeGraph := by
  cases e <;> simp only [reaction, encodeGraph, DevelopmentalAssociation.step,
    DevelopmentalAssociation.divide, DevelopmentalAssociation.changeRetention,
    DevelopmentalAssociation.detach, DevelopmentalAssociation.aggregate]
  all_goals split <;> simp_all [encodeGraph]

theorem development_correspondence (es : List DevelopmentalAssociation.Event)
    (s : DevelopmentalAssociation.State) :
    developmentalRun es (encodeGraph s) =
      (DevelopmentalAssociation.run es s).map encodeGraph := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih =>
    simp only [developmentalRun, DevelopmentalAssociation.run, reaction_correspondence]
    cases h : DevelopmentalAssociation.step e s with
    | none => rfl
    | some t => simpa using ih t

theorem sample_correspondence (w : DevelopmentalReconstruction.World)
    (r : DevelopmentalReconstruction.Requirement) (p substrate fuel : Nat) :
    sample (encode w) r p substrate fuel =
      (DevelopmentalReconstruction.transfer w r p substrate fuel).map encode := by
  cases r <;> simp only [sample, encode, encodeGraph, DevelopmentalReconstruction.transfer,
    DevelopmentalReconstruction.eligible, DevelopmentalReconstruction.attached]
  all_goals split <;> simp_all [encode, encodeGraph] <;> assumption

theorem transition_correspondence (e : DevelopmentalReconstruction.Event)
    (w : DevelopmentalReconstruction.World) :
    transition e (encode w) = (DevelopmentalReconstruction.step e w).map encode := by
  cases e with
  | develop es =>
    simp only [transition, encode, DevelopmentalReconstruction.step,
      DevelopmentalReconstruction.develop, development_correspondence]
    cases DevelopmentalAssociation.run es w.culture <;> rfl
  | transfer r p substrate fuel => exact sample_correspondence w r p substrate fuel

theorem history_correspondence (es : List DevelopmentalReconstruction.Event)
    (w : DevelopmentalReconstruction.World) :
    history es (encode w) = (DevelopmentalReconstruction.run es w).map encode := by
  induction es generalizing w with
  | nil => rfl
  | cons e es ih =>
    simp only [history, DevelopmentalReconstruction.run, transition_correspondence]
    cases h : DevelopmentalReconstruction.step e w with
    | none => rfl
    | some t => simpa using ih t

theorem decoded_history_equal (es : List DevelopmentalReconstruction.Event)
    (w : DevelopmentalReconstruction.World) :
    (history es (encode w)).map decode = DevelopmentalReconstruction.run es w := by
  rw [history_correspondence]
  cases DevelopmentalReconstruction.run es w with
  | none => rfl
  | some t => simp [decode_encode]

theorem failure_equal (es : List DevelopmentalReconstruction.Event)
    (w : DevelopmentalReconstruction.World) :
    history es (encode w) = none ↔ DevelopmentalReconstruction.run es w = none := by
  rw [history_correspondence]
  cases DevelopmentalReconstruction.run es w <;> simp

/-- Every readout of the admitted full state agrees, not only cell counts. -/
theorem readout_equal {α : Type} (readout : DevelopmentalReconstruction.World → α)
    (es : List DevelopmentalReconstruction.Event) (w : DevelopmentalReconstruction.World) :
    (history es (encode w)).map (fun n => readout (decode n)) =
      (DevelopmentalReconstruction.run es w).map readout := by
  rw [history_correspondence]
  cases DevelopmentalReconstruction.run es w <;> simp [decode_encode]

/-- A selector may use the current full state. Equivalence is not limited to
a fixed event schedule, provided both implementations use the same selector. -/
def adaptiveOriginal (choose : DevelopmentalReconstruction.World → DevelopmentalReconstruction.Event) :
    Nat → DevelopmentalReconstruction.World → Option DevelopmentalReconstruction.World
  | 0, w => some w
  | k + 1, w => (DevelopmentalReconstruction.step (choose w) w).bind (adaptiveOriginal choose k)

def adaptiveNetwork (choose : DevelopmentalReconstruction.World → DevelopmentalReconstruction.Event) :
    Nat → Network → Option Network
  | 0, n => some n
  | k + 1, n => (transition (choose (decode n)) n).bind (adaptiveNetwork choose k)

theorem adaptive_correspondence
    (choose : DevelopmentalReconstruction.World → DevelopmentalReconstruction.Event)
    (k : Nat) (w : DevelopmentalReconstruction.World) :
    adaptiveNetwork choose k (encode w) = (adaptiveOriginal choose k w).map encode := by
  induction k generalizing w with
  | zero => rfl
  | succ k ih =>
    simp only [adaptiveNetwork, adaptiveOriginal, decode_encode, transition_correspondence]
    cases h : DevelopmentalReconstruction.step (choose w) w with
    | none => rfl
    | some t => simpa using ih t

end EvolutionNetworkComparison
