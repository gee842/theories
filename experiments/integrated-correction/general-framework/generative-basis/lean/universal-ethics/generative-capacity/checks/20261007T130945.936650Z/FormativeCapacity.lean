import GenerativeCore

/-!
# Finite terminal production and continuing structural formation

A supplied local assembly law, not an ethical definition. A tree's rightmost
terminal is either an input socket or an ordinary atom. Input can enter only
through that socket. Each growth event incorporates the old terminal as a branch
and forms a new atom and replacement terminal from two stored parts. Thus an open
tree's next socket is at a newly formed, deeper address; phase alone grants no
input access. Work is separate from structural material and is consumed.

Both routes share one feed and initial socket. Commissioning consumes one work
unit. Closing converts the socket into an atom, so all subsequent construction
uses a finite accumulated stock. Keeping it open permits a capture/build cycle.
The constant feed supplies unbounded input; no physical inexhaustibility, source
formation, biological life, increasing variety, universal innovation, or ethical
ranking is proved. Depth is configured dependency depth in one fixed grammar.
-/

namespace FormativeCapacity

inductive Tree where
  | atom
  | socket
  | branch (left right : Tree)
  deriving DecidableEq, Repr

def parts : Tree → Nat
  | .atom | .socket => 1
  | .branch l r => parts l + parts r + 1

def depth : Tree → Nat
  | .atom | .socket => 0
  | .branch l r => max (depth l) (depth r) + 1

/-- The address length of the actual accessible input terminal, if present. -/
def socketAddress : Tree → Option Nat
  | .atom => none
  | .socket => some 0
  | .branch _ r => (socketAddress r).map (· + 1)

def live (t : Tree) : Bool := (socketAddress t).isSome

/-- The old terminal becomes the branch; two raw parts form the new terminals. -/
def grow : Tree → Tree
  | .atom => .branch .atom .atom
  | .socket => .branch .atom .socket
  | .branch l r => .branch l (grow r)

/-- A structural reconfiguration, not a freely switchable permission flag. -/
def close : Tree → Tree
  | .atom | .socket => .atom
  | .branch l r => .branch l (close r)

def spine : Nat → Tree → Tree
  | 0, terminal => terminal
  | n + 1, terminal => .branch .atom (spine n terminal)

theorem grow_parts (t : Tree) : parts (grow t) = parts t + 2 := by
  induction t with
  | atom | socket => rfl
  | branch l r _ ih => simp only [grow, parts, ih]; omega

theorem close_parts (t : Tree) : parts (close t) = parts t := by
  induction t with
  | atom | socket => rfl
  | branch l r _ ih => simp only [close, parts, ih]

theorem close_has_no_socket (t : Tree) : socketAddress (close t) = none := by
  induction t with
  | atom | socket => rfl
  | branch l r _ ih => simp only [close, socketAddress, ih, Option.map_none]

theorem grow_socket_address (t : Tree) :
    socketAddress (grow t) = (socketAddress t).map (· + 1) := by
  induction t with
  | atom | socket => rfl
  | branch l r _ ih =>
    simp only [grow, socketAddress, ih]

theorem grow_live (t : Tree) : live (grow t) = live t := by
  unfold live
  rw [grow_socket_address]
  cases socketAddress t <;> rfl

theorem spine_grows (n : Nat) (terminal : Tree)
    (h : terminal = .atom ∨ terminal = .socket) :
    grow (spine n terminal) = spine (n + 1) terminal := by
  induction n with
  | zero => rcases h with rfl | rfl <;> rfl
  | succ n ih => simp only [spine, grow, ih]

theorem spine_depth (n : Nat) (terminal : Tree)
    (h : terminal = .atom ∨ terminal = .socket) : depth (spine n terminal) = n := by
  induction n with
  | zero => rcases h with rfl | rfl <;> rfl
  | succ n ih => simp only [spine, depth, ih, Nat.zero_max]

theorem spine_socket_address (n : Nat) : socketAddress (spine n .socket) = some n := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [spine, socketAddress, ih, Option.map_some]

theorem spine_closed_address (n : Nat) : socketAddress (spine n .atom) = none := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [spine, socketAddress, ih, Option.map_none]

inductive Phase where
  | gathering
  | building
  deriving DecidableEq, Repr

structure State where
  tree : Tree
  raw : Nat
  work : Nat
  cursor : Nat
  phase : Phase
  deriving DecidableEq, Repr

inductive Event where
  | capture
  | commissionClosed
  | commissionOpen
  | build
  deriving DecidableEq, Repr

/-- Availability of successive source lots: each transfers two parts and one work unit.
The same schedule is used by both routes. It is a supplied relation of this model. -/
abbrev Feed := Nat → Bool

def initial : State := ⟨.socket, 0, 0, 0, .gathering⟩

def advance (s : State) : Event → State
  | .capture => {s with raw := s.raw + 2, work := s.work + 1, cursor := s.cursor + 1}
  | .commissionClosed => {s with tree := close s.tree, work := s.work - 1, phase := .building}
  | .commissionOpen => {s with work := s.work - 1, phase := .building}
  | .build => {s with tree := grow s.tree, raw := s.raw - 2, work := s.work - 1}

def Enabled (feed : Feed) (s : State) : Event → Prop
  | .capture => live s.tree = true ∧ feed s.cursor = true
  | .commissionClosed | .commissionOpen => s.phase = .gathering ∧ 1 ≤ s.work
  | .build => s.phase = .building ∧ 2 ≤ s.raw ∧ 1 ≤ s.work

instance enabledDecidable (feed : Feed) (s : State) (e : Event) : Decidable (Enabled feed s e) := by
  cases e <;> unfold Enabled <;> infer_instance

def Step (feed : Feed) (s : State) (e : Event) (t : State) : Prop :=
  Enabled feed s e ∧ t = advance s e

def process (feed : Feed) : Generative.Process State Event := ⟨Step feed⟩

def children (feed : Feed) (s : State) : List State :=
  ([Event.capture, .commissionClosed, .commissionOpen, .build].filter
    (fun e => decide (Enabled feed s e))).map (advance s)

theorem finite_branching (feed : Feed) (s t : State) :
    (∃ e, Step feed s e t) ↔ t ∈ children feed s := by
  constructor
  · rintro ⟨e, he, rfl⟩
    apply List.mem_map.mpr
    refine ⟨e, List.mem_filter.mpr ⟨?_, by simpa using he⟩, rfl⟩
    cases e <;> simp
  · intro ht
    obtain ⟨e, he, rfl⟩ := List.mem_map.mp ht
    have enabled : Enabled feed s e := of_decide_eq_true (List.mem_filter.mp he).2
    exact ⟨e, enabled, rfl⟩

def material (s : State) : Nat := parts s.tree + s.raw

def inputLots : Event → Nat
  | .capture => 1
  | _ => 0

def workSpent : Event → Nat
  | .capture => 0
  | _ => 1

def total (f : Event → Nat) : List Event → Nat
  | [] => 0
  | e :: es => f e + total f es

theorem step_accounts {feed : Feed} {s t : State} {e : Event}
    (h : Step feed s e t) :
    material t = material s + 2 * inputLots e ∧
    t.work + workSpent e = s.work + inputLots e ∧
    t.cursor = s.cursor + inputLots e := by
  obtain ⟨he, rfl⟩ := h
  refine ⟨?_, ?_, ?_⟩ <;> cases e <;> simp only [Enabled] at he <;>
    simp only [advance, material, inputLots, workSpent, grow_parts, close_parts,
      Nat.mul_one] <;> omega

theorem trace_accounts {feed : Feed} {s t : State} {es : List Event}
    (h : Generative.Trace (process feed) s es t) :
    material t = material s + 2 * total inputLots es ∧
    t.work + total workSpent es = s.work + total inputLots es ∧
    t.cursor = s.cursor + total inputLots es := by
  induction h with
  | nil => simp [total]
  | cons hs _ ih =>
    have step := step_accounts hs
    simp only [total]
    omega

/-- The new accessible socket is one structural address deeper, not a phase bit. -/
theorem build_reconstructs_next_interface {feed : Feed} {s t : State} {address : Nat}
    (h : Step feed s .build t) (old : socketAddress s.tree = some address) :
    socketAddress t.tree = some (address + 1) ∧
    parts t.tree = parts s.tree + 2 ∧ t.raw + 2 = s.raw ∧ t.work + 1 = s.work := by
  obtain ⟨he, rfl⟩ := h
  simp only [Enabled] at he
  refine ⟨?_, grow_parts s.tree, by simp only [advance]; omega, by simp only [advance]; omega⟩
  simp only [advance, grow_socket_address, old, Option.map_some]

theorem no_socket_no_capture (feed : Feed) (s : State) (h : live s.tree = false) :
    ¬ Enabled feed s .capture := by
  intro he
  have := he.1
  simp [h] at this

theorem closed_step_spends {feed : Feed} {s t : State} {e : Event}
    (h : Step feed s e t) (closed : live s.tree = false) :
    live t.tree = false ∧ t.work + 1 = s.work ∧ t.cursor = s.cursor := by
  obtain ⟨he, rfl⟩ := h
  cases e with
  | capture => exact False.elim (no_socket_no_capture feed s closed he)
  | commissionClosed =>
    refine ⟨?_, ?_, rfl⟩
    · simp only [advance, live, close_has_no_socket, Option.isSome_none]
    · simp only [Enabled] at he; simp only [advance]; omega
  | commissionOpen =>
    refine ⟨closed, ?_, rfl⟩
    simp only [Enabled] at he; simp only [advance]; omega
  | build =>
    refine ⟨?_, ?_, rfl⟩
    · simp only [advance, grow_live, closed]
    · simp only [Enabled] at he; simp only [advance]; omega

def InfiniteFrom (feed : Feed) (start : State) (states : Nat → State)
    (events : Nat → Event) : Prop := states 0 = start ∧ ∀ n, Step feed (states n) (events n) (states (n+1))

theorem closed_no_infinite {feed : Feed} {start : State} (closed : live start.tree = false) :
    ¬ ∃ states events, InfiniteFrom feed start states events := by
  rintro ⟨states, events, first, steps⟩
  have bound : ∀ n, live (states n).tree = false ∧ (states n).work + n = start.work := by
    intro n
    induction n with
    | zero => simp [first, closed]
    | succ n ih =>
      have next := closed_step_spends (steps n) ih.1
      exact ⟨next.1, by omega⟩
  have impossible := (bound (start.work + 1)).2
  omega

theorem infinite_never_commissions_closed {feed : Feed} {start : State}
    {states : Nat → State} {events : Nat → Event}
    (run : InfiniteFrom feed start states events) (n : Nat) : events n ≠ .commissionClosed := by
  intro he
  have step := run.2 n
  rw [he] at step
  have closed : live (states (n+1)).tree = false := by
    rw [step.2]
    simp only [advance, live, close_has_no_socket, Option.isSome_none]
  apply closed_no_infinite closed
  refine ⟨fun k => states (n+1+k), fun k => events (n+1+k), rfl, ?_⟩
  intro k
  simpa only [Nat.add_assoc] using run.2 (n+1+k)

/-- An infinite execution of the one-shot route only gathers; it never forms a layer. -/
theorem one_shot_infinite_only_gathers {feed : Feed} {states : Nat → State} {events : Nat → Event}
    (run : InfiniteFrom feed initial states events)
    (oneShot : ∀ n, events n ≠ .commissionOpen) :
    ∀ n, (states n).phase = .gathering ∧ (states n).tree = .socket ∧ events n = .capture := by
  intro n
  have config : ∀ k, (states k).phase = .gathering ∧ (states k).tree = .socket := by
    intro k
    induction k with
    | zero => rw [run.1]; exact ⟨rfl, rfl⟩
    | succ k ih =>
      have step := run.2 k
      have event : events k = .capture := by
        cases he : events k with
        | capture => rfl
        | commissionClosed => exact False.elim (infinite_never_commissions_closed run k he)
        | commissionOpen => exact False.elim (oneShot k he)
        | build =>
          rw [he] at step
          have phase := step.1.1
          rw [ih.1] at phase
          cases phase
      rw [event] at step
      rw [step.2]
      exact ih
  have state := config n
  refine ⟨state.1, state.2, ?_⟩
  have step := run.2 n
  cases he : events n with
  | capture => rfl
  | commissionClosed => exact False.elim (infinite_never_commissions_closed run n he)
  | commissionOpen => exact False.elim (oneShot n he)
  | build =>
    rw [he] at step
    have phase := step.1.1
    rw [state.1] at phase
    cases phase

def constantFeed : Feed := fun _ => true

def gathered (n : Nat) : State := ⟨.socket, 2*n, n, n, .gathering⟩

theorem gather_step (n : Nat) : Step constantFeed (gathered n) .capture (gathered (n+1)) := by
  constructor
  · exact ⟨rfl, rfl⟩
  · simp [gathered, advance, Nat.mul_add]

def gatherWord : Nat → List Event
  | 0 => []
  | n+1 => gatherWord n ++ [.capture]

theorem gather_trace (n : Nat) :
    Generative.Trace (process constantFeed) initial (gatherWord n) (gathered n) := by
  induction n with
  | zero => exact .nil _
  | succ n ih =>
    exact Generative.trace_append_iff.mpr ⟨gathered n, ih, .cons (gather_step n) (.nil _)⟩

def batchState (formed remaining : Nat) : State :=
  ⟨spine formed .atom, 2*(remaining+1), remaining, formed+remaining+1, .building⟩

theorem batch_commission (n : Nat) :
    Step constantFeed (gathered (n+1)) .commissionClosed (batchState 0 n) := by
  constructor
  · exact ⟨rfl, by simp [gathered]⟩
  · simp [gathered, batchState, spine, advance, close]

theorem batch_build (formed remaining : Nat) :
    Step constantFeed (batchState formed (remaining+1)) .build (batchState (formed+1) remaining) := by
  constructor
  · refine ⟨rfl, ?_, ?_⟩ <;> simp only [batchState] <;> omega
  · simp only [batchState, advance, spine_grows _ _ (Or.inl rfl)]
    congr 1 <;> omega

theorem batch_builds (formed remaining : Nat) :
    Generative.Trace (process constantFeed) (batchState formed remaining)
      (List.replicate remaining .build) (batchState (formed+remaining) 0) := by
  induction remaining generalizing formed with
  | zero => exact .nil _
  | succ remaining ih =>
    have continuation := ih (formed+1)
    have endpoint : formed+1+remaining = formed+(remaining+1) := by omega
    rw [endpoint] at continuation
    exact .cons (batch_build formed remaining) continuation

theorem batch_terminal (n : Nat) : ∀ e, ¬ Enabled constantFeed (batchState n 0) e := by
  intro e he
  cases e with
  | capture =>
    exact no_socket_no_capture _ _ (by simp [batchState, live, spine_closed_address]) he
  | commissionClosed | commissionOpen => cases he.1
  | build => have := he.2.2; simp [batchState] at this

/-- No unbounded initial stock is supplied: each finite stock has an actual capture history. -/
theorem arbitrary_finite_terminal_depth (n : Nat) :
    ∃ word, Generative.Trace (process constantFeed) initial word (batchState n 0) ∧
      depth (batchState n 0).tree = n ∧
      (∀ e, ¬ Enabled constantFeed (batchState n 0) e) := by
  refine ⟨gatherWord (n+1) ++ (.commissionClosed :: List.replicate n .build), ?_, ?_, batch_terminal n⟩
  · apply Generative.trace_append_iff.mpr
    refine ⟨gathered (n+1), gather_trace _, .cons (batch_commission n) ?_⟩
    simpa only [Nat.zero_add] using batch_builds 0 n
  · exact spine_depth n .atom (Or.inl rfl)

def milestone (n : Nat) : State := ⟨spine n .socket, 2, 0, n+1, .building⟩

def charged (n : Nat) : State := ⟨spine n .socket, 4, 1, n+2, .building⟩

theorem open_commission : Step constantFeed (gathered 1) .commissionOpen (milestone 0) := by
  exact ⟨⟨rfl, by decide⟩, rfl⟩

theorem cycle_capture (n : Nat) : Step constantFeed (milestone n) .capture (charged n) := by
  constructor
  · exact ⟨by simp [milestone, live, spine_socket_address], rfl⟩
  · rfl

theorem cycle_build (n : Nat) : Step constantFeed (charged n) .build (milestone (n+1)) := by
  constructor
  · exact ⟨rfl, by change 2 ≤ 4; decide, by change 1 ≤ 1; decide⟩
  · simp only [charged, milestone, advance, spine_grows _ _ (Or.inr rfl)]

def nextFrame (f : Nat × Bool) : Nat × Bool := if f.2 then (f.1+1, false) else (f.1, true)

def frame : Nat → Nat × Bool
  | 0 => (0, false)
  | n+1 => nextFrame (frame n)

theorem two_frames (n : Nat) (b : Bool) : nextFrame (nextFrame (n,b)) = (n+1,b) := by
  cases b <;> rfl

theorem even_frame (n : Nat) : frame (2*n) = (n,false) := by
  induction n with
  | zero => rfl
  | succ n ih =>
    have twice : 2*(n+1) = (2*n+1)+1 := by omega
    rw [twice, frame, frame, ih, two_frames]

def growthStates (n : Nat) : State := if (frame n).2 then charged (frame n).1 else milestone (frame n).1
def growthEvents (n : Nat) : Event := if (frame n).2 then .build else .capture

theorem growth_lawful (n : Nat) :
    Step constantFeed (growthStates n) (growthEvents n) (growthStates (n+1)) := by
  unfold growthStates growthEvents
  rw [frame]
  obtain ⟨k,b⟩ := frame n
  cases b with
  | false => exact cycle_capture k
  | true => exact cycle_build k

def fullStates : Nat → State
  | 0 => initial
  | 1 => gathered 1
  | n+2 => growthStates n

def fullEvents : Nat → Event
  | 0 => .capture
  | 1 => .commissionOpen
  | n+2 => growthEvents n

theorem continuing_formation_run : InfiniteFrom constantFeed initial fullStates fullEvents := by
  refine ⟨rfl, ?_⟩
  intro n
  cases n with
  | zero => exact gather_step 0
  | succ n =>
    cases n with
    | zero => exact open_commission
    | succ n => exact growth_lawful n

theorem actual_growth_milestones (n : Nat) :
    fullStates (2*n+2) = milestone n ∧
    depth (fullStates (2*n+2)).tree = n ∧
    socketAddress (fullStates (2*n+2)).tree = some n ∧
    (fullStates (2*n+2)).cursor = n+1 := by
  have hs : fullStates (2*n+2) = milestone n := by
    simp only [fullStates, growthStates, even_frame]
    rfl
  refine ⟨hs, ?_, ?_, ?_⟩
  · rw [hs]; exact spine_depth n .socket (Or.inr rfl)
  · rw [hs]; exact spine_socket_address n
  · rw [hs]; rfl

theorem completed_formations_recur (n : Nat) : fullEvents (2*n+3) = .build := by
  have index : 2*n+3 = (2*n+1)+2 := by omega
  rw [index]
  simp only [fullEvents, growthEvents, frame, even_frame, nextFrame]
  rfl

theorem actual_depth_unbounded : ∀ bound, ∃ time, bound < depth (fullStates time).tree := by
  intro bound
  refine ⟨2*(bound+1)+2, ?_⟩
  rw [(actual_growth_milestones (bound+1)).2.1]
  omega

/-- The same unbounded feed also permits no formation at all. Existence is not inevitability. -/
theorem infinite_gathering_without_formation :
    InfiniteFrom constantFeed initial gathered (fun _ => .capture) ∧
    (∀ n, depth (gathered n).tree = 0) := by
  exact ⟨⟨rfl, gather_step⟩, fun _ => rfl⟩

def finiteFeed (lots : Nat) : Feed := fun cursor => decide (cursor < lots)

theorem finite_feed_cursor_bound (lots : Nat) {s t : State} {e : Event}
    (h : Step (finiteFeed lots) s e t) (bound : s.cursor ≤ lots) : t.cursor ≤ lots := by
  obtain ⟨he, rfl⟩ := h
  cases e with
  | capture =>
    have hn : s.cursor < lots := of_decide_eq_true he.2
    simp only [advance]
    omega
  | commissionClosed | commissionOpen | build => exact bound

theorem finite_feed_trace_bound (lots : Nat) {t : State} {es : List Event}
    (h : Generative.Trace (process (finiteFeed lots)) initial es t) :
    t.cursor ≤ lots ∧ material t ≤ 1+2*lots ∧ total workSpent es ≤ lots := by
  have cursor : ∀ {s t : State} {es : List Event},
      Generative.Trace (process (finiteFeed lots)) s es t → s.cursor ≤ lots → t.cursor ≤ lots := by
    intro s t es tr
    induction tr with
    | nil => exact id
    | cons hs _ ih => exact fun bound => ih (finite_feed_cursor_bound lots hs bound)
  have hc := cursor h (Nat.zero_le lots)
  have accounts := trace_accounts h
  change material t = 1 + 2 * total inputLots es ∧
    t.work + total workSpent es = 0 + total inputLots es ∧
    t.cursor = 0 + total inputLots es at accounts
  exact ⟨hc, by omega, by omega⟩

end FormativeCapacity
