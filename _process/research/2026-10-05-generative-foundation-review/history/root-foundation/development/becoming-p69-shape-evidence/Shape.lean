/-!
# What the shape `step : S → A → S → Prop` commits to (scratch evidence for P69, not landed)

Prelude only, no import, mirroring `Generative.Process` and `Generative.Trace`. Checks:
1. labels go into configurations with nothing lost;
2. an added variable with no law relating it adds nothing; with a law it does;
3. the label of a joint change is a relation between the parts' configurations;
4. a history is a run of the process it follows, and a law of every step of the history is
   a law of every step of that process;
5. configurations that can become alike cannot be told apart by any word of change;
6. a law and a history are not the same: law to histories loses dead ends, histories to their
   law gains spliced histories;
7. memory closes the gap: where configurations keep their past, histories that meet share it;
8. a way bound by balance fixes the standing after, the standings do not fix the way, and a
   free label fixes nothing;
9. passing fixes standing only from a beginning;
10. still at one grain, moving at a finer one.
-/

namespace Shape

universe u v w

structure Process (S : Type u) (A : Type v) where
  step : S → A → S → Prop

inductive Trace {S : Type u} {A : Type v} (P : Process S A) : S → List A → S → Prop where
  | nil (s : S) : Trace P s [] s
  | cons {s m t : S} {a : A} {as : List A} :
      P.step s a m → Trace P m as t → Trace P s (a :: as) t

def Reach {S : Type u} {A : Type v} (P : Process S A) (s t : S) : Prop := ∃ as, Trace P s as t

variable {S : Type u} {A : Type v}

/-! ## 1. Labels go into configurations -/

/-- Unlabelled change, with the configurations visited. -/
inductive Path {X : Type u} (R : X → X → Prop) : X → List X → X → Prop where
  | nil (x : X) : Path R x [] x
  | cons {x m y : X} {l : List X} : R x m → Path R m l y → Path R x (m :: l) y

/-- Each configuration keeps the way it was entered; change is then a plain relation. -/
def unlabel (P : Process S A) (x y : S × Option A) : Prop :=
  ∃ a, y.2 = some a ∧ P.step x.1 a y.1

theorem trace_to_path {P : Process S A} {s t : S} {w : List A} (h : Trace P s w t) :
    ∀ o : Option A, ∃ l y, Path (unlabel P) (s, o) l y ∧ y.1 = t ∧ l.map Prod.snd = w.map some := by
  induction h with
  | nil s => exact fun o => ⟨[], (s, o), .nil _, rfl, rfl⟩
  | @cons s m t a as hs _ ih =>
    intro o
    match ih (some a) with
    | ⟨l, y, p, hy, hl⟩ =>
      exact ⟨(m, some a) :: l, y, .cons ⟨a, rfl, hs⟩ p, hy, congrArg (some a :: ·) hl⟩

theorem path_to_trace {P : Process S A} {x y : S × Option A} {l : List (S × Option A)}
    (p : Path (unlabel P) x l y) : ∀ w : List A, l.map Prod.snd = w.map some → Trace P x.1 w y.1 := by
  induction p with
  | nil x =>
    intro w hw
    cases w with
    | nil => exact .nil _
    | cons _ _ => cases hw
  | @cons x m y l r _ ih =>
    intro w hw
    cases w with
    | nil => cases hw
    | cons a as =>
      injection hw with h1 h2
      match r with
      | ⟨b, hb, hs⟩ =>
        have same : b = a := Option.some.inj (hb.symm.trans h1)
        exact .cons (same ▸ hs) (ih as h2)

/-- Nothing is lost: the words of change are exactly the ways recorded along unlabelled paths. -/
theorem unlabel_exact (P : Process S A) (s t : S) (w : List A) (o : Option A) :
    Trace P s w t ↔ ∃ l y, Path (unlabel P) (s, o) l y ∧ y.1 = t ∧ l.map Prod.snd = w.map some :=
  ⟨fun h => trace_to_path h o, fun ⟨_, _, p, hy, hl⟩ => hy ▸ path_to_trace p w hl⟩

/-- Conversely, plain change is labelled change with one label. -/
def labelled {X : Type u} (R : X → X → Prop) : Process X Unit := ⟨fun x _ y => R x y⟩

theorem labelled_step {X : Type u} (R : X → X → Prop) (x y : X) :
    (labelled R).step x () y ↔ R x y := Iff.rfl

/-! ## 2. An added variable: idle without a law, content with one -/

variable {X : Type w}

/-- Add a variable to the label and relate it to nothing. -/
def idle (P : Process S A) (X : Type w) : Process S (A × X) := ⟨fun s ax t => P.step s ax.1 t⟩

theorem idle_trace {P : Process S A} {s t : S} {w : List (A × X)} (h : Trace (idle P X) s w t) :
    Trace P s (w.map Prod.fst) t := by
  induction h with
  | nil s => exact .nil s
  | cons hs _ ih => exact .cons hs ih

theorem trace_idle {P : Process S A} (x : X) {s t : S} {w : List A} (h : Trace P s w t) :
    Trace (idle P X) s (w.map (fun a => (a, x))) t := by
  induction h with
  | nil s => exact .nil s
  | cons hs _ ih => exact .cons hs ih

/-- An idle variable changes nothing about what can be reached. -/
theorem idle_reach (P : Process S A) (x : X) (s t : S) : Reach (idle P X) s t ↔ Reach P s t :=
  ⟨fun ⟨_, h⟩ => ⟨_, idle_trace h⟩, fun ⟨_, h⟩ => ⟨_, trace_idle x h⟩⟩

/-- Add a variable to the configuration, with a law `L` relating it to the change. -/
def withLaw (P : Process S A) (L : X → A → X → Prop) : Process (S × X) A :=
  ⟨fun x a y => P.step x.1 a y.1 ∧ L x.2 a y.2⟩

/-- With a law, the variable has content: change goes on only while the relation holds. -/
def flip : Process Bool Unit := ⟨fun s _ t => t = !s⟩

theorem flip_reaches : Reach flip false true := ⟨[()], .cons rfl (.nil _)⟩

theorem law_blocks {w : List Unit} {y : Bool × Bool}
    (h : Trace (withLaw flip (fun r _ _ => r = true)) (false, false) w y) : y = (false, false) := by
  cases h with
  | nil => rfl
  | cons hs _ => exact nomatch hs.2

theorem law_has_content :
    Reach flip false true ∧ ¬ Reach (withLaw flip (fun r _ _ => r = true)) (false, false) (true, false) :=
  ⟨flip_reaches, fun ⟨_, h⟩ => nomatch law_blocks h⟩

/-! ## 3. The label of a joint change is a relation between the parts -/

variable {T : Type u}

/-- The core's synchronized product: both parts change in one step under one label. -/
def product (P : Process S A) (Q : Process T A) : Process (S × T) A :=
  ⟨fun x a y => P.step x.1 a y.1 ∧ Q.step x.2 a y.2⟩

/-- A joint change is exactly two unlabelled changes whose ways are related: the same. -/
theorem joint_iff_related (P : Process S A) (Q : Process T A) (s t : S) (q r : T)
    (o o' : Option A) :
    (∃ a, (product P Q).step (s, q) a (t, r)) ↔
      ∃ e e', unlabel P (s, o) (t, e) ∧ unlabel Q (q, o') (r, e') ∧ e = e' := by
  constructor
  · intro ⟨a, hp, hq⟩
    exact ⟨some a, some a, ⟨a, rfl, hp⟩, ⟨a, rfl, hq⟩, rfl⟩
  · intro ⟨e, e', ⟨a, ha, hp⟩, ⟨b, hb, hq⟩, he⟩
    have same : a = b := Option.some.inj (ha.symm.trans (he.trans hb))
    exact ⟨a, hp, same ▸ hq⟩

/-- Forget the label first and the parts only share the clock. -/
def forget (P : Process S A) : Process S Unit := ⟨fun s _ t => ∃ a, P.step s a t⟩

inductive Pos | o | x | y
inductive Way | a | b

inductive Forks : Pos → Way → Pos → Prop
  | left : Forks .o .a .x
  | right : Forks .o .b .y

def fork : Process Pos Way := ⟨Forks⟩

/-- Two parts that fork the same way: the label keeps their ways together; forgetting it
lets one take `a` while the other takes `b`. -/
theorem label_couples :
    (¬ ∃ w, (product fork fork).step (.o, .o) w (.x, .y)) ∧
      (product (forget fork) (forget fork)).step (.o, .o) () (.x, .y) :=
  ⟨(fun ⟨w, h1, h2⟩ => match w, h1, h2 with
    | .a, _, h2 => nomatch h2
    | .b, h1, _ => nomatch h1),
   ⟨⟨.a, .left⟩, ⟨.b, .right⟩⟩⟩

/-! ## 4. A history and its law -/

/-- The process a history follows: exactly its own steps. -/
def follows (h : Nat → S) (f : Nat → A) : Process S A :=
  ⟨fun s a t => ∃ n, h n = s ∧ f n = a ∧ h (n + 1) = t⟩

structure Run (P : Process S A) where
  state : Nat → S
  act : Nat → A
  step : ∀ n, P.step (state n) (act n) (state (n + 1))

def historyRun (h : Nat → S) (f : Nat → A) : Run (follows h f) :=
  ⟨h, f, fun n => ⟨n, rfl, rfl, rfl⟩⟩

/-- A law holds at every step of a history exactly when it holds of every step of the process
the history follows. -/
theorem law_iff_every_step (h : Nat → S) (f : Nat → A) (L : S → A → S → Prop) :
    (∀ n, L (h n) (f n) (h (n + 1))) ↔ ∀ s a t, (follows h f).step s a t → L s a t := by
  constructor
  · intro all s a t ⟨n, hs, ha, ht⟩
    exact hs ▸ ha ▸ ht ▸ all n
  · intro all n
    exact all _ _ _ ⟨n, rfl, rfl, rfl⟩

/-- Every run's history follows the process, so a process is the family of histories it admits. -/
theorem run_follows {P : Process S A} (r : Run P) (s : S) (a : A) (t : S) :
    (follows r.state r.act).step s a t → P.step s a t := by
  intro ⟨n, hs, ha, ht⟩
  exact hs ▸ ha ▸ ht ▸ r.step n

/-! ## 5. A configuration is what it can become -/

/-- What a configuration can become: the curried step. -/
def becomings (P : Process S A) (s : S) : A → S → Prop := P.step s

/-- Configurations related so that each can become whatever the other can, alike again. -/
structure Bisim (P : Process S A) (B : S → S → Prop) : Prop where
  forth : ∀ s s' a t, B s s' → P.step s a t → ∃ t', P.step s' a t' ∧ B t t'
  back : ∀ s s' a t', B s s' → P.step s' a t' → ∃ t, P.step s a t ∧ B t t'

theorem Bisim.trace {P : Process S A} {B : S → S → Prop} (hB : Bisim P B) {s t : S} {w : List A}
    (h : Trace P s w t) : ∀ s', B s s' → ∃ t', Trace P s' w t' ∧ B t t' := by
  induction h with
  | nil s => exact fun s' hs => ⟨s', .nil _, hs⟩
  | @cons s m t a as hs _ ih =>
    intro s' hss
    match hB.forth s s' a m hss hs with
    | ⟨m', hm', hmm⟩ =>
      match ih m' hmm with
      | ⟨t', ht', htt⟩ => exact ⟨t', .cons hm' ht', htt⟩

/-- The converse relation of a bisimulation is one. -/
theorem Bisim.symm {P : Process S A} {B : S → S → Prop} (hB : Bisim P B) :
    Bisim P (fun s s' => B s' s) :=
  ⟨fun s s' a t h st => match hB.back s' s a t h st with | ⟨t', h1, h2⟩ => ⟨t', h1, h2⟩,
   fun s s' a t' h st => match hB.forth s' s a t' h st with | ⟨t, h1, h2⟩ => ⟨t, h1, h2⟩⟩

/-- No word of change tells bisimilar configurations apart. -/
theorem Bisim.same_words {P : Process S A} {B : S → S → Prop} (hB : Bisim P B) {s s' : S}
    (hs : B s s') (w : List A) : (∃ t, Trace P s w t) ↔ ∃ t', Trace P s' w t' :=
  ⟨fun ⟨_, h⟩ => match hB.trace h s' hs with | ⟨t', h', _⟩ => ⟨t', h'⟩,
   fun ⟨_, h⟩ => match hB.symm.trace h s hs with | ⟨t, h', _⟩ => ⟨t, h'⟩⟩

/-! ## 6. A law and a history are not the same

`law_iff_every_step` with the law taken to be `P.step` itself says: a history is a run of `P`
exactly when every step it follows is a step of `P`. That is a correspondence, with two gaps. -/

/-- Law to histories loses: a step into a configuration with no continuation lies on no run. -/
def stop : Process Bool Unit := ⟨fun s _ t => s = false ∧ t = true⟩

theorem dead_end :
    stop.step false () true ∧ ¬ ∃ r : Run stop, ∃ n, r.state n = false ∧ r.state (n + 1) = true :=
  ⟨⟨rfl, rfl⟩, fun ⟨r, n, _, h⟩ => absurd (h.symm.trans (r.step (n + 1)).1) (by decide)⟩

/-- Histories to law gains: two histories meeting at a configuration. -/
def h1 : Nat → Nat
  | 0 => 0
  | 1 => 1
  | _ + 2 => 2

def h2 : Nat → Nat
  | 0 => 3
  | 1 => 1
  | _ + 2 => 4

/-- The law the two histories follow. -/
def both : Process Nat Unit :=
  ⟨fun s a t => (follows h1 (fun _ => ())).step s a t ∨ (follows h2 (fun _ => ())).step s a t⟩

/-- Begin as the first, continue as the second. -/
def spliced : Nat → Nat
  | 0 => 0
  | 1 => 1
  | _ + 2 => 4

theorem h1_ne (m : Nat) : h1 m ≠ 4 := match m with
  | 0 => by decide
  | 1 => by decide
  | _ + 2 => fun e => absurd (show (2 : Nat) = 4 from e) (by decide)

theorem h2_ne (m : Nat) : h2 m ≠ 0 := match m with
  | 0 => by decide
  | 1 => by decide
  | _ + 2 => fun e => absurd (show (4 : Nat) = 0 from e) (by decide)

/-- The spliced history is admitted by the law both histories follow, and is neither of them
from any starting point. -/
theorem splice_new :
    (∀ n, both.step (spliced n) () (spliced (n + 1))) ∧
      (∀ k, ∃ n, spliced n ≠ h1 (n + k)) ∧ (∀ k, ∃ n, spliced n ≠ h2 (n + k)) :=
  ⟨fun n => match n with
    | 0 => .inl ⟨0, rfl, rfl, rfl⟩
    | 1 => .inr ⟨1, rfl, rfl, rfl⟩
    | n + 2 => .inr ⟨n + 2, rfl, rfl, rfl⟩,
   fun k => ⟨2, fun e => h1_ne (2 + k) (e.symm.trans rfl)⟩,
   fun k => ⟨0, fun e => h2_ne (0 + k) (e.symm.trans rfl)⟩⟩

/-! ## 7. Memory closes the gap -/

/-- The configuration that keeps its whole past. -/
def past (h : Nat → S) : Nat → List S
  | 0 => [h 0]
  | n + 1 => h (n + 1) :: past h n

/-- Where configurations keep their past, two histories that meet share their whole past:
nothing can be spliced at a meeting. -/
theorem past_meet {g g' : Nat → S} :
    ∀ n m, past g n = past g' m → n = m ∧ ∀ k, k ≤ n → g k = g' k
  | 0, 0, e => by
    injection e with e1 _
    exact ⟨rfl, fun k hk => by cases hk; exact e1⟩
  | 0, m + 1, e => by
    injection e with _ e2
    cases m <;> exact nomatch e2
  | n + 1, 0, e => by
    injection e with _ e2
    cases n <;> exact nomatch e2
  | n + 1, m + 1, e => by
    injection e with e1 e2
    match past_meet n m e2 with
    | ⟨rfl, ih⟩ =>
      exact ⟨rfl, fun k hk => match Nat.lt_or_eq_of_le hk with
        | .inl lt => ih k (Nat.le_of_lt_succ lt)
        | .inr eq => by subst eq; exact e1⟩

/-! ## 8. A free way and a bound way -/

/-- Balance at one condition across one step, as in `Flow.BalancesOn`. -/
def Balanced (before after taken given : Nat) : Prop := after + taken = before + given

/-- Cancellation, with no axiom. -/
theorem cancel : ∀ k {a b : Nat}, a + k = b + k → a = b
  | 0, _, _, h => h
  | k + 1, _, _, h => cancel k (Nat.succ.inj h)

/-- Bound by balance, the exchange fixes the level after the step. -/
theorem exchange_fixes {b a a' k g : Nat} (e : Balanced b a k g) (e' : Balanced b a' k g) :
    a = a' :=
  cancel k (e.trans e'.symm)

/-- The levels before and after do not fix the exchange: a circulation and no exchange at all. -/
theorem change_leaves_exchange : Balanced 1 1 1 1 ∧ Balanced 1 1 0 0 := ⟨rfl, rfl⟩

/-- A free way fixes nothing: one configuration, one label, two outcomes. -/
def coin : Process Bool Unit := ⟨fun _ _ _ => True⟩

theorem free_way : coin.step false () false ∧ coin.step false () true := ⟨trivial, trivial⟩

/-! ## 9. Standing and passing: each needs what only the other carries -/

/-- Passing fixes standing, given a beginning: two amounts with the same takings and givings at
every step and the same start are the same at every step. -/
theorem passing_fixes_standing {q q' x y : Nat → Nat}
    (e : ∀ t, q (t + 1) + x t = q t + y t) (e' : ∀ t, q' (t + 1) + x t = q' t + y t)
    (start : q 0 = q' 0) : ∀ n, q n = q' n
  | 0 => start
  | n + 1 => cancel (x n) ((e n).trans ((congrArg (· + y n) (passing_fixes_standing e e' start n)).trans (e' n).symm))

/-- Without the beginning it does not: the same passing at every step, different standing. -/
theorem start_needed :
    ∃ q q' x y : Nat → Nat, (∀ t, q (t + 1) + x t = q t + y t) ∧
      (∀ t, q' (t + 1) + x t = q' t + y t) ∧ q 0 ≠ q' 0 :=
  ⟨fun t => t, fun t => t + 1, fun _ => 0, fun _ => 1, fun _ => rfl, fun _ => rfl, by decide⟩

/-! ## 10. Still at one grain, moving at a finer one -/

def alt : Nat → Nat
  | 0 => 1
  | 1 => 0
  | n + 2 => alt n

theorem alt_even : ∀ n, alt (2 * n) = 1
  | 0 => rfl
  | n + 1 => alt_even n

theorem alt_moves : ∀ n, alt n ≠ alt (n + 1)
  | 0 => by decide
  | 1 => by decide
  | n + 2 => alt_moves n

/-- Read every two steps, the amount stands still; read every step, it never does. -/
theorem still_coarse_moving_fine :
    (∀ n, alt (2 * n) = alt (2 * (n + 1))) ∧ ∀ n, alt n ≠ alt (n + 1) :=
  ⟨fun n => (alt_even n).trans (alt_even (n + 1)).symm, alt_moves⟩

end Shape

#print axioms Shape.unlabel_exact
#print axioms Shape.labelled_step
#print axioms Shape.idle_reach
#print axioms Shape.law_has_content
#print axioms Shape.joint_iff_related
#print axioms Shape.label_couples
#print axioms Shape.law_iff_every_step
#print axioms Shape.run_follows
#print axioms Shape.Bisim.same_words
#print axioms Shape.dead_end
#print axioms Shape.splice_new
#print axioms Shape.past_meet
#print axioms Shape.exchange_fixes
#print axioms Shape.change_leaves_exchange
#print axioms Shape.free_way
#print axioms Shape.passing_fixes_standing
#print axioms Shape.start_needed
#print axioms Shape.still_coarse_moving_fine
