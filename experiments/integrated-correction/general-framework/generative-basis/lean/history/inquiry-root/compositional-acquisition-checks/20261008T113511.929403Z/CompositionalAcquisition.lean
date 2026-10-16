import KnowledgeCorrespondence

/-!
Acquired compositional interpretation in an explicitly restricted law family.
The grammar, primitive operations, uniform recursive law, faithful probes,
training schedule and accounting convention are supplied. No theorem defines
cognition, consciousness, natural language or evolutionary advantage.
Evidence and targets are projections of a common local law/history.
-/
namespace Generative.CompositionalAcquisition

inductive Expr where
  | atom : Bool → Expr
  | join : Expr → Expr → Expr
  | twice : Expr → Expr
  deriving DecidableEq, Repr

structure Code where
  first : Bool
  second : Bool
  reversed : Bool
  deriving DecidableEq, Repr

def eval (c : Code) : Expr → List Bool
  | .atom false => [c.first]
  | .atom true => [c.second]
  | .join p q => if c.reversed then eval c q ++ eval c p else eval c p ++ eval c q
  | .twice p => eval c p ++ eval c p

def p0 : Expr := .atom false
def p1 : Expr := .atom true
def orderProbe : Expr := .join p0 p1

structure Evidence where
  first : Bool
  second : Bool
  ordered : List Bool
  deriving DecidableEq, Repr

def observe (c : Code) : Evidence :=
  ⟨c.first, c.second, eval c orderProbe⟩

def acquire (e : Evidence) : Code :=
  ⟨e.first, e.second, !(e.ordered == [e.first, e.second])⟩

theorem probe_readings (c : Code) :
    eval c p0 = [(observe c).first] ∧ eval c p1 = [(observe c).second] := by
  constructor <;> rfl

theorem acquired_code_exact (c : Code) (distinct : c.first ≠ c.second) :
    acquire (observe c) = c := by
  rcases c with ⟨a,b,r⟩
  cases a <;> cases b <;> cases r <;> simp_all [acquire, observe, eval, orderProbe, p0, p1]

-- Exactness covers every finite expression, with no tested-depth restriction.
theorem acquired_all_expressions (c : Code) (distinct : c.first ≠ c.second)
    (e : Expr) : eval (acquire (observe c)) e = eval c e := by
  rw [acquired_code_exact c distinct]

def rename : Expr → Expr
  | .atom b => .atom (!b)
  | .join p q => .join (rename p) (rename q)
  | .twice p => .twice (rename p)

def renamed (c : Code) : Code := ⟨c.second,c.first,c.reversed⟩

theorem reencoding_preserves_content (c : Code) (e : Expr) :
    eval (renamed c) (rename e) = eval c e := by
  induction e with
  | atom b => cases b <;> rfl
  | join p q hp hq =>
    simp only [rename, eval]
    rw [hp,hq]
    rfl
  | twice p hp => simp only [rename,eval]; rw [hp]

def operationCost (c : Code) (e : Expr) : Nat := 1 + (eval c e).length
def acquisitionCost (c : Code) : Nat :=
  operationCost c p0 + operationCost c p1 + operationCost c orderProbe

theorem acquisition_cost (c : Code) : acquisitionCost c = 7 := by
  rcases c with ⟨a,b,r⟩
  cases r <;> simp [acquisitionCost, operationCost, eval, p0, p1, orderProbe]

structure Learner where
  code : Option Code
  support : Nat
  records : List (Expr × List Bool)
  deriving DecidableEq, Repr

def trialRecords (c : Code) : List (Expr × List Bool) :=
  [(p0,eval c p0),(p1,eval c p1),(orderProbe,eval c orderProbe)]

def train (c : Code) (s : Learner) : Learner :=
  if acquisitionCost c ≤ s.support then
    ⟨some (acquire (observe c)), s.support - acquisitionCost c,
      s.records ++ trialRecords c⟩
  else s

theorem training_uses_actual_records (c : Code) (s : Learner)
    (enough : 7 ≤ s.support) :
    (train c s).records = s.records ++ trialRecords c := by
  simp [train, acquisition_cost, enough]

theorem training_forms_interpreter (c : Code) (s : Learner)
    (enough : 7 ≤ s.support) (distinct : c.first ≠ c.second) :
    (train c s).code = some c := by
  simp [train, acquisition_cost, enough, acquired_code_exact c distinct]

theorem training_support_conserved (c : Code) (s : Learner)
    (enough : 7 ≤ s.support) : (train c s).support + 7 = s.support := by
  simp [train, acquisition_cost, enough]

theorem insufficient_training_unchanged (c : Code) (s : Learner)
    (short : s.support < 7) : train c s = s := by
  simp [train, acquisition_cost, Nat.not_le_of_lt short]

def execute (s : Learner) (e : Expr) : Option (List Bool × Nat) :=
  match s.code with
  | none => none
  | some c => if operationCost c e ≤ s.support then
      some (eval c e, s.support - operationCost c e) else none

theorem acquired_execution (c : Code) (s : Learner) (e : Expr)
    (distinct : c.first ≠ c.second)
    (enough : 7 + operationCost c e ≤ s.support) :
    execute (train c s) e =
      some (eval c e, s.support - 7 - operationCost c e) := by
  have ht : 7 ≤ s.support := by omega
  have he : operationCost c e ≤ s.support - 7 := by omega
  simp [execute, train, acquisition_cost, ht, acquired_code_exact c distinct, he]

theorem acquired_execution_conserved (c : Code) (s : Learner) (e : Expr)
    (enough : 7 + operationCost c e ≤ s.support) :
    (s.support - 7 - operationCost c e) + operationCost c e + 7 = s.support := by
  omega

-- A genuine information limit in the admitted family, using the earlier interface.
def primitiveEvidence (c : Code) : Bool × Bool := (c.first,c.second)
def separated (c : Code) : Prop := c.first ≠ c.second

theorem primitive_readings_do_not_resolve_order :
    ¬ KnowledgeCorrespondence.Resolves separated primitiveEvidence Code.reversed := by
  intro h
  have impossible := h ⟨false,true,false⟩ ⟨false,true,true⟩
    (by simp [separated]) (by simp [separated]) rfl
  cases impossible

theorem no_exact_order_without_composite_probe :
    ¬ ∃ answer, KnowledgeCorrespondence.ExactOn separated primitiveEvidence
      Code.reversed answer := by
  rintro ⟨answer,h⟩
  exact primitive_readings_do_not_resolve_order
    (KnowledgeCorrespondence.exact_requires_resolution h)

def usual : Code := ⟨false,true,false⟩
def switched : Code := ⟨false,true,true⟩
def novel : Expr := .join (.twice p0) p1
def initial (n : Nat) : Learner := ⟨none,n,[]⟩

theorem novel_expression_not_a_training_item :
    novel ≠ p0 ∧ novel ≠ p1 ∧ novel ≠ orderProbe := by decide

theorem novel_execution_from_acquisition :
    execute (train usual (initial 11)) novel = some ([false,false,true],0) := by decide

theorem acquired_capacity_can_outlast_executable_support :
    (train usual (initial 7)).code = some usual ∧
    execute (train usual (initial 7)) novel = none := by decide

theorem changed_order_invalidates_transfer :
    eval (acquire (observe usual)) novel ≠ eval switched novel := by decide

-- An actual larger law family, not an unexplained semantic truth flag.
-- This nonuniform law agrees on the three encountered forms and swaps their
-- binary outputs on every other form; the three records cannot exclude it.
def nonuniform (e : Expr) : List Bool :=
  if e = p0 ∨ e = p1 ∨ e = orderProbe then eval usual e
  else (eval usual e).map Bool.not

theorem nonuniform_matches_training :
    nonuniform p0 = eval usual p0 ∧ nonuniform p1 = eval usual p1 ∧
    nonuniform orderProbe = eval usual orderProbe := by decide

theorem nonuniform_fails_transfer : nonuniform novel ≠ eval usual novel := by decide

-- Positive content is not the same relation as choosing a favored consequence.
def pick (preferred : Bool) (c : Code) : Expr :=
  if c.first = preferred then p0 else p1

theorem changed_motivation_preserves_acquired_content :
    eval (acquire (observe usual)) (pick false (acquire (observe usual))) = [false] ∧
    eval (acquire (observe usual)) (pick true (acquire (observe usual))) = [true] := by decide

end Generative.CompositionalAcquisition
