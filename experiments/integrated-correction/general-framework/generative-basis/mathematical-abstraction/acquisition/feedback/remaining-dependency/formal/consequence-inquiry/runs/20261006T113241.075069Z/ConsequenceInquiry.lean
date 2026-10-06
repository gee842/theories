import RemainingDependency

/-!
Observation scope after source exhaustion in the unchanged relay law.
The view below is an analyst's quotient, richer than the actual controller's
input. It retains discharged total while forgetting its load/waste allocation
and the full-load response law. No physical outcome is erased or restored.
-/
namespace ConsequenceInquiry
open RemainingDependency

set_option maxRecDepth 32768
set_option maxHeartbeats 4000000

def viewBody (b : Body) : Body :=
  {b with stocks := {source := b.stocks.source, load := b.stocks.load + b.stocks.waste, waste := 0}}

def view (s : State) : State :=
  {s with config := {s.config with full := ⟨false,false⟩}, body := viewBody s.body}

theorem view_preserves_source (s : State) :
    (view s).body.stocks.source = s.body.stocks.source := rfl

theorem view_preserves_stock_total (s : State) :
    (view s).body.stocks.total = s.body.stocks.total := by
  simp [view, viewBody, Stocks.total, Nat.add_assoc]

theorem advance_preserves_empty_source (cfg : Config) (b : Body) (e : Event)
    (hz : b.stocks.source = 0) : (advance cfg b e).stocks.source = 0 := by
  cases e <;> simp [advance, paid, fullTransfer, hz]
  all_goals repeat' first | split | progress simp_all

theorem advance_preserves_stocks_at_empty_source (cfg : Config) (b : Body) (e : Event)
    (hz : b.stocks.source = 0) : (advance cfg b e).stocks = b.stocks := by
  cases e <;> simp [advance, paid, fullTransfer, hz]
  all_goals repeat' first | split | progress simp_all

theorem view_advance_at_empty_source (cfg : Config) (b : Body) (e : Event)
    (hz : b.stocks.source = 0) :
    viewBody (advance cfg b e) =
      advance {cfg with full := ⟨false,false⟩} (viewBody b) e := by
  cases e <;> simp [advance, paid, fullTransfer, viewBody, hz]
  all_goals repeat' first | split | progress simp_all [viewBody]

end ConsequenceInquiry

#print axioms ConsequenceInquiry.view_preserves_source
#print axioms ConsequenceInquiry.view_preserves_stock_total
#print axioms ConsequenceInquiry.advance_preserves_empty_source
#print axioms ConsequenceInquiry.advance_preserves_stocks_at_empty_source
#print axioms ConsequenceInquiry.view_advance_at_empty_source
