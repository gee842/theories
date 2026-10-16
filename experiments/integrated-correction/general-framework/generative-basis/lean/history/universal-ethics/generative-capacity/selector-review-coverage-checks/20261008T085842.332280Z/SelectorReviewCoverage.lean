import PracticalJudgment

/- Review descriptions and plans are differentiated descriptions of one relevant
continuation. These interfaces preserve a represented comparative certificate,
not all of its reasons, empirical adequacy, authority or absolute protection.
Different review types need no identity map. The substantive G0/J commitments,
claim meanings and admission of reviews remain outside this logical interface. -/
namespace SelectorReviewCoverage
open PracticalJudgment

/-- A supported application has an eligible strict superior to the plan. -/
def PossibleDefeat {W H : Type} (live : W → Prop) (menu : H → Prop)
    (better : W → H → H → Prop) (a : H) : Prop :=
  ∃ w, live w ∧ ∃ b, menu b ∧ better w b a

/-- Eligibility is explicit even when the live review family is empty. This is
not a guarantee of absolute safety, justified choice, or feasible enactment. -/
def Clear {W H : Type} (live : W → Prop) (menu : H → Prop)
    (better : W → H → H → Prop) (a : H) : Prop :=
  menu a ∧ ∀ w, live w → Frontier menu (better w) a

/-- Reflection of the existence of a represented objection. This does not assert
identity of review labels, fidelity of reasons, or absence of false objections. -/
def CertificateCoverage {W V H : Type} (oldLive : W → Prop) (newLive : V → Prop)
    (menu : H → Prop) (oldBetter : W → H → H → Prop)
    (newBetter : V → H → H → Prop) : Prop :=
  ∀ a, menu a → PossibleDefeat oldLive menu oldBetter a →
    PossibleDefeat newLive menu newBetter a

theorem clear_iff_no_possible_defeat {W H : Type}
    (live : W → Prop) (menu : H → Prop) (better : W → H → H → Prop) (a : H) :
    Clear live menu better a ↔ menu a ∧ ¬ PossibleDefeat live menu better a := by
  constructor
  · rintro ⟨ha,h⟩
    refine ⟨ha, ?_⟩
    rintro ⟨w,hw,b,hb,defeat⟩
    exact (h w hw).2 b hb defeat
  · rintro ⟨ha,h⟩
    exact ⟨ha,fun w hw => ⟨ha,fun b hb defeat => h ⟨w,hw,b,hb,defeat⟩⟩⟩

/-- Exact characterization of one-way transport of represented certificates.
The reverse implication uses classical double-negation elimination. -/
theorem coverage_iff_certificate_transport {W V H : Type}
    (oldLive : W → Prop) (newLive : V → Prop) (menu : H → Prop)
    (oldBetter : W → H → H → Prop) (newBetter : V → H → H → Prop) :
    CertificateCoverage oldLive newLive menu oldBetter newBetter ↔
      ∀ a, Clear newLive menu newBetter a → Clear oldLive menu oldBetter a := by
  classical
  constructor
  · intro cover a h
    obtain ⟨ha,hn⟩ := (clear_iff_no_possible_defeat _ _ _ _).1 h
    exact (clear_iff_no_possible_defeat _ _ _ _).2
      ⟨ha,fun old => hn (cover a ha old)⟩
  · intro transport a ha old
    by_cases hn : PossibleDefeat newLive menu newBetter a
    · exact hn
    apply False.elim
    have clearNew := (clear_iff_no_possible_defeat _ _ _ _).2 ⟨ha,hn⟩
    exact ((clear_iff_no_possible_defeat _ _ _ _).1 (transport a clearNew)).2 old

/-- A stronger pairwise reflection is sufficient, but not demanded by the
certificate interface: both the representing review and defeating plan may vary. -/
theorem pairwise_reflection_suffices {W V H : Type}
    (oldLive : W → Prop) (newLive : V → Prop) (menu : H → Prop)
    (oldBetter : W → H → H → Prop) (newBetter : V → H → H → Prop)
    (reflect : ∀ a b, menu a → menu b →
      (∃ w, oldLive w ∧ oldBetter w b a) →
      ∃ v, newLive v ∧ newBetter v b a) :
    CertificateCoverage oldLive newLive menu oldBetter newBetter := by
  rintro a ha ⟨w,hw,b,hb,hba⟩
  obtain ⟨v,hv,hvba⟩ := reflect a b ha hb ⟨w,hw,hba⟩
  exact ⟨v,hv,b,hb,hvba⟩

theorem certificate_coverage_composes {W V X H : Type}
    (first : W → Prop) (second : V → Prop) (third : X → Prop)
    (menu : H → Prop) (r : W → H → H → Prop)
    (s : V → H → H → Prop) (t : X → H → H → Prop)
    (left : CertificateCoverage first second menu r s)
    (right : CertificateCoverage second third menu s t) :
    CertificateCoverage first third menu r t :=
  fun a ha h => right a ha (left a ha h)

/-- Universal certificate transport across menus requires preserving every
pairwise objection. New relations must exclude self-defeat: otherwise a spurious
self-loop could suppress every certificate without retaining the real challenger.
This ranges over a fixed plan domain and fixed interpreted comparison relations. -/
theorem all_menus_coverage_iff_pairwise_reflection {W V H : Type}
    (oldLive : W → Prop) (newLive : V → Prop)
    (oldBetter : W → H → H → Prop) (newBetter : V → H → H → Prop)
    (noSelf : ∀ v, newLive v → ∀ a, ¬ newBetter v a a) :
    (∀ menu, CertificateCoverage oldLive newLive menu oldBetter newBetter) ↔
      ∀ a b, (∃ w, oldLive w ∧ oldBetter w b a) →
        ∃ v, newLive v ∧ newBetter v b a := by
  constructor
  · intro all a b old
    let two : H → Prop := fun x => x = a ∨ x = b
    obtain ⟨w,hw,hba⟩ := old
    obtain ⟨v,hv,c,hc,hca⟩ := all two a (Or.inl rfl)
      ⟨w,hw,b,Or.inr rfl,hba⟩
    rcases hc with hc | hc
    · subst c
      exact False.elim (noSelf v hv a hca)
    · subst c
      exact ⟨v,hv,hca⟩
  · intro reflect menu
    exact pairwise_reflection_suffices oldLive newLive menu oldBetter newBetter
      (fun a b _ _ h => reflect a b h)

/-- An existential objection summary preserves precisely this certificate. It
is not a new whole application of J or necessarily a transitive preference. -/
def objectionSummary {W H : Type} (live : W → Prop)
    (better : W → H → H → Prop) (_ : Unit) (b a : H) : Prop :=
  ∃ w, live w ∧ better w b a

theorem objection_summary_preserves_exact_certificate {W H : Type}
    (live : W → Prop) (menu : H → Prop) (better : W → H → H → Prop) (a : H) :
    Clear (fun _ : Unit => True) menu (objectionSummary live better) a ↔
      Clear live menu better a := by
  constructor
  · rintro ⟨ha,h⟩
    exact ⟨ha,fun w hw => ⟨ha,fun b hb hba => (h () True.intro).2 b hb ⟨w,hw,hba⟩⟩⟩
  · rintro ⟨ha,h⟩
    refine ⟨ha,fun _ _ => ⟨ha,?_⟩⟩
    rintro b hb ⟨w,hw,hba⟩
    exact (h w hw).2 b hb hba

inductive Plan where
  | routine | output | repair
  deriving DecidableEq

/-- Two supported causal applications differ over the effective support route.
Before a repair plan is eligible, each assigns the same basic profile to routine
and output. Output has one further realization in either application. -/
def protection (application : Bool) (plan : Plan) (_ : Unit) : Prop :=
  if application then plan = .repair else plan ≠ .repair

def gain (plan : Plan) (_ : Unit) : Prop := plan = .output

def comparison (application : Bool) : Plan → Plan → Prop :=
  Better (protection application) gain

def fullLive (_ : Bool) : Prop := True

def oldMenu (plan : Plan) : Prop := plan ≠ .repair

def enlargedMenu (_ : Plan) : Prop := True

/-- Compression retains one application; its type has no copy of the other label. -/
def compressed (_ : Unit) : Plan → Plan → Prop := comparison false

theorem output_defeats_routine_in_both_applications (w : Bool) :
    comparison w .output .routine := by
  cases w <;> apply Or.inr <;> refine ⟨?_,?_,?_,?_⟩
  all_goals simp [Included,protection,gain]

/-- Nonvacuous old-menu equality: output defeats routine in both applications,
while no eligible plan defeats output. The missing review label is unnecessary
for this comparative certificate on this menu. -/
theorem compression_is_exact_on_old_menu (a : Plan) :
    Clear (fun _ : Unit => True) oldMenu compressed a ↔
      Clear fullLive oldMenu comparison a := by
  cases a with
  | repair => simp [Clear,oldMenu]
  | routine =>
    constructor
    · intro h
      exact False.elim ((h.2 () True.intro).2 .output (by simp [oldMenu])
        (output_defeats_routine_in_both_applications false))
    · intro h
      exact False.elim ((h.2 false True.intro).2 .output (by simp [oldMenu])
        (output_defeats_routine_in_both_applications false))
  | output =>
    have all : Clear fullLive oldMenu comparison .output := by
      refine ⟨by simp [oldMenu], fun w _ => ⟨by simp [oldMenu], ?_⟩⟩
      intro b hb h
      cases b with
      | repair => exact hb rfl
      | output => exact better_irrefl _ _ _ h
      | routine =>
        exact better_irrefl _ _ _ (better_trans _ _
          (output_defeats_routine_in_both_applications w) h)
    exact ⟨fun _ => all, fun _ => ⟨by simp [oldMenu],fun _ _ => all.2 false True.intro⟩⟩

theorem compressed_review_covers_old_menu :
    CertificateCoverage fullLive (fun _ : Unit => True) oldMenu comparison compressed :=
  (coverage_iff_certificate_transport _ _ _ _ _).2
    (fun a h => (compression_is_exact_on_old_menu a).1 h)

theorem expanded_menu_retains_compressed_output_certificate :
    Clear (fun _ : Unit => True) enlargedMenu compressed .output := by
  refine ⟨True.intro, fun _ _ => ⟨True.intro, ?_⟩⟩
  intro b _ h
  cases b with
  | output => exact better_irrefl _ _ _ h
  | routine => exact better_irrefl _ _ _ (better_trans _ _
      (output_defeats_routine_in_both_applications false) h)
  | repair =>
    exact no_protection_trade_by_count () (by simp [protection])
      (by simp [protection]) h

theorem new_repair_defeats_output_in_omitted_application :
    comparison true .repair .output := by
  apply protection_anchor (c := ())
  · intro _ h; simp [protection] at h
  · simp [protection]
  · simp [protection]

theorem menu_growth_breaks_old_certificate_coverage :
    ¬ CertificateCoverage fullLive (fun _ : Unit => True)
      enlargedMenu comparison compressed := by
  intro cover
  have h := (coverage_iff_certificate_transport _ _ _ _ _).1 cover .output
    expanded_menu_retains_compressed_output_certificate
  exact (h.2 true True.intro).2 .repair True.intro
    new_repair_defeats_output_in_omitted_application

theorem repair_keeps_real_output_loss :
    gain .output () ∧ ¬ gain .repair () ∧ comparison true .repair .output := by
  exact ⟨rfl,by simp [gain],new_repair_defeats_output_in_omitted_application⟩

/-- The compressed objection summary restores the correct negative certificate
without pretending the competing support applications have become one ranking. -/
theorem restored_summary_rejects_output_certificate :
    ¬ Clear (fun _ : Unit => True) enlargedMenu
      (objectionSummary fullLive comparison) .output := by
  intro h
  have full := (objection_summary_preserves_exact_certificate _ _ _ _).1 h
  exact (full.2 true True.intro).2 .repair True.intro
    new_repair_defeats_output_in_omitted_application

/-- Two admitted support laws: one preserves the basic condition at every
plan intensity; one preserves it only up to a supplied capacity n. Secondary
realizations are shared descriptions in both applications. These are constructed
correspondences, not measured living outcomes or a definition of life as output. -/
def prefixProtection (n : Nat) (application : Bool) (plan : Nat) (_ : Unit) : Prop :=
  if application then plan ≤ n else True

def prefixGain (plan : Nat) (i : Nat) : Prop := i < plan

def prefixComparison (n : Nat) (application : Bool) : Nat → Nat → Prop :=
  Better (prefixProtection n application) prefixGain

def prefixMenu (n : Nat) (plan : Nat) : Prop := plan ≤ n

def prefixCompressed (n : Nat) (_ : Unit) : Nat → Nat → Prop :=
  prefixComparison n false

/-- All complete represented protection profiles agree on the audited prefix;
the gain profile is already the same function in both applications. -/
theorem finite_audit_protection_profiles_agree (n a : Nat) (ha : a ≤ n) (i : Unit) :
    prefixProtection n true a i ↔ prefixProtection n false a i := by
  simp [prefixProtection,ha]

theorem prefix_pairwise_comparison (n a b : Nat) (w : Bool)
    (ha : a ≤ n) (hb : b ≤ n) :
    prefixComparison n w a b ↔ prefixComparison n false a b := by
  cases w <;>
    simp [prefixComparison,Better,StrictIncluded,Included,prefixProtection,ha,hb]

/-- For every audit length, compression is exact for every certificate in the
audited menu, not merely for one favored plan. -/
theorem every_finite_prefix_has_exact_compression (n a : Nat) :
    Clear (fun _ : Unit => True) (prefixMenu n) (prefixCompressed n) a ↔
      Clear fullLive (prefixMenu n) (prefixComparison n) a := by
  constructor
  · rintro ⟨ha,h⟩
    refine ⟨ha,fun w _ => ⟨ha,?_⟩⟩
    intro b hb hba
    exact (h () True.intro).2 b hb
      ((prefix_pairwise_comparison n b a w hb ha).1 hba)
  · rintro ⟨ha,h⟩
    exact ⟨ha,fun _ _ => h false True.intro⟩

/-- No amount of this finite-prefix success licenses extrapolation to the next
eligible plan. The next intensity adds a genuine secondary realization while
exceeding the omitted support capacity; n is superior under that application. -/
theorem every_finite_prefix_has_a_failing_next_plan (n : Nat) :
    Clear (fun _ : Unit => True) (prefixMenu (n+1)) (prefixCompressed n) (n+1) ∧
    PossibleDefeat fullLive (prefixMenu (n+1)) (prefixComparison n) (n+1) ∧
    prefixGain (n+1) n ∧ ¬ prefixGain n n := by
  have basic : prefixProtection n true n () := by simp [prefixProtection]
  have loss : ¬ prefixProtection n true (n+1) () := by simp [prefixProtection]
  have better : prefixComparison n true n (n+1) :=
    protection_anchor (fun _ h => False.elim (loss h)) () basic loss
  refine ⟨⟨by simp [prefixMenu],fun _ _ => ⟨by simp [prefixMenu],?_⟩⟩,
    ⟨true,True.intro,n,by simp [prefixMenu],better⟩,
    by simp [prefixGain],by simp [prefixGain]⟩
  intro b hb h
  rcases h with h | h
  · exact h.2 (fun _ _ => True.intro)
  · apply h.2.2.2
    intro i hi
    unfold prefixGain at *
    change b ≤ n+1 at hb
    omega

end SelectorReviewCoverage
