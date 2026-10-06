import SuccessionWitness

namespace ApplicationEvidence
open PaidRecipientReasons
set_option maxRecDepth 16384
set_option maxHeartbeats 2000000

/-- A property of accessible archive bytes, not an invented fulfillment flag. -/
def PositiveFrame (reader : PaidArchiveReader.State W) (i : Nat) (r : RecipientArchive.Frame) : Prop :=
  i<3 ∧ reader.archive i=some r ∧ r.context=reader.currentContext ∧
  r.present=true ∧ r.receipt=true

theorem decode_has_positive_frame {x : Option RecipientArchive.Frame} {c d b : Bool}
    (h : RecipientArchive.decode c d x=some b) :
    ∃ r, x=some r ∧ r.context=c ∧ r.present=true ∧ r.receipt=true := by
  cases x with
  | none => cases h
  | some r =>
    simp only [RecipientArchive.decode] at h
    split at h
    · rename_i hp
      simp only [Bool.and_eq_true,beq_iff_eq] at hp
      exact ⟨r,rfl,hp.1.1,hp.1.2,hp.2⟩
    · contradiction

theorem normalize_nonempty {d : Bool} {x : Option Bool}
    (h : RecipientReasons.normalize d x≠none) : ∃ b,x=some b := by
  cases x with
  | none => exact False.elim (h rfl)
  | some b => exact ⟨b,rfl⟩

theorem empty_closure_has_no_command :
    RecipientAction.route (ReasonReplay.closureMask RecipientReasons.star
      (RecipientReasons.derived RecipientReasons.empty))=none := by decide

theorem supported_normalized_nonempty {s : State W} {z command : Bool}
    (hi : PublicationSafety.Invariant z s) (hc : CurrentPublication s)
    (hs : RecipientAction.route s.working=some command) :
    s.normalized.first≠none ∨ s.normalized.second≠none ∨ s.normalized.third≠none := by
  by_cases ha:s.normalized.first=none
  · by_cases hb:s.normalized.second=none
    · by_cases hd:s.normalized.third=none
      · have hn : s.normalized=RecipientReasons.empty := by
          cases he:s.normalized with
          | mk a b c => simp_all [RecipientReasons.empty]
        have hw:=PublicationSafety.invariant_publication_exact hi hc
        rw [hw,hn,empty_closure_has_no_command] at hs
        cases hs
      · exact Or.inr (Or.inr hd)
    · exact Or.inr (Or.inl hb)
  · exact Or.inl ha

theorem normalized_support_has_cache {s : State W} {z command : Bool}
    (hi : PublicationSafety.Invariant z s) (hc : CurrentPublication s)
    (hs : RecipientAction.route s.working=some command) :
    ∃ i, i<3 ∧ ∃ b,s.reader.cache i=some b := by
  have hp:s.phase≠0:=by rw [hc.2.1]; decide
  have hh:=hi.selected hp
  rcases supported_normalized_nonempty hi hc hs with h|h|h
  · rcases hh.1 with bad|good
    · exact False.elim (h bad)
    · exact ⟨0,by decide,normalize_nonempty (good ▸ h)⟩
  · rcases hh.2.1 with bad|good
    · exact False.elim (h bad)
    · exact ⟨1,by decide,normalize_nonempty (good ▸ h)⟩
  · rcases hh.2.2 with bad|good
    · exact False.elim (h bad)
    · exact ⟨2,by decide,normalize_nonempty (good ▸ h)⟩

theorem current_command_has_accessible_positive_frame {s : State W} {z command : Bool}
    (hi : PublicationSafety.Invariant z s) (hc : CurrentPublication s)
    (hs : RecipientAction.route s.working=some command) :
    ∃ i r, PositiveFrame s.reader i r := by
  rcases normalized_support_has_cache hi hc hs with ⟨i,hi3,b,hb⟩
  have hcomplete:=hc.2.2.1
  have hn:=hcomplete.2.2
  have he:=hi.cache hcomplete.1 hcomplete.2.1 i (by omega)
  have hd:RecipientArchive.decode s.reader.currentContext (RecipientArchive.designated i)
      (s.reader.archive i)=some b:=he.symm.trans hb
  rcases decode_has_positive_frame hd with ⟨r,hr,hctx,hp,hrc⟩
  exact ⟨i,r,hi3,hr,hctx,hp,hrc⟩

theorem initialized_paid_command_has_positive_frame
    {w : W} {records : Nat→Option RecipientArchive.Frame} {c : Bool} {fuel reserve : Nat}
    {z command : Bool} {t : State W} {es : List Event}
    (hf : PaidArchiveReader.Facts z (PaidArchiveReader.initial w records c fuel))
    (history : Generative.Trace (process W)
      (initial (PaidArchiveReader.initial w records c fuel) reserve) es t)
    (current : CurrentPublication t) (supported : RecipientAction.route t.working=some command) :
    (∃ i r, PositiveFrame t.reader i r) ∧ energy t+spent es=fuel+reserve := by
  have hi:=PublicationSafety.trace_invariant
    (PublicationSafety.initial_invariant _ reserve (PaidArchiveReader.initial_cache_agrees _ _ _ _) hf) history
  exact ⟨current_command_has_accessible_positive_frame hi current supported,trace_ledger history⟩

end ApplicationEvidence
