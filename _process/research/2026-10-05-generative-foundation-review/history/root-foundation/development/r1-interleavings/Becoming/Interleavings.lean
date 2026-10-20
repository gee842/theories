import Becoming.Frame

/-!
# Interleavings: the step index read off the relata's own courses

The spine counts steps `0, 1, 2, …` shared by every relatum. `Becoming.Order` and
`Becoming.OrderNormal` showed, for a world given with that index, that the laws need only the
order of joined exchanges. This module starts from the other side, with no shared index: exchanges
act locally, each reading and changing only the relata it touches (`LocalLaw`), and what is given
is each relatum's own course, the exchanges it takes part in, in order. A shared index is an
interleaving of those courses: a list of exchanges whose course at every relatum is that
relatum's own (`ownCourse`, `Interleaves`). No premise beyond what each theorem names.

* **The interleaving carries nothing the relata do not.** Two lists of exchanges giving every
  relatum the same own course reach the same configuration from the same start
  (`run_of_courses`), and so do two traces of the exchange process (`LocalLaw.process`,
  `trace_of_courses`, `trace_of_interleavings`). The proof moves the first exchange of one list
  forward in the other past exchanges sharing no relatum with it (`split_heads`, `run_move`), which
  commute (`act_comm`, `trace_swap`).
* **The index is built, not assumed.** With the relata listed and exchanges told apart, a
  scheduler takes, at each stage, an exchange heading the course of every relatum it touches
  (`ready`, `pick`), and drops it from those courses (`pop`). It completes, within as many stages
  as the courses have exchanges, exactly where some interleaving exists (`schedule_iff`), that is
  exactly where some trace takes every relatum through its given course (`traced_iff`): what it
  returns is an interleaving (`schedule_interleaves`), and where one exists every ready exchange
  can be taken first (`pop_interleaves`), so it is never stuck (`schedule_some`).
* **Exactly where the index is fixed by the relations.** With the relata listed, the own courses
  fix the interleaving (equal own courses, equal lists) exactly where every exchange touches some
  relatum and every two exchanges are the same or share a relatum (`unique_iff`, and on the traces
  from any configuration `traced_unique_iff`). Two exchanges sharing no relatum have the same own
  courses in either order (`swap_courses`).

Reading (the AI's, pending Ren): the shared index of steps is a reading of the relations, not
their ground. What each relatum undergoes, and in what order, is its own course; a global index
adds only an order between exchanges that share no relatum, and that order changes no
configuration. The index is derived from the relations exactly where every two exchanges share a
relatum; elsewhere it is a commitment of the representation, a choice among interleavings that
the relations leave open and the configurations do not read.

Not shown: courses without end (the courses here are finite lists); exchanges that read relata
they do not change, in a footprint of their own (here what an exchange reads and what it may
change are one footprint); the correspondence with a world's footprint of `Becoming.Order`. No
ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace Interleavings

section Lists

variable {α : Type}

theorem mem_cons_split {a b : α} {l : List α} : b ∈ a :: l → b = a ∨ b ∈ l
  | .head _ => .inl rfl
  | .tail _ mem => .inr mem

theorem cons_ne_nil {a : α} {l : List α} : a :: l ≠ [] :=
  fun same => nomatch same

theorem cons_heads {a b : α} {l m : List α} (same : a :: l = b :: m) : a = b :=
  (List.cons.inj same).1

theorem cons_tails {a b : α} {l m : List α} (same : a :: l = b :: m) : l = m :=
  (List.cons.inj same).2

theorem bool_absurd {P : Prop} {b : Bool} (yes : b = true) (no : b = false) : P :=
  Bool.noConfusion (yes.symm.trans no)

/-- The first member of a list where a test holds, if any: before it the test fails. -/
theorem split_first (p : α → Bool) : ∀ L : List α,
    (∀ f, f ∈ L → p f = false) ∨
      ∃ A f B, L = A ++ f :: B ∧ (∀ a, a ∈ A → p a = false) ∧ p f = true
  | [] => .inl fun _ mem => nomatch mem
  | g :: L => by
    cases here : p g with
    | true => exact .inr ⟨[], g, L, rfl, fun _ mem => (nomatch mem), here⟩
    | false =>
      match split_first p L with
      | .inl absent =>
        exact .inl fun f mem => match mem_cons_split mem with
          | .inl same => by rw [same]; exact here
          | .inr rest => absent f rest
      | .inr ⟨A, f, B, split, before, found⟩ =>
        exact .inr ⟨g :: A, f, B, by rw [split]; rfl, fun a mem => match mem_cons_split mem with
          | .inl same => by rw [same]; exact here
          | .inr rest => before a rest, found⟩

theorem length_tail_le : ∀ l : List α, l.tail.length ≤ l.length
  | [] => Nat.le_refl 0
  | _ :: m => Nat.le_succ m.length

end Lists

/-- Exchanges acting locally on relata: each exchange touches some relata, leaves every other
relatum's state as it was (`keeps`), and changes a relatum it touches as the states of the relata
it touches determine (`reads`). -/
structure LocalLaw (X E σ : Type) where
  touches : E → X → Bool
  act : E → (X → σ) → (X → σ)
  keeps : ∀ e s x, touches e x = false → act e s x = s x
  reads : ∀ e s s' x, (∀ y, touches e y = true → s y = s' y) → touches e x = true →
    act e s x = act e s' x

variable {X E σ : Type}

namespace LocalLaw

variable (law : LocalLaw X E σ)

/-- The configuration reached by taking the exchanges of a list in turn. -/
def run : List E → (X → σ) → (X → σ)
  | [], s => s
  | e :: es, s => run es (law.act e s)

/-- A relatum's own course in a list of exchanges: the exchanges touching it, in order. -/
def ownCourse (x : X) : List E → List E
  | [] => []
  | e :: es => match law.touches e x with
    | true => e :: ownCourse x es
    | false => ownCourse x es

/-- Two exchanges share no relatum. -/
def Apart (e f : E) : Prop :=
  ∀ x, law.touches e x = true → law.touches f x = false

/-- The process of exchanges: a step by `e` reaches the configuration `e` makes, relatum by
relatum. -/
def process : Process (X → σ) E :=
  ⟨fun s e s' => ∀ x, s' x = law.act e s x⟩

/-- A list interleaves given courses where every relatum's own course in it is its given one. -/
def Interleaves (c : X → List E) (L : List E) : Prop :=
  ∀ x, law.ownCourse x L = c x

/-- Whether two exchanges share one of the listed relata. -/
def shares : List X → E → E → Bool
  | [], _, _ => false
  | x :: xs, e, f => (law.touches e x && law.touches f x) || shares xs e f

/-- Every exchange touches some relatum, and every two exchanges are the same or share one. -/
def Connected : Prop :=
  (∀ e, ∃ x, law.touches e x = true) ∧
    ∀ e f, e = f ∨ ∃ x, law.touches e x = true ∧ law.touches f x = true

variable {law}

/-! ## Own courses -/

theorem ownCourse_true {x : X} {e : E} (es : List E) (touch : law.touches e x = true) :
    law.ownCourse x (e :: es) = e :: law.ownCourse x es := by
  show (match law.touches e x with
    | true => e :: law.ownCourse x es
    | false => law.ownCourse x es) = _
  rw [touch]

theorem ownCourse_false {x : X} {e : E} (es : List E) (touch : law.touches e x = false) :
    law.ownCourse x (e :: es) = law.ownCourse x es := by
  show (match law.touches e x with
    | true => e :: law.ownCourse x es
    | false => law.ownCourse x es) = _
  rw [touch]

theorem ownCourse_append (x : X) : ∀ A B : List E,
    law.ownCourse x (A ++ B) = law.ownCourse x A ++ law.ownCourse x B
  | [], _ => rfl
  | a :: A, B => by
    show law.ownCourse x (a :: (A ++ B)) = law.ownCourse x (a :: A) ++ law.ownCourse x B
    cases touch : law.touches a x with
    | true =>
      rw [ownCourse_true _ touch, ownCourse_true _ touch, ownCourse_append x A B]
      rfl
    | false =>
      rw [ownCourse_false _ touch, ownCourse_false _ touch, ownCourse_append x A B]

theorem ownCourse_untouched {x : X} : ∀ {A : List E}, (∀ a, a ∈ A → law.touches a x = false) →
    law.ownCourse x A = []
  | [], _ => rfl
  | a :: A, absent => by
    rw [ownCourse_false _ (absent a (.head A))]
    exact ownCourse_untouched fun b mem => absent b (.tail a mem)

/-! ## Running -/

/-- An exchange taken on agreeing configurations gives agreeing configurations. -/
theorem act_agree (e : E) {s s' : X → σ} (same : ∀ x, s x = s' x) :
    ∀ x, law.act e s x = law.act e s' x := by
  intro x
  cases touch : law.touches e x with
  | false => rw [law.keeps e s x touch, law.keeps e s' x touch]; exact same x
  | true => exact law.reads e s s' x (fun y _ => same y) touch

theorem run_agree : ∀ (L : List E) {s s' : X → σ}, (∀ x, s x = s' x) →
    ∀ x, law.run L s x = law.run L s' x
  | [], _, _, same => same
  | e :: L, _, _, same => run_agree L (act_agree e same)

theorem Apart.symm {e f : E} (apart : law.Apart e f) : law.Apart f e := by
  intro x touch
  cases other : law.touches e x with
  | false => rfl
  | true => exact bool_absurd touch (apart x other)

/-- **Exchanges sharing no relatum commute.** -/
theorem act_comm {e f : E} (apart : law.Apart e f) (s : X → σ) :
    ∀ x, law.act f (law.act e s) x = law.act e (law.act f s) x := by
  intro x
  cases touchE : law.touches e x with
  | true =>
    rw [law.keeps f _ x (apart x touchE)]
    exact (law.reads e (law.act f s) s x
      (fun y touchY => law.keeps f s y (apart y touchY)) touchE).symm
  | false =>
    cases touchF : law.touches f x with
    | false =>
      rw [law.keeps f _ x touchF, law.keeps e s x touchE, law.keeps e _ x touchE,
        law.keeps f s x touchF]
    | true =>
      rw [law.keeps e _ x touchE]
      exact law.reads f (law.act e s) s x
        (fun y touchY => law.keeps e s y (apart.symm y touchY)) touchF

/-- **Moving an exchange forward past exchanges sharing no relatum with it** reaches the same
configuration. -/
theorem run_move {e : E} (B : List E) : ∀ (A : List E), (∀ a, a ∈ A → law.Apart e a) →
    ∀ s x, law.run (A ++ e :: B) s x = law.run (e :: (A ++ B)) s x
  | [], _, _, _ => rfl
  | a :: A, apart, s, x => by
    show law.run (A ++ e :: B) (law.act a s) x = law.run (A ++ B) (law.act a (law.act e s)) x
    rw [run_move B A (fun b mem => apart b (.tail a mem)) (law.act a s) x]
    exact run_agree (A ++ B) (fun y => (act_comm (apart a (.head A)) s y).symm) x

/-- A list of exchanges touching no relatum leaves every relatum as it was. -/
theorem run_idle : ∀ {L : List E}, (∀ x, law.ownCourse x L = []) →
    ∀ s x, law.run L s x = s x
  | [], _, _, _ => rfl
  | e :: L, idle, s, x => by
    have untouched : ∀ y, law.touches e y = false := by
      intro y
      cases touch : law.touches e y with
      | false => rfl
      | true => exact absurd ((ownCourse_true L touch).symm.trans (idle y)) cons_ne_nil
    have rest : ∀ y, law.ownCourse y L = [] := fun y =>
      (ownCourse_false L (untouched y)).symm.trans (idle y)
    show law.run L (law.act e s) x = s x
    rw [run_agree L (fun y => law.keeps e s y (untouched y)) x]
    exact run_idle rest s x

/-! ## Listed relata -/

theorem shares_of_mem {e f : E} {x : X} (touchE : law.touches e x = true)
    (touchF : law.touches f x = true) : ∀ {xs : List X}, x ∈ xs → law.shares xs e f = true
  | y :: xs, mem => by
    show (law.touches e y && law.touches f y || law.shares xs e f) = true
    match mem_cons_split mem with
    | .inl same =>
      rw [← same, touchE, touchF]
      rfl
    | .inr rest =>
      rw [shares_of_mem touchE touchF rest]
      cases (law.touches e y && law.touches f y) <;> rfl

theorem exists_of_shares {e f : E} : ∀ {xs : List X}, law.shares xs e f = true →
    ∃ x, law.touches e x = true ∧ law.touches f x = true
  | [], yes => Bool.noConfusion yes
  | x :: xs, yes => by
    have h : (law.touches e x && law.touches f x || law.shares xs e f) = true := yes
    cases touchE : law.touches e x with
    | false =>
      rw [touchE] at h
      exact exists_of_shares h
    | true =>
      cases touchF : law.touches f x with
      | true => exact ⟨x, touchE, touchF⟩
      | false =>
        rw [touchE, touchF] at h
        exact exists_of_shares h

theorem apart_of_shares {xs : List X} (listed : ∀ x, x ∈ xs) {e f : E}
    (no : law.shares xs e f = false) : law.Apart e f := by
  intro x touchE
  cases touchF : law.touches f x with
  | false => rfl
  | true => exact bool_absurd (shares_of_mem touchE touchF (listed x)) no

theorem untouched_of_shares {xs : List X} (listed : ∀ x, x ∈ xs) {e : E}
    (no : law.shares xs e e = false) (x : X) : law.touches e x = false := by
  cases touch : law.touches e x with
  | false => rfl
  | true => exact bool_absurd (shares_of_mem touch touch (listed x)) no

/-- **Where `e` heads the own course of every relatum it touches in `M`**, and touches one, `M` is
`A ++ e :: B` with every exchange of `A` sharing no relatum with `e`: `e` is first in `M` at every
relatum it touches, and at every other relatum `M` and `A ++ B` have the same own course. -/
theorem split_heads {xs : List X} (listed : ∀ x, x ∈ xs) {e : E} {x₀ : X}
    (touch : law.touches e x₀ = true) {M : List E}
    (headsAt : ∀ x, law.touches e x = true → ∃ m, law.ownCourse x M = e :: m) :
    ∃ A B, M = A ++ e :: B ∧ (∀ a, a ∈ A → law.Apart e a) ∧
      (∀ x, law.touches e x = true → law.ownCourse x M = e :: law.ownCourse x (A ++ B)) ∧
      (∀ x, law.touches e x = false → law.ownCourse x M = law.ownCourse x (A ++ B)) := by
  match split_first (law.shares xs e) M with
  | .inl absent =>
    match headsAt x₀ touch with
    | ⟨m, h⟩ =>
      have empty : law.ownCourse x₀ M = [] :=
        ownCourse_untouched fun f mem => apart_of_shares listed (absent f mem) x₀ touch
      exact absurd (h.symm.trans empty) cons_ne_nil
  | .inr ⟨A, f, B, split, before, found⟩ =>
    have apartA : ∀ a, a ∈ A → law.Apart e a := fun a mem => apart_of_shares listed (before a mem)
    match exists_of_shares found with
    | ⟨x₁, touchE, touchF⟩ =>
      match headsAt x₁ touchE with
      | ⟨m, h⟩ =>
        have h' : f :: law.ownCourse x₁ B = e :: m := by
          rw [split, ownCourse_append, ownCourse_untouched (fun a mem => apartA a mem x₁ touchE),
            ownCourse_true B touchF] at h
          exact h
        have heads : e = f := (cons_heads h').symm
        subst heads
        refine ⟨A, B, split, apartA, fun x touchX => ?_, fun x touchX => ?_⟩
        · rw [split, ownCourse_append, ownCourse_append,
            ownCourse_untouched (fun a mem => apartA a mem x touchX), ownCourse_true B touchX]
          rfl
        · rw [split, ownCourse_append, ownCourse_append, ownCourse_false B touchX]

/-! ## The interleaving carries nothing the relata do not -/

/-- **Equal own courses, equal configurations.** With the relata listed, two lists of exchanges
giving every relatum the same own course reach the same configuration from the same start. -/
theorem run_of_courses {xs : List X} (listed : ∀ x, x ∈ xs) : ∀ (L M : List E),
    (∀ x, law.ownCourse x L = law.ownCourse x M) → ∀ s x, law.run L s x = law.run M s x
  | [], M, same, s, x => (run_idle (fun y => (same y).symm) s x).symm
  | e :: L, M, same, s, x => by
    cases hit : law.shares xs e e with
    | false =>
      have untouched := untouched_of_shares listed hit
      have rest : ∀ y, law.ownCourse y L = law.ownCourse y M := fun y =>
        (ownCourse_false L (untouched y)).symm.trans (same y)
      show law.run L (law.act e s) x = law.run M s x
      rw [run_agree L (fun y => law.keeps e s y (untouched y)) x]
      exact run_of_courses listed L M rest s x
    | true =>
      match exists_of_shares hit with
      | ⟨x₀, touch, _⟩ =>
        match split_heads listed touch (M := M)
          (fun y touchY => ⟨law.ownCourse y L, ((same y).symm.trans (ownCourse_true L touchY))⟩)
        with
        | ⟨A, B, split, apartA, onTouched, onOther⟩ =>
          have rest : ∀ y, law.ownCourse y L = law.ownCourse y (A ++ B) := fun y => by
            cases touchY : law.touches e y with
            | true =>
              have h := (ownCourse_true L touchY).symm.trans ((same y).trans (onTouched y touchY))
              exact cons_tails h
            | false =>
              exact (ownCourse_false L touchY).symm.trans ((same y).trans (onOther y touchY))
          rw [split, run_move B A apartA s x]
          exact run_of_courses listed L (A ++ B) rest (law.act e s) x

/-! ## The exchange process -/

theorem trace_run : ∀ {s t : X → σ} {L : List E}, Trace law.process s L t →
    ∀ x, t x = law.run L s x
  | _, _, [], .nil _, _ => rfl
  | s, _, e :: L, .cons step rest, x => by
    show _ = law.run L (law.act e s) x
    rw [trace_run rest x]
    exact run_agree L step x

theorem run_trace : ∀ (s : X → σ) (L : List E), Trace law.process s L (law.run L s)
  | s, [] => .nil s
  | s, e :: L => .cons (fun _ => rfl) (run_trace (law.act e s) L)

/-- **The traces of the exchange process carry nothing the relata's own courses do not**: two
traces from one configuration whose lists give every relatum the same own course end at the same
configuration. -/
theorem trace_of_courses {xs : List X} (listed : ∀ x, x ∈ xs) {s t t' : X → σ} {L M : List E}
    (first : Trace law.process s L t) (second : Trace law.process s M t')
    (same : ∀ x, law.ownCourse x L = law.ownCourse x M) : ∀ x, t x = t' x := fun x =>
  (trace_run first x).trans ((run_of_courses listed L M same s x).trans (trace_run second x).symm)

/-- **Two traces interleaving the same courses end at the same configuration**: which interleaving is
taken changes nothing the configurations read. -/
theorem trace_of_interleavings {xs : List X} (listed : ∀ x, x ∈ xs) {c : X → List E}
    {s t t' : X → σ} {L M : List E} (first : Trace law.process s L t)
    (second : Trace law.process s M t') (inL : law.Interleaves c L) (inM : law.Interleaves c M) :
    ∀ x, t x = t' x :=
  trace_of_courses listed first second fun y => (inL y).trans (inM y).symm

/-! ## Two exchanges sharing no relatum -/

theorem swap_courses {e f : E} (apart : law.Apart e f) (x : X) :
    law.ownCourse x [e, f] = law.ownCourse x [f, e] := by
  cases touchE : law.touches e x with
  | true =>
    rw [ownCourse_true _ touchE, ownCourse_false _ (apart x touchE),
      ownCourse_false _ (apart x touchE), ownCourse_true _ touchE]
  | false =>
    rw [ownCourse_false _ touchE]
    cases touchF : law.touches f x with
    | true => rw [ownCourse_true _ touchF, ownCourse_true _ touchF, ownCourse_false _ touchE]
    | false => rw [ownCourse_false _ touchF, ownCourse_false _ touchF, ownCourse_false _ touchE]

/-- **Two exchanges sharing no relatum, taken in either order, end at the same configuration.** -/
theorem trace_swap {xs : List X} (listed : ∀ x, x ∈ xs) {e f : E} (apart : law.Apart e f)
    {s t t' : X → σ} (first : Trace law.process s [e, f] t) (second : Trace law.process s [f, e] t') :
    ∀ x, t x = t' x :=
  trace_of_courses listed first second (swap_courses apart)

/-! ## Exactly where the own courses fix the interleaving -/

theorem eq_of_courses (connected : law.Connected) : ∀ (L M : List E),
    (∀ x, law.ownCourse x L = law.ownCourse x M) → L = M
  | [], [], _ => rfl
  | [], f :: _, same => match connected.1 f with
    | ⟨x, touch⟩ => absurd ((same x).trans (ownCourse_true _ touch)).symm cons_ne_nil
  | e :: _, [], same => match connected.1 e with
    | ⟨x, touch⟩ => absurd ((ownCourse_true _ touch).symm.trans (same x)) cons_ne_nil
  | e :: L, f :: M, same => by
    have heads : e = f := match connected.2 e f with
      | .inl same' => same'
      | .inr ⟨x, touchE, touchF⟩ => by
        have h := same x
        rw [ownCourse_true L touchE, ownCourse_true M touchF] at h
        exact cons_heads h
    subst heads
    have rest : ∀ x, law.ownCourse x L = law.ownCourse x M := fun x => by
      have h := same x
      cases touch : law.touches e x with
      | true =>
        rw [ownCourse_true L touch, ownCourse_true M touch] at h
        exact cons_tails h
      | false =>
        rw [ownCourse_false L touch, ownCourse_false M touch] at h
        exact h
    rw [eq_of_courses connected L M rest]

/-- **The own courses fix the interleaving exactly where every exchange touches a relatum and every
two exchanges are the same or share one**, with the relata listed. -/
theorem unique_iff {xs : List X} (listed : ∀ x, x ∈ xs) :
    (∀ L M : List E, (∀ x, law.ownCourse x L = law.ownCourse x M) → L = M) ↔ law.Connected := by
  constructor
  · intro unique
    constructor
    · intro e
      cases hit : law.shares xs e e with
      | true => match exists_of_shares hit with
        | ⟨x, touch, _⟩ => exact ⟨x, touch⟩
      | false =>
        exact absurd (unique [e] [] fun y => ownCourse_false []
          (untouched_of_shares listed hit y)) cons_ne_nil
    · intro e f
      cases both : law.shares xs e f with
      | true => exact .inr (exists_of_shares both)
      | false => exact .inl (cons_heads (unique [e, f] [f, e]
          (swap_courses (apart_of_shares listed both))))
  · exact eq_of_courses

/-- **The same, read on the traces of the exchange process** from any one configuration. -/
theorem traced_unique_iff {xs : List X} (listed : ∀ x, x ∈ xs) (s : X → σ) :
    (∀ (L M : List E) (t t' : X → σ), Trace law.process s L t → Trace law.process s M t' →
      (∀ x, law.ownCourse x L = law.ownCourse x M) → L = M) ↔ law.Connected := by
  refine Iff.trans ⟨fun unique L M same => ?_, fun unique L M _ _ _ _ same => unique L M same⟩
    (unique_iff listed)
  exact unique L M _ _ (run_trace s L) (run_trace s M) same

/-! ## Building the index -/

section Schedule

variable [DecidableEq E]

variable (law) in
/-- Whether `e` heads the course of every listed relatum it touches. -/
def ready (c : X → List E) : List X → E → Bool
  | [], _ => true
  | x :: xs, e => (!law.touches e x || heads (c x) e) && ready c xs e
where
  /-- Whether `e` heads a course. -/
  heads : List E → E → Bool
    | [], _ => false
    | a :: _, e => decide (a = e)

variable (law) in
/-- `e` dropped from the courses of the relata it touches. -/
def pop (e : E) (c : X → List E) : X → List E := fun x =>
  match law.touches e x with
  | true => (c x).tail
  | false => c x

variable (law) in
/-- A ready exchange heading the course of a listed relatum it touches, the first such in the
listing, if any. -/
def pick (c : X → List E) (all : List X) : List X → Option E
  | [] => none
  | x :: xs => match c x with
    | [] => pick c all xs
    | e :: _ => match law.touches e x && law.ready c all e with
      | true => some e
      | false => pick c all xs

/-- Whether every listed course is empty. -/
def done (c : X → List E) : List X → Bool
  | [] => true
  | x :: xs => match c x with
    | [] => done c xs
    | _ :: _ => false

/-- The total length of the listed courses. -/
def total (c : X → List E) : List X → Nat
  | [] => 0
  | x :: xs => (c x).length + total c xs

variable (law) in
/-- **The scheduler**: while some course remains, take a ready exchange and drop it. -/
def schedule (xs : List X) : Nat → (X → List E) → Option (List E)
  | 0, c => match done c xs with
    | true => some []
    | false => none
  | n + 1, c => match done c xs with
    | true => some []
    | false => match law.pick c xs xs with
      | none => none
      | some e => (schedule xs n (law.pop e c)).map (e :: ·)

theorem heads_eq : ∀ {l : List E} {e : E}, ready.heads l e = true → ∃ m, l = e :: m
  | [], _, yes => Bool.noConfusion yes
  | _ :: m, _, yes => ⟨m, congrArg (· :: m) (of_decide_eq_true yes)⟩

theorem heads_cons (e : E) (m : List E) : ready.heads (e :: m) e = true :=
  decide_eq_true rfl

theorem ready_heads {c : X → List E} {e : E} : ∀ {xs : List X}, law.ready c xs e = true →
    ∀ x, x ∈ xs → law.touches e x = true → ready.heads (c x) e = true
  | y :: xs, yes, x, mem, touch => by
    have h : ((!law.touches e y || ready.heads (c y) e) && law.ready c xs e) = true := yes
    cases first : (!law.touches e y || ready.heads (c y) e) with
    | false => rw [first] at h; exact Bool.noConfusion h
    | true =>
      rw [first] at h
      match mem_cons_split mem with
      | .inl same =>
        rw [same] at touch ⊢
        rw [touch] at first
        exact first
      | .inr rest => exact ready_heads h x rest touch

theorem ready_of_heads {c : X → List E} {e : E} : ∀ {xs : List X},
    (∀ x, x ∈ xs → law.touches e x = true → ready.heads (c x) e = true) →
      law.ready c xs e = true
  | [], _ => rfl
  | y :: xs, all => by
    show ((!law.touches e y || ready.heads (c y) e) && law.ready c xs e) = true
    rw [ready_of_heads (fun x mem => all x (.tail y mem))]
    cases touch : law.touches e y with
    | false => rfl
    | true => rw [all y (.head xs) touch]; rfl

omit [DecidableEq E] in
theorem pop_true {e : E} {c : X → List E} {x : X} (touch : law.touches e x = true) :
    law.pop e c x = (c x).tail := by
  show (match law.touches e x with
    | true => (c x).tail
    | false => c x) = _
  rw [touch]

omit [DecidableEq E] in
theorem pop_false {e : E} {c : X → List E} {x : X} (touch : law.touches e x = false) :
    law.pop e c x = c x := by
  show (match law.touches e x with
    | true => (c x).tail
    | false => c x) = _
  rw [touch]

omit [DecidableEq E] in
theorem done_nil {c : X → List E} : ∀ {xs : List X}, done c xs = true → ∀ x, x ∈ xs → c x = []
  | y :: xs, yes, x, mem => by
    have h : (match c y with | [] => done c xs | _ :: _ => false) = true := yes
    match hy : c y with
    | [] =>
      rw [hy] at h
      match mem_cons_split mem with
      | .inl same => rw [same]; exact hy
      | .inr rest => exact done_nil h x rest
    | _ :: _ =>
      rw [hy] at h
      exact Bool.noConfusion h

omit [DecidableEq E] in
theorem not_done {c : X → List E} : ∀ {xs : List X}, done c xs = false →
    ∃ x e m, x ∈ xs ∧ c x = e :: m
  | [], no => Bool.noConfusion no
  | y :: xs, no => by
    have h : (match c y with | [] => done c xs | _ :: _ => false) = false := no
    match hy : c y with
    | [] =>
      rw [hy] at h
      match not_done h with
      | ⟨x, e, m, mem, hx⟩ => exact ⟨x, e, m, .tail y mem, hx⟩
    | a :: m => exact ⟨y, a, m, .head xs, hy⟩

theorem pick_cons (c : X → List E) (all : List X) (y : X) (xs : List X) :
    law.pick c all (y :: xs) = (match c y with
      | [] => law.pick c all xs
      | e :: _ => match law.touches e y && law.ready c all e with
        | true => some e
        | false => law.pick c all xs) := rfl

theorem pick_nil_head {c : X → List E} {all : List X} {y : X} (xs : List X) (hy : c y = []) :
    law.pick c all (y :: xs) = law.pick c all xs := by
  rw [pick_cons, hy]

theorem pick_cons_head {c : X → List E} {all : List X} {y : X} (xs : List X) {a : E} {m : List E}
    (hy : c y = a :: m) :
    law.pick c all (y :: xs) = (match law.touches a y && law.ready c all a with
      | true => some a
      | false => law.pick c all xs) := by
  rw [pick_cons, hy]

theorem pick_spec {c : X → List E} {all : List X} {e : E} : ∀ {xs : List X},
    law.pick c all xs = some e →
      ∃ x m, x ∈ xs ∧ c x = e :: m ∧ law.touches e x = true ∧ law.ready c all e = true
  | [], no => nomatch no
  | y :: xs, found => by
    match hy : c y with
    | [] =>
      rw [pick_nil_head xs hy] at found
      match pick_spec found with
      | ⟨x, m, mem, hx, touch, isReady⟩ => exact ⟨x, m, .tail y mem, hx, touch, isReady⟩
    | a :: m =>
      rw [pick_cons_head xs hy] at found
      cases test : (law.touches a y && law.ready c all a) with
      | true =>
        rw [test] at found
        change some a = some e at found
        have same : a = e := Option.some.inj found
        subst same
        cases touch : law.touches a y with
        | false => rw [touch] at test; exact Bool.noConfusion test
        | true =>
          rw [touch] at test
          exact ⟨y, m, .head xs, hy, touch, test⟩
      | false =>
        rw [test] at found
        change law.pick c all xs = some e at found
        match pick_spec found with
        | ⟨x, m', mem, hx, touch, isReady⟩ => exact ⟨x, m', .tail y mem, hx, touch, isReady⟩

theorem pick_some {c : X → List E} {all : List X} {e : E} {x : X} {m : List E}
    (touch : law.touches e x = true) (isReady : law.ready c all e = true) (hx : c x = e :: m) :
    ∀ {xs : List X}, x ∈ xs → ∃ e', law.pick c all xs = some e'
  | y :: xs, mem => by
    match hy : c y with
    | [] =>
      rw [pick_nil_head xs hy]
      match mem_cons_split mem with
      | .inl same => rw [same] at hx; exact nomatch (hy.symm.trans hx)
      | .inr rest => exact pick_some touch isReady hx rest
    | a :: m' =>
      rw [pick_cons_head xs hy]
      cases test : (law.touches a y && law.ready c all a) with
      | true => exact ⟨a, rfl⟩
      | false =>
        change ∃ e', law.pick c all xs = some e'
        match mem_cons_split mem with
        | .inl same =>
          rw [same] at hx touch
          have heads : a = e := cons_heads (hy.symm.trans hx)
          rw [heads, touch, isReady] at test
          exact Bool.noConfusion test
        | .inr rest => exact pick_some touch isReady hx rest

theorem schedule_zero (xs : List X) (c : X → List E) :
    law.schedule xs 0 c = (match done c xs with
      | true => some []
      | false => none) := rfl

theorem schedule_succ (xs : List X) (n : Nat) (c : X → List E) :
    law.schedule xs (n + 1) c = (match done c xs with
      | true => some []
      | false => match law.pick c xs xs with
        | none => none
        | some e => (law.schedule xs n (law.pop e c)).map (e :: ·)) := rfl

/-- **What the scheduler returns interleaves the courses**, the relata listed. -/
theorem schedule_interleaves {xs : List X} (listed : ∀ x, x ∈ xs) : ∀ (n : Nat) (c : X → List E)
    (L : List E), law.schedule xs n c = some L → law.Interleaves c L
  | 0, c, L, result => by
    rw [schedule_zero] at result
    cases fin : done c xs with
    | true =>
      rw [fin] at result
      change some [] = some L at result
      have same : [] = L := Option.some.inj result
      subst same
      exact fun x => (done_nil fin x (listed x)).symm
    | false =>
      rw [fin] at result
      exact nomatch result
  | n + 1, c, L, result => by
    rw [schedule_succ] at result
    cases fin : done c xs with
    | true =>
      rw [fin] at result
      change some [] = some L at result
      have same : [] = L := Option.some.inj result
      subst same
      exact fun x => (done_nil fin x (listed x)).symm
    | false =>
      rw [fin] at result
      change (match law.pick c xs xs with
        | none => none
        | some e => (law.schedule xs n (law.pop e c)).map (e :: ·)) = some L at result
      cases found : law.pick c xs xs with
      | none =>
        rw [found] at result
        exact nomatch result
      | some e =>
        rw [found] at result
        change (law.schedule xs n (law.pop e c)).map (e :: ·) = some L at result
        match hrest : law.schedule xs n (law.pop e c) with
        | none =>
          rw [hrest] at result
          exact nomatch result
        | some L' =>
          rw [hrest] at result
          change some (e :: L') = some L at result
          have same : e :: L' = L := Option.some.inj result
          subst same
          have rest := schedule_interleaves listed n (law.pop e c) L' hrest
          match pick_spec found with
          | ⟨_, _, _, _, _, isReady⟩ =>
            intro x
            cases touch : law.touches e x with
            | true =>
              rw [ownCourse_true L' touch, rest x, pop_true touch]
              match heads_eq (ready_heads isReady x (listed x) touch) with
              | ⟨m, hx⟩ => rw [hx]; rfl
            | false =>
              rw [ownCourse_false L' touch, rest x, pop_false touch]

/-- **Where some list interleaves the courses, every ready exchange can be taken first**: the
courses with it dropped are interleaved by the list with it moved out. -/
theorem pop_interleaves {xs : List X} (listed : ∀ x, x ∈ xs) {c : X → List E} {L : List E}
    (inter : law.Interleaves c L) {e : E} {x₀ : X} (touch : law.touches e x₀ = true)
    (isReady : law.ready c xs e = true) :
    ∃ A B, L = A ++ e :: B ∧ law.Interleaves (law.pop e c) (A ++ B) := by
  match split_heads listed touch (M := L) (fun x touchX =>
      match heads_eq (ready_heads isReady x (listed x) touchX) with
      | ⟨m, hx⟩ => ⟨m, (inter x).trans hx⟩) with
  | ⟨A, B, split, _, onTouched, onOther⟩ =>
    refine ⟨A, B, split, fun x => ?_⟩
    cases touchX : law.touches e x with
    | true =>
      rw [pop_true touchX, ← inter x, onTouched x touchX]
      rfl
    | false =>
      rw [pop_false touchX, ← inter x, onOther x touchX]

omit [DecidableEq E] in
theorem total_le {c c' : X → List E} (le : ∀ x, (c x).length ≤ (c' x).length) :
    ∀ xs : List X, total c xs ≤ total c' xs
  | [] => Nat.le_refl 0
  | x :: xs => Nat.add_le_add (le x) (total_le le xs)

omit [DecidableEq E] in
theorem total_lt {c c' : X → List E} (le : ∀ x, (c x).length ≤ (c' x).length) {x₀ : X}
    (lt : (c x₀).length + 1 ≤ (c' x₀).length) : ∀ {xs : List X}, x₀ ∈ xs →
      total c xs + 1 ≤ total c' xs
  | y :: xs, mem => by
    show (c y).length + total c xs + 1 ≤ (c' y).length + total c' xs
    match mem_cons_split mem with
    | .inl same =>
      rw [Nat.add_right_comm]
      rw [same] at lt
      exact Nat.add_le_add lt (total_le le xs)
    | .inr rest =>
      rw [Nat.add_assoc]
      exact Nat.add_le_add (le y) (total_lt le lt rest)

omit [DecidableEq E] in
theorem total_pos {c : X → List E} {x : X} {e : E} {m : List E} (hx : c x = e :: m) :
    ∀ {xs : List X}, x ∈ xs → 1 ≤ total c xs
  | y :: xs, mem => by
    show 1 ≤ (c y).length + total c xs
    match mem_cons_split mem with
    | .inl same =>
      rw [← same, hx]
      exact Nat.le_trans (Nat.succ_le_succ (Nat.zero_le m.length)) (Nat.le_add_right _ _)
    | .inr rest => exact Nat.le_trans (total_pos hx rest) (Nat.le_add_left _ _)

omit [DecidableEq E] in
theorem total_pop {xs : List X} {e : E} {c : X → List E} {x₀ : X} {m₀ : List E}
    (touch : law.touches e x₀ = true) (hx : c x₀ = e :: m₀) (mem : x₀ ∈ xs) :
    total (law.pop e c) xs + 1 ≤ total c xs := by
  refine total_lt (fun x => ?_) ?_ mem
  · cases touchX : law.touches e x with
    | true => rw [pop_true touchX]; exact length_tail_le (c x)
    | false => rw [pop_false touchX]; exact Nat.le_refl _
  · rw [pop_true touch, hx]
    exact Nat.le_refl _

/-- **Where some list interleaves the courses, the scheduler completes** with enough steps. -/
theorem schedule_some {xs : List X} (listed : ∀ x, x ∈ xs) : ∀ (n : Nat) (c : X → List E)
    (L : List E), law.Interleaves c L → total c xs ≤ n → ∃ L', law.schedule xs n c = some L'
  | n, c, L, inter, bound => by
    cases fin : done c xs with
    | true =>
      match n with
      | 0 => exact ⟨[], by rw [schedule_zero, fin]⟩
      | _ + 1 => exact ⟨[], by rw [schedule_succ, fin]⟩
    | false =>
      match not_done fin with
      | ⟨x, e, m, mem, hx⟩ =>
        match n with
        | 0 => exact absurd (Nat.le_trans (total_pos hx mem) bound) (Nat.not_succ_le_zero 0)
        | n + 1 =>
          -- an exchange ready in `c`: the first exchange of `L` touching a relatum
          have ready_exists : ∃ g x₁ m₁, law.touches g x₁ = true ∧ c x₁ = g :: m₁ ∧
              law.ready c xs g = true := by
            match split_first (fun a => law.shares xs a a) L with
            | .inl absent =>
              have empty : law.ownCourse x L = [] :=
                ownCourse_untouched fun a mem' => untouched_of_shares listed (absent a mem') x
              have h := (inter x).symm.trans empty
              rw [hx] at h
              exact absurd h cons_ne_nil
            | .inr ⟨A, g, B, split, before, found⟩ =>
              have untouchedA : ∀ a, a ∈ A → ∀ y, law.touches a y = false := fun a mem' y =>
                untouched_of_shares listed (before a mem') y
              have headsG : ∀ y, law.touches g y = true → c y = g :: law.ownCourse y B := by
                intro y touchY
                rw [← inter y, split, ownCourse_append,
                  ownCourse_untouched (fun a mem' => untouchedA a mem' y), ownCourse_true B touchY]
                rfl
              match exists_of_shares found with
              | ⟨x₁, touch₁, _⟩ =>
                exact ⟨g, x₁, law.ownCourse x₁ B, touch₁, headsG x₁ touch₁,
                  ready_of_heads fun y _ touchY => by
                    rw [headsG y touchY]
                    exact heads_cons g _⟩
          match ready_exists with
          | ⟨g, x₁, m₁, touch₁, hx₁, readyG⟩ =>
            match pick_some touch₁ readyG hx₁ (listed x₁) with
            | ⟨e', found⟩ =>
              match pick_spec found with
              | ⟨x', m', mem', hx', touch', ready'⟩ =>
                match pop_interleaves listed inter touch' ready' with
                | ⟨A, B, _, inter'⟩ =>
                  have bound' : total (law.pop e' c) xs ≤ n :=
                    Nat.le_of_succ_le_succ (Nat.le_trans (total_pop touch' hx' mem') bound)
                  match schedule_some listed n (law.pop e' c) (A ++ B) inter' bound' with
                  | ⟨L', result⟩ =>
                    exact ⟨e' :: L', by
                      rw [schedule_succ, fin]
                      change (match law.pick c xs xs with
                        | none => none
                        | some e => (law.schedule xs n (law.pop e c)).map (e :: ·)) = _
                      rw [found]
                      change (law.schedule xs n (law.pop e' c)).map (e' :: ·) = _
                      rw [result]
                      rfl⟩

/-- **An interleaving of given courses exists exactly where the scheduler completes**, run with as
many steps as the courses have exchanges in all; the relata listed and exchanges told apart. -/
theorem schedule_iff {xs : List X} (listed : ∀ x, x ∈ xs) (c : X → List E) :
    (∃ L, law.Interleaves c L) ↔ ∃ L, law.schedule xs (total c xs) c = some L :=
  ⟨fun ⟨L, inter⟩ => schedule_some listed _ c L inter (Nat.le_refl _),
   fun ⟨L, result⟩ => ⟨L, schedule_interleaves listed _ c L result⟩⟩

/-- **A trace of the exchange process taking every relatum through its given course exists exactly
where the scheduler completes**, from any configuration. -/
theorem traced_iff {xs : List X} (listed : ∀ x, x ∈ xs) (c : X → List E) (s : X → σ) :
    (∃ L t, law.Interleaves c L ∧ Trace law.process s L t) ↔
      ∃ L, law.schedule xs (total c xs) c = some L :=
  Iff.trans ⟨fun ⟨L, _, inter, _⟩ => ⟨L, inter⟩, fun ⟨L, inter⟩ => ⟨L, _, inter, run_trace s L⟩⟩
    (schedule_iff listed c)

end Schedule

end LocalLaw

end Interleavings

end Becoming
