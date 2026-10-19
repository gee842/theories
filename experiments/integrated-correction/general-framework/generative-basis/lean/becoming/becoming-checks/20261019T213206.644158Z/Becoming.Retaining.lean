import Becoming.Regions

/-!
# Retaining: what one level path keeps of another

Retaining and adding, for any significance, with no condition on it: what `Becoming.Significance`
compares under the continuation condition, stated where it needs nothing.

* **Retaining and adding.** From a standpoint, one level path *retains* what has significance
  along another when it admits every continuation with significance that the other admits
  (`Web.Retains`), and *adds* when it admits one the other does not (`Web.Adds`). Retaining is
  reflexive and transitive and ends nothing the other path holds (`Web.Retains.refl`,
  `Web.Retains.trans`, `Web.Retains.not_added`); inclusion retains for every significance
  (`Web.Includes.retains`) and adding exceeds (`Web.Adds.exceeds`). Where fewer continuations
  have significance, more is retained (`Web.Retains.of_fewer`); significance bounded by a region
  (`bounded`) retains what is admitted within the region (`Web.retains_bounded_iff`).
* **The stepwise classes and loss.** Levels below a need are exceeded by every level path that
  admits the formation there (`Web.exceeded_of_below`), so an undermining event leaves the levels
  exceeded (`Web.UnderminingOn.exceeded`), keeping what can form excludes undermining
  (`Web.Includes.not_undermining`), and from a standpoint at which the continuations met have
  significance nothing is retained (`Web.UnderminingOn.not_retains`).
* **Not harm is an exact boundary.** The levels with a part retain what has significance without
  it exactly when the part's net draw stays within the margin for every continuation with
  significance that the levels without it admit (`Flow.retains_iff_within_margin_at`; in a
  balanced flow `Flow.Balances.retains_iff_within_margin`); the part loses a continuation exactly
  beyond the margin and adds one exactly where its net exchange brings a formation within it
  (`Flow.loses_iff_beyond_margin_at`, `Flow.adds_iff_within_margin_at` and their balanced
  forms). The levels with a part widen those without it exactly when the draw stays within the
  margin and the exchange brings one more formation within it
  (`Flow.widens_iff_within_margin_at`, `Flow.Balances.widens_iff_within_margin`).
* **What has not yet formed counts.** In `Preemption` a drawer takes a condition's unit before
  any dependence on it forms: its event is within renewal and not undermining, yet the part does
  not keep what can form (`Preemption.within_renewal_yet_loses`).

Every declaration moved here unchanged, with its name, from `Becoming.Significance` in R31
(20 October 2026); none takes the continuation condition, which `Becoming.Significance` states and
under which retaining is inclusion. No condition, ranking or axiom occurs.
-/

namespace Becoming

variable {F C Pos : Type}

/-- Significance kept inside each standpoint's region: from `p`, the continuation of `f` has
significance exactly when `f` lies in `p`'s region. -/
def bounded (region : Pos → F → Prop) : Pos → Nat → F → Prop :=
  fun p _ f => region p f

/-! ## Retaining and adding what has significance -/

namespace Web

variable (W : Web F C)

/-- From standpoint `p`, the level path `l` retains what has significance along `l'`: it admits
every continuation with significance that `l'` admits. -/
def Retains (sig : Pos → Nat → F → Prop) (p : Pos) (l l' : Nat → C → Nat) : Prop :=
  ∀ t f, sig p t f → W.Admits (l' t) t f → W.Admits (l t) t f

/-- From standpoint `p`, the level path `l` adds a continuation with significance that `l'` does
not admit. -/
def Adds (sig : Pos → Nat → F → Prop) (p : Pos) (l l' : Nat → C → Nat) : Prop :=
  ∃ t f, sig p t f ∧ W.Admits (l t) t f ∧ ¬ W.Admits (l' t) t f

variable {W}

/-- Retaining is reflexive. -/
theorem Retains.refl (sig : Pos → Nat → F → Prop) (p : Pos) (l : Nat → C → Nat) :
    W.Retains sig p l l :=
  fun _ _ _ admits => admits

/-- Retaining is transitive. -/
theorem Retains.trans {sig : Pos → Nat → F → Prop} {p : Pos} {l l' l'' : Nat → C → Nat}
    (first : W.Retains sig p l l') (second : W.Retains sig p l' l'') : W.Retains sig p l l'' :=
  fun t f significant admits => first t f significant (second t f significant admits)

/-- Comparison by retaining licenses no ending: a level path that retains what has significance
along another ends none of it, so the other adds nothing to it. -/
theorem Retains.not_added {sig : Pos → Nat → F → Prop} {p : Pos} {l l' : Nat → C → Nat}
    (retains : W.Retains sig p l l') : ¬ W.Adds sig p l' l
  | ⟨t, f, significant, admitted, ended⟩ => ended (retains t f significant admitted)

/-- Inclusion retains, whatever has significance. -/
theorem Includes.retains {l l' : Nat → C → Nat} (includes : W.Includes l l')
    (sig : Pos → Nat → F → Prop) (p : Pos) : W.Retains sig p l l' :=
  fun t f _ admits => includes t f admits

/-- Adding exceeds, whatever has significance. -/
theorem Adds.exceeds {sig : Pos → Nat → F → Prop} {p : Pos} {l l' : Nat → C → Nat} :
    W.Adds sig p l l' → W.Exceeds l l'
  | ⟨t, f, _, admits, not⟩ => ⟨t, f, admits, not⟩

/-- Where fewer continuations have significance, more is retained. -/
theorem Retains.of_fewer {sig sig' : Pos → Nat → F → Prop}
    (fewer : ∀ p t f, sig' p t f → sig p t f) {p : Pos} {l l' : Nat → C → Nat}
    (retains : W.Retains sig p l l') : W.Retains sig' p l l' :=
  fun t f significant admits => retains t f (fewer p t f significant) admits

/-- Significance bounded by a region retains exactly what is admitted within the region at every
step. -/
theorem retains_bounded_iff {region : Pos → F → Prop} {p : Pos} {l l' : Nat → C → Nat} :
    W.Retains (bounded region) p l l' ↔ ∀ t, W.AdmitsWithin (region p) (l t) (l' t) t :=
  ⟨fun retains t f inside => retains t f inside, fun within t f inside => within t f inside⟩

/-! ## The stepwise classes and loss

Undermining, a stepwise class of a formation's event, and the order on what can form read the
same levels. Where the levels fall below a need, every level path admitting the formation there
exceeds them. So an undermining event, through dependences that hold across its step at no smaller
need, leaves the levels short of what every level path meeting those dependences after the step
admits; the levels with a part that undermines do not include the levels without it wherever
these meet the dependences. An event within renewal gives no such guarantee in the other direction
(`Preemption.within_renewal_yet_loses`). -/

/-- **Levels below a need are exceeded by every path admitting the formation there.** -/
theorem exceeded_of_below {l : Nat → C → Nat} {s : Nat} {g : F} {c : C} (requires : W.requires s g c)
    (below : W.level s c < W.need s g c) (admits : W.Admits (l s) s g) : W.Exceeds l W.level :=
  ⟨s, g, admits, fun admitted => Nat.not_le_of_gt below (admitted c requires)⟩

/-- **An undermining event leaves the levels exceeded.** Where every dependence on the condition
holds across the step at no smaller need, and a level path admits after the step every formation
depending on the condition before it, that path exceeds the levels. -/
theorem UnderminingOn.exceeded {l : Nat → C → Nat} {t : Nat} {f : F} {c : C}
    (undermining : W.UnderminingOn t f c)
    (holds : ∀ g, W.requires t g c → W.requires (t + 1) g c ∧ W.need t g c ≤ W.need (t + 1) g c)
    (admits : ∀ g, W.requires t g c → W.Admits (l (t + 1)) (t + 1) g) : W.Exceeds l W.level :=
  match undermining with
  | ⟨_, g, depends, _, below⟩ =>
    exceeded_of_below (holds g depends).1
      (Nat.lt_of_lt_of_le below (holds g depends).2) (admits g depends)

/-- **Keeping what can form excludes undermining where the other path meets the dependences.** The
levels include a level path admitting after a step every formation depending on a condition before
it, through dependences that hold across the step at no smaller need, only if no event at the step
undermines that condition. -/
theorem Includes.not_undermining {l : Nat → C → Nat} (includes : W.Includes W.level l) {t : Nat}
    {f : F} {c : C}
    (holds : ∀ g, W.requires t g c → W.requires (t + 1) g c ∧ W.need t g c ≤ W.need (t + 1) g c)
    (admits : ∀ g, W.requires t g c → W.Admits (l (t + 1)) (t + 1) g) : ¬ W.UnderminingOn t f c :=
  fun undermining => includes.not_exceeded (undermining.exceeded holds admits)

/-- **An undermining event loses what has significance.** Under the same hypotheses, from a
standpoint at which the continuation after the step of every formation depending on the condition
has significance, the levels do not retain what has significance along the other path. -/
theorem UnderminingOn.not_retains {l : Nat → C → Nat} {t : Nat} {f : F} {c : C}
    (undermining : W.UnderminingOn t f c)
    (holds : ∀ g, W.requires t g c → W.requires (t + 1) g c ∧ W.need t g c ≤ W.need (t + 1) g c)
    (admits : ∀ g, W.requires t g c → W.Admits (l (t + 1)) (t + 1) g)
    {sig : Pos → Nat → F → Prop} {p : Pos} (significant : ∀ g, W.requires t g c → sig p (t + 1) g) :
    ¬ W.Retains sig p W.level l :=
  match undermining with
  | ⟨_, g, depends, _, below⟩ => fun retains =>
    Nat.not_le_of_gt (Nat.lt_of_lt_of_le below (holds g depends).2)
      (retains (t + 1) g (significant g depends) (admits g depends) c (holds g depends).1)

end Web

/-! ## Not harm is an exact boundary -/

namespace Flow

variable {L : Flow F C} {part : F → Bool} {W : Web F C}

/-- From standpoint `p`, with balance only at the conditions required by the continuations with
significance that the levels without the part admit, across the steps before each: the levels with
the part retain what has significance without it exactly when, for each such continuation, the
part's net draw on each condition the formation requires stays within the margin. -/
theorem retains_iff_within_margin_at {l : Nat → C → Nat} (without : L.WithheldLevels part W l)
    {sig : Pos → Nat → F → Prop} {p : Pos}
    (balances : ∀ t f, sig p t f → W.Admits (l t) t f → ∀ c, W.requires t f c → ∀ s, s < t →
      L.BalancesOn W [c] s) :
    W.Retains sig p W.level l ↔ ∀ t f, sig p t f → W.Admits (l t) t f → ∀ c, W.requires t f c →
      W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
        l t c + total (steps 0 t) (fun s => L.partGiven part s c) :=
  ⟨fun retains t f significant admits =>
      (supported_iff_within_margin_at without (balances t f significant admits)).mp
        (retains t f significant admits),
   fun within t f significant admits =>
      (supported_iff_within_margin_at without (balances t f significant admits)).mpr
        (within t f significant admits)⟩

/-- From standpoint `p`, with balance as in `retains_iff_within_margin_at`: a part loses a
continuation with significance exactly where the levels without it admit the formation and the
part's net draw on some condition it requires exceeds the margin. -/
theorem loses_iff_beyond_margin_at {l : Nat → C → Nat} (without : L.WithheldLevels part W l)
    {sig : Pos → Nat → F → Prop} {p : Pos}
    (balances : ∀ t f, sig p t f → W.Admits (l t) t f → ∀ c, W.requires t f c → ∀ s, s < t →
      L.BalancesOn W [c] s) :
    W.Adds sig p l W.level ↔ ∃ t f, sig p t f ∧ W.Admits (l t) t f ∧ ¬ ∀ c, W.requires t f c →
      W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
        l t c + total (steps 0 t) (fun s => L.partGiven part s c) :=
  ⟨fun ⟨t, f, significant, admits, lost⟩ => ⟨t, f, significant, admits, fun within =>
      lost ((supported_iff_within_margin_at without (balances t f significant admits)).mpr
        within)⟩,
   fun ⟨t, f, significant, admits, beyond⟩ => ⟨t, f, significant, admits, fun supported =>
      beyond ((supported_iff_within_margin_at without (balances t f significant admits)).mp
        supported)⟩⟩

/-- From standpoint `p`, with balance only at the conditions required by the continuations with
significance that the levels without the part do not admit, across the steps before each: a part
adds a continuation with significance exactly where the levels without it do not admit the
formation and, with the part's net exchange, its need is met within the margin on every condition
it requires. -/
theorem adds_iff_within_margin_at {l : Nat → C → Nat} (without : L.WithheldLevels part W l)
    {sig : Pos → Nat → F → Prop} {p : Pos}
    (balances : ∀ t f, sig p t f → ¬ W.Admits (l t) t f → ∀ c, W.requires t f c → ∀ s, s < t →
      L.BalancesOn W [c] s) :
    W.Adds sig p W.level l ↔ ∃ t f, sig p t f ∧ (∀ c, W.requires t f c →
      W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
        l t c + total (steps 0 t) (fun s => L.partGiven part s c)) ∧ ¬ W.Admits (l t) t f :=
  ⟨fun ⟨t, f, significant, supported, fresh⟩ => ⟨t, f, significant,
      (supported_iff_within_margin_at without (balances t f significant fresh)).mp supported,
      fresh⟩,
   fun ⟨t, f, significant, within, fresh⟩ => ⟨t, f, significant,
      (supported_iff_within_margin_at without (balances t f significant fresh)).mpr within,
      fresh⟩⟩

/-- From standpoint `p`, the levels with a part retain what has significance without it exactly
when, at every step, for every continuation with significance that the levels without it admit,
the part's net draw on each condition the formation requires stays within the margin. -/
theorem Balances.retains_iff_within_margin (balances : L.Balances W) {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {sig : Pos → Nat → F → Prop} {p : Pos} :
    W.Retains sig p W.level l ↔ ∀ t f, sig p t f → W.Admits (l t) t f → ∀ c, W.requires t f c →
      W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
        l t c + total (steps 0 t) (fun s => L.partGiven part s c) :=
  retains_iff_within_margin_at without fun _ _ _ _ c _ s _ => balances.on [c] s

/-- From standpoint `p`, a part loses a continuation with significance exactly where the levels
without it admit the formation and the part's net draw on some condition it requires exceeds the
margin. -/
theorem Balances.loses_iff_beyond_margin (balances : L.Balances W) {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {sig : Pos → Nat → F → Prop} {p : Pos} :
    W.Adds sig p l W.level ↔ ∃ t f, sig p t f ∧ W.Admits (l t) t f ∧ ¬ ∀ c, W.requires t f c →
      W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
        l t c + total (steps 0 t) (fun s => L.partGiven part s c) :=
  loses_iff_beyond_margin_at without fun _ _ _ _ c _ s _ => balances.on [c] s

/-- From standpoint `p`, a part adds a continuation with significance exactly where the levels
without it do not admit the formation and, with the part's net exchange, its need is met within
the margin on every condition it requires. -/
theorem Balances.adds_iff_within_margin (balances : L.Balances W) {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) {sig : Pos → Nat → F → Prop} {p : Pos} :
    W.Adds sig p W.level l ↔ ∃ t f, sig p t f ∧ (∀ c, W.requires t f c →
      W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
        l t c + total (steps 0 t) (fun s => L.partGiven part s c)) ∧ ¬ W.Admits (l t) t f :=
  adds_iff_within_margin_at without fun _ _ _ _ c _ s _ => balances.on [c] s

/-- The exact boundary of the generative space, with no axiom, and balance only where it is used:
at the conditions each formation requires, across the steps before it. The levels with a part
widen those without it exactly when the part's net draw stays within the margin for every
formation the levels without it admit, and, at some step, its net exchange brings within the
margin a formation the levels without it do not admit. -/
theorem widens_iff_within_margin_at {l : Nat → C → Nat} (without : L.WithheldLevels part W l)
    (balances : ∀ t f c, W.requires t f c → ∀ s, s < t → L.BalancesOn W [c] s) :
    W.Widens W.level l ↔
      (∀ t f, W.Admits (l t) t f → ∀ c, W.requires t f c →
        W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
          l t c + total (steps 0 t) (fun s => L.partGiven part s c)) ∧
      ∃ t f, (∀ c, W.requires t f c →
        W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
          l t c + total (steps 0 t) (fun s => L.partGiven part s c)) ∧ ¬ W.Admits (l t) t f :=
  ⟨fun ⟨includes, t, f, admits, not⟩ =>
    ⟨fun t f admitted => (supported_iff_within_margin_at without (balances t f)).mp
        (includes t f admitted),
     t, f, (supported_iff_within_margin_at without (balances t f)).mp admits, not⟩,
   fun ⟨within, t, f, brought, not⟩ =>
    ⟨fun t f admitted => (supported_iff_within_margin_at without (balances t f)).mpr
        (within t f admitted),
     t, f, (supported_iff_within_margin_at without (balances t f)).mpr brought, not⟩⟩

/-- In a balanced flow, the exact boundary of the generative space (`widens_iff_within_margin_at`). -/
theorem Balances.widens_iff_within_margin (balances : L.Balances W) {l : Nat → C → Nat}
    (without : L.WithheldLevels part W l) :
    W.Widens W.level l ↔
      (∀ t f, W.Admits (l t) t f → ∀ c, W.requires t f c →
        W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
          l t c + total (steps 0 t) (fun s => L.partGiven part s c)) ∧
      ∃ t f, (∀ c, W.requires t f c →
        W.need t f c + total (steps 0 t) (fun s => L.partTaken part s c) ≤
          l t c + total (steps 0 t) (fun s => L.partGiven part s c)) ∧ ¬ W.Admits (l t) t f :=
  widens_iff_within_margin_at without fun _ _ c _ s _ => balances.on [c] s

end Flow

/-! ## Witnesses -/

/-! A drawer takes a condition's unit before any dependence on it forms. -/

namespace Preemption

/-- Across the first step the drawer `true` takes the condition's one unit; nothing gives. -/
def flow : Flow Bool Unit where
  present t := match t with
    | 0 => [true]
    | _ + 1 => []
  take t x _ := match t, x with
    | 0, true => 1
    | 0, false => 0
    | _ + 1, _ => 0
  give _ _ _ := 0

/-- The drawer requires nothing and is active at the first step. `false` requires the condition
at need one from the second step on and is never active. -/
def web : Web Bool Unit where
  level t _ := unitDrop t
  active t x := match x with
    | true => t = 0
    | false => False
  requires t x _ := match x with
    | true => False
    | false => 0 < t
  need _ _ _ := 1
  draws t x _ := match t, x with
    | 0, true => True
    | 0, false => False
    | _ + 1, _ => False

/-- The drawer's part. -/
def drawerPart : Bool → Bool
  | true => true
  | false => false

/-- Without the drawer's part the condition stays at one. -/
theorem withheld : flow.WithheldLevels drawerPart web fun _ _ => 1 :=
  ⟨fun t () => match t with
    | 0 => rfl
    | _ + 1 => rfl,
   fun () => rfl⟩

/-- **Within renewal, yet closing a possibility.** The drawer's event at the first step is within
renewal, since no dependence on the condition has formed for the step to keep, and is not
undermining; yet the levels with the drawer's part do not include those without it. So no event's
being within renewal or not undermining shows that a part keeps what can form: the stepwise
classes count only dependences that have formed. -/
theorem within_renewal_yet_loses {l : Nat → Unit → Nat}
    (without : flow.WithheldLevels drawerPart web l) :
    web.RenewingAt 0 true ∧ ¬ web.UnderminingAt 0 true ∧ ¬ web.Includes web.level l :=
  ⟨⟨rfl, fun _ _ g requires => match g, requires with
    | true, no => (nomatch no)
    | false, no => absurd no (Nat.lt_irrefl 0)⟩,
   fun ⟨(), _, g, requires, _⟩ => match g, requires with
    | true, no => no
    | false, no => Nat.lt_irrefl 0 no,
   fun includes => Nat.not_succ_le_zero 0
     (includes 1 false (fun () _ => Nat.le_of_eq (without.unique withheld 1 ()).symm) ()
       (Nat.succ_pos 0))⟩

end Preemption

end Becoming