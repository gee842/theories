import CorrectionRelations
import CorrectionHandoff

set_option autoImplicit false

/-!
Versioned, stepwise correction through two banks of translation relations.
Banks and requests are roles in one installation, not independent substances.
A bank is assembled one translation at a time; publication and capture/pinning
are short atomic protocol steps. A request reads each actual retained bank hop.
All changes obey the guards; physical faults, weak memory and forged requests
are outside this interleaving model. The route endpoint correspondence is supplied.
-/
namespace CorrectionVersioned
open CorrectionRelations

structure Bank where
  path : List Bool
  summary : Bool
  sealed : Bool
  deriving DecidableEq, Repr

def Sound (b : Bank) : Prop := b.summary = Parity b.path

def Ready (span : Nat) (b : Bank) : Prop :=
  b.sealed = true ∧ b.path.length = span

instance readyDecidable (span : Nat) (b : Bank) : Decidable (Ready span b) := by
  unfold Ready
  infer_instance

def emptyBank : Bank := ⟨[], false, false⟩

def appendBank (b : Bank) (p : Bool) : Bank :=
  ⟨b.path ++ [p], xor b.summary p, false⟩

def asChannel (b : Bank) : CorrectionHandoff.Channel :=
  ⟨0, Parity b.path, b.sealed, some ⟨0, b.summary⟩⟩

theorem empty_sound : Sound emptyBank := rfl

theorem append_sound (b : Bank) (h : Sound b) (p : Bool) : Sound (appendBank b p) := by
  unfold Sound appendBank
  rw [h, parity_append]
  cases p <;> rfl

theorem inherited_channel_sound (b : Bank) (h : Sound b) :
    CorrectionHandoff.Sound (asChannel b) := by
  intro r hr
  simp only [asChannel, Option.some.injEq] at hr
  subst r
  exact ⟨Nat.le_refl _, fun _ => h⟩

theorem inherited_channel_ready (span : Nat) (b : Bank) (h : Ready span b) :
    CorrectionHandoff.Ready (asChannel b) :=
  ⟨h.1, ⟨0, b.summary⟩, rfl, rfl⟩

theorem prepared_path_delivers (span : Nat) (b : Bank) (hs : Sound b)
    (hr : Ready span b) (requested : Bool) :
    Follow b.path (xor requested b.summary) = requested := by
  have old := CorrectionHandoff.ready_executes (asChannel b)
    (inherited_channel_sound b hs) (inherited_channel_ready span b hr) requested
  simp only [CorrectionHandoff.execute, asChannel, hr.1, ↓reduceIte,
    Option.map_some, CorrectionHandoff.decode, Option.some.injEq] at old
  rw [propagation_parity]
  exact old

structure Packet where
  slot : Bool
  cursor : Nat
  payload : Bool
  requested : Bool
  deriving DecidableEq, Repr

structure Installation where
  active : Bool
  banks : Bool → Bank
  packets : List Packet

def PacketValid (span : Nat) (s : Installation) (p : Packet) : Prop :=
  Ready span (s.banks p.slot) ∧ p.cursor ≤ (s.banks p.slot).path.length ∧
    Follow ((s.banks p.slot).path.drop p.cursor) p.payload = p.requested

def Invariant (span : Nat) (s : Installation) : Prop :=
  (∀ b, Sound (s.banks b)) ∧ Ready span (s.banks s.active) ∧
    ∀ p ∈ s.packets, PacketValid span s p

def busy (s : Installation) (b : Bool) : Bool :=
  s.packets.any (fun p => p.slot == b)

def replaceBank (s : Installation) (b : Bool) (bank : Bank) : Installation :=
  { s with banks := fun j => if j = b then bank else s.banks j }

def available (s : Installation) (b : Bool) : Prop := b ≠ s.active ∧ busy s b = false

instance availableDecidable (s : Installation) (b : Bool) : Decidable (available s b) := by
  unfold available
  infer_instance

theorem live_packet_pins (s : Installation) (p : Packet) (hp : p ∈ s.packets) :
    busy s p.slot = true := by
  simp only [busy, List.any_eq_true]
  exact ⟨p, hp, by simp⟩

theorem unpinned_differs (s : Installation) (b : Bool) (hb : busy s b = false)
    (p : Packet) (hp : p ∈ s.packets) : p.slot ≠ b := by
  intro he
  have pin := live_packet_pins s p hp
  rw [he, hb] at pin
  contradiction

theorem replace_available_preserves (span : Nat) (s : Installation) (h : Invariant span s)
    (b : Bool) (free : available s b) (bank : Bank) (hs : Sound bank) :
    Invariant span (replaceBank s b bank) := by
  constructor
  · intro j
    simp only [replaceBank]
    split_ifs
    · exact hs
    · exact h.1 j
  constructor
  · simpa [replaceBank, Ne.symm free.1] using h.2.1
  · intro p hp
    have ne := unpinned_differs s b free.2 p hp
    simpa [PacketValid, replaceBank, ne] using h.2.2 p hp

def reset (s : Installation) (b : Bool) : Installation :=
  if available s b then replaceBank s b emptyBank else s

def append (span : Nat) (s : Installation) (b p : Bool) : Installation :=
  if available s b ∧ (s.banks b).sealed = false ∧ (s.banks b).path.length < span then
    replaceBank s b (appendBank (s.banks b) p) else s

def certify (span : Nat) (s : Installation) (b : Bool) : Installation :=
  if available s b ∧ (s.banks b).path.length = span then
    replaceBank s b { s.banks b with sealed := true } else s

def publish (span : Nat) (s : Installation) (b : Bool) : Installation :=
  if Ready span (s.banks b) then { s with active := b } else s

/-- Capture of active version, command encoding and request registration is
    atomic here. Reading active first and registering later is not this step. -/
def beginRequest (capacity : Nat) (s : Installation) (requested : Bool) : Installation :=
  if s.packets.length < capacity then
    { s with packets := s.packets ++ [⟨s.active, 0,
      xor requested (s.banks s.active).summary, requested⟩] } else s

theorem reset_preserves (span : Nat) (s : Installation) (h : Invariant span s) (b : Bool) :
    Invariant span (reset s b) := by
  unfold reset
  split_ifs with hf
  · exact replace_available_preserves span s h b hf emptyBank empty_sound
  · exact h

theorem append_preserves (span : Nat) (s : Installation) (h : Invariant span s) (b p : Bool) :
    Invariant span (append span s b p) := by
  unfold append
  split_ifs with hf
  · exact replace_available_preserves span s h b hf.1 _ (append_sound _ (h.1 b) p)
  · exact h

theorem seal_preserves (span : Nat) (s : Installation) (h : Invariant span s) (b : Bool) :
    Invariant span (certify span s b) := by
  unfold certify
  split_ifs with hf
  · exact replace_available_preserves span s h b hf.1 _ (h.1 b)
  · exact h

theorem publish_preserves (span : Nat) (s : Installation) (h : Invariant span s) (b : Bool) :
    Invariant span (publish span s b) := by
  unfold publish
  split_ifs with hr
  · exact ⟨h.1, hr, h.2.2⟩
  · exact h

theorem begin_preserves (span capacity : Nat) (s : Installation) (h : Invariant span s)
    (requested : Bool) : Invariant span (beginRequest capacity s requested) := by
  unfold beginRequest
  split_ifs
  · refine ⟨h.1, h.2.1, ?_⟩
    intro p hp
    simp only [List.mem_append, List.mem_singleton] at hp
    rcases hp with hp | hp
    · exact h.2.2 p hp
    · subst p
      exact ⟨h.2.1, Nat.zero_le _, prepared_path_delivers span _ (h.1 _) h.2.1 requested⟩
  · exact h

/-- One hop reads the pinned bank, not the currently published bank. Completion
    removes the pin only after obtaining the delivered value. -/
def tick (s : Installation) : Installation × Option (Bool × Bool) :=
  match s.packets with
  | [] => (s, none)
  | p :: ps =>
    match (s.banks p.slot).path.drop p.cursor with
    | [] => ({ s with packets := ps }, some (p.requested, p.payload))
    | bit :: _ => ({ s with packets :=
        { p with cursor := p.cursor + 1, payload := xor p.payload bit } :: ps }, none)

theorem drop_after_hop (path : List Bool) (cursor : Nat) (bit : Bool) (tail : List Bool)
    (h : path.drop cursor = bit :: tail) : path.drop (cursor + 1) = tail := by
  rw [← List.drop_drop, h]
  rfl

theorem tick_preserves_and_output (span : Nat) (s : Installation) (h : Invariant span s) :
    Invariant span (tick s).1 ∧ ∀ request value, (tick s).2 = some (request, value) → value = request := by
  cases hp : s.packets with
  | nil => simp [tick, hp, h]
  | cons p ps =>
    have vp := h.2.2 p (by simp [hp])
    cases hd : (s.banks p.slot).path.drop p.cursor with
    | nil =>
      simp only [tick, hp, hd]
      constructor
      · refine ⟨h.1, h.2.1, ?_⟩
        intro q hq
        exact h.2.2 q (by simp [hp, hq])
      · intro request value out
        simp only [Option.some.injEq, Prod.mk.injEq] at out
        have result := vp.2.2
        rw [hd] at result
        change p.payload = p.requested at result
        exact out.2.symm.trans (result.trans out.1)
    | cons bit tail =>
      simp only [tick, hp, hd]
      constructor
      · refine ⟨h.1, h.2.1, ?_⟩
        intro q hq
        simp only [List.mem_cons] at hq
        rcases hq with hq | hq
        · subst q
          refine ⟨vp.1, ?_, ?_⟩
          · have len := congrArg List.length hd
            simp only [List.length_drop, List.length_cons] at len
            dsimp
            omega
          · change Follow ((s.banks p.slot).path.drop (p.cursor + 1))
              (xor p.payload bit) = p.requested
            rw [drop_after_hop _ _ _ _ hd]
            have result := vp.2.2
            rw [hd] at result
            exact result
        · exact h.2.2 q (by simp [hp, hq])
      · intro request value out
        simp at out

/-- The FIFO scheduler gives the head one hop on each tick. No scheduler
    fairness or wall-clock deadline is supplied by the safety invariant. -/
def drain : Nat → Installation → Installation × List (Bool × Bool)
  | 0, s => (s, [])
  | n + 1, s =>
      let next := tick s
      let result := drain n next.1
      (result.1, next.2.toList ++ result.2)

theorem head_traversal_completes (remaining : List Bool) (s : Installation)
    (p : Packet) (ps : List Packet) (hp : s.packets = p :: ps)
    (hr : (s.banks p.slot).path.drop p.cursor = remaining) :
    let result := drain (remaining.length + 1) s
    result.1.packets = ps ∧ result.1.banks = s.banks ∧ result.1.active = s.active ∧
      result.2 = [(p.requested, Follow remaining p.payload)] := by
  induction remaining generalizing s p with
  | nil => simp [drain, tick, hp, hr, Follow]
  | cons bit tail ih =>
    let nextPacket : Packet := { p with cursor := p.cursor + 1, payload := xor p.payload bit }
    let nextState : Installation := { s with packets := nextPacket :: ps }
    have hnext : (nextState.banks nextPacket.slot).path.drop nextPacket.cursor = tail :=
      drop_after_hop _ _ _ _ hr
    have result := ih nextState nextPacket rfl hnext
    simpa [drain, tick, hp, hr, Follow, nextState, nextPacket] using result

theorem valid_head_completes (span : Nat) (s : Installation) (h : Invariant span s)
    (p : Packet) (ps : List Packet) (hp : s.packets = p :: ps) :
    let result := drain (((s.banks p.slot).path.drop p.cursor).length + 1) s
    result.1.packets = ps ∧ result.1.banks = s.banks ∧ result.1.active = s.active ∧
      result.2 = [(p.requested, p.requested)] := by
  have result := head_traversal_completes _ s p ps hp rfl
  have valid := h.2.2 p (by simp [hp])
  simpa [valid.2.2] using result

inductive Operation where
  | reset (slot : Bool)
  | append (slot bit : Bool)
  | certify (slot : Bool)
  | publish (slot : Bool)
  | beginRequest (requested : Bool)
  | tick
  | pause
  deriving DecidableEq, Repr

def step (span capacity : Nat) (s : Installation) : Operation → Installation × Option (Bool × Bool)
  | .reset b => (reset s b, none)
  | .append b p => (append span s b p, none)
  | .certify b => (certify span s b, none)
  | .publish b => (publish span s b, none)
  | .beginRequest r => (beginRequest capacity s r, none)
  | .tick => tick s
  | .pause => (s, none)

theorem step_preserves_and_output (span capacity : Nat) (s : Installation)
    (h : Invariant span s) (op : Operation) :
    Invariant span (step span capacity s op).1 ∧
      ∀ request value, (step span capacity s op).2 = some (request, value) → value = request := by
  cases op with
  | reset b => exact ⟨reset_preserves span s h b, by simp [step]⟩
  | append b p => exact ⟨append_preserves span s h b p, by simp [step]⟩
  | certify b => exact ⟨seal_preserves span s h b, by simp [step]⟩
  | publish b => exact ⟨publish_preserves span s h b, by simp [step]⟩
  | beginRequest r => exact ⟨begin_preserves span capacity s h r, by simp [step]⟩
  | tick => exact tick_preserves_and_output span s h
  | pause => exact ⟨h, by simp [step]⟩

def run (span capacity : Nat) (s : Installation) : List Operation → Installation
  | [] => s
  | op :: ops => run span capacity (step span capacity s op).1 ops

theorem run_preserves (span capacity : Nat) (s : Installation)
    (h : Invariant span s) (ops : List Operation) : Invariant span (run span capacity s ops) := by
  induction ops generalizing s with
  | nil => exact h
  | cons op ops ih => exact ih _ (step_preserves_and_output span capacity s h op).1

theorem every_prefix_correct (span capacity : Nat) (s : Installation)
    (h : Invariant span s) (ops : List Operation) (n : Nat) (op : Operation)
    (request value : Bool)
    (out : (step span capacity (run span capacity s (ops.take n)) op).2 = some (request,value)) :
    value = request :=
  (step_preserves_and_output span capacity _ (run_preserves span capacity s h _) op).2 _ _ out

theorem pinned_bank_cannot_be_reset (s : Installation) (p : Packet) (hp : p ∈ s.packets) :
    reset s p.slot = s := by
  simp [reset, available, live_packet_pins s p hp]

theorem pinned_bank_cannot_be_appended (span : Nat) (s : Installation) (p : Packet)
    (hp : p ∈ s.packets) (bit : Bool) : append span s p.slot bit = s := by
  simp [append, available, live_packet_pins s p hp]

/-- Even an atomic change preserving the instantaneous whole relation can
    defeat a request which traverses a mixture of the two versions. -/
theorem equal_whole_relations_do_not_protect_mixed_requests (p requested : Bool) :
    (∀ a z, Path [p,p] a z ↔ Path [!p,!p] a z) ∧
      Follow [!p] (Follow [p] requested) = !requested := by
  constructor
  · intro a z
    rw [path_iff_propagated, path_iff_propagated]
    cases p <;> cases a <;> rfl
  · cases p <;> cases requested <;> rfl


def initial (path : List Bool) : Installation :=
  ⟨false, fun b => if b then emptyBank else ⟨path, Parity path, true⟩, []⟩

theorem initial_invariant (path : List Bool) : Invariant path.length (initial path) := by
  refine ⟨?_, ?_, ?_⟩
  · intro b
    cases b <;> rfl
  · exact ⟨rfl, rfl⟩
  · simp [initial]

theorem publication_selects_ready (span : Nat) (s : Installation) (b : Bool)
    (h : Ready span (s.banks b)) : (publish span s b).active = b := by
  simp [publish, h]

theorem full_request_capacity_blocks_admission (capacity : Nat) (s : Installation)
    (h : capacity ≤ s.packets.length) (requested : Bool) : beginRequest capacity s requested = s := by
  simp [beginRequest, Nat.not_lt.mpr h]

theorem two_banks_can_both_be_unavailable (s : Installation) (p : Packet)
    (hp : p ∈ s.packets) (old : p.slot ≠ s.active) : ∀ b, ¬ available s b := by
  intro b free
  have same : b = p.slot := by
    cases hb : b <;> cases ha : s.active <;> cases hs : p.slot <;>
      simp_all [available]
  have pin := live_packet_pins s p hp
  rw [← same, free.2] at pin
  contradiction

def handoffExample : List Operation :=
  [.beginRequest true, .tick, .reset true, .append true true, .append true true,
   .certify true, .publish true, .reset false, .tick, .tick, .reset false,
   .beginRequest false, .tick, .tick, .tick]

theorem staged_handoff_finishes_both_requests :
    (drain 3 (run 2 2 (initial [false,false])
      [.beginRequest true, .tick, .reset true, .append true true, .append true true,
       .certify true, .publish true, .reset false])).2 = [(true,true)] ∧
    (run 2 2 (initial [false,false]) handoffExample).packets = [] ∧
    (run 2 2 (initial [false,false]) handoffExample).active = true := by decide

/-- A retired slot may only be reused after its registered requests drain.
    Bypassing that guard can mix histories even with a sound new summary. -/
def forceReuse (s : Installation) (b : Bool) (path : List Bool) : Installation :=
  replaceBank s b ⟨path, Parity path, true⟩

theorem premature_reuse_can_deliver_wrong :
    let s := run 2 2 (initial [true,true]) [.beginRequest true, .tick,
      .reset true, .append true false, .append true false, .certify true, .publish true]
    (drain 2 (forceReuse s false [false,false])).2 = [(true,false)] := by decide

def readCurrentVersion (s : Installation) : Installation :=
  { s with packets := s.packets.map (fun p => { p with slot := s.active }) }

theorem switching_version_mid_request_fails :
    let s := run 2 2 (initial [true,true]) [.beginRequest true, .tick,
      .reset true, .append true false, .append true false, .certify true, .publish true]
    (drain 2 (readCurrentVersion s)).2 = [(true,false)] := by decide

/-- This is deliberately a split-acquisition counterexample. The packet fields
    are exactly those captured from initial [true,true] for a true request,
    but registration occurs only after publication, reclamation and reuse. -/
theorem late_registration_after_capture_can_fail :
    let current := run 2 2 (initial [true,true])
      [.reset true, .append true false, .append true false, .certify true, .publish true,
       .reset false, .append false true, .append false false, .certify false]
    (drain 3 { current with packets := [⟨false,0,true,true⟩] }).2 = [(true,false)] := by decide

theorem completion_allows_old_retirement (span : Nat) (s : Installation)
    (h : Invariant span s) (p : Packet) (hp : s.packets = [p])
    (old : p.slot ≠ s.active) :
    available (drain (((s.banks p.slot).path.drop p.cursor).length + 1) s).1 p.slot := by
  have result := valid_head_completes span s h p [] hp
  constructor
  · rw [result.2.2.1]
    exact old
  · unfold busy
    rw [result.1]
    rfl

theorem pause_is_not_a_progress_guarantee :
    (run 2 2 (initial [false,false]) [.beginRequest true, .pause, .pause]).packets.length = 1 := by decide

end CorrectionVersioned
