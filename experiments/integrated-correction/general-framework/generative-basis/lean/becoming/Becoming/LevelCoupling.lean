import Becoming.Observation

/-!
# Level coupling: where a level couples into a formation

The naming study of 17-18 October (N1, study §6.2) adopted "couples into" for what
`Web.CoupledInto` names, in two grains: by threshold (`Web.DependsOn`) and by level (`obs`).
Ren agreed and asked for the instance check: "Claim and prove the instance check of coupling by
level against Observation/Loops (study §6.2), still no renames." `obs` is a supplied relation,
while a coupling of `Becoming.Loops` is a positive strength of an exchange law and a route of
`Becoming.Observation` is a reading of one. This module states, with no premise beyond what each
theorem names, how the three meet. No name is changed.

* **A response is a coupling of every strength array.** Across the step from `t`, `h`'s exchange
  with `c` responds to the level of `d` at `s` when two histories differing at most in that
  level give a positive exchange gap (`ExchangeLaw.RespondsTo`). Strength zero is exactly no
  response (`ExchangeLaw.respondsWithin_zero_iff`); a response forces every strength of the law
  for that level to be positive (`ExchangeLaw.RespondsTo.strength_pos`), so it is a coupling of
  `Becoming.Loops` for every strength array of the law (`ExchangeLaw.RespondsTo.couples`) and a
  route of length one (`ExchangeLaw.RespondsTo.upstream`).
* **Only what couples into a formation responds.** For a law reading, for each formation outside
  the part, only what couples into it (`ExchangeLaw.Through`): a level that couples into it
  neither by threshold nor by level is coupled with strength zero (`ExchangeLaw.Through.respondsWithin_uncoupled`), so a
  response comes from a condition that couples into it (`ExchangeLaw.Through.couples_of_respondsTo`),
  and is a route of reading in every schedule covering what couples into it
  (`ExchangeLaw.Through.reads_of_respondsTo`, `ExchangeLaw.Through.couples_readCouplings`) and a
  route of the law's strengths restricted to that schedule
  (`ExchangeLaw.Through.upstream_restrictInto`).
* **By threshold, only a crossing passes.** A change of one level that leaves its need met
  alike is a response by level (`ExchangeLaw.RespondsByLevel`). Where the condition does not
  couple into the formation by level, no law reading through its couplings responds to it by level
  (`ExchangeLaw.Through.not_respondsByLevel`): through the threshold only a crossing passes.
* **By threshold, a crossing passes.** A response to a condition that does not couple into the
  formation by level is a crossing of its need (`ExchangeLaw.Through.crosses_of_unobserved`). Where the formation
  requires at a step exactly that one condition, with a positive need, a law reading through its
  couplings responds to a crossing there, at every condition (`thresholdLaw`,
  `thresholdLaw_through`, `thresholdLaw_respondsByCrossing`, `crossing_passes`). The 18 October
  continuation (N3) added this half.
* **Among several conditions, a crossing passes through the conjunction.** A response to a
  condition that does not couple into the formation by level changes its admission at that step, at or before the
  step of the exchange (`ExchangeLaw.Through.admission_changes_of_unobserved`), so it happens only
  where the formation's other requirements there are met (`ExchangeLaw.Through.others_met_of_unobserved`).
  A response by a crossing needs a positive requirement (`ExchangeLaw.RespondsByCrossing.requires_pos`).
  Where the formation's admission at the step is decided, a crossing of a condition passes, through
  a law reading only that decision, into every later exchange and at every condition, exactly where
  the formation requires the condition there with a positive need (`admissionLaw`,
  `admissionLaw_through`, `admissionLaw_respondsByCrossing`, `crossing_passes_iff`); a listed
  support decides admission (`admitsDecidableOfSupport`, `crossing_passes_of_support`). The second
  18 October continuation (N4) added this.
* **By level, the level passes.** Where the condition couples into it by level, a law reading
  through its couplings responds to it by level at every step and condition (`levelLaw`,
  `levelLaw_through`, `levelLaw_respondsByLevel`). So coupling by level (`obs`) is exactly where a level can couple
  into a formation within its threshold (`not_not_obs_iff_respondsByLevel`).

**Reading (the AI's).** `obs` is not a second kind of relation beside the couplings of
`Becoming.Loops` and the readings of `Becoming.Observation`: it marks where a level can couple
into a formation by level, as `Web.DependsOn` marks where it can couple by threshold (a crossing
of the need), and every coupling a response forces lies within them. "Coupled by level" names this exactly; what can
couple in bounds what responds, and a law's actual responses are its couplings. The double negation of the last
equivalence is the constructive form: the converse shows that a level coupling is not left out.

What is not derived: which law the rest follows, or whether a level coupled by level is in fact
responded to (a law reading through the couplings may ignore what couples in); a crossing
passing where the formation's admission at the step is not decided (the decision is the
witness's one input, and a law that responds reads no more than it); a strength's size beyond
being positive. The representation commits to discrete steps and natural amounts. No
ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {F C : Type}

namespace ExchangeLaw

variable (law : ExchangeLaw F C)

/-- **The exchange responds to a level.** Across the step from `t`, `h`'s exchange with `c`
responds to the level of `d` at step `s`: two histories differing at most in that level give a
positive exchange gap. -/
def RespondsTo (t : Nat) (h : F) (c : C) (s : Nat) (d : C) : Prop :=
  ∃ l l' : Nat → C → Nat, (∀ s' e, ¬ (s' = s ∧ e = d) → l s' e = l' s' e) ∧
    0 < law.exchangeGap t h c l l'

/-- **The exchange responds to a level by level.** As `RespondsTo`, by a change of the level that
leaves `h`'s need for `d` at `s` met alike in `W`. -/
def RespondsByLevel (W : Web F C) (t : Nat) (h : F) (c : C) (s : Nat) (d : C) : Prop :=
  ∃ l l' : Nat → C → Nat, (∀ s' e, ¬ (s' = s ∧ e = d) → l s' e = l' s' e) ∧
    (W.requires s h d → (W.need s h d ≤ l s d ↔ W.need s h d ≤ l' s d)) ∧
    0 < law.exchangeGap t h c l l'

end ExchangeLaw

/-! ## A response is a coupling of every strength array -/

section Response

variable {law : ExchangeLaw F C} {t s : Nat} {h : F} {c d : C}

/-- A response by level is a response. -/
theorem ExchangeLaw.RespondsByLevel.respondsTo {W : Web F C}
    (responds : law.RespondsByLevel W t h c s d) : law.RespondsTo t h c s d :=
  let ⟨l, l', off, _, pos⟩ := responds
  ⟨l, l', off, pos⟩

/-- **Strength zero is exactly no response.** -/
theorem ExchangeLaw.respondsWithin_zero_iff :
    law.RespondsWithin t h c s d 0 ↔ ¬ law.RespondsTo t h c s d :=
  ⟨fun within ⟨l, l', off, pos⟩ =>
    Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le pos
      (Nat.le_trans (within l l' off) (Nat.le_of_eq (Nat.zero_mul _)))),
   fun none l l' off =>
    Nat.le_trans (Nat.ge_of_not_lt fun pos => none ⟨l, l', off, pos⟩)
      (Nat.le_of_eq (Nat.zero_mul _).symm)⟩

/-- **A response forces a positive strength.** Every strength of the law for a level its
exchange responds to is positive. -/
theorem ExchangeLaw.RespondsTo.strength_pos (responds : law.RespondsTo t h c s d) {k : Nat}
    (within : law.RespondsWithin t h c s d k) : 0 < k :=
  match k, within with
  | 0, within => absurd responds (ExchangeLaw.respondsWithin_zero_iff.mp within)
  | _ + 1, _ => Nat.succ_pos _

variable {cs : List C} {part : F → Bool} {present : Nat → List F}
  {k : Nat → F → C → Nat → C → Nat}

/-- **A response is a coupling of every strength array.** For every strength array of the law, a
response of a formation present outside the part, to a listed level up to the step, couples that
level into the condition in the sense of `Becoming.Loops`. -/
theorem ExchangeLaw.RespondsTo.couples
    (strengths : ∀ t h c s d, part h = false → s ≤ t → law.RespondsWithin t h c s d (k t h c s d))
    (responds : law.RespondsTo t h c s d) (mem : h ∈ present t) (out : part h = false)
    (le : s ≤ t) (listed : d ∈ cs) : Couples cs part k present d c :=
  ⟨t, h, s, mem, out, le, listed, responds.strength_pos (strengths t h c s d out le)⟩

/-- A response is a route of length one. -/
theorem ExchangeLaw.RespondsTo.upstream
    (strengths : ∀ t h c s d, part h = false → s ≤ t → law.RespondsWithin t h c s d (k t h c s d))
    (responds : law.RespondsTo t h c s d) (mem : h ∈ present t) (out : part h = false)
    (le : s ≤ t) (listed : d ∈ cs) : Upstream cs part k present d c :=
  Upstream.single (responds.couples strengths mem out le listed)

end Response

/-! ## Only what couples into a formation responds -/

section Through

variable {law : ExchangeLaw F C} {W : Web F C} {obs : F → C → Prop} {part : F → Bool}
  {t s : Nat} {h : F} {c d : C}

/-- **A level that does not couple in is coupled with strength zero.** For a law reading through
the couplings, a level that couples into a formation outside the part neither by threshold nor by
level is
coupled into its exchange with every condition, at every step, with strength zero. -/
theorem ExchangeLaw.Through.respondsWithin_uncoupled (through : law.Through W obs part)
    (out : part h = false) (uncoupled : ¬ W.CoupledInto obs h d) :
    law.RespondsWithin t h c s d 0 :=
  ExchangeLaw.respondsWithin_zero_iff.mpr fun ⟨l, l', off, pos⟩ =>
    have apart : ∀ e, W.CoupledInto obs h e → ∀ s', ¬ (s' = s ∧ e = d) := fun _ registers _ both =>
      uncoupled (both.2 ▸ registers)
    have alike := through h out t l l' fun s' _ =>
      ⟨⟨fun admits e requires =>
          (off s' e (apart e (Or.inl ⟨s', requires⟩) s')) ▸ admits e requires,
        fun admits e requires =>
          (off s' e (apart e (Or.inl ⟨s', requires⟩) s')).symm ▸ admits e requires⟩,
       fun e seen => off s' e (apart e (Or.inr seen) s')⟩
    Nat.lt_irrefl 0 ((ExchangeLaw.exchangeGap_of_alike alike c) ▸ pos)

/-- **A response comes from what couples into the formation.** -/
theorem ExchangeLaw.Through.couples_of_respondsTo (through : law.Through W obs part)
    (out : part h = false) (responds : law.RespondsTo t h c s d) : ¬ ¬ W.CoupledInto obs h d :=
  fun uncoupled =>
    ExchangeLaw.respondsWithin_zero_iff.mp (through.respondsWithin_uncoupled out uncoupled)
      responds

/-- **A response is read in every schedule covering what couples in.** -/
theorem ExchangeLaw.Through.reads_of_respondsTo {reads : Nat → F → C → Bool}
    (through : law.Through W obs part)
    (cover : ∀ t h d, part h = false → W.CoupledInto obs h d → reads t h d = true)
    (out : part h = false) (responds : law.RespondsTo t h c s d) : reads t h d = true :=
  match unread : reads t h d with
  | true => rfl
  | false => absurd responds (ExchangeLaw.respondsWithin_zero_iff.mp
      ((through.readsAt cover).respondsWithin_unread out unread c s))

/-- **A response is a route of reading.** For a law reading through the couplings and a schedule
covering it, a response of a formation present outside the part, to a listed level up to the
step, is a coupling of the routes of reading of `Becoming.Observation`. -/
theorem ExchangeLaw.Through.couples_readCouplings {reads : Nat → F → C → Bool} {cs : List C}
    {present : Nat → List F} (through : law.Through W obs part)
    (cover : ∀ t h d, part h = false → W.CoupledInto obs h d → reads t h d = true)
    (responds : law.RespondsTo t h c s d) (mem : h ∈ present t) (out : part h = false)
    (le : s ≤ t) (listed : d ∈ cs) :
    Couples cs part (readCouplings fun t h _ _ d => reads t h d) present d c :=
  ⟨t, h, s, mem, out, le, listed,
   show 0 < cond (reads t h d) 1 0 from
     (through.reads_of_respondsTo cover out responds) ▸ Nat.one_pos⟩

/-- **A response is a route of the strengths restricted to what is read.** For a law reading
through the couplings, a schedule covering it and any strength array of the law, a response of a
formation present outside the part, to a listed level up to the step, is a route of length one of
the strengths restricted to the schedule. -/
theorem ExchangeLaw.Through.upstream_restrictInto {reads : Nat → F → C → Bool} {cs : List C}
    {present : Nat → List F} {k : Nat → F → C → Nat → C → Nat} (through : law.Through W obs part)
    (cover : ∀ t h d, part h = false → W.CoupledInto obs h d → reads t h d = true)
    (strengths : ∀ t h c s d, part h = false → s ≤ t → law.RespondsWithin t h c s d (k t h c s d))
    (responds : law.RespondsTo t h c s d) (mem : h ∈ present t) (out : part h = false)
    (le : s ≤ t) (listed : d ∈ cs) :
    Upstream cs part (restrictInto (fun t h _ _ d => reads t h d) k) present d c :=
  responds.upstream ((through.readsInto cover).restrict strengths) mem out le listed

/-- Histories with equal levels at a step are alike there through the couplings. -/
theorem Web.alikeThrough_of_levels {g : F} {l l' : Nat → C → Nat} {s' : Nat}
    (same : ∀ e, l s' e = l' s' e) : W.AlikeThrough obs g l l' s' :=
  ⟨⟨fun admits e requires => (same e) ▸ admits e requires,
    fun admits e requires => (same e).symm ▸ admits e requires⟩,
   fun e _ => same e⟩

/-- **By threshold, only a crossing passes.** For a law reading through the couplings, a formation
outside the part into which a condition does not couple by level is not responded to by level: a change of that
level leaving its need met alike changes nothing it exchanges. -/
theorem ExchangeLaw.Through.not_respondsByLevel [DecidableEq C] (through : law.Through W obs part)
    (out : part h = false) (unobserved : ¬ obs h d) : ¬ law.RespondsByLevel W t h c s d :=
  fun ⟨l, l', off, threshold, pos⟩ =>
    have alike := through h out t l l' fun s' _ =>
      match Nat.decEq s' s with
      | isTrue same => by
          subst same
          exact Web.alike_of_threshold unobserved
            (fun e _ other => off _ e fun both => other both.2) threshold
      | isFalse other => Web.alikeThrough_of_levels fun e => off s' e fun both => other both.1
    Nat.lt_irrefl 0 ((ExchangeLaw.exchangeGap_of_alike alike c) ▸ pos)

end Through

/-! ## By level, the level passes -/

section Witness

variable {W : Web F C} {obs : F → C → Prop} {part : F → Bool} {d : C}

/-- **A law taking the level that couples in by level.** Each marked formation takes from every condition the
level of `d` at the step; nothing else is exchanged. -/
def levelLaw (mark : F → Bool) (d : C) : ExchangeLaw F C :=
  ⟨fun t h l _ => bif mark h then l t d else 0, fun _ _ _ _ => 0⟩

/-- **The law taking a level coupled by level reads through the couplings.** -/
theorem levelLaw_through {mark : F → Bool} (marked : ∀ h, mark h = true → obs h d) :
    (levelLaw mark d).Through W obs part :=
  fun h _ t l l' alike _ => by
    refine ⟨?_, rfl⟩
    show cond (mark h) (l t d) 0 = cond (mark h) (l' t d) 0
    cases m : mark h with
    | true => exact (alike t (Nat.le_refl t)).2 d (marked h m)
    | false => rfl

/-- Two histories: every level at `n`, and the level of `d` at `t` one higher in the second. -/
def raisedAt [DecidableEq C] (n t : Nat) (d : C) : Nat → C → Nat :=
  fun s e => if s = t ∧ e = d then n + 1 else n

/-- **The law taking a level coupled by level responds to it by level** at every step and condition,
for every marked formation. -/
theorem levelLaw_respondsByLevel [DecidableEq C] {mark : F → Bool} {h : F} (marked : mark h = true)
    (t : Nat) (c : C) : (levelLaw mark d).RespondsByLevel W t h c t d :=
  ⟨fun _ _ => W.need t h d, raisedAt (W.need t h d) t d,
   fun _ _ apart => (if_neg apart).symm,
   fun _ => ⟨fun _ => Nat.le_trans (Nat.le_succ _) (Nat.le_of_eq (if_pos ⟨rfl, rfl⟩).symm),
     fun _ => Nat.le_refl _⟩,
   have before : cond (mark h) (W.need t h d) 0 = W.need t h d :=
     congrArg (fun b => cond b (W.need t h d) 0) marked
   have after : cond (mark h) (raisedAt (W.need t h d) t d t d) 0 = W.need t h d + 1 :=
     (congrArg (fun b => cond b (raisedAt (W.need t h d) t d t d) 0) marked).trans
       (if_pos ⟨rfl, rfl⟩)
   have one : gap (W.need t h d) (W.need t h d + 1) = 1 :=
     (gap_comm _ _).trans (gap_add_self _ 1)
   Nat.lt_of_lt_of_le Nat.one_pos (Nat.le_trans
     (Nat.le_of_eq (one.symm.trans (congr (congrArg gap before) after).symm))
     (Nat.le_add_right _ (gap 0 0)))⟩

/-- **Coupling by level is exactly where a level can couple into a formation within its threshold.**
For a formation outside the part: it is not refuted that the condition couples into it by level
exactly where it is not refuted that some law reading through its couplings responds to the condition by
level. -/
theorem not_not_obs_iff_respondsByLevel [DecidableEq C] [DecidableEq F] {h : F}
    (out : part h = false) :
    ¬ ¬ obs h d ↔
      ¬ ¬ ∃ law : ExchangeLaw F C, law.Through W obs part ∧
        ∃ t c s, law.RespondsByLevel W t h c s d :=
  ⟨fun nn none => nn fun observed =>
    none ⟨levelLaw (fun h' => decide (h' = h)) d,
      levelLaw_through fun _ m => (of_decide_eq_true m) ▸ observed,
      0, d, 0, levelLaw_respondsByLevel (mark := fun h' => decide (h' = h)) (decide_eq_true rfl) 0 d⟩,
   fun nn unobserved => nn fun ⟨_, through, _, _, _, responds⟩ =>
    through.not_respondsByLevel out unobserved responds⟩

end Witness

/-! ## By threshold, a crossing passes -/

namespace ExchangeLaw

variable (law : ExchangeLaw F C)

/-- **The exchange responds to a crossing.** As `RespondsTo`, by a change of the level of `d` at
`s` across `h`'s need for it in `W`: the need is met under the first history and not under the
second. -/
def RespondsByCrossing (W : Web F C) (t : Nat) (h : F) (c : C) (s : Nat) (d : C) : Prop :=
  ∃ l l' : Nat → C → Nat, (∀ s' e, ¬ (s' = s ∧ e = d) → l s' e = l' s' e) ∧
    W.requires s h d ∧ W.need s h d ≤ l s d ∧ ¬ W.need s h d ≤ l' s d ∧
    0 < law.exchangeGap t h c l l'

end ExchangeLaw

section Crossing

variable {law : ExchangeLaw F C} {W : Web F C} {obs : F → C → Prop} {part : F → Bool}
  {t s : Nat} {h : F} {c d : C}

/-- A response by a crossing is a response. -/
theorem ExchangeLaw.RespondsByCrossing.respondsTo (responds : law.RespondsByCrossing W t h c s d) :
    law.RespondsTo t h c s d :=
  let ⟨l, l', off, _, _, _, pos⟩ := responds
  ⟨l, l', off, pos⟩

/-- **A response to a condition not coupled in by level is a crossing.** For a law reading through
the couplings and a formation outside the part into which `d` does not couple by level: wherever two histories
differing at most in the level of `d` at `s` give a positive exchange gap, the formation is not
refuted to require `d` at `s`, and the two levels do not meet its need alike. -/
theorem ExchangeLaw.Through.crosses_of_unobserved [DecidableEq C] (through : law.Through W obs part)
    (out : part h = false) (unobserved : ¬ obs h d) {l l' : Nat → C → Nat}
    (off : ∀ s' e, ¬ (s' = s ∧ e = d) → l s' e = l' s' e) (pos : 0 < law.exchangeGap t h c l l') :
    ¬ ¬ W.requires s h d ∧ ¬ (W.need s h d ≤ l s d ↔ W.need s h d ≤ l' s d) :=
  ⟨fun none => through.not_respondsByLevel out unobserved
      ⟨l, l', off, fun requires => absurd requires none, pos⟩,
   fun alike => through.not_respondsByLevel out unobserved ⟨l, l', off, fun _ => alike, pos⟩⟩

/-- Two numbers below the same bound compare alike with it. -/
theorem ble_eq_of_iff {a b b' : Nat} (iff : a ≤ b ↔ a ≤ b') : Nat.ble a b = Nat.ble a b' :=
  match hb : Nat.ble a b, hb' : Nat.ble a b' with
  | true, true => rfl
  | false, false => rfl
  | true, false =>
    Bool.noConfusion ((Nat.ble_eq_true_of_le (iff.mp (Nat.le_of_ble_eq_true hb))).symm.trans hb')
  | false, true =>
    Bool.noConfusion ((Nat.ble_eq_true_of_le (iff.mpr (Nat.le_of_ble_eq_true hb'))).symm.trans hb)

/-- Where a formation requires at a step exactly the one condition `d`, the levels admit it
exactly where they meet its need for `d`. -/
theorem Web.admits_iff_of_sole {l : C → Nat} {t : Nat} (sole : ∀ e, W.requires t h e ↔ e = d) :
    W.Admits l t h ↔ W.need t h d ≤ l d :=
  ⟨fun admits => admits d ((sole d).mpr rfl),
   fun met e requires => ((sole e).mp requires) ▸ met⟩

/-- **A law taking a crossing of the need.** Each marked formation takes, across the step from
`T` only, one unit from every condition where the level of `d` at `T` meets its need, and nothing
otherwise; nothing else is exchanged. -/
def thresholdLaw (W : Web F C) (mark : F → Bool) (d : C) (T : Nat) : ExchangeLaw F C :=
  ⟨fun t h l _ => bif mark h then
      (bif Nat.beq t T then (bif Nat.ble (W.need t h d) (l t d) then 1 else 0) else 0) else 0,
   fun _ _ _ _ => 0⟩

/-- **The law taking a crossing reads through the couplings** where every marked formation
requires at `T` exactly the one condition `d`. -/
theorem thresholdLaw_through {mark : F → Bool} {T : Nat}
    (sole : ∀ h, mark h = true → ∀ e, W.requires T h e ↔ e = d) :
    (thresholdLaw W mark d T).Through W obs part :=
  fun h _ t l l' alike _ => by
    refine ⟨?_, rfl⟩
    show cond (mark h) (cond (Nat.beq t T) (cond (Nat.ble (W.need t h d) (l t d)) 1 0) 0) 0 =
      cond (mark h) (cond (Nat.beq t T) (cond (Nat.ble (W.need t h d) (l' t d)) 1 0) 0) 0
    cases m : mark h with
    | false => rfl
    | true =>
      cases q : Nat.beq t T with
      | false => rfl
      | true =>
        have same : t = T := Nat.eq_of_beq_eq_true q
        subst same
        have admits := (alike t (Nat.le_refl t)).1
        have iff : W.need t h d ≤ l t d ↔ W.need t h d ≤ l' t d :=
          ⟨fun met => (Web.admits_iff_of_sole (sole h m)).mp
              (admits.mp ((Web.admits_iff_of_sole (sole h m)).mpr met)),
           fun met => (Web.admits_iff_of_sole (sole h m)).mp
              (admits.mpr ((Web.admits_iff_of_sole (sole h m)).mpr met))⟩
        exact congrArg (fun b => cond b 1 0) (ble_eq_of_iff iff)

/-- The levels at the need, and the level of `d` at `t` lowered to nothing in the second. -/
def loweredAt [DecidableEq C] (n t : Nat) (d : C) : Nat → C → Nat :=
  fun s e => if s = t ∧ e = d then 0 else n

/-- **The law taking a crossing responds to it** at every condition, for every marked formation
requiring `d` at `t` with a positive need. -/
theorem thresholdLaw_respondsByCrossing [DecidableEq C] {mark : F → Bool} (marked : mark h = true)
    (requires : W.requires t h d) (positive : 0 < W.need t h d) (c : C) :
    (thresholdLaw W mark d t).RespondsByCrossing W t h c t d :=
  have unmet : ¬ W.need t h d ≤ loweredAt (W.need t h d) t d t d := fun le =>
    Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le positive (Nat.le_trans le (Nat.le_of_eq (if_pos ⟨rfl, rfl⟩))))
  have below : Nat.ble (W.need t h d) (loweredAt (W.need t h d) t d t d) = false :=
    match hb : Nat.ble (W.need t h d) (loweredAt (W.need t h d) t d t d) with
    | true => absurd (Nat.le_of_ble_eq_true hb) unmet
    | false => rfl
  have before : cond (mark h)
      (cond (Nat.beq t t) (cond (Nat.ble (W.need t h d) (W.need t h d)) 1 0) 0) 0 = 1 :=
    (congrArg (fun b => cond b
      (cond (Nat.beq t t) (cond (Nat.ble (W.need t h d) (W.need t h d)) 1 0) 0) 0) marked).trans
      ((congrArg (fun b => cond b (cond (Nat.ble (W.need t h d) (W.need t h d)) 1 0) 0)
        (Loops.beq_self t)).trans
        (congrArg (fun b => cond b 1 0) (Nat.ble_eq_true_of_le (Nat.le_refl _))))
  have after : cond (mark h) (cond (Nat.beq t t)
      (cond (Nat.ble (W.need t h d) (loweredAt (W.need t h d) t d t d)) 1 0) 0) 0 = 0 :=
    (congrArg (fun b => cond b (cond (Nat.beq t t)
      (cond (Nat.ble (W.need t h d) (loweredAt (W.need t h d) t d t d)) 1 0) 0) 0) marked).trans
      ((congrArg (fun b => cond b
        (cond (Nat.ble (W.need t h d) (loweredAt (W.need t h d) t d t d)) 1 0) 0) (Loops.beq_self t)).trans
        (congrArg (fun b => cond b 1 0) below))
  ⟨fun _ _ => W.need t h d, loweredAt (W.need t h d) t d,
   fun _ _ apart => (if_neg apart).symm, requires, Nat.le_refl _, unmet,
   Nat.lt_of_lt_of_le Nat.one_pos (Nat.le_trans
     (Nat.le_of_eq ((gap_zero 1).symm.trans (congr (congrArg gap before) after).symm))
     (Nat.le_add_right _ (gap 0 0)))⟩

/-- **By threshold, a crossing passes.** For a formation outside the part requiring at `t`
exactly the one condition `d`, with a positive need: some law reading through its couplings
responds to a crossing of its need at `t`, at every condition. Conversely, where `d` does not
couple into the formation by level, a response of any law reading through the couplings to `d` is a crossing
(`ExchangeLaw.Through.crosses_of_unobserved`). -/
theorem crossing_passes [DecidableEq C] [DecidableEq F]
    (sole : ∀ e, W.requires t h e ↔ e = d) (positive : 0 < W.need t h d) :
    ∃ law : ExchangeLaw F C, law.Through W obs part ∧ ∀ c, law.RespondsByCrossing W t h c t d :=
  ⟨thresholdLaw W (fun h' => decide (h' = h)) d t,
   thresholdLaw_through fun _ m => (of_decide_eq_true m) ▸ sole,
   fun c => thresholdLaw_respondsByCrossing (mark := fun h' => decide (h' = h))
     (decide_eq_true rfl) ((sole d).mpr rfl) positive c⟩

end Crossing

/-! ## A crossing among several conditions -/

section Gate

variable {law : ExchangeLaw F C} {W : Web F C} {obs : F → C → Prop} {part : F → Bool}
  {t s : Nat} {h : F} {c d : C}

/-- **A response to a condition not coupled in by level changes admission.** For a law reading through
the couplings and a formation outside the part into which `d` does not couple by level: wherever two histories
differing at most in the level of `d` at `s` give a positive exchange gap, `s` is at most the
step of the exchange, and the two histories do not admit the formation alike at `s`. -/
theorem ExchangeLaw.Through.admission_changes_of_unobserved (through : law.Through W obs part)
    (out : part h = false) (unobserved : ¬ obs h d) {l l' : Nat → C → Nat}
    (off : ∀ s' e, ¬ (s' = s ∧ e = d) → l s' e = l' s' e) (pos : 0 < law.exchangeGap t h c l l') :
    s ≤ t ∧ ¬ (W.Admits (l s) s h ↔ W.Admits (l' s) s h) :=
  have none : (s ≤ t → (W.Admits (l s) s h ↔ W.Admits (l' s) s h)) → False := fun iff =>
    have alike := through h out t l l' fun s' le =>
      match Nat.decEq s' s with
      | isTrue same => by
          subst same
          exact ⟨iff le, fun e seen => off _ e fun both => unobserved (both.2 ▸ seen)⟩
      | isFalse other => Web.alikeThrough_of_levels fun e => off s' e fun both => other both.1
    Nat.lt_irrefl 0 ((ExchangeLaw.exchangeGap_of_alike alike c) ▸ pos)
  ⟨match Nat.decLe s t with
    | isTrue le => le
    | isFalse late => (none fun le => absurd le late).elim,
   fun iff => none fun _ => iff⟩

/-- **A crossing passes only where the other requirements are met.** Under the same conditions,
it is not refuted that every other condition the formation requires at `s` meets its need there
under the first history, and so under the second: a response to `d` alone changes admission only
where the rest of the conjunction holds. -/
theorem ExchangeLaw.Through.others_met_of_unobserved (through : law.Through W obs part)
    (out : part h = false) (unobserved : ¬ obs h d) {l l' : Nat → C → Nat}
    (off : ∀ s' e, ¬ (s' = s ∧ e = d) → l s' e = l' s' e) (pos : 0 < law.exchangeGap t h c l l') :
    ¬ ¬ ∀ e, W.requires s h e → ¬ e = d → W.need s h e ≤ l s e :=
  fun unmet => (through.admission_changes_of_unobserved out unobserved off pos).2
    ⟨fun admits => absurd (fun e requires _ => admits e requires) unmet,
     fun admits => absurd (fun e requires other => Nat.le_trans (admits e requires)
       (Nat.le_of_eq (off s e fun both => other both.2).symm)) unmet⟩

/-- **A response by a crossing needs a positive requirement.** The formation requires the
condition at the step of the level, with a positive need. -/
theorem ExchangeLaw.RespondsByCrossing.requires_pos (responds : law.RespondsByCrossing W t h c s d) :
    W.requires s h d ∧ 0 < W.need s h d :=
  let ⟨_, l', _, requires, _, unmet, _⟩ := responds
  ⟨requires, Nat.lt_of_le_of_lt (Nat.zero_le (l' s d)) (Nat.gt_of_not_le unmet)⟩

/-- Two decided propositions that are equivalent are decided alike. -/
theorem decide_eq_of_iff {p q : Prop} (dp : Decidable p) (dq : Decidable q) (iff : p ↔ q) :
    @decide p dp = @decide q dq :=
  match dp, dq with
  | isTrue _, isTrue _ => rfl
  | isFalse _, isFalse _ => rfl
  | isTrue yes, isFalse no => absurd (iff.mp yes) no
  | isFalse no, isTrue yes => absurd (iff.mpr yes) no

/-- **A law taking a decided admission.** The formation `g` takes, across every step from `T`
on, one unit from every condition where the levels at `T` admit it, and nothing otherwise;
nothing else is exchanged. Its only input is the decision of `g`'s admission at `T`. -/
def admissionLaw [DecidableEq F] (W : Web F C) (g : F) (T : Nat)
    (dec : ∀ l : C → Nat, Decidable (W.Admits l T g)) : ExchangeLaw F C :=
  ⟨fun t h l _ => bif decide (h = g) then
      (bif Nat.ble T t then (bif @decide _ (dec (l T)) then 1 else 0) else 0) else 0,
   fun _ _ _ _ => 0⟩

/-- **The law taking a decided admission reads through the couplings.** -/
theorem admissionLaw_through [DecidableEq F] {g : F} {T : Nat}
    (dec : ∀ l : C → Nat, Decidable (W.Admits l T g)) :
    (admissionLaw W g T dec).Through W obs part :=
  fun h _ t l l' alike _ => by
    refine ⟨?_, rfl⟩
    show cond (decide (h = g)) (cond (Nat.ble T t) (cond (@decide _ (dec (l T))) 1 0) 0) 0 =
      cond (decide (h = g)) (cond (Nat.ble T t) (cond (@decide _ (dec (l' T))) 1 0) 0) 0
    cases m : decide (h = g) with
    | false => rfl
    | true =>
      cases q : Nat.ble T t with
      | false => rfl
      | true =>
        have same : h = g := of_decide_eq_true m
        subst same
        exact congrArg (fun b => cond b 1 0)
          (decide_eq_of_iff (dec (l T)) (dec (l' T)) (alike T (Nat.le_of_ble_eq_true q)).1)

/-- The levels at each need of `g`, and the level of `d` at `T` lowered to nothing in the
second. -/
def needLoweredAt [DecidableEq C] (W : Web F C) (g : F) (T : Nat) (d : C) : Nat → C → Nat :=
  fun s e => if s = T ∧ e = d then 0 else W.need s g e

/-- **The law taking a decided admission responds to a crossing** of every condition `g`
requires at `T` with a positive need, across every step from `T` on, at every condition. -/
theorem admissionLaw_respondsByCrossing [DecidableEq C] [DecidableEq F] {g : F} {T : Nat}
    (dec : ∀ l : C → Nat, Decidable (W.Admits l T g)) (requires : W.requires T g d)
    (positive : 0 < W.need T g d) (late : T ≤ t) (c : C) :
    (admissionLaw W g T dec).RespondsByCrossing W t g c T d :=
  have unmet : ¬ W.need T g d ≤ needLoweredAt W g T d T d := fun le =>
    Nat.lt_irrefl 0 (Nat.lt_of_lt_of_le positive (Nat.le_trans le (Nat.le_of_eq (if_pos ⟨rfl, rfl⟩))))
  have admitted : W.Admits (fun e => W.need T g e) T g := fun _ _ => Nat.le_refl _
  have refused : ¬ W.Admits (needLoweredAt W g T d T) T g := fun admits => unmet (admits d requires)
  have before : (admissionLaw W g T dec).take t g (fun s e => W.need s g e) c = 1 := by
    show cond (decide (g = g))
      (cond (Nat.ble T t) (cond (@decide _ (dec (fun e => W.need T g e))) 1 0) 0) 0 = 1
    cases m : decide (g = g) with
    | false => exact absurd rfl (of_decide_eq_false m)
    | true =>
      cases q : Nat.ble T t with
      | false => exact Bool.noConfusion ((Nat.ble_eq_true_of_le late).symm.trans q)
      | true =>
        cases r : @decide _ (dec (fun e => W.need T g e)) with
        | false => exact absurd admitted (of_decide_eq_false r)
        | true => rfl
  have after : (admissionLaw W g T dec).take t g (needLoweredAt W g T d) c = 0 := by
    show cond (decide (g = g))
      (cond (Nat.ble T t) (cond (@decide _ (dec (needLoweredAt W g T d T))) 1 0) 0) 0 = 0
    cases m : decide (g = g) with
    | false => rfl
    | true =>
      cases q : Nat.ble T t with
      | false => rfl
      | true =>
        cases r : @decide _ (dec (needLoweredAt W g T d T)) with
        | false => rfl
        | true => exact absurd (of_decide_eq_true r) refused
  ⟨fun s e => W.need s g e, needLoweredAt W g T d,
   fun _ _ apart => (if_neg apart).symm, requires, Nat.le_refl _, unmet,
   Nat.lt_of_lt_of_le Nat.one_pos (Nat.le_trans
     (Nat.le_of_eq ((gap_zero 1).symm.trans (congr (congrArg gap before) after).symm))
     (Nat.le_add_right _ (gap 0 0)))⟩

/-- **Among several conditions, a crossing passes exactly where it is required.** For a
formation whose admission at `T` is decided: some law reading through the couplings responds to a
crossing of the level of `d` at `T`, across every step from `T` on and at every condition, exactly
where the formation requires `d` at `T` with a positive need. -/
theorem crossing_passes_iff [DecidableEq C] [DecidableEq F] {g : F} {T : Nat}
    (dec : ∀ l : C → Nat, Decidable (W.Admits l T g)) :
    (W.requires T g d ∧ 0 < W.need T g d) ↔
      ∃ law : ExchangeLaw F C, law.Through W obs part ∧
        ∀ t, T ≤ t → ∀ c, law.RespondsByCrossing W t g c T d :=
  ⟨fun ⟨requires, positive⟩ => ⟨admissionLaw W g T dec, admissionLaw_through dec,
     fun _ late c => admissionLaw_respondsByCrossing dec requires positive late c⟩,
   fun ⟨_, _, responds⟩ => (responds T (Nat.le_refl T) d).requires_pos⟩

/-- Whether levels meet a formation's need at a step for every listed condition, decided by going
through the list. -/
def metAllDec (W : Web F C) (T : Nat) (g : F) (l : C → Nat) :
    (es : List C) → Decidable (∀ e, List.Mem e es → W.need T g e ≤ l e)
  | [] => isTrue fun _ mem => nomatch mem
  | a :: es =>
    match Nat.decLe (W.need T g a) (l a), metAllDec W T g l es with
    | isTrue met, isTrue rest => isTrue fun e mem => match e, mem with
      | _, .head _ => met
      | e, .tail _ mem => rest e mem
    | isFalse unmet, _ => isFalse fun all => unmet (all a (.head _))
    | isTrue _, isFalse unmet => isFalse fun all => unmet fun e mem => all e (.tail _ mem)

/-- **A listed support decides admission.** Where the conditions a formation requires at a step
are exactly those of a list, whether levels admit it there is decided. -/
def admitsDecidableOfSupport {g : F} {T : Nat} (es : List C)
    (support : ∀ e, W.requires T g e ↔ List.Mem e es) (l : C → Nat) : Decidable (W.Admits l T g) :=
  match metAllDec W T g l es with
  | isTrue all => isTrue fun e requires => all e ((support e).mp requires)
  | isFalse unmet => isFalse fun admits => unmet fun e mem => admits e ((support e).mpr mem)

/-- **With a listed support, a crossing passes exactly where it is required.** -/
theorem crossing_passes_of_support [DecidableEq C] [DecidableEq F] {g : F} {T : Nat} (es : List C)
    (support : ∀ e, W.requires T g e ↔ List.Mem e es) :
    (W.requires T g d ∧ 0 < W.need T g d) ↔
      ∃ law : ExchangeLaw F C, law.Through W obs part ∧
        ∀ t, T ≤ t → ∀ c, law.RespondsByCrossing W t g c T d :=
  crossing_passes_iff (admitsDecidableOfSupport es support)

end Gate

end Becoming
