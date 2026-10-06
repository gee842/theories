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

theorem advance_preserves_stocks_at_empty_source (cfg : Config) (b : Body) (e : Event)
    (hz : b.stocks.source = 0) : (advance cfg b e).stocks = b.stocks := by
  cases e with
  | contextChange => rfl
  | transfer => simp [advance, fullTransfer, hz]
  | commit =>
    apply paid_stocks_preserved
    intro z
    cases cfg.clamp <;> rfl
  | _ =>
    apply paid_stocks_preserved
    intro z
    rfl

theorem advance_preserves_empty_source (cfg : Config) (b : Body) (e : Event)
    (hz : b.stocks.source = 0) : (advance cfg b e).stocks.source = 0 := by
  rw [advance_preserves_stocks_at_empty_source cfg b e hz]
  exact hz

theorem viewBody_account (b : Body) : (viewBody b).account = b.account := rfl

/-- Projecting the body commutes with any charged effect that itself commutes.
The original charge implementation stays opaque in this structural argument. -/
theorem viewBody_paid (b : Body) (w l t e r : Nat) (f g : Body → Body)
    (hf : ∀ z, viewBody (f z) = g (viewBody z)) :
    viewBody (paid b w l t e r f) = paid (viewBody b) w l t e r g := by
  simp only [paid, viewBody_account]
  split
  · exact hf _
  · rfl

theorem view_advance_at_empty_source (cfg : Config) (b : Body) (e : Event)
    (hz : b.stocks.source = 0) :
    viewBody (advance cfg b e) =
      advance {cfg with full := ⟨false,false⟩} (viewBody b) e := by
  cases e with
  | contextChange => rfl
  | transfer => simp [advance, fullTransfer, viewBody, hz]
  | commit =>
    apply viewBody_paid
    intro z
    cases cfg.clamp <;> rfl
  | _ =>
    apply viewBody_paid
    intro z
    rfl

theorem step_preserves_empty_source (s : State) (e : Event)
    (hz : s.body.stocks.source = 0) : (step s e).body.stocks.source = 0 :=
  advance_preserves_empty_source s.config s.body e hz

theorem view_step_at_empty_source (s : State) (e : Event)
    (hz : s.body.stocks.source = 0) : view (step s e) = step (view s) e := by
  cases s with
  | mk ancestor cfg b =>
    simp only [view, step]
    rw [view_advance_at_empty_source cfg b e hz]

theorem run_preserves_empty_source (s : State) (es : List Event)
    (hz : s.body.stocks.source = 0) : (run s es).body.stocks.source = 0 := by
  induction es generalizing s with
  | nil => exact hz
  | cons e es ih => exact ih (step s e) (step_preserves_empty_source s e hz)

theorem view_run_at_empty_source (s : State) (es : List Event)
    (hz : s.body.stocks.source = 0) : view (run s es) = run (view s) es := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih =>
    rw [run, ih (step s e) (step_preserves_empty_source s e hz), view_step_at_empty_source s e hz]
    rfl

/-- Every finite request word has equal projected endpoints, including arbitrary
alternate contacts and denied attempts; the original native scheduler is not
assumed. Actual destination stocks are retained in the unprojected processes. -/
theorem equal_view_runs (s t : State) (es : List Event)
    (hs : s.body.stocks.source = 0) (ht : t.body.stocks.source = 0)
    (hv : view s = view t) : view (run s es) = view (run t es) := by
  rw [view_run_at_empty_source s es hs, view_run_at_empty_source t es ht, hv]

end ConsequenceInquiry

#print axioms ConsequenceInquiry.view_preserves_source
#print axioms ConsequenceInquiry.view_preserves_stock_total
#print axioms ConsequenceInquiry.advance_preserves_stocks_at_empty_source
#print axioms ConsequenceInquiry.advance_preserves_empty_source
#print axioms ConsequenceInquiry.viewBody_account
#print axioms ConsequenceInquiry.viewBody_paid
#print axioms ConsequenceInquiry.view_advance_at_empty_source
#print axioms ConsequenceInquiry.step_preserves_empty_source
#print axioms ConsequenceInquiry.view_step_at_empty_source
#print axioms ConsequenceInquiry.run_preserves_empty_source
#print axioms ConsequenceInquiry.view_run_at_empty_source
#print axioms ConsequenceInquiry.equal_view_runs
