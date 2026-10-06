import GenerativeOutcomeModel
import InquirySufficiency

/-!
Public addition to the unchanged structural/outcome model: a constructive
bounded-policy sufficiency criterion over its actual Process transitions.
Response progress, every admitted successor, prefix conditions and the changing
candidate configuration are retained. No event law, value scale, installed
planner or acquired stopping criterion is introduced. The separate source-bound
checker preserves the original model's exact dependency reports.
-/
