import RealFeedback

/-! Time-dependent effective gains in the same paired-state feedback law.
The gain schedule is initially arbitrary. A separate model must account for
how actual acquired consequences select and support that schedule. -/
namespace SystemsComplexity.AdaptiveCore

noncomputable section

def trajectory (gain : ℕ → ℝ) (initial : ℝ × ℝ) : ℕ → ℝ × ℝ
  | 0 => initial
  | n + 1 => RealFeedback.delayedStep (gain n) (trajectory gain initial n)

def envelope (s : ℝ × ℝ) : ℝ :=
  max (abs s.1) (max (abs s.2) (abs (s.1 - s.2)))

end
end SystemsComplexity.AdaptiveCore
