import Becoming.Frontier

/-!
# The practical commitments on a frame: the moves a step can make, compared and required

`Becoming.Lexical` and `Becoming.Frontier` state the practical commitments for alternatives of any
type: J1/J2 as the condition `BasicPriority` (the comparison is the lexical order of the basic
claims, then the gains), and J3/J4 as the frontier of a comparison among eligible alternatives
and what it requires. This module states them on a frame of the spine. The alternatives are the
configurations of a frame, compared by the contents they realize, and the eligible alternatives at
a configuration are the configurations one move of the frame's process reaches from it
(`Options`): what can be done is read off the unfolding, not supplied beside it. The commitments
stay conditions; nothing here asserts a comparison.

* **J1/J2 on a frame.** `better` meets the condition on a frame where it compares configurations
  as `Lexical.Frame.Above` does, by the basic claims they realize, then the living ones
  (`Priority`). The lexical order meets it (`Priority.above`); under it `better` is irreflexive
  and transitive (`Priority.irrefl`, `Priority.trans`); a configuration keeping every basic claim
  another realizes and realizing one it lacks is better, whatever the living claims
  (`Priority.anchor`), and no number of living claims makes a configuration losing a realized
  basic claim better (`Priority.no_trade`). A generative extension is never refuted to be better
  (`Priority.not_not_of_extension`), and the condition satisfies C wherever it is decided whether
  an extension adds a basic claim (`Priority.comparison`). Every two-tier condition is this one
  on its tier frame (`basicPriority_iff_priority`).
* **The choice at a step.** The chosen configurations at `s` are the options no option betters
  (`Frontier (Options F s) better`). An option bettered by another is not chosen
  (`excluded`). Where the options are listed and the comparison is weakly decided on them, J1/J2
  leave some option chosen (`Priority.choice_exists`); asked of every frame and every comparison
  irreflexive and transitive on the options, that some option is chosen is exactly weak excluded
  middle (`choice_exists_iff_weakly`): the choice is found by settling how the moves compare. A task required of the choice is performed
  by whichever option is chosen (`performed`), what every chosen option performing it performs is
  required (`means`), and where no move is possible nothing is required (`nothing_required`).
* **A kept basic claim is required.** Where one option keeps every basic claim any option
  realizes, a basic claim it realizes is never refuted at a chosen option, with no decision
  (`Priority.kept_unrefuted`), and is required of the choice where the options are listed, the
  comparison weakly decided and the claim decided on them (`Priority.kept_required`).
* **Fresh contents under every classification.** On a frame of old and newly distinguished
  contents (`Lexical.Frame.old`, `Lexical.Frame.fresh`), with the old ones split into basic and
  living and the fresh ones classified basic where `q` holds (`classifiedOn`): with none basic
  the comparison is that with the fresh contents as gains (`classifiedOn_none_iff`); a
  configuration is above another under every classification exactly where it keeps the other's
  fresh contents and is above with them as gains, the forward direction with no decision and the
  backward one where whether the other realizes each fresh content, and the tie at each
  classification, are decided (`classifiedOn_robust_iff_of_decided`), so wherever excluded middle
  is named (`classifiedOn_robust_iff_of_em`); the two extreme classifications suffice
  (`classifiedOn_extremes_iff_of_decided`). Where every option lacking a formation is bettered,
  with the fresh contents as gains, by an option keeping its fresh contents, the formation is
  required of the choice under every classification (`classifiedOn_required`).

Each theorem is the law of `Becoming.Lexical` or `Becoming.Frontier` it names, read on a frame;
none is a further result. Direction as in `Becoming.Lexical`: `better s t` says `s` is better.
No premise enters beyond what each theorem names; every declaration has an empty axiom report.
-/

namespace Becoming

open Generative Lexical Requirement

namespace FrontierFrames

variable {S A C : Type}

/-! ## J1/J2 on a frame -/

/-- **J1/J2 on a frame**: `better` compares the configurations of `F` as the lexical order of the
basic claims they realize, then the living ones. A condition; the core asserts it nowhere. -/
def Priority (F : Frame S A C) (basic living : C → Prop) (better : S → S → Prop) : Prop :=
  BasicPriority (fun s c => basic c ∧ F.realized s c) (fun s c => living c ∧ F.realized s c) better

variable {F : Frame S A C} {basic living : C → Prop} {better : S → S → Prop}

/-- The lexical order of what a frame realizes meets the condition. -/
theorem Priority.above : Priority F basic living (Lexical.Frame.Above F basic living) :=
  BasicPriority.above

/-- Under the condition, `better` is the lexical order of what the configurations realize. -/
theorem Priority.iff (priority : Priority F basic living better) (s t : S) :
    better s t ↔ Lexical.Frame.Above F basic living s t :=
  BasicPriority.iff priority s t

theorem Priority.irrefl (priority : Priority F basic living better) (s : S) : ¬ better s s :=
  BasicPriority.irrefl priority s

theorem Priority.trans (priority : Priority F basic living better) {s t u : S}
    (first : better s t) (second : better t u) : better s u :=
  BasicPriority.trans priority first second

/-- **A kept basic claim anchors the comparison**: a configuration realizing every basic claim `t`
realizes and a basic claim `t` lacks is better than `t`, whatever the living claims. -/
theorem Priority.anchor (priority : Priority F basic living better) {s t : S}
    (retain : ∀ c, basic c → F.realized t c → F.realized s c) (c : C) (isBasic : basic c)
    (restored : F.realized s c) (lost : ¬ F.realized t c) : better s t :=
  BasicPriority.anchor priority (fun c held => ⟨held.1, retain c held.1 held.2⟩) c
    ⟨isBasic, restored⟩ fun held => lost held.2

/-- **No number of living claims trades for a basic claim**: a configuration losing a basic claim
`t` realizes is not better than `t`. -/
theorem Priority.no_trade (priority : Priority F basic living better) {s t : S} (c : C)
    (isBasic : basic c) (held : F.realized t c) (lost : ¬ F.realized s c) : ¬ better s t :=
  BasicPriority.no_trade priority c ⟨isBasic, held⟩ fun realized => lost realized.2

/-- **A generative extension is never refuted to be better**, with no decision. -/
theorem Priority.not_not_of_extension (priority : Priority F basic living better) {s t : S}
    (extension : Extension F living s t) : ¬ ¬ better t s :=
  fun notBetter => Lexical.Frame.not_not_above_of_extension (basic' := basic) extension
    fun above => notBetter ((priority.iff t s).mpr above)

/-- **The condition satisfies C** wherever it is decided whether an extension adds a basic
claim. `Comparison`'s `Better s t` says `t` is better. -/
theorem Priority.comparison (priority : Priority F basic living better)
    (decided : ∀ s t, Decided (Included (fun c => basic c ∧ F.realized t c)
      (fun c => basic c ∧ F.realized s c))) :
    Comparison F living fun s t => better t s :=
  fun s t extension => (priority.iff t s).mpr (Lexical.Frame.comparison_of_decided decided s t extension)

/-- **Every two-tier condition is one on a frame**: its tier frame's. -/
theorem basicPriority_iff_priority {H C' G : Type} {basic : H → C' → Prop} {gain : H → G → Prop}
    {better : H → H → Prop} :
    BasicPriority basic gain better ↔ Priority (tierFrame basic gain) basicSide gainSide better :=
  ⟨fun priority => ⟨fun a b => (priority.iff a b).trans above_iff_frame⟩,
   fun priority => ⟨fun a b => (BasicPriority.iff priority a b).trans above_iff_frame.symm⟩⟩

/-! ## The choice at a step -/

/-- The options at `s`: the configurations one move of the frame's process reaches from `s`. -/
def Options (F : Frame S A C) (s : S) (t : S) : Prop := ∃ a, F.P.step s a t

/-- **An option another option betters is not chosen.** -/
theorem excluded {s t u : S} (option : Options F s u) (beats : better u t) :
    ¬ Frontier (Options F s) better t :=
  Frontier.excluded option beats

/-- **J1/J2 leave some option chosen** where the options from `s` are listed and whether one
betters another is weakly decided on them. -/
theorem Priority.choice_exists (priority : Priority F basic living better) {s : S} (x : S)
    (rest : List S) (exact : ∀ t, Options F s t ↔ t ∈ x :: rest)
    (weakly : ∀ t u, Options F s t → Options F s u → WeaklyDecided (better t u)) :
    ∃ t, Frontier (Options F s) better t :=
  frontier_exists x rest exact weakly priority.irrefl fun first second => priority.trans first second

/-- **A choice at every step is weak excluded middle.** That at every configuration of every frame
whose options are listed, every comparison irreflexive and transitive on the options leaves some
option chosen holds exactly where every proposition is weakly decided, its failure decided or
refuted. Where whether one move betters another is an open question, a step need leave no move
known to be chosen: the choice is found by settling, up to double negation, how the moves
compare. -/
theorem choice_exists_iff_weakly :
    (∀ (S A C : Type) (F : Frame S A C) (better : S → S → Prop) (s x : S) (rest : List S),
        (∀ t, Options F s t ↔ t ∈ x :: rest) →
        (∀ t, Options F s t → ¬ better t t) →
        (∀ t u v, Options F s t → Options F s u → Options F s v → better t u → better u v →
          better t v) →
        ∃ t, Frontier (Options F s) better t) ↔ ∀ p : Prop, WeaklyDecided p :=
  ⟨fun choice => exists_undominated_iff_weakly.mp fun β better x rest irreflexive transitive =>
    have exact : ∀ t, Options (⟨⟨fun _ _ t => t ∈ x :: rest⟩, fun _ _ => True⟩ : Frame β Unit Unit) x t ↔
        t ∈ x :: rest :=
      fun _ => ⟨fun ⟨_, mem⟩ => mem, fun mem => ⟨(), mem⟩⟩
    match choice β Unit Unit ⟨⟨fun _ _ t => t ∈ x :: rest⟩, fun _ _ => True⟩ better x x rest exact
        (fun t option => irreflexive t ((exact t).mp option))
        (fun t u v ot ou ov => transitive t u v ((exact t).mp ot) ((exact u).mp ou) ((exact v).mp ov)) with
    | ⟨t, chosen⟩ => ⟨t, (frontier_iff_undominated exact).mp chosen⟩,
   fun weakly _ _ _ _ _ _ x rest exact irreflexive transitive =>
    match exists_undominated x rest (fun _ _ _ _ => weakly _)
        (fun t mem => irreflexive t ((exact t).mpr mem))
        (fun t u v mt mu mv => transitive t u v ((exact t).mpr mt) ((exact u).mpr mu) ((exact v).mpr mv)) with
    | ⟨t, undominated⟩ => ⟨t, (frontier_iff_undominated exact).mpr undominated⟩⟩

/-- **A task required of the choice is performed by whichever option is chosen.** -/
theorem performed {s t : S} {task : S → Prop} (required : Required (Frontier (Options F s) better) task)
    (chosen : Frontier (Options F s) better t) : task t :=
  Required.performed required chosen

/-- **What every chosen option performing a required task performs is required.** -/
theorem means {s : S} {task means : S → Prop}
    (required : Required (Frontier (Options F s) better) task)
    (law : ∀ t, Frontier (Options F s) better t → task t → means t) :
    Required (Frontier (Options F s) better) means :=
  Required.means required law

/-- **Where no move is possible, nothing is required.** -/
theorem nothing_required {s : S} {task : S → Prop} (stuck : ∀ a t, ¬ F.P.step s a t) :
    ¬ Required (Frontier (Options F s) better) task :=
  Required.impossible fun t chosen => match chosen.1 with
    | ⟨a, step⟩ => stuck a t step

/-- **A kept basic claim is never refuted at a chosen option**: where option `u` realizes every
basic claim any option realizes, a basic claim `u` realizes is not refuted at any chosen option.
No decision is used. -/
theorem Priority.kept_unrefuted (priority : Priority F basic living better) {s u t : S}
    (option : Options F s u) (keeps : ∀ t c, Options F s t → basic c → F.realized t c → F.realized u c)
    {c : C} (isBasic : basic c) (realizes : F.realized u c)
    (chosen : Frontier (Options F s) better t) : ¬ ¬ F.realized t c :=
  fun lacks => chosen.2 u option
    (priority.anchor (fun c' basicC held => keeps t c' chosen.1 basicC held) c isBasic realizes lacks)

/-- **A kept basic claim is required of the choice**: where option `u` realizes every basic claim
any option realizes, a basic claim `u` realizes is required of the choice, the options listed,
the comparison weakly decided and the claim decided on them. -/
theorem Priority.kept_required (priority : Priority F basic living better) {s u : S} (x : S)
    (rest : List S) (exact : ∀ t, Options F s t ↔ t ∈ x :: rest)
    (weakly : ∀ t t', Options F s t → Options F s t' → WeaklyDecided (better t t'))
    (option : Options F s u) (keeps : ∀ t c, Options F s t → basic c → F.realized t c → F.realized u c)
    {c : C} (isBasic : basic c) (realizes : F.realized u c)
    (decided : ∀ t, Options F s t → Decided (F.realized t c)) :
    Required (Frontier (Options F s) better) fun t => F.realized t c :=
  required_of_bettered x rest exact weakly priority.irrefl
    (fun first second => priority.trans first second) decided
    fun t opt lacks => ⟨u, option,
      priority.anchor (fun c' basicC held => keeps t c' opt basicC held) c isBasic realizes lacks⟩

/-! ## Fresh contents under every classification -/

section Classified

variable {I J : Type}

/-- The lexical order on a frame of old and fresh contents, the old ones split by `basic` and
`living`, the fresh ones classified basic where `q` holds. -/
def classifiedOn (F : Frame S A (Sum I J)) (basic living : I → Prop) (q : J → Prop) :
    S → S → Prop :=
  classified (fun s i => basic i ∧ Lexical.Frame.old F s i) (fun s i => living i ∧ Lexical.Frame.old F s i)
    (Lexical.Frame.fresh F) q

variable {F : Frame S A (Sum I J)} {basic living : I → Prop} {a b : S}

/-- **With no fresh content basic, the comparison is the one with the fresh contents as gains.** -/
theorem classifiedOn_none_iff :
    classifiedOn F basic living (fun _ => False) a b ↔
      Lexical.Above (fun s i => basic i ∧ Lexical.Frame.old F s i)
        (Lexical.adjoin (fun s i => living i ∧ Lexical.Frame.old F s i) (Lexical.Frame.fresh F)) a b :=
  classified_none_iff

/-- **The criterion under every classification on a frame**: above under every classification
exactly where the fresh contents of `b` are kept and `a` is above with them as gains, where whether
`b` realizes each fresh content, and the tie at each classification, are decided. -/
theorem classifiedOn_robust_iff_of_decided (held : ∀ j, Decided (Lexical.Frame.fresh F b j))
    (tie : ∀ q : J → Prop, Decided (∀ j, Lexical.Frame.fresh F a j → q j → Lexical.Frame.fresh F b j)) :
    (∀ q, classifiedOn F basic living q a b) ↔
      Included (Lexical.Frame.fresh F b) (Lexical.Frame.fresh F a) ∧
        Lexical.Above (fun s i => basic i ∧ Lexical.Frame.old F s i)
          (Lexical.adjoin (fun s i => living i ∧ Lexical.Frame.old F s i) (Lexical.Frame.fresh F)) a b :=
  classified_robust_iff_of_decided held tie

/-- **The criterion on a frame with excluded middle named.** -/
theorem classifiedOn_robust_iff_of_em (em : ∀ r : Prop, Decided r) :
    (∀ q, classifiedOn F basic living q a b) ↔
      Included (Lexical.Frame.fresh F b) (Lexical.Frame.fresh F a) ∧
        Lexical.Above (fun s i => basic i ∧ Lexical.Frame.old F s i)
          (Lexical.adjoin (fun s i => living i ∧ Lexical.Frame.old F s i) (Lexical.Frame.fresh F)) a b :=
  classified_robust_iff_of_em em

/-- **Two extreme classifications suffice on a frame**, with the same decisions. -/
theorem classifiedOn_extremes_iff_of_decided (held : ∀ j, Decided (Lexical.Frame.fresh F b j))
    (tie : ∀ q : J → Prop, Decided (∀ j, Lexical.Frame.fresh F a j → q j → Lexical.Frame.fresh F b j)) :
    (∀ q, classifiedOn F basic living q a b) ↔
      classifiedOn F basic living (fun _ => False) a b ∧ classifiedOn F basic living (fun _ => True) a b :=
  classified_extremes_iff_of_decided held tie

/-- **Formation required of the choice under every classification**: where every option lacking
the formation is bettered, with the fresh contents as gains, by an option keeping its fresh
contents, the formation is required of the choice at `s` under every classification, the options
listed, the comparisons weakly decided, the formation decided and the decisions of the criterion
named. -/
theorem classifiedOn_required {s : S} {formed : S → Prop} (x : S) (rest : List S)
    (exact : ∀ t, Options F s t ↔ t ∈ x :: rest)
    (weakly : ∀ (q : J → Prop) t u, Options F s t → Options F s u →
      WeaklyDecided (classifiedOn F basic living q t u))
    (decidedFormed : ∀ t, Options F s t → Decided (formed t))
    (held : ∀ t j, Options F s t → Decided (Lexical.Frame.fresh F t j))
    (tie : ∀ (q : J → Prop) t u, Options F s t → Options F s u →
      Decided (∀ j, Lexical.Frame.fresh F t j → q j → Lexical.Frame.fresh F u j))
    (construction : ∀ t, Options F s t → ¬ formed t →
      ∃ u, Options F s u ∧ Included (Lexical.Frame.fresh F t) (Lexical.Frame.fresh F u) ∧
        Lexical.Above (fun s i => basic i ∧ Lexical.Frame.old F s i)
          (Lexical.adjoin (fun s i => living i ∧ Lexical.Frame.old F s i) (Lexical.Frame.fresh F)) u t) :
    ∀ q, Required (Frontier (Options F s) (classifiedOn F basic living q)) formed :=
  required_under_every_classification x rest exact weakly decidedFormed held tie construction

end Classified

end FrontierFrames

end Becoming
