import Becoming.Observation

/-!
# Level coupling: where a level couples into a formation

The naming study of 17-18 October (N1, study §6.2) adopted "couples into" for what
`Web.Registers` names, in two grains: by threshold (`Web.DependsOn`) and by level (`obs`).
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
  the part, only what it registers (`ExchangeLaw.Through`): a level it neither depends on nor
  observes is coupled with strength zero (`ExchangeLaw.Through.respondsWithin_unregistered`), so a
  response comes from a condition it registers (`ExchangeLaw.Through.registers_of_respondsTo`),
  and is a route of reading in every schedule covering what it registers
  (`ExchangeLaw.Through.reads_of_respondsTo`, `ExchangeLaw.Through.couples_readCouplings`).
* **By threshold, only a crossing passes.** A change of one level that leaves its need met
  alike is a response by level (`ExchangeLaw.RespondsByLevel`). Where the formation does not
  observe the condition, no law reading through its registration responds to it by level
  (`ExchangeLaw.Through.not_respondsByLevel`): through the threshold only a crossing passes.
* **By level, the level passes.** Where it observes the condition, a law reading through its
  registration responds to it by level at every step and condition (`levelLaw`,
  `levelLaw_through`, `levelLaw_respondsByLevel`). So observing is exactly where a level can couple
  into a formation within its threshold (`not_not_obs_iff_respondsByLevel`).

**Reading (the AI's).** `obs` is not a second kind of relation beside the couplings of
`Becoming.Loops` and the readings of `Becoming.Observation`: it marks where a level can couple
into a formation by level, as `Web.DependsOn` marks where it can couple by threshold, and every
coupling a response forces lies within them. "Coupled by level" names this exactly; registration
bounds coupling, and a law's actual responses are its couplings. The double negation of the last
equivalence is the constructive form: the converse shows that a level coupling is not left out.

What is not derived: which law the rest follows, or whether an observed level is in fact
responded to (a law reading through registration may ignore what it registers); a strength's
size beyond being positive. The representation commits to discrete steps and natural amounts. No
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

/-- **An unregistered level is coupled with strength zero.** For a law reading through
registration, a level that a formation outside the part neither depends on nor observes is
coupled into its exchange with every condition, at every step, with strength zero. -/
theorem ExchangeLaw.Through.respondsWithin_unregistered (through : law.Through W obs part)
    (out : part h = false) (unregistered : ¬ W.Registers obs h d) :
    law.RespondsWithin t h c s d 0 :=
  ExchangeLaw.respondsWithin_zero_iff.mpr fun ⟨l, l', off, pos⟩ =>
    have apart : ∀ e, W.Registers obs h e → ∀ s', ¬ (s' = s ∧ e = d) := fun _ registers _ both =>
      unregistered (both.2 ▸ registers)
    have alike := through h out t l l' fun s' _ =>
      ⟨⟨fun admits e requires =>
          (off s' e (apart e (Or.inl ⟨s', requires⟩) s')) ▸ admits e requires,
        fun admits e requires =>
          (off s' e (apart e (Or.inl ⟨s', requires⟩) s')).symm ▸ admits e requires⟩,
       fun e seen => off s' e (apart e (Or.inr seen) s')⟩
    Nat.lt_irrefl 0 ((ExchangeLaw.exchangeGap_of_alike alike c) ▸ pos)

/-- **A response comes from what couples into the formation.** -/
theorem ExchangeLaw.Through.registers_of_respondsTo (through : law.Through W obs part)
    (out : part h = false) (responds : law.RespondsTo t h c s d) : ¬ ¬ W.Registers obs h d :=
  fun unregistered =>
    ExchangeLaw.respondsWithin_zero_iff.mp (through.respondsWithin_unregistered out unregistered)
      responds

/-- **A response is read in every schedule covering registration.** -/
theorem ExchangeLaw.Through.reads_of_respondsTo {reads : Nat → F → C → Bool}
    (through : law.Through W obs part)
    (cover : ∀ t h d, part h = false → W.Registers obs h d → reads t h d = true)
    (out : part h = false) (responds : law.RespondsTo t h c s d) : reads t h d = true :=
  match unread : reads t h d with
  | true => rfl
  | false => absurd responds (ExchangeLaw.respondsWithin_zero_iff.mp
      ((through.readsAt cover).respondsWithin_unread out unread c s))

/-- **A response is a route of reading.** For a law reading through registration and a schedule
covering it, a response of a formation present outside the part, to a listed level up to the
step, is a coupling of the routes of reading of `Becoming.Observation`. -/
theorem ExchangeLaw.Through.couples_readCouplings {reads : Nat → F → C → Bool} {cs : List C}
    {present : Nat → List F} (through : law.Through W obs part)
    (cover : ∀ t h d, part h = false → W.Registers obs h d → reads t h d = true)
    (responds : law.RespondsTo t h c s d) (mem : h ∈ present t) (out : part h = false)
    (le : s ≤ t) (listed : d ∈ cs) :
    Couples cs part (readCouplings fun t h _ _ d => reads t h d) present d c :=
  ⟨t, h, s, mem, out, le, listed,
   show 0 < cond (reads t h d) 1 0 from
     (through.reads_of_respondsTo cover out responds) ▸ Nat.one_pos⟩

/-- Histories with equal levels at a step register alike there. -/
theorem Web.registersAlike_of_levels {g : F} {l l' : Nat → C → Nat} {s' : Nat}
    (same : ∀ e, l s' e = l' s' e) : W.RegistersAlike obs g l l' s' :=
  ⟨⟨fun admits e requires => (same e) ▸ admits e requires,
    fun admits e requires => (same e).symm ▸ admits e requires⟩,
   fun e _ => same e⟩

/-- **By threshold, only a crossing passes.** For a law reading through registration, a formation
outside the part that does not observe a condition is not responded to by level: a change of that
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
      | isFalse other => Web.registersAlike_of_levels fun e => off s' e fun both => other both.1
    Nat.lt_irrefl 0 ((ExchangeLaw.exchangeGap_of_alike alike c) ▸ pos)

end Through

/-! ## By level, the level passes -/

section Witness

variable {W : Web F C} {obs : F → C → Prop} {part : F → Bool} {d : C}

/-- **A law taking the level it observes.** Each marked formation takes from every condition the
level of `d` at the step; nothing else is exchanged. -/
def levelLaw (mark : F → Bool) (d : C) : ExchangeLaw F C :=
  ⟨fun t h l _ => bif mark h then l t d else 0, fun _ _ _ _ => 0⟩

/-- **The law taking an observed level reads through registration.** -/
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

/-- **The law taking an observed level responds to it by level** at every step and condition,
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

/-- **Observing is exactly where a level can couple into a formation within its threshold.** For
a formation outside the part: it is not refuted that it observes the condition exactly where it
is not refuted that some law reading through its registration responds to the condition by
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

end Becoming
