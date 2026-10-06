import RemainingDependency

/-!
Target-relative relevance within the already supplied calibration family.
After one full response at setting r is known to be f, all weak tables remain
possible. A single faithful weak query settles whether weak and full agree at
r exactly when that query is at r. This is an epistemic sufficiency result, not
formation of a policy, physical affordability, unique general fault diagnosis,
or ethical warrant. The enumeration below describes the finite family; it adds
no native event, controller, contact or candidate-update law.

Here q denotes the weak test's physical relay setting, not the contact-route
selector. The earlier contact-zero separator tests relay setting one and uses
contact route zero. This theorem neither chooses nor establishes faithfulness
of that observation route. The full bit is historical; the queried weak bit is
current. Interpreting their difference as an old report's refutation requires
the separately stated stationarity/binding premises.
-/
namespace InquiryRelevance
open RemainingDependency

def LocalAgreement (weak : Pair Bool) (r f : Bool) : Prop := weak.get r = f

def QuerySufficient (r f q : Bool) : Prop :=
  ∀ weak alternative : Pair Bool, weak.get q = alternative.get q →
    (LocalAgreement weak r f ↔ LocalAgreement alternative r f)

theorem used_setting_sufficient (r f : Bool) : QuerySufficient r f r := by
  intro weak alternative h
  unfold LocalAgreement
  rw [h]

/-- The two tables agree at the off-target query but give opposite answers to
the question about the used setting. Neither unobserved bit is supplied as an
acquired observation. -/
theorem off_target_witness (r f q : Bool) (hq : q ≠ r) :
    let weak : Pair Bool := ⟨f, f⟩
    let alternative := weak.set r (!f)
    weak.get q = alternative.get q ∧
      LocalAgreement weak r f ∧ ¬ LocalAgreement alternative r f := by
  cases r <;> cases f <;> cases q <;>
    simp_all [Pair.get, Pair.set, LocalAgreement]

theorem query_sufficient_iff_used_setting (r f q : Bool) :
    QuerySufficient r f q ↔ q = r := by
  constructor
  · intro sufficient
    by_cases hq : q = r
    · exact hq
    · obtain ⟨same, agrees, disagrees⟩ := off_target_witness r f q hq
      exact False.elim (disagrees ((sufficient _ _ same).mp agrees))
  · intro hq
    subst q
    exact used_setting_sufficient r f

/-- Explicit full Cartesian family of the two-setting Boolean response laws. -/
def tables : List (Pair Bool) :=
  [⟨false,false⟩, ⟨false,true⟩, ⟨true,false⟩, ⟨true,true⟩]

theorem every_table_listed (weak : Pair Bool) : weak ∈ tables := by
  rcases weak with ⟨a,b⟩
  cases a <;> cases b <;> decide

/-- All pairs of weak/full laws compatible with the acquired full bit. The
unqueried full coordinate remains free, as in the prior calibration study. -/
def posterior (r f : Bool) : List (Pair Bool × Pair Bool) :=
  (tables.flatMap fun weak => tables.map fun full => (weak,full)).filter
    (fun pair => pair.2.get r == f)

theorem posterior_membership (weak full : Pair Bool) (r f : Bool) :
    (weak,full) ∈ posterior r f ↔ full.get r = f := by
  rcases weak with ⟨a,b⟩
  rcases full with ⟨c,d⟩
  cases a <;> cases b <;> cases c <;> cases d <;> cases r <;> cases f <;> decide

theorem posterior_size (r f : Bool) : (posterior r f).length = 8 := by
  cases r <;> cases f <;> decide

/-- Both weak queries partition the same eight possibilities into two groups
of four. Equal unqualified split size does not make them equally sufficient
for the independently specified local-agreement question. -/
theorem either_query_splits_equally (r f q answer : Bool) :
    ((posterior r f).filter fun pair => pair.1.get q == answer).length = 4 := by
  cases r <;> cases f <;> cases q <;> cases answer <;> decide

end InquiryRelevance

#print axioms InquiryRelevance.LocalAgreement
#print axioms InquiryRelevance.QuerySufficient
#print axioms InquiryRelevance.used_setting_sufficient
#print axioms InquiryRelevance.off_target_witness
#print axioms InquiryRelevance.query_sufficient_iff_used_setting
#print axioms InquiryRelevance.tables
#print axioms InquiryRelevance.every_table_listed
#print axioms InquiryRelevance.posterior
#print axioms InquiryRelevance.posterior_membership
#print axioms InquiryRelevance.posterior_size
#print axioms InquiryRelevance.either_query_splits_equally
