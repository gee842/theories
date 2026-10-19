import Becoming.Histories

/-!
# History languages: a prefix-closed language is the language of its histories

A **language** is a property of finite courses of moves. The law that extends an admitted history
by one move (`law`) takes, from an admitted history, exactly the courses whose extension stays
admitted, where the language is closed under prefixes (`PrefixClosed`, `trace_iff`). From the empty
history it realizes exactly the admitted words (`feasible_iff`). The feasible words of every process
from a configuration are prefix-closed (`feasible_prefixClosed`), so every process's language is
realized by its histories (`realizes_feasible`): the history carries what the language needs, with
no finite-memory premise. A history is its own configuration; nothing beyond the language is
realized (not hidden configurations, branches or probabilities). Where one configuration must carry
the language it can fail: the language of courses of at most one move has no law on one
configuration (`Bounded.no_one_point_law`), while its histories realize it
(`Bounded.history_realizes`).

**Continuation profiles.** A history's profile is the continuations the language admits after it
(`Future`, `SameFuture`). Extending a history updates its profile by concatenation alone
(`future_update`), so histories with one profile keep one profile after a common extension
(`same_future_extends`); for a process's language the profile after a course is the union of the
languages from where the course can end (`future_iff_reach`). A language is **stable** where no
admitted history changes the profile (`Stable`). For a prefix-closed language admitting the empty
word, stable is exactly letterwise: a word admitted exactly where each of its letters is
(`stable_iff_letterwise`). A word whose letters are each admitted, while the word is not, refutes
stability (`joint_obstruction_refutes_stability`); where the language is decided it locates an
admitted prefix after which the next letter, admitted alone, is blocked, and the prefix's profile
changed (`obstruction_locates_changed_profile`). A lost continuation and a formed one each separate
a profile from the start's (`blocked_extension_separates`, `enabled_extension_separates`). Every
process's feasible words are such a language (`Feasible.stable_iff_letterwise` and its companions).
In `latch` a move `true` closes the route by `false` and the run continues
(`latch_changes_profile_and_continues`); in `gate` it opens it (`gate_gains_profile`); the language
of every word over `Bool` keeps one profile (`unrestricted_stable`).

The language is supplied, not derived; the profile records which words are feasible, not which
branch or cause produces them. This module states in the core what `HistoryRealization`,
`ContinuationConditions`, `ExplanatoryNecessity`'s bounded language (6 to 8 October 2026) and the
join `FeasibleProfileTraces` (17 October) proved on their own definitions (board item F3E,
18 October 2026). No ethical predicate, ranking or axiom occurs; every declaration has an empty
axiom report.
-/

namespace Becoming

open Generative

universe u v

namespace HistoryLanguages

variable {A : Type v}

/-! ## A prefix-closed language and the law of its histories -/

/-- A language is closed under prefixes: an admitted course has every prefix admitted. -/
def PrefixClosed (L : List A → Prop) : Prop :=
  ∀ pre suffix, L (pre ++ suffix) → L pre

/-- The law of a language's histories: a history extends by one move where the extension is
admitted. The configuration is the whole history. -/
def law (L : List A → Prop) : Process (List A) A where
  step before a after := after = before ++ [a] ∧ L after

/-- **From an admitted history, the law of a prefix-closed language takes exactly the courses whose
extension is admitted**, ending at the extension. -/
theorem trace_iff {L : List A → Prop} (closed : PrefixClosed L) :
    ∀ {before : List A} {word : List A} {after : List A}, L before →
      (Trace (law L) before word after ↔ after = before ++ word ∧ L after)
  | before, [], _, admitted =>
    ⟨fun path => match trace_nil_iff.mp path with
      | same => ⟨same ▸ (ListTests.append_nil before).symm, same ▸ admitted⟩,
     fun ⟨same, _⟩ => trace_nil_iff.mpr (same.trans (ListTests.append_nil before)).symm⟩
  | before, a :: rest, _, _ =>
    have shift : before ++ [a] ++ rest = before ++ (a :: rest) := ListTests.append_assoc before [a] rest
    ⟨fun path => match trace_cons_iff.mp path with
      | ⟨_, ⟨first, middle⟩, tail⟩ =>
        have tail := first ▸ tail
        have middle : L (before ++ [a]) := first ▸ middle
        match (trace_iff closed middle).mp tail with
        | ⟨same, held⟩ => ⟨same.trans shift, held⟩,
     fun ⟨same, held⟩ =>
      have middle : L (before ++ [a]) :=
        closed _ rest (Eq.subst (motive := L) (same.trans shift.symm) held)
      trace_cons_iff.mpr ⟨before ++ [a], ⟨rfl, middle⟩,
        (trace_iff closed middle).mpr ⟨same.trans shift.symm, held⟩⟩⟩

/-- From the empty history the law of a prefix-closed language admitting the empty word goes by a
course exactly to the course, where the course is admitted. -/
theorem trace_from_empty_iff {L : List A → Prop} (closed : PrefixClosed L) (empty : L [])
    (word after : List A) : Trace (law L) [] word after ↔ after = word ∧ L word :=
  ⟨fun path => match (trace_iff closed empty).mp path with
    | ⟨same, held⟩ => ⟨same, Eq.subst (motive := L) same held⟩,
   fun ⟨same, held⟩ => (trace_iff closed empty).mpr ⟨same, Eq.subst (motive := L) same.symm held⟩⟩

/-- **The histories of a prefix-closed language admitting the empty word realize it**: from the
empty history the feasible words are the admitted ones. -/
theorem feasible_iff {L : List A → Prop} (closed : PrefixClosed L) (empty : L [])
    (word : List A) : Feasible (law L) [] word ↔ L word :=
  ⟨fun ⟨after, path⟩ => ((trace_from_empty_iff closed empty word after).mp path).2,
   fun held => ⟨word, (trace_from_empty_iff closed empty word word).mpr ⟨rfl, held⟩⟩⟩

/-- **The feasible words of a process from a configuration are prefix-closed.** -/
theorem feasible_prefixClosed {S : Type u} (P : Process S A) (s : S) :
    PrefixClosed (Feasible P s) :=
  fun _ _ held => feasible_prefix held

/-- The empty word is feasible from every configuration. -/
theorem feasible_nil {S : Type u} (P : Process S A) (s : S) : Feasible P s [] :=
  ⟨s, .nil s⟩

/-- **Every process's language is realized by its histories**: the histories of the feasible words
from `s` take exactly the words feasible from `s`. -/
theorem realizes_feasible {S : Type u} (P : Process S A) (s : S) (word : List A) :
    Feasible (law (Feasible P s)) [] word ↔ Feasible P s word :=
  feasible_iff (feasible_prefixClosed P s) (feasible_nil P s) word

/-! ## A language one configuration cannot carry -/

namespace Bounded

/-- Courses of at most one move. -/
def lang (word : List Unit) : Prop := word = [] ∨ ∃ a, word = [a]

theorem empty : lang [] := Or.inl rfl

theorem single (a : Unit) : lang [a] := Or.inr ⟨a, rfl⟩

theorem not_double : ¬ lang [(), ()]
  | .inl same => nomatch same
  | .inr ⟨_, same⟩ => nomatch same

theorem prefixClosed : PrefixClosed lang
  | [], _, _ => empty
  | [a], _, _ => single a
  | _ :: _ :: _, _, .inl same => nomatch same
  | _ :: _ :: _, _, .inr ⟨_, same⟩ => nomatch same

/-- **No law on one configuration realizes the courses of at most one move.** -/
theorem no_one_point_law : ¬ ∃ P : Process Unit Unit, ∀ word, Feasible P () word ↔ lang word
  | ⟨P, same⟩ => match (same [()]).mpr (single ()) with
    | ⟨(), path⟩ =>
      have step : P.step () () () := trace_singleton_iff.mp path
      not_double ((same [(), ()]).mp ⟨(), .cons step (.cons step (.nil ()))⟩)

/-- **Its histories realize it.** -/
theorem history_realizes (word : List Unit) : Feasible (law lang) [] word ↔ lang word :=
  feasible_iff prefixClosed empty word

end Bounded

/-! ## Continuation profiles -/

/-- The continuations admitted after a history. -/
def Future (L : List A → Prop) (past suffix : List A) : Prop :=
  L (past ++ suffix)

/-- Two histories with one profile: the same continuations are admitted after each. -/
def SameFuture (L : List A → Prop) (h k : List A) : Prop :=
  ∀ suffix, Future L h suffix ↔ Future L k suffix

/-- No admitted history changes the profile. -/
def Stable (L : List A → Prop) : Prop :=
  ∀ h, L h → SameFuture L h []

/-- Each letter of the word is admitted alone. -/
def Letterwise (L : List A → Prop) : List A → Prop
  | [] => True
  | a :: rest => L [a] ∧ Letterwise L rest

/-- **A profile updates by concatenation alone.** -/
theorem future_update (L : List A → Prop) (h extension suffix : List A) :
    Future L (h ++ extension) suffix ↔ Future L h (extension ++ suffix) :=
  show L (h ++ extension ++ suffix) ↔ L (h ++ (extension ++ suffix)) from
    (ListTests.append_assoc h extension suffix) ▸ Iff.rfl

/-- **Histories with one profile keep one profile after a common extension.** -/
theorem same_future_extends (L : List A → Prop) {h k : List A} (same : SameFuture L h k)
    (extension : List A) : SameFuture L (h ++ extension) (k ++ extension) :=
  fun suffix => (future_update L h extension suffix).trans
    ((same (extension ++ suffix)).trans (future_update L k extension suffix).symm)

theorem letterwise_append (L : List A → Prop) :
    ∀ h k : List A, Letterwise L (h ++ k) ↔ Letterwise L h ∧ Letterwise L k
  | [], _ => ⟨fun held => ⟨True.intro, held⟩, fun held => held.2⟩
  | _ :: h, k =>
    ⟨fun held => match (letterwise_append L h k).mp held.2 with
      | ⟨left, right⟩ => ⟨⟨held.1, left⟩, right⟩,
     fun held => ⟨held.1.1, (letterwise_append L h k).mpr ⟨held.1.2, held.2⟩⟩⟩

/-- A stable prefix-closed language admitting the empty word admits exactly the letterwise
words. -/
theorem stable_implies_letterwise (L : List A → Prop) (closed : PrefixClosed L) (empty : L [])
    (stable : Stable L) : ∀ word, L word ↔ Letterwise L word
  | [] => ⟨fun _ => True.intro, fun _ => empty⟩
  | a :: word =>
    ⟨fun held =>
      have first : L [a] := closed [a] word held
      ⟨first, (stable_implies_letterwise L closed empty stable word).mp
        ((stable [a] first word).mp held)⟩,
     fun held => (stable [a] held.1 word).mpr
      ((stable_implies_letterwise L closed empty stable word).mpr held.2)⟩

theorem letterwise_implies_stable (L : List A → Prop)
    (exactLetters : ∀ word, L word ↔ Letterwise L word) : Stable L :=
  fun h held suffix =>
    ⟨fun after => (exactLetters suffix).mpr
      ((letterwise_append L h suffix).mp ((exactLetters (h ++ suffix)).mp after)).2,
     fun after => (exactLetters (h ++ suffix)).mpr
      ((letterwise_append L h suffix).mpr ⟨(exactLetters h).mp held, (exactLetters suffix).mp after⟩)⟩

/-- **A prefix-closed language admitting the empty word is stable exactly where it is letterwise.** -/
theorem stable_iff_letterwise (L : List A → Prop) (closed : PrefixClosed L) (empty : L []) :
    Stable L ↔ ∀ word, L word ↔ Letterwise L word :=
  ⟨stable_implies_letterwise L closed empty, letterwise_implies_stable L⟩

/-- **A joint obstruction refutes stability**: a word whose letters are each admitted while the word
is not. -/
theorem joint_obstruction_refutes_stability (L : List A → Prop) (closed : PrefixClosed L)
    (empty : L []) (word : List A) (letters : Letterwise L word) (blocked : ¬ L word) :
    ¬ Stable L :=
  fun stable => blocked ((stable_implies_letterwise L closed empty stable word).mpr letters)

/-- **A lost continuation separates the profile from the start's.** -/
theorem blocked_extension_separates (L : List A → Prop) (past suffix : List A)
    (initially : L suffix) (blocked : ¬ L (past ++ suffix)) : ¬ SameFuture L past [] :=
  fun same => blocked ((same suffix).mpr initially)

/-- **A formed continuation separates it too.** -/
theorem enabled_extension_separates (L : List A → Prop) (past suffix : List A)
    (formed : L (past ++ suffix)) (unavailable : ¬ L suffix) : ¬ SameFuture L past [] :=
  fun same => unavailable ((same suffix).mp formed)

/-- Where the language is decided, an obstruction after an admitted history locates an admitted
prefix after which the next letter is blocked. -/
theorem locate_first_obstruction (L : List A → Prop) [DecidablePred L] :
    ∀ (start word : List A), L start → Letterwise L word → ¬ L (start ++ word) →
      ∃ pre a suffix, word = pre ++ (a :: suffix) ∧ L (start ++ pre) ∧ L [a] ∧
        ¬ L ((start ++ pre) ++ [a])
  | start, [], admitted, _, blocked => absurd ((ListTests.append_nil start).symm ▸ admitted) blocked
  | start, a :: word, admitted, letters, blocked =>
    if next : L (start ++ [a]) then
      have later : ¬ L ((start ++ [a]) ++ word) :=
        fun held => blocked ((ListTests.append_assoc start [a] word) ▸ held)
      match locate_first_obstruction L (start ++ [a]) word next letters.2 later with
      | ⟨pre, b, suffix, same, held, letter, stuck⟩ =>
        ⟨a :: pre, b, suffix, congrArg (List.cons a) same,
         (ListTests.append_assoc start [a] pre) ▸ held, letter,
         fun reached => stuck ((congrArg (fun xs => xs ++ [b])
           (ListTests.append_assoc start [a] pre)).symm ▸ reached)⟩
    else
      ⟨[], a, word, rfl, (ListTests.append_nil start).symm ▸ admitted, letters.1,
       fun reached => next ((congrArg (fun xs => xs ++ [a]) (ListTests.append_nil start)) ▸ reached)⟩

/-- **A decided obstruction locates a changed profile**: an admitted prefix of the word, whose next
letter is admitted alone and blocked after it, and whose profile differs from the start's. -/
theorem obstruction_locates_changed_profile (L : List A → Prop) [DecidablePred L] (empty : L [])
    (word : List A) (letters : Letterwise L word) (blocked : ¬ L word) :
    ∃ pre a suffix, word = pre ++ (a :: suffix) ∧ L pre ∧ L [a] ∧ ¬ L (pre ++ [a]) ∧
      ¬ SameFuture L pre [] :=
  match locate_first_obstruction L [] word empty letters blocked with
  | ⟨pre, a, suffix, same, held, letter, stuck⟩ =>
    ⟨pre, a, suffix, same, held, letter, stuck,
     blocked_extension_separates L pre [a] letter stuck⟩

/-! ## The laws of every process's feasible words -/

namespace Feasible

variable {S : Type u}

/-- Stability passes to a language with the same words. -/
theorem stable_of_same {L L' : List A → Prop} (same : ∀ w, L w ↔ L' w) (stable : Stable L) :
    Stable L' :=
  fun h held suffix =>
    (same (h ++ suffix)).symm.trans ((stable h ((same h).mpr held) suffix).trans (same ([] ++ suffix)))

/-- **The feasible words from `s` keep one profile after every feasible history exactly when a word
is feasible exactly where each of its letters is.** -/
theorem stable_iff_letterwise (P : Process S A) (s : S) :
    Stable (Feasible P s) ↔ ∀ word, Feasible P s word ↔ Letterwise (Feasible P s) word :=
  HistoryLanguages.stable_iff_letterwise _ (feasible_prefixClosed P s) (feasible_nil P s)

/-- **A word whose letters are each feasible from `s`, while the word is not, refutes
stability.** -/
theorem joint_obstruction_refutes_stability (P : Process S A) (s : S) {word : List A}
    (letters : Letterwise (Feasible P s) word) (blocked : ¬ Feasible P s word) :
    ¬ Stable (Feasible P s) :=
  HistoryLanguages.joint_obstruction_refutes_stability _ (feasible_prefixClosed P s)
    (feasible_nil P s) word letters blocked

/-- **A decided obstruction locates a changed profile** of a process's feasible words. -/
theorem obstruction_locates_changed_profile (P : Process S A) (s : S)
    [DecidablePred (Feasible P s)] {word : List A}
    (letters : Letterwise (Feasible P s) word) (blocked : ¬ Feasible P s word) :
    ∃ pre a suffix, word = pre ++ (a :: suffix) ∧ Feasible P s pre ∧ Feasible P s [a] ∧
      ¬ Feasible P s (pre ++ [a]) ∧ ¬ SameFuture (Feasible P s) pre [] :=
  HistoryLanguages.obstruction_locates_changed_profile _ (feasible_nil P s) word letters blocked

end Feasible

/-! ## Three languages -/

/-- Every word over `Bool`. -/
def unrestricted : List Bool → Prop := fun _ => True

/-- **The language of every word keeps one profile after every history.** -/
theorem unrestricted_stable : Stable unrestricted :=
  fun _ _ _ => ⟨fun _ => True.intro, fun _ => True.intro⟩

theorem unrestricted_realized (word : List Bool) : Feasible (law unrestricted) [] word :=
  (feasible_iff (fun _ _ _ => True.intro) True.intro word).mpr True.intro

/-- **Its histories keep one profile too.** -/
theorem unrestricted_histories_stable : Stable (Feasible (law unrestricted) []) :=
  Feasible.stable_of_same (fun word => ⟨fun _ => unrestricted_realized word, fun _ => True.intro⟩)
    unrestricted_stable

/-- A latch: `true` closes the route by `false`, and `true` stays possible. -/
def latch : Process Bool Bool where
  step before event after := (before = false ∨ event = true) ∧ after = (before || event)

theorem latch_obstruction :
    Feasible latch false [true] ∧ Feasible latch false [false] ∧
      ¬ Feasible latch false [true, false] ∧ Feasible latch false [true, true] :=
  ⟨⟨true, .cons ⟨Or.inl rfl, rfl⟩ (.nil true)⟩,
   ⟨false, .cons ⟨Or.inl rfl, rfl⟩ (.nil false)⟩,
   fun ⟨_, path⟩ => match trace_cons_iff.mp path with
    | ⟨middle, first, rest⟩ =>
      have set : middle = true := (first : (false = false ∨ true = true) ∧ middle = (false || true)).2
      match trace_cons_iff.mp (set ▸ rest) with
      | ⟨last, second, _⟩ =>
        match (second : (true = false ∨ false = true) ∧ last = (true || false)).1 with
        | .inl closed => Bool.noConfusion closed
        | .inr closed => Bool.noConfusion closed,
   ⟨true, .cons ⟨Or.inl rfl, rfl⟩ (.cons ⟨Or.inr rfl, rfl⟩ (.nil true))⟩⟩

/-- **The latch changes the profile and the run continues.** -/
theorem latch_changes_profile_and_continues :
    ¬ SameFuture (Feasible latch false) [true] [] ∧ Feasible latch false [true, true] :=
  ⟨blocked_extension_separates _ [true] [false] latch_obstruction.2.1 latch_obstruction.2.2.1,
   latch_obstruction.2.2.2⟩

/-- A gate: `true` opens the route by `false`. -/
def gate : Process Bool Bool where
  step before event after := (event = true ∨ before = true) ∧ after = (before || event)

theorem gate_formation :
    Feasible gate false [true] ∧ ¬ Feasible gate false [false] ∧ Feasible gate false [true, false] :=
  ⟨⟨true, .cons ⟨Or.inl rfl, rfl⟩ (.nil true)⟩,
   fun ⟨last, path⟩ =>
    match (trace_singleton_iff.mp path : (false = true ∨ false = true) ∧ last = (false || false)).1 with
    | .inl shut => Bool.noConfusion shut
    | .inr shut => Bool.noConfusion shut,
   ⟨true, .cons ⟨Or.inl rfl, rfl⟩ (.cons ⟨Or.inr rfl, rfl⟩ (.nil true))⟩⟩

/-- **The gate gains a profile.** -/
theorem gate_gains_profile : ¬ SameFuture (Feasible gate false) [true] [] :=
  enabled_extension_separates _ [true] [false] gate_formation.2.2 gate_formation.2.1

end HistoryLanguages

end Becoming
