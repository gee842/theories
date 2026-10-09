import Becoming.Population

/-!
# Identity across steps

A web names its formations by a fixed index type, so which formation at one step is the
same as which at the next is stipulated by the names. The relations at each step do not
fix it. A *re-identification* (`Reidentify`) relates two namings one to one at each
step. The re-identified web (`Web.reidentify`) has, at every step, the same levels,
activity, dependences and drawing; it differs only in which formation of one step
continues which of the step before. A *renaming* is a re-identification that is the same
at every step. Splits and merges, which change how many formations there are, are not
re-identifications.

Results:
* Names carry nothing. A renaming preserves the readings that follow a formation
  through the run: the class of a formation (renewing or consuming in the run), the
  tenure of a dependence (`MetAbove`), undermining, forming and dissolving, arising and
  unceasing generation.
* What each step and each condition is does not depend on identity across steps. Every
  re-identification preserves support, keeping and breaking, the class of every
  condition (renewed, consumed, lost), whether activity needs support (`Dependent`),
  and, at each event, being within renewal and breaking. Consumption reads a dependence
  as it stood when it held, against the condition's later levels; it does not follow the
  formation. Re-identifying a flow preserves what is taken and given at each step, the
  balance of depletion and replenishment, and how many formations take and give, so
  whether generation is more without end (`More`). A census of the active formations and
  `Taking` carry over too, so under them more without end makes generation unceasing
  under every re-identification (`More.unceasing_reidentified`): the arising it forces
  is not an artefact of naming.
* What a formation is across steps depends on it (`Turnover`). Exchanging names at
  every odd step, with every step's relations unchanged:
  - a formation renewing in the run and one consuming become a web in which no
    formation renews and two consume;
  - a drawer that undermines at every step, because the formation whose need it broke
    still needs the condition, gives way to a web in which no event after the first
    step undermines: each formation needing the condition now has a tenure of one
    step, and its need was never met in it;
  - a web in which no dependence forms or dissolves and nothing arises becomes one in
    which a formation transforms its dependence across a step and formations arise at
    every odd step, so that generation is unceasing. These arisings lower no
    condition: `Depletes` fails, and `Unceasing.rises` does not apply.
* Continuity constrains what is left. A re-identification that keeps the name of every
  formation active before and after a step (`KeepsActive`) makes no arising: what
  arises under the new names arose under the old, so it makes no unceasing generation.
  One that keeps the name of every formation whose dependence on a condition continues
  across a step (`KeepsTenure`) keeps a formation's name over a tenure, keeps every
  dependence met while it held, and removes no undermining. Such a re-identification
  can still join a formation that ends at a step with one that begins there: whether
  the one that begins continues the one that ends is succession. Joining them can hide
  arising and add undermining:
  - two members of a lineage active at alternate steps arise without end when named
    apart, and named as one the lineage is always active and nothing arises
    (`Lineage`);
  - an heir that needs the pool from the step at which the elder's need ends was never
    met while it held, so drawing after the elder's loss undermines nothing when the two
    are named apart, and undermines at every step when the heir succeeds the elder
    (`Succession`).
  Both namings in each witness keep every continuing activity and dependence.

So identity across steps is substantive exactly where a reading follows a formation or
one of its dependences through time: the class of a formation over the run, the tenure
of a dependence, hence undermining and the working stepwise reading of `living`,
transformation as against an ending and another forming, and arising, hence `Unceasing`.
Continuity of activity and dependence rules out making arising and removing undermining,
and leaves succession open: whether a lineage is one formation continuing or many
generated, and whether an heir inherits a loss, is a further reading. Where generation is
more without end under a census, it is unceasing under every reading of identity. The
representation supplies identity through the index type; for an application it is a
correspondence claim. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {F F' C : Type}

/-- Two namings of formations related one to one at each step: at step `t`, the
formation named `x` is the one named `old t x` before, and `new t f` names `f`. -/
structure Reidentify (F F' : Type) where
  old : Nat → F' → F
  new : Nat → F → F'
  old_new : ∀ t f, old t (new t f) = f
  new_old : ∀ t x, new t (old t x) = x

/-- A renaming: the same correspondence at every step. -/
def Reidentify.rename (old : F' → F) (new : F → F') (old_new : ∀ f, old (new f) = f)
    (new_old : ∀ x, new (old x) = x) : Reidentify F F' :=
  ⟨fun _ => old, fun _ => new, fun _ => old_new, fun _ => new_old⟩

/-- What holds of every formation as named at a step holds of every formation. -/
theorem Reidentify.every (σ : Reidentify F F') (t : Nat) {p : F → Prop}
    (named : ∀ x, p (σ.old t x)) : ∀ f, p f :=
  fun f => σ.old_new t f ▸ named (σ.new t f)

/-- At each step, the new names name distinct formations distinctly. -/
theorem Reidentify.new_injective (σ : Reidentify F F') (t : Nat) :
    ∀ f g, σ.new t f = σ.new t g → f = g :=
  fun f g same => (σ.old_new t f).symm.trans ((congrArg (σ.old t) same).trans (σ.old_new t g))

/-- What holds of some formation holds of one as named at a step. -/
theorem Reidentify.some (σ : Reidentify F F') (t : Nat) {p : F → Prop} :
    (∃ f, p f) → ∃ x, p (σ.old t x)
  | ⟨f, holds⟩ => ⟨σ.new t f, (σ.old_new t f).symm ▸ holds⟩

namespace Web

/-- The same web with its formations re-identified across steps: every step's levels,
activity, dependences and drawing are unchanged. -/
def reidentify (W : Web F C) (σ : Reidentify F F') : Web F' C where
  level := W.level
  active t x := W.active t (σ.old t x)
  requires t x := W.requires t (σ.old t x)
  need t x := W.need t (σ.old t x)
  draws t x := W.draws t (σ.old t x)

variable (W : Web F C) (σ : Reidentify F F')

/-! ## What each step and each condition is -/

/-- Each step's relations are unchanged: support, keeping and breaking. -/
theorem reidentify_step (t : Nat) (x : F') (c : C) :
    ((W.reidentify σ).Supported t x ↔ W.Supported t (σ.old t x)) ∧
    ((W.reidentify σ).Kept t x c ↔ W.Kept t (σ.old t x) c) ∧
    ((W.reidentify σ).Broken t x c ↔ W.Broken t (σ.old t x) c) :=
  ⟨.rfl, .rfl, .rfl⟩

theorem reidentify_renewed (c : C) : (W.reidentify σ).Renewed c ↔ W.Renewed c :=
  ⟨fun renewed t => σ.every t (p := fun g => W.requires t g c → W.Kept t g c) (renewed t),
   fun renewed t x => renewed t (σ.old t x)⟩

theorem reidentify_consumed (c : C) : (W.reidentify σ).Consumed c ↔ W.Consumed c :=
  ⟨fun ⟨x, T, unmet⟩ => ⟨σ.old T x, T, unmet⟩,
   fun ⟨g, T, unmet⟩ => match σ.some T (p := fun g =>
      W.requires T g c ∧ ∀ t, T < t → W.level t c < W.need T g c) ⟨g, unmet⟩ with
    | ⟨x, unmet⟩ => ⟨x, T, unmet⟩⟩

theorem reidentify_lost (c : C) : (W.reidentify σ).Lost c ↔ W.Lost c :=
  ⟨fun ⟨x, T, lost⟩ => ⟨σ.old T x, T, lost⟩,
   fun ⟨g, T, lost⟩ => match σ.some T (p := fun g =>
      W.Broken T g c ∧ ∀ t, T < t → W.level t c < W.need T g c) ⟨g, lost⟩ with
    | ⟨x, lost⟩ => ⟨x, T, lost⟩⟩

theorem reidentify_dependent : (W.reidentify σ).Dependent ↔ W.Dependent :=
  ⟨fun dependent t => σ.every t (p := fun f => W.active t f → W.Supported t f) (dependent t),
   fun dependent t x => dependent t (σ.old t x)⟩

/-- At each event, being within renewal is unchanged. -/
theorem reidentify_renewingAt (t : Nat) (x : F') :
    (W.reidentify σ).RenewingAt t x ↔ W.RenewingAt t (σ.old t x) :=
  ⟨fun ⟨active, keeps⟩ => ⟨active, fun c joins =>
    σ.every t (p := fun g => W.requires t g c → W.Kept t g c) (keeps c joins)⟩,
   fun ⟨active, keeps⟩ => ⟨active, fun c joins y depends => keeps c joins (σ.old t y) depends⟩⟩

/-- At each event, breaking is unchanged. -/
theorem reidentify_breakingOn (t : Nat) (x : F') (c : C) :
    (W.reidentify σ).BreakingOn t x c ↔ W.BreakingOn t (σ.old t x) c :=
  ⟨fun ⟨drawn, y, broken⟩ => ⟨drawn, σ.old t y, broken⟩,
   fun ⟨drawn, broken⟩ => ⟨drawn, σ.some t (p := fun g => W.Broken t g c) broken⟩⟩

/-! ## Names carry nothing -/

section Renaming

variable (old : F' → F) (new : F → F') (old_new : ∀ f, old (new f) = f)
  (new_old : ∀ x, new (old x) = x)

theorem rename_renewingIn (x : F') :
    (W.reidentify (.rename old new old_new new_old)).RenewingIn x ↔ W.RenewingIn (old x) :=
  ⟨fun renewing t c joins => (W.reidentify_renewed _ c).mp (renewing t c joins),
   fun renewing t c joins => (W.reidentify_renewed _ c).mpr (renewing t c joins)⟩

theorem rename_consumingIn (x : F') :
    (W.reidentify (.rename old new old_new new_old)).ConsumingIn x ↔ W.ConsumingIn (old x) :=
  ⟨fun ⟨t, c, drawn, consumed⟩ => ⟨t, c, drawn, (W.reidentify_consumed _ c).mp consumed⟩,
   fun ⟨t, c, drawn, consumed⟩ => ⟨t, c, drawn, (W.reidentify_consumed _ c).mpr consumed⟩⟩

/-- A renaming keeps every tenure, forming and dissolving, and arising. -/
theorem rename_tenure (t : Nat) (x : F') (c : C) (m : Nat) :
    ((W.reidentify (.rename old new old_new new_old)).MetAbove t x c m ↔
      W.MetAbove t (old x) c m) ∧
    ((W.reidentify (.rename old new old_new new_old)).Forms t x c ↔ W.Forms t (old x) c) ∧
    ((W.reidentify (.rename old new old_new new_old)).Dissolves t x c ↔
      W.Dissolves t (old x) c) ∧
    ((W.reidentify (.rename old new old_new new_old)).Arises t x ↔ W.Arises t (old x)) :=
  ⟨.rfl, .rfl, .rfl, .rfl⟩

theorem rename_undermining (t : Nat) (x : F') :
    (W.reidentify (.rename old new old_new new_old)).UnderminingAt t x ↔
      W.UnderminingAt t (old x) :=
  ⟨fun ⟨c, drawn, y, depends, met, fell⟩ => ⟨c, drawn, old y, depends, met, fell⟩,
   fun ⟨c, drawn, undermined⟩ => ⟨c, drawn, (Reidentify.rename old new old_new new_old).some t
    (p := fun g => W.requires t g c ∧ W.MetAbove t g c (W.level (t + 1) c) ∧
      W.level (t + 1) c < W.need t g c)
    undermined⟩⟩

theorem rename_unceasing :
    (W.reidentify (.rename old new old_new new_old)).Unceasing ↔ W.Unceasing :=
  ⟨fun unceasing N => match unceasing N with
    | ⟨t, x, later, arises⟩ => ⟨t, old x, later, arises⟩,
   fun unceasing N => match unceasing N with
    | ⟨t, f, later, arises⟩ =>
      match (Reidentify.rename old new old_new new_old).some t (p := W.Arises t) ⟨f, arises⟩ with
      | ⟨x, arises⟩ => ⟨t, x, later, arises⟩⟩

end Renaming

end Web

/-! ## Flows and censuses -/

section Lists

variable {α β : Type} {g : α → β}

theorem mem_map_of {a : α} : ∀ {l : List α}, a ∈ l → g a ∈ l.map g
  | _ :: _, .head _ => .head _
  | _ :: _, .tail _ mem => .tail _ (mem_map_of mem)

theorem mem_of_map (inj : ∀ a b, g a = g b → a = b) {a : α} :
    ∀ {l : List α}, g a ∈ l.map g → a ∈ l
  | [], mem => nomatch mem
  | b :: _, mem => match mem_cons_cases mem with
    | .inl same => Eq.subst (motive := fun x => x ∈ b :: _) (inj a b same).symm (.head _)
    | .inr mem => .tail b (mem_of_map inj mem)

/-- Mapping a list one to one keeps it without repetition. -/
theorem distinct_map (inj : ∀ a b, g a = g b → a = b) :
    ∀ {l : List α}, Distinct l → Distinct (l.map g)
  | [], _ => trivial
  | _ :: _, ⟨fresh, distinct⟩ => ⟨fun mem => fresh (mem_of_map inj mem), distinct_map inj distinct⟩

end Lists

/-- What is listed under the new names at a step is what is listed under the old. -/
theorem Reidentify.mem_map (σ : Reidentify F F') (t : Nat) {l : List F} {x : F'} :
    x ∈ l.map (σ.new t) ↔ σ.old t x ∈ l :=
  ⟨fun mem => mem_of_map (σ.new_injective t)
    (Eq.subst (motive := fun y => y ∈ l.map (σ.new t)) (σ.new_old t x).symm mem),
   fun mem => Eq.subst (motive := fun y => y ∈ l.map (σ.new t)) (σ.new_old t x)
    (mem_map_of mem)⟩

/-- A census of the active formations lists them under any re-identification. -/
theorem Web.Census.reidentify {W : Web F C} {alive : Nat → List F} (census : W.Census alive)
    (σ : Reidentify F F') : (W.reidentify σ).Census fun t => (alive t).map (σ.new t) :=
  fun t => ⟨distinct_map (σ.new_injective t) (census t).1, fun x =>
    ((census t).2 (σ.old t x)).trans (σ.mem_map t).symm⟩

/-- A total over the renamed list is the total over the list. -/
theorem total_reidentify (σ : Reidentify F F') (t : Nat) (q : F → Nat) :
    ∀ fs : List F, total (fs.map (σ.new t)) (fun x => q (σ.old t x)) = total fs q
  | [] => rfl
  | f :: fs => congr (congrArg (· + ·) (congrArg q (σ.old_new t f))) (total_reidentify σ t q fs)

namespace Flow

/-- The same flow with its formations re-identified across steps. -/
def reidentify (L : Flow F C) (σ : Reidentify F F') : Flow F' C where
  present t := (L.present t).map (σ.new t)
  take t x := L.take t (σ.old t x)
  give t x := L.give t (σ.old t x)

variable (L : Flow F C) (σ : Reidentify F F')

/-- What is taken from and given to each condition at each step is unchanged. -/
theorem reidentify_amounts (t : Nat) (c : C) :
    (L.reidentify σ).taken t c = L.taken t c ∧ (L.reidentify σ).given t c = L.given t c :=
  ⟨total_reidentify σ t (fun f => L.take t f c) (L.present t),
   total_reidentify σ t (fun f => L.give t f c) (L.present t)⟩

theorem reidentify_balances (W : Web F C) :
    (L.reidentify σ).Balances (W.reidentify σ) ↔ L.Balances W :=
  ⟨fun balances t c =>
    (L.reidentify_amounts σ t c).1 ▸ (L.reidentify_amounts σ t c).2 ▸ balances t c,
   fun balances t c =>
    (L.reidentify_amounts σ t c).1.symm ▸ (L.reidentify_amounts σ t c).2.symm ▸ balances t c⟩

/-- How many formations take and give at each step is unchanged. -/
theorem reidentify_counts (cs : List C) (t : Nat) :
    (L.reidentify σ).takers cs t = L.takers cs t ∧
      (L.reidentify σ).renewers cs t = L.renewers cs t :=
  ⟨total_reidentify σ t (fun f => sign (total cs (L.take t f))) (L.present t),
   total_reidentify σ t (fun f => sign (total cs (L.give t f))) (L.present t)⟩

/-- Only active formations take, from what they draw on, under any re-identification. -/
theorem Taking.reidentify {L : Flow F C} {W : Web F C} (taking : L.Taking W)
    (σ : Reidentify F F') : (L.reidentify σ).Taking (W.reidentify σ) :=
  fun t x c mem positive => taking t (σ.old t x) c ((σ.mem_map t).mp mem) positive

theorem reidentify_more (cs : List C) : (L.reidentify σ).More cs ↔ L.More cs :=
  ⟨fun more K => match more K with
    | ⟨T, many⟩ => ⟨T, fun t later => (L.reidentify_counts σ cs t).1 ▸ many t later⟩,
   fun more K => match more K with
    | ⟨T, many⟩ => ⟨T, fun t later => (L.reidentify_counts σ cs t).1.symm ▸ many t later⟩⟩

end Flow

/-- Under a census, with each formation taking part listed once and only active formations
taking, more without end makes generation unceasing under every re-identification. -/
theorem Flow.More.unceasing_reidentified {W : Web F C} [decide : ∀ t f, Decidable (W.active t f)]
    {L : Flow F C} {cs : List C} {alive : Nat → List F} (census : W.Census alive)
    (distinct : ∀ t, Distinct (L.present t)) (taking : L.Taking W) (more : L.More cs)
    (σ : Reidentify F F') : (W.reidentify σ).Unceasing :=
  have : ∀ t x, Decidable ((W.reidentify σ).active t x) := fun t x => decide t (σ.old t x)
  Flow.More.unceasing (census.reidentify σ)
    (fun t => distinct_map (σ.new_injective t) (distinct t)) (taking.reidentify σ)
    ((L.reidentify_more σ cs).mpr more)

/-! ## Continuity leaves succession open -/

namespace Reidentify

variable (σ : Reidentify F F') (W : Web F C)

/-- The re-identification keeps the name of every formation active before and after a
step. -/
def KeepsActive : Prop :=
  ∀ t f, W.active t f → W.active (t + 1) f → σ.new (t + 1) f = σ.new t f

/-- The re-identification keeps the name of every formation whose dependence on a
condition holds before and after a step. -/
def KeepsTenure : Prop :=
  ∀ t g c, W.requires t g c → W.requires (t + 1) g c → σ.new (t + 1) g = σ.new t g

variable {σ W}

/-- Keeping continuing dependences, a formation keeps one name over a tenure. -/
theorem steady (keeps : σ.KeepsTenure W) {g : F} {c : C} {s : Nat} :
    ∀ {t}, (∀ u, s ≤ u → u ≤ t → W.requires u g c) →
      ∀ u, s ≤ u → u ≤ t → σ.new u g = σ.new t g
  | 0, _, u, _, le => congrArg (σ.new · g) (Nat.le_antisymm le (Nat.zero_le u))
  | t + 1, held, u, from_, le => match Nat.lt_or_ge u (t + 1) with
    | .inl below =>
      have within : u ≤ t := Nat.le_of_lt_succ below
      (steady keeps (fun v a b => held v a (Nat.le_succ_of_le b)) u from_ within).trans
        (keeps t g c (held t (Nat.le_trans from_ within) (Nat.le_succ t))
          (held (t + 1) (Nat.le_trans from_ (Nat.le_succ_of_le within)) (Nat.le_refl _))).symm
    | .inr above => congrArg (σ.new · g) (Nat.le_antisymm le above)

end Reidentify

namespace Web

variable {W : Web F C} {σ : Reidentify F F'}

/-- Keeping continuing activity, a re-identification makes no arising: what arises under
the new names arose under the old. -/
theorem arises_of_keepsActive (keeps : σ.KeepsActive W) {t : Nat} {x : F'}
    (arises : (W.reidentify σ).Arises t x) : W.Arises t (σ.old (t + 1) x) :=
  ⟨fun active =>
    have named : σ.new t (σ.old (t + 1) x) = x :=
      (keeps t _ active arises.2).symm.trans (σ.new_old (t + 1) x)
    arises.1 (Eq.subst (motive := fun f => W.active t f)
      ((σ.old_new t _).symm.trans (congrArg (σ.old t) named)) active),
   arises.2⟩

theorem unceasing_of_keepsActive (keeps : σ.KeepsActive W)
    (unceasing : (W.reidentify σ).Unceasing) : W.Unceasing :=
  fun N => match unceasing N with
    | ⟨t, _, later, arises⟩ => ⟨t, _, later, arises_of_keepsActive keeps arises⟩

/-- Keeping continuing dependences, a dependence met above `m` while it held is met above
`m` while it held under the new names. -/
theorem metAbove_of_keepsTenure (keeps : σ.KeepsTenure W) {t : Nat} {g : F} {c : C} {m : Nat} :
    W.MetAbove t g c m → (W.reidentify σ).MetAbove t (σ.new t g) c m
  | ⟨s, le, held, met, above⟩ =>
    have same : ∀ u, s ≤ u → u ≤ t → g = σ.old u (σ.new t g) := fun u a b =>
      (σ.old_new u g).symm.trans (congrArg (σ.old u) (Reidentify.steady keeps held u a b))
    ⟨s, le, fun u a b => Eq.subst (motive := fun f => W.requires u f c) (same u a b) (held u a b),
     Eq.subst (motive := fun f => W.need s f c ≤ W.level s c) (same s (Nat.le_refl s) le) met,
     Eq.subst (motive := fun f => m < W.need s f c) (same s (Nat.le_refl s) le) above⟩

/-- Keeping continuing dependences, a re-identification removes no undermining. -/
theorem undermining_of_keepsTenure (keeps : σ.KeepsTenure W) {t : Nat} {f : F} :
    W.UnderminingAt t f → (W.reidentify σ).UnderminingAt t (σ.new t f)
  | ⟨c, drawn, g, depends, met, fell⟩ =>
    ⟨c, Eq.subst (motive := fun f => W.draws t f c) (σ.old_new t f).symm drawn, σ.new t g,
      Eq.subst (motive := fun g => W.requires t g c) (σ.old_new t g).symm depends,
      metAbove_of_keepsTenure keeps met,
      Eq.subst (motive := fun g => W.level (t + 1) c < W.need t g c) (σ.old_new t g).symm fell⟩

end Web

/-! ## Witnesses -/

/-- Whether a step is odd. -/
def odd : Nat → Bool
  | 0 => false
  | t + 1 => !odd t

namespace Turnover

/-- A pool and a spring. -/
inductive Condition where
  | pool
  | spring

/-- A drawer on the pool, a keeper of the spring, a formation that needs the pool, and an
idle one. -/
inductive Formation where
  | drawer
  | keeper
  | needy
  | idle

/-- The pool holds two units and falls to one. -/
def pool : Nat → Nat
  | 0 => 2
  | _ + 1 => 1

/-- The drawer draws the pool. The keeper needs one unit of the spring and draws it. The
needy formation needs two units of the pool and is active at the first step only, while
the pool supports it. The idle formation does nothing. -/
def web : Web Formation Condition where
  level t c := match c with
    | .pool => pool t
    | .spring => 1
  active t f := match f with
    | .drawer | .keeper => True
    | .needy => t = 0
    | .idle => False
  requires _ f c := match f with
    | .keeper => c = .spring
    | .needy => c = .pool
    | .drawer | .idle => False
  need _ f _ := match f with
    | .keeper => 1
    | .needy => 2
    | .drawer | .idle => 0
  draws _ f c := match f with
    | .drawer => c = .pool
    | .keeper => c = .spring
    | .needy | .idle => False

/-- Exchange the drawer with the idle formation and the keeper with the needy one. -/
def swap : Formation → Formation
  | .drawer => .idle
  | .idle => .drawer
  | .keeper => .needy
  | .needy => .keeper

/-- Exchange at odd steps. -/
def turn : Bool → Formation → Formation
  | true, f => swap f
  | false, f => f

theorem turn_turn : ∀ b f, turn b (turn b f) = f
  | true, .drawer | true, .keeper | true, .needy | true, .idle => rfl
  | false, _ => rfl

/-- At every odd step, the drawer and the idle formation exchange names, and so do the
keeper and the needy formation. -/
def exchange : Reidentify Formation Formation :=
  ⟨fun t => turn (odd t), fun t => turn (odd t), fun t => turn_turn (odd t),
    fun t => turn_turn (odd t)⟩

/-- The re-identified web. -/
abbrev turned : Web Formation Condition := web.reidentify exchange

theorem pool_late : ∀ {t}, 1 ≤ t → pool t = 1
  | _ + 1, _ => rfl
  | 0, h => absurd h (Nat.not_succ_le_zero 0)

theorem pool_not_renewed : ¬ web.Renewed .pool :=
  fun renewed => Nat.not_succ_le_self 1 (renewed 0 .needy rfl).2

/-- Whoever needs the spring needs one unit. -/
theorem needs_spring : ∀ {t} f, web.requires t f .spring → web.need t f .spring ≤ 1
  | _, .keeper, _ => Nat.le_refl 1
  | _, .needy, h | _, .drawer, h | _, .idle, h => nomatch h

/-- Whoever needs the pool needs two units. -/
theorem needs_pool : ∀ {t} f, web.requires t f .pool → web.need t f .pool = 2
  | _, .needy, _ => rfl
  | _, .keeper, h | _, .drawer, h | _, .idle, h => nomatch h

/-- No one name needs the pool both before and after an exchange. -/
theorem not_both : ∀ b f, web.requires 0 (turn b f) .pool → ¬ web.requires 0 (turn (!b) f) .pool
  | true, .keeper, _, h | false, .needy, _, h
  | true, .drawer, h, _ | true, .needy, h, _ | true, .idle, h, _
  | false, .drawer, h, _ | false, .keeper, h, _ | false, .idle, h, _ => nomatch h

/-- As named in `web`: activity needs support; the keeper renews and the drawer consumes;
the drawer undermines at every step, the needy formation's need having been met at the
first; and no dependence forms and nothing arises. -/
theorem identified :
    web.Dependent ∧ web.RenewingIn .keeper ∧ web.ConsumingIn .drawer ∧
    (∀ t, web.UnderminingAt t .drawer) ∧ (∀ t f c, ¬ web.Forms t f c) ∧ ¬ web.Unceasing :=
  ⟨fun t f active c depends => match f, active, depends with
    | .keeper, _, depends => match c, depends with
      | .spring, _ => Nat.le_refl 1
      | .pool, h => nomatch h
    | .needy, active, depends => match t, c, active, depends with
      | 0, .pool, _, _ => Nat.le_refl 2
      | 0, .spring, _, h | _ + 1, _, h, _ => nomatch h
    | .drawer, _, h | .idle, h, _ => (nomatch h),
   fun _ c joins => match c, joins with
    | .spring, _ => fun _ g depends => match g, depends with
      | .keeper, _ => ⟨Nat.le_refl 1, Nat.le_refl 1⟩
      | .needy, h | .drawer, h | .idle, h => nomatch h
    | .pool, .inl h | .pool, .inr h => (nomatch h),
   ⟨0, .pool, rfl, .needy, 0, rfl, fun t later => match t, later with
    | _ + 1, _ => Nat.lt_succ_self 1
    | 0, h => absurd h (Nat.lt_irrefl 0)⟩,
   fun _ => ⟨.pool, rfl, .needy, rfl,
    ⟨0, Nat.zero_le _, fun _ _ _ => rfl, Nat.le_refl 2, Nat.lt_succ_self 1⟩, Nat.lt_succ_self 1⟩,
   fun _ _ _ ⟨before, after⟩ => before after,
   fun unceasing => match unceasing 0 with
    | ⟨_, f, _, inactive, active⟩ => match f, active with
      | .drawer, _ | .keeper, _ => inactive trivial
      | .needy, h | .idle, h => nomatch h⟩

/-- Re-identified, with every step's relations unchanged: activity still needs support; no
formation renews and two consume; no event after the first step undermines; the keeper
transforms its dependence across the first step; and formations arise at every odd step,
lowering no condition. -/
theorem reidentified :
    turned.Dependent ∧ (∀ x, ¬ turned.RenewingIn x) ∧ turned.ConsumingIn .drawer ∧
    turned.ConsumingIn .idle ∧ (∀ t x, 1 ≤ t → ¬ turned.UnderminingAt t x) ∧
    turned.Dissolves 0 .keeper .spring ∧ turned.Forms 0 .keeper .pool ∧ turned.Unceasing ∧
    ¬ turned.Depletes [.pool, .spring] fun t => ∃ x, turned.Arises t x :=
  have unrenewed : ¬ turned.Renewed .pool :=
    fun renewed => pool_not_renewed ((web.reidentify_renewed exchange .pool).mp renewed)
  have consumed : turned.Consumed .pool :=
    ⟨.needy, 0, rfl, fun t later => match t, later with
      | _ + 1, _ => Nat.lt_succ_self 1
      | 0, h => absurd h (Nat.lt_irrefl 0)⟩
  have arises : ∀ t, odd t = true → turned.Arises t .drawer := fun t odd' =>
    have odd_next : odd (t + 1) = false := congrArg (!·) odd'
    ⟨Eq.subst (motive := fun b => web.active t (turn b .drawer) → False) odd'.symm id,
     Eq.subst (motive := fun b => web.active (t + 1) (turn b .drawer)) odd_next.symm trivial⟩
  ⟨(web.reidentify_dependent exchange).mpr identified.1,
   fun x renewing => match x with
    | .drawer => unrenewed (renewing 0 .pool (.inr rfl))
    | .keeper => unrenewed (renewing 1 .pool (.inl rfl))
    | .needy => unrenewed (renewing 0 .pool (.inl rfl))
    | .idle => unrenewed (renewing 1 .pool (.inr rfl)),
   ⟨0, .pool, rfl, consumed⟩,
   ⟨1, .pool, rfl, consumed⟩,
   fun t _ late ⟨c, _, y, depends, ⟨s, before, held, met, _⟩, fell⟩ => match c with
    | .spring => Nat.not_le_of_gt fell (needs_spring (t := t) _ depends)
    | .pool => match t, late with
      | 0, h => absurd h (Nat.not_succ_le_zero 0)
      | m + 1, _ => match Nat.lt_or_ge s (m + 1) with
        | .inl earlier =>
          not_both (odd m) y (held m (Nat.le_of_lt_succ earlier) (Nat.le_succ m))
            (held (m + 1) (Nat.le_succ_of_le (Nat.le_of_lt_succ earlier)) (Nat.le_refl _))
        | .inr later =>
          Nat.not_succ_le_self 1 (Nat.le_trans
            (Nat.le_of_eq (needs_pool (t := s) _ (held s (Nat.le_refl s) before)).symm)
            (Nat.le_trans met (Nat.le_of_eq (pool_late (Nat.le_trans (Nat.succ_le_succ
              (Nat.zero_le m)) later))))),
   ⟨rfl, fun h => nomatch h⟩, ⟨fun h => (nomatch h), rfl⟩,
   fun N => match h : odd N with
    | true => ⟨N, .drawer, Nat.le_refl N, arises N h⟩
    | false => ⟨N + 1, .drawer, Nat.le_succ N, arises (N + 1) (congrArg (!·) h)⟩,
   fun depletes => match depletes 1 ⟨.drawer, arises 1 rfl⟩
      (fun c _ rises => match c, rises with
        | .pool, rises | .spring, rises => Nat.lt_irrefl 1 rises) with
    | ⟨c, _, falls⟩ => match c, falls with
      | .pool, falls | .spring, falls => Nat.lt_irrefl 1 falls⟩

end Turnover

namespace Lineage

/-- Two members of a lineage. -/
inductive Member where
  | first
  | second

/-- The first member is active at even steps and the second at odd steps; neither
depends on or draws anything. -/
def web : Web Member Unit where
  level _ _ := 0
  active t m := match m with
    | .first => odd t = false
    | .second => odd t = true
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

def swap : Member → Member
  | .first => .second
  | .second => .first

def turn : Bool → Member → Member
  | true, m => swap m
  | false, m => m

theorem turn_turn : ∀ b m, turn b (turn b m) = m
  | true, .first | true, .second | false, _ => rfl

/-- One name for the lineage: at odd steps the members exchange names. -/
def one : Reidentify Member Member :=
  ⟨fun t => turn (odd t), fun t => turn (odd t), fun t => turn_turn (odd t),
    fun t => turn_turn (odd t)⟩

/-- Named apart, a member arises at every odd step and generation is unceasing. Named as
one, the lineage is always active and nothing arises. Naming it as one keeps every
continuing activity, since no member is active at two successive steps. -/
theorem readings :
    one.KeepsActive web ∧ web.Unceasing ∧ ¬ (web.reidentify one).Unceasing :=
  have always : ∀ t, (web.reidentify one).active t .first := fun t =>
    show web.active t (turn (odd t) .first) from match h : odd t with
      | true => h
      | false => h
  have never : ∀ t, ¬ (web.reidentify one).active t .second := fun t =>
    show web.active t (turn (odd t) .second) → False from match h : odd t with
      | true => fun first => nomatch h.symm.trans first
      | false => fun second => nomatch h.symm.trans second
  ⟨fun _ m now next => match m, now, next with
    | .first, now, next => nomatch (congrArg (!·) now).symm.trans next
    | .second, now, next => (nomatch (congrArg (!·) now).symm.trans next),
   fun N =>
    have arises : ∀ t, odd t = true → web.Arises t .first := fun _ odd' =>
      ⟨fun even => (nomatch odd'.symm.trans even), congrArg (!·) odd'⟩
    match h : odd N with
    | true => ⟨N, .first, Nat.le_refl N, arises N h⟩
    | false => ⟨N + 1, .first, Nat.le_succ N, arises (N + 1) (congrArg (!·) h)⟩,
   fun unceasing => match unceasing 0 with
    | ⟨t, m, _, inactive, active⟩ => match m, inactive, active with
      | .first, inactive, _ => inactive (always t)
      | .second, _, active => never (t + 1) active⟩

end Lineage

namespace Succession

/-- A drawer, an elder that needs the pool at the first step, and an heir that needs it
from the second step on. -/
inductive Formation where
  | drawer
  | elder
  | heir

/-- The pool of `Turnover`: two units, then one. The elder is active at the first step,
while the pool supports it; the heir is never supported and never active. -/
def web : Web Formation Unit where
  level t _ := Turnover.pool t
  active t f := match f with
    | .drawer => True
    | .elder => t = 0
    | .heir => False
  requires t f _ := match f with
    | .drawer => False
    | .elder => t = 0
    | .heir => 1 ≤ t
  need _ f _ := match f with
    | .drawer => 0
    | .elder | .heir => 2
  draws _ f _ := match f with
    | .drawer => True
    | .elder | .heir => False

def swap : Formation → Formation
  | .drawer => .drawer
  | .elder => .heir
  | .heir => .elder

/-- From the second step on, the heir and the elder exchange names. -/
def after : Nat → Formation → Formation
  | 0, f => f
  | _ + 1, f => swap f

theorem after_after : ∀ t f, after t (after t f) = f
  | 0, _ => rfl
  | _ + 1, .drawer | _ + 1, .elder | _ + 1, .heir => rfl

theorem after_drawer : ∀ t, after t .drawer = .drawer
  | 0 => rfl
  | _ + 1 => rfl

/-- The heir succeeds the elder: from the second step on, it bears the elder's name. -/
def succeeds : Reidentify Formation Formation :=
  ⟨after, after, after_after, after_after⟩

/-- The re-identified web. -/
abbrev inherited : Web Formation Unit := web.reidentify succeeds

/-- Under the elder's name, the pool is needed at two units at every step. -/
theorem elder_named : ∀ t, inherited.requires t .elder () ∧ inherited.need t .elder () = 2
  | 0 => ⟨rfl, rfl⟩
  | m + 1 => ⟨Nat.succ_le_succ (Nat.zero_le m), rfl⟩

/-- Succession keeps every continuing activity and dependence. Named apart, the drawer
undermines at the first step, where it breaks the elder's dependence, and at no later
step: the heir's need was never met while it held. With the heir succeeding the elder,
the elder's tenure continues in the heir, and the drawer undermines at every step. -/
theorem readings :
    succeeds.KeepsActive web ∧ succeeds.KeepsTenure web ∧ web.UnderminingAt 0 .drawer ∧
    (∀ t, 1 ≤ t → ¬ web.UnderminingAt t .drawer) ∧ (∀ t, inherited.UnderminingAt t .drawer) :=
  ⟨fun t f now next => match f, now, next with
    | .drawer, _, _ => (after_drawer (t + 1)).trans (after_drawer t).symm
    | .elder, _, next => (nomatch next)
    | .heir, now, _ => (nomatch now),
   fun t g _ now next => match g, t, now, next with
    | .drawer, _, now, _ => (nomatch now)
    | .elder, _, _, next => (nomatch next)
    | .heir, _ + 1, _, _ => rfl
    | .heir, 0, now, _ => absurd now (Nat.not_succ_le_zero 0),
   ⟨(), trivial, .elder, rfl, .now rfl (Nat.le_refl 2) (Nat.lt_succ_self 1), Nat.lt_succ_self 1⟩,
   fun _ late ⟨_, _, g, depends, ⟨s, before, held, met, _⟩, _⟩ => match g, depends, held, met with
    | .drawer, h, _, _ => nomatch h
    | .elder, h, _, _ => Nat.not_succ_le_zero 0 (Eq.subst (motive := fun n => 1 ≤ n) h late)
    | .heir, _, held, met => Nat.not_succ_le_self 1 (Nat.le_trans met
      (Nat.le_of_eq (Turnover.pool_late (held s (Nat.le_refl s) before)))),
   fun t => ⟨(), Eq.subst (motive := fun f => web.draws t f ()) (after_drawer t).symm trivial,
    .elder, (elder_named t).1,
    ⟨0, Nat.zero_le t, fun u _ _ => (elder_named u).1, Nat.le_refl 2, Nat.lt_succ_self 1⟩,
    Eq.subst (motive := fun n => 1 < n) (elder_named t).2.symm (Nat.lt_succ_self 1)⟩⟩

end Succession

end Becoming
