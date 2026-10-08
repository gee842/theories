import BecomingReversibility
open BecomingReversibility Generative
example : ¬ Reach oneWay true false := oneWay_no_return
example : ∃ q, Possible oneWay false q ∧ ¬ Possible oneWay true q :=
  irreversible_iff_endpoint_loss.mp oneWay_no_return
