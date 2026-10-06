import GenerativeCore

/- Generic prepaid archive. A core event carries a genuine producer successor;
its payload is derived by emission, never supplied by an archive-write event. -/
namespace EmissionArchive

structure Producer (World Event Header Record : Type) where
  step : World → Event → World → Prop
  bind : World → Nat → Header → Prop
  writable : World → Prop
  emission : Header → World → Event → World → Option Record
  encode : Record → List Bool
  fourBits : ∀ r, (encode r).length = 4
  encoding_injective : ∀ {r x}, encode r = encode x → r = x
  energy : World → Nat
  charge : World → Event → World → Nat
  ledger : ∀ {s t e}, step s e t → energy t + charge s e t = energy s

inductive Phase (Header Record : Type) where
  | idle
  | bound (address : Nat) (header : Header)
  | latched (address : Nat) (record : Record) (written : List Bool)

structure State (World Header Record : Type) where
  world : World
  budget : Nat
  escrow : Nat
  blanks : Nat
  records : Nat → Option Record
  phase : Phase Header Record

def empty (world : W) (budget cells : Nat) : State W H R :=
  ⟨world,budget,0,cells,fun _ => none,.idle⟩

def stored (s : State W H R) (i : Nat) (r : R) : Prop := s.records i = some r

def held (s : State W H R) (i : Nat) (r : R) : Prop :=
  stored s i r ∨ ∃ bits, s.phase = .latched i r bits

def Valid (p : Producer W E H R) (s : State W H R) : Prop :=
  match s.phase with
  | .idle => s.escrow = 0
  | .bound i _ => s.records i = none ∧ s.escrow = 4
  | .latched i r bits => s.records i = none ∧ bits.length < 4 ∧
      bits = (p.encode r).take bits.length ∧ s.escrow + bits.length = 4

inductive Event (World CoreEvent Header : Type) where
  | bind (address : Nat) (header : Header)
  | core (event : CoreEvent) (successor : World)
  | write

def latch (p : Producer W E H R) (s : State W H R) (e : E) (w : W) : Phase H R :=
  match s.phase with
  | .bound i h => match p.emission h s.world e w with
    | none => s.phase
    | some r => .latched i r []
  | _ => s.phase

def put (f : Nat → Option R) (i : Nat) (r : R) : Nat → Option R :=
  fun j => if j = i then some r else f j

def advance (p : Producer W E H R) (s : State W H R) : Event W E H → State W H R
  | .bind i h => { s with
      budget := s.budget-5, escrow := 4, blanks := s.blanks-4, phase := .bound i h }
  | .core e w => { s with world := w, phase := latch p s e w }
  | .write => match s.phase with
    | .latched i r bits =>
      if bits.length = 3 then { s with escrow := s.escrow-1, records := put s.records i r, phase := .idle }
      else { s with
        escrow := s.escrow-1, phase := .latched i r ((p.encode r).take (bits.length+1)) }
    | _ => s

def Enabled (p : Producer W E H R) (addresses : Nat) (s : State W H R) : Event W E H → Prop
  | .bind i h => s.phase = .idle ∧ i < addresses ∧ s.records i = none ∧
      4 ≤ s.blanks ∧ 5 ≤ s.budget ∧ p.bind s.world i h
  | .core e w => p.step s.world e w
  | .write => p.writable s.world ∧ ∃ i r bits, s.phase = .latched i r bits ∧ bits.length < 4 ∧ 0 < s.escrow

def Step (p : Producer W E H R) (n : Nat) (s : State W H R) (e : Event W E H) (t : State W H R) : Prop :=
  Valid p s ∧ Enabled p n s e ∧ t = advance p s e

def process (p : Producer W E H R) (n : Nat) : Generative.Process (State W H R) (Event W E H) := ⟨Step p n⟩
def energy (p : Producer W E H R) (s : State W H R) : Nat := p.energy s.world+s.budget+s.escrow

def charge (p : Producer W E H R) (s : State W H R) : Event W E H → Nat
  | .bind _ _ | .write => 1
  | .core e w => p.charge s.world e w

def spentAlong (p : Producer W E H R) (s : State W H R) : List (Event W E H) → Nat
  | [] => 0
  | e :: es => charge p s e + spentAlong p (advance p s e) es

def origin (p : Producer W E H R) (s : State W H R) : Event W E H → List (Nat × R)
  | .core e w => match s.phase with
    | .bound i h => (p.emission h s.world e w).toList.map (fun r => (i,r))
    | _ => []
  | _ => []

def originsAlong (p : Producer W E H R) (s : State W H R) : List (Event W E H) → List (Nat × R)
  | [] => []
  | e :: es => origin p s e ++ originsAlong p (advance p s e) es

theorem empty_valid (p : Producer W E H R) (w : W) (b c : Nat) : Valid p (empty w b c) := rfl

theorem empty_holds_nothing (w : W) (b c i : Nat) (r : R) : ¬ held (empty (H := H) w b c) i r := by
  simp [held,stored,empty]

theorem binding_preserves_world (p : Producer W E H R) (s : State W H R) (i : Nat) (h : H) :
    (advance p s (.bind i h)).world = s.world := rfl

theorem write_preserves_world (p : Producer W E H R) (s : State W H R) :
    (advance p s .write).world = s.world := by
  cases hp : s.phase <;> simp [advance,hp]
  split <;> rfl

theorem core_preserves_archive_funds (p : Producer W E H R) (s : State W H R) (e : E) (w : W) :
    (advance p s (.core e w)).budget = s.budget ∧
    (advance p s (.core e w)).escrow = s.escrow := ⟨rfl,rfl⟩

theorem cannot_bind_completed (p : Producer W E H R) (n : Nat) (s : State W H R)
    (i : Nat) (h : H) (r : R) (hs : stored s i r) : ¬ Enabled p n s (.bind i h) := by
  simp only [Enabled,stored] at *
  intro he
  rw [hs] at he
  cases he.2.2.1

theorem step_energy {p : Producer W E H R} {n : Nat} {s t : State W H R} {e : Event W E H}
    (h : Step p n s e t) : energy p t + charge p s e = energy p s := by
  rcases h with ⟨hv,he,rfl⟩
  cases e with
  | bind i h =>
      have heq : s.escrow = 0 := by simpa [Valid,he.1] using hv
      have hf := he.2.2.2.2.1
      simp [advance,energy,charge,heq]; omega
  | core e w =>
      have hh := p.ledger he
      simp only [advance,energy,charge]
      omega
  | write =>
      rcases he.2 with ⟨i,r,bits,hp,_,hf⟩
      simp only [advance,hp,charge]
      split <;> simp [energy] <;> omega

theorem trace_energy {p : Producer W E H R} {n : Nat} {s t : State W H R} {es : List (Event W E H)}
    (h : Generative.Trace (process p n) s es t) : energy p t + spentAlong p s es = energy p s := by
  induction h with
  | nil => simp [spentAlong]
  | cons hs _ ih =>
      have he := step_energy hs
      rcases hs with ⟨_,_,rfl⟩
      simp only [spentAlong]
      omega

theorem step_completed_immutable {p : Producer W E H R} {n : Nat} {s t : State W H R}
    {e : Event W E H} {i : Nat} {r : R} (h : Step p n s e t) (hs : stored s i r) : stored t i r := by
  rcases h with ⟨hv,he,rfl⟩
  cases e with
  | bind j header => exact hs
  | core e w => exact hs
  | write =>
      rcases he.2 with ⟨j,x,bits,hp,_,_⟩
      have hv' := hv
      simp only [Valid,hp] at hv'
      have hn : s.records j = none := hv'.1
      have hij : i ≠ j := by intro hij; subst j; rw [hs] at hn; contradiction
      simp only [stored,advance,hp]
      split <;> simpa [put,hij] using hs

theorem trace_completed_immutable {p : Producer W E H R} {n : Nat} {s t : State W H R}
    {es : List (Event W E H)} {i : Nat} {r : R}
    (h : Generative.Trace (process p n) s es t) (hs : stored s i r) : stored t i r := by
  induction h with
  | nil => exact hs
  | cons he _ ih => exact ih (step_completed_immutable he hs)

theorem step_valid {p : Producer W E H R} {n : Nat} {s t : State W H R}
    {e : Event W E H} (h : Step p n s e t) : Valid p t := by
  rcases h with ⟨hv,he,rfl⟩
  cases e with
  | bind i header => simp [Valid,advance,he.2.2.1]
  | core e w =>
      cases hp : s.phase with
      | idle => simpa [Valid,advance,latch,hp] using hv
      | latched i r bits => simpa [Valid,advance,latch,hp] using hv
      | bound i header =>
          simp only [Valid,hp] at hv
          cases hem : p.emission header s.world e w <;>
            simp [Valid,advance,latch,hp,hem,hv.1,hv.2]
  | write =>
      rcases he.2 with ⟨i,r,bits,hp,hlen,hesc⟩
      simp only [Valid,hp] at hv
      by_cases hn : bits.length = 3
      · simp [advance,hp,hn,Valid]; omega
      · have hlen' : bits.length+1 < 4 := by omega
        have hsmall : bits.length+1 ≤ (p.encode r).length := by rw [p.fourBits]; omega
        have ht : ((p.encode r).take (bits.length+1)).length = bits.length+1 := by
          simp [List.length_take,Nat.min_eq_left hsmall]
        simp only [advance,hp,if_neg hn,Valid,ht]
        exact ⟨hv.1,hlen',by trivial,by omega⟩

theorem trace_valid {p : Producer W E H R} {n : Nat} {s t : State W H R}
    {es : List (Event W E H)} (hv : Valid p s)
    (h : Generative.Trace (process p n) s es t) : Valid p t := by
  induction h with
  | nil => exact hv
  | cons hs _ ih => exact ih (step_valid hs)

theorem step_held_origin {p : Producer W E H R} {n : Nat} {s t : State W H R}
    {e : Event W E H} {i : Nat} {r : R} (h : Step p n s e t)
    (hh : held t i r) : held s i r ∨ (i,r) ∈ origin p s e := by
  rcases h with ⟨hv,he,rfl⟩
  cases e with
  | bind j header =>
      simp [held,stored,advance] at hh
      exact Or.inl (Or.inl hh)
  | core e w =>
      cases hp : s.phase with
      | idle =>
          simp [held,stored,advance,latch,hp] at hh
          exact Or.inl (Or.inl hh)
      | latched j x bits =>
          exact Or.inl (by simpa [held,stored,advance,latch,hp] using hh)
      | bound j header =>
          cases hem : p.emission header s.world e w with
          | none =>
              simp [held,stored,advance,latch,hp,hem] at hh
              exact Or.inl (Or.inl hh)
          | some x =>
              simp [held,stored,advance,latch,hp,hem] at hh
              rcases hh with hs | ⟨hi,hr⟩
              · exact Or.inl (Or.inl hs)
              · subst j; subst x
                exact Or.inr (by simp [origin,hp,hem])
  | write =>
      rcases he.2 with ⟨j,x,bits,hp,_,_⟩
      by_cases hn : bits.length = 3
      · simp only [held,stored,advance,hp,if_pos hn,put] at hh
        by_cases hij : i = j
        · subst j
          simp at hh
          subst x
          exact Or.inl (Or.inr ⟨bits,hp⟩)
        · simp [hij] at hh
          exact Or.inl (Or.inl hh)
      · simp [held,stored,advance,hp,hn] at hh
        rcases hh with hs | ⟨hi,hr⟩
        · exact Or.inl (Or.inl hs)
        · subst j; subst x
          exact Or.inl (Or.inr ⟨bits,hp⟩)

theorem trace_held_origin {p : Producer W E H R} {n : Nat} {s t : State W H R}
    {es : List (Event W E H)} {i : Nat} {r : R}
    (h : Generative.Trace (process p n) s es t) (hh : held t i r) :
    held s i r ∨ (i,r) ∈ originsAlong p s es := by
  induction h with
  | nil => exact Or.inl hh
  | cons hs _ ih =>
      rcases ih hh with old | later
      · rcases step_held_origin hs old with before | now
        · exact Or.inl before
        · exact Or.inr (List.mem_append_left _ now)
      · rcases hs with ⟨_,_,rfl⟩
        exact Or.inr (List.mem_append_right _ later)

theorem empty_trace_provenance {p : Producer W E H R} {n b c i : Nat} {w : W}
    {t : State W H R} {es : List (Event W E H)} {r : R}
    (h : Generative.Trace (process p n) (empty w b c) es t) (hs : stored t i r) :
    (i,r) ∈ originsAlong p (empty w b c) es := by
  rcases trace_held_origin h (Or.inl hs) with bad | good
  · exact False.elim (empty_holds_nothing w b c i r bad)
  · exact good

def bindings : List (Event W E H) → Nat
  | [] => 0
  | .bind _ _ :: es => 1+bindings es
  | _ :: es => bindings es

theorem step_cell_ledger {p : Producer W E H R} {n : Nat} {s t : State W H R}
    {e : Event W E H} (h : Step p n s e t) : t.blanks+4*bindings [e]=s.blanks := by
  rcases h with ⟨_,he,rfl⟩
  cases e with
  | bind i header => simp [advance,bindings]; have hc := he.2.2.2.1; omega
  | core e w => simp [advance,bindings]
  | write =>
      rcases he.2 with ⟨i,r,bits,hp,_,_⟩
      simp only [advance,hp]
      split <;> simp [bindings]

theorem trace_cell_ledger {p : Producer W E H R} {n : Nat} {s t : State W H R}
    {es : List (Event W E H)} (h : Generative.Trace (process p n) s es t) :
    t.blanks+4*bindings es=s.blanks := by
  induction h with
  | nil => simp [bindings]
  | @cons s u t e es hs ht ih =>
      have hh := step_cell_ledger hs
      cases e <;> simp only [bindings] at * <;> omega

theorem twelve_cells_admit_at_most_three {p : Producer W E H R} {n : Nat} {w : W} {b : Nat}
    {t : State W H R} {es : List (Event W E H)}
    (h : Generative.Trace (process p n) (empty w b 12) es t) : bindings es ≤ 3 := by
  have hh := trace_cell_ledger h
  simp only [empty] at hh
  omega

def writeRun (p : Producer W E H R) (s : State W H R) : Nat → State W H R
  | 0 => s
  | k+1 => writeRun p (advance p s .write) k

theorem four_writes_endpoint (p : Producer W E H R) (s : State W H R) (i : Nat) (r : R)
    (hp : s.phase=.latched i r []) (hf : s.escrow=4) :
    (writeRun p s 4).records i=some r ∧ (writeRun p s 4).escrow=0 ∧
    (writeRun p s 4).phase=.idle ∧ (writeRun p s 4).world=s.world := by
  simp [writeRun,advance,hp,hf,p.fourBits,put]

end EmissionArchive

#print axioms EmissionArchive.empty_valid
#print axioms EmissionArchive.empty_holds_nothing
#print axioms EmissionArchive.binding_preserves_world
#print axioms EmissionArchive.write_preserves_world
#print axioms EmissionArchive.core_preserves_archive_funds
#print axioms EmissionArchive.cannot_bind_completed
#print axioms EmissionArchive.step_energy
#print axioms EmissionArchive.trace_energy
#print axioms EmissionArchive.step_completed_immutable
#print axioms EmissionArchive.trace_completed_immutable
#print axioms EmissionArchive.step_valid
#print axioms EmissionArchive.trace_valid
#print axioms EmissionArchive.step_held_origin
#print axioms EmissionArchive.trace_held_origin
#print axioms EmissionArchive.empty_trace_provenance
#print axioms EmissionArchive.step_cell_ledger
#print axioms EmissionArchive.trace_cell_ledger
#print axioms EmissionArchive.twelve_cells_admit_at_most_three
#print axioms EmissionArchive.four_writes_endpoint
