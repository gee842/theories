import PublicationSafety

namespace PublicationBudget
open PaidRecipientReasons PublicationSafety

def readerCredit (r : PaidArchiveReader.State W) : Nat :=
  if r.active then if r.token=some r.currentContext then 2+4*r.next else 1 else 0

def credit (s : State W) : Nat :=
  match s.phase with
  | 0 => readerCredit s.reader
  | 1 => 15 | 2 => 16 | 3 => 17 | 4 => 18
  | 5 => 19 | 6 => 20 | 7 => 22 | 8 => 24
  | _ => 0

def isPublication : Event → Nat | .publish=>1 | _=>0

def publications : List Event → Nat | []=>0 | e::es=>isPublication e+publications es

theorem complete_reader_credit {r : PaidArchiveReader.State W}
    (h : PaidArchiveReader.Complete r) : readerCredit r=14 := by
  simp [readerCredit,h.1,h.2.1,h.2.2]

theorem reader_step_credit {r t : PaidArchiveReader.State W} {e : PaidArchiveReader.Event}
    (h : PaidArchiveReader.Step r e t) : readerCredit t≤readerCredit r+PaidArchiveReader.charge e := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | activate => simp [readerCredit,PaidArchiveReader.advance,PaidArchiveReader.charge]
  | contextChange c => simp [readerCredit,PaidArchiveReader.advance,PaidArchiveReader.charge]
  | sense => simp [readerCredit,PaidArchiveReader.advance,PaidArchiveReader.charge,he.1,he.2.1,he.2.2.1]
  | read => simp [readerCredit,PaidArchiveReader.advance,PaidArchiveReader.charge,he.1,he.2.1]; omega

theorem complete_no_sense {r : PaidArchiveReader.State W} (h : PaidArchiveReader.Complete r) :
    ¬ PaidArchiveReader.Enabled r .sense := by
  intro he
  have h1:=h.2.1; have h2:=he.2.1
  rw [h1] at h2
  contradiction

theorem complete_no_read {r : PaidArchiveReader.State W} (h : PaidArchiveReader.Complete r) :
    ¬ PaidArchiveReader.Enabled r .read := by
  intro he
  have h1:=h.2.2; have h2:=he.2.2.1
  omega

theorem step_credit {s t : State W} {e : Event}
    (hi : ActiveComplete s) (h : Step s e t) :
    credit t+24*isPublication e≤credit s+charge e := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | reader e =>
      by_cases hp : s.phase=0
      · have hh:=reader_step_credit (show PaidArchiveReader.Step _ e _ from ⟨he,rfl⟩)
        simpa [credit,hp,advance,isPublication,charge] using hh
      · have hc:=hi hp
        cases e with
        | activate => simp [credit,advance,readerCredit,isPublication,charge,PaidArchiveReader.advance,PaidArchiveReader.charge]
        | contextChange c => simp [credit,advance,readerCredit,isPublication,charge,PaidArchiveReader.advance,PaidArchiveReader.charge]
        | sense => exact False.elim (complete_no_sense hc he)
        | read => exact False.elim (complete_no_read hc he)
  | fund => simp [credit,advance,he.1,readerCredit,isPublication,charge]
  | activate =>
      have hc:=complete_reader_credit he.2.2.1
      simp [credit,advance,he.2.1,isPublication,charge,hc]
  | infer i access =>
      have hp:=he.1
      have hb : i=0 ∨ i=1 ∨ i=2 := by have hlt:=he.2.1; omega
      rcases hb with rfl|rfl|rfl <;> simp [credit,advance,hp,isPublication,charge]
  | path p =>
      have hp:=he.1
      cases p <;> simp [ReasonReplay.pathIndex] at hp <;>
        simp [credit,advance,hp,isPublication,charge,ReasonReplay.pathCost]
  | publish => simp [credit,advance,he.1,isPublication,charge]
  | cold => simp [credit,advance,isPublication,charge,readerCredit]

theorem trace_credit {s t : State W} {es : List Event}
    (hi : ActiveComplete s) (h : Generative.Trace (process W) s es t) :
    credit t+24*publications es≤credit s+spent es := by
  induction h with
  | nil => simp [publications,spent]
  | cons hs _ ih =>
      have step:=step_credit hi hs
      have tail:=ih (step_active_complete hi hs)
      simp only [publications,spent]
      omega

theorem initialized_count_bound {reader : PaidArchiveReader.State W} {reserve : Nat}
    {t : State W} {es : List Event}
    (h : Generative.Trace (process W) (initial reader reserve) es t) :
    24*publications es≤readerCredit reader+spent es := by
  have hh:=trace_credit (s:=initial reader reserve) (by simp [ActiveComplete,initial]) h
  simpa [credit,initial] using (show 24*publications es≤credit (initial reader reserve)+spent es by omega)

theorem unread_count_bound {w : W} {archive : Nat → Option RecipientArchive.Frame}
    {c : Bool} {fuel reserve : Nat} {t : State W} {es : List Event}
    (h : Generative.Trace (process W) (initial (PaidArchiveReader.initial w archive c fuel) reserve) es t) :
    24*publications es≤spent es := by
  simpa [readerCredit,PaidArchiveReader.initial] using initialized_count_bound h

theorem completed_handoff_count_bound {reader : PaidArchiveReader.State W} {reserve : Nat}
    {t : State W} {es : List Event} (hc : PaidArchiveReader.Complete reader)
    (h : Generative.Trace (process W) (initial reader reserve) es t) :
    24*publications es≤spent es+14 := by
  have hh:=initialized_count_bound h
  rw [complete_reader_credit hc] at hh
  omega

theorem inherited_fuel_count_bound {reader : PaidArchiveReader.State W} {F : Nat}
    {t : State W} {es : List Event} (hf : 94≤F)
    (hc : PaidArchiveReader.Complete reader) (fuel : reader.fuel=6)
    (h : Generative.Trace (process W) (initial reader (F-94)) es t) :
    74+24*publications es≤F := by
  have bound:=completed_handoff_count_bound hc h
  have ledger:=trace_ledger h
  simp only [energy,initial] at ledger
  rw [fuel] at ledger
  omega

end PublicationBudget

#print axioms PublicationBudget.complete_reader_credit
#print axioms PublicationBudget.reader_step_credit
#print axioms PublicationBudget.complete_no_sense
#print axioms PublicationBudget.complete_no_read
#print axioms PublicationBudget.step_credit
#print axioms PublicationBudget.trace_credit
#print axioms PublicationBudget.initialized_count_bound
#print axioms PublicationBudget.unread_count_bound
#print axioms PublicationBudget.completed_handoff_count_bound
#print axioms PublicationBudget.inherited_fuel_count_bound
