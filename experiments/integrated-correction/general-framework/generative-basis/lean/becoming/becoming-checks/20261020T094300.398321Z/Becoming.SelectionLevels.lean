import Becoming.SelectionTerm

/-!
# Selection levels: selection within groups and among them

`Becoming.SelectionTerm` states the selection term proper of a family: concordance less
discordance of weight and amount over ordered pairs of members, the covariance with its
denominators cleared. Where the family is listed group by group, the same term divides into
selection within the groups and selection among them. This module states that division, the
multilevel form of Price's equation (Price 1972), for groups of equal size.

* **The division, an arithmetic identity.** List a family as `k` groups of `m` members each
  (`whole`). Read each group by its own concordance and discordance, summed over the groups
  (`concordWithin`, `discordWithin`), and the groups as members read by their totals of weight
  and amount (`concordAmong`, `discordAmong`). Then the whole's concordance, with `k` times the
  groups' discordance and the discordance among groups, is the whole's discordance, with `k`
  times the groups' concordance and the concordance among groups (`levels`). Read over the
  rationals and divided through, the whole's covariance of weight and amount is the mean of the
  groups' own covariances with the covariance of the groups' means: the law of total covariance,
  Price's partition of selection into within-group and between-group parts. It rests on the
  covariation of the whole, of each group, and of the groups read by their totals
  (`SelectionTerm.covariation`), with the family's totals the sums of the groups' (`whole_total`,
  `whole_weighted`, `whole_length`).
* **Which level wins.** So the whole's selection term is positive exactly where the concordance
  among groups with `k` times the groups' concordance exceeds the discordance among groups with
  `k` times the groups' discordance (`rises_iff`), and none exactly where they are equal
  (`none_iff`). Where selection within the groups goes against the amount, the whole selects for
  it only where selection among the groups goes for it (`among_for_of_rises`), and conversely
  (`within_for_of_rises`). Where every group is uniform in amount, or in weight, nothing is
  selected within them and the whole's selection is selection among groups alone
  (`within_none_of_uniform`, `levels_of_uniform`); where the groups' totals are all alike,
  nothing is selected among them and the whole's selection is `k` times selection within
  (`among_none_of_alike`, `levels_of_alike`).
* **Over generations.** In listed generations (`SelectionTerm.Generations`) with exact
  transmission, a generation listed as groups of equal size raises its mean amount across the step
  exactly where, read by offspring number, the among-group and `k` times the within-group
  concordance exceed the corresponding discordances (`rises_exact_iff_levels`); so an amount
  selected against within the groups has its mean rise only where selection among them goes for
  it (`among_for_of_raises`).
* **Witnesses.** Two groups of two, the amount one at a member that holds back and none at the
  others. In both, the one holding back leaves fewer offspring than its groupmate, so selection
  within goes against holding back. Where the group without it leaves no offspring, selection
  among groups goes for holding back and outweighs it: the whole selects for it (`AmongWins`).
  Where the group without it leaves as many as its members can, selection among groups goes
  against holding back as well, and the whole selects against it (`WithinWins`).

The weights are any natural numbers; with offspring numbers they are the selection term proper
of `Becoming.SelectionTerm` divided by level. Nothing is supposed about what the groups are or
why their members' offspring numbers differ: which level wins is read off the counts, not
explained. Modelling choices: natural-number weights and amounts, finite families as lists,
groups of equal size (with unequal sizes the division weights each group's own term by the
whole's size over the group's, which is not stated). No ethical predicate, ranking or axiom
occurs; every declaration has an empty axiom report.
-/

namespace Becoming

namespace SelectionLevels

open SelectionTerm

variable {α : Type}

/-! ## The family listed by groups -/

/-- The family listed group by group. -/
def whole (gs : List (List α)) : List α := gs.flatMap id

/-- A total over the family is the sum of the groups' totals. -/
theorem whole_total (gs : List (List α)) (q : α → Nat) :
    total (whole gs) q = total gs fun g => total g q :=
  match gs with
  | [] => rfl
  | g :: gs => (total_append q (whole gs) g).trans (congrArg (total g q + ·) (whole_total gs q))

/-- So is the weighted total. -/
theorem whole_weighted (gs : List (List α)) (w a : α → Nat) :
    weighted (whole gs) w a = total gs fun g => weighted g w a :=
  whole_total gs fun p => w p * a p

/-- And the number of members. -/
theorem whole_length (gs : List (List α)) : (whole gs).length = total gs fun g => g.length :=
  (total_ones (whole gs)).symm.trans
    ((whole_total gs fun _ => 1).trans (total_congr (fun g => total_ones g) gs))

/-- Totals agreeing at every member agree. -/
theorem total_eq_of_mem {p q : α → Nat} : ∀ {as : List α}, (∀ a, a ∈ as → p a = q a) →
    total as p = total as q
  | [], _ => rfl
  | a :: _, same => Naturals.add_congr (same a (.head _))
      (total_eq_of_mem fun b mem => same b (.tail a mem))

/-- With groups of `m` members each, the family has `k` times `m`. -/
theorem whole_length_of_equal {gs : List (List α)} {m : Nat} (equal : ∀ g, g ∈ gs → g.length = m) :
    (whole gs).length = gs.length * m :=
  (whole_length gs).trans ((total_eq_of_mem equal).trans (total_const m gs))

/-- The groups' own concordance, summed over the groups. -/
def concordWithin (gs : List (List α)) (w a : α → Nat) : Nat := total gs fun g => concord g w a

/-- The groups' own discordance, summed over the groups. -/
def discordWithin (gs : List (List α)) (w a : α → Nat) : Nat := total gs fun g => discord g w a

/-- Concordance among the groups, each read by its totals of weight and amount. -/
def concordAmong (gs : List (List α)) (w a : α → Nat) : Nat :=
  concord gs (fun g => total g w) (fun g => total g a)

/-- Discordance among the groups, each read by its totals of weight and amount. -/
def discordAmong (gs : List (List α)) (w a : α → Nat) : Nat :=
  discord gs (fun g => total g w) (fun g => total g a)

/-! ## The division -/

theorem lhs_shape (a c s x p y : Nat) : a + c + (s + x) + (p + y) = c + x + y + (a + s + p) :=
  (congrArg (· + (p + y)) (Nat.add_add_add_comm a c s x)).trans
    ((Nat.add_add_add_comm (a + s) (c + x) p y).trans (Nat.add_comm _ _))

theorem rhs_shape (s d p x a y : Nat) : s + d + (p + x) + (a + y) = d + x + y + (a + s + p) :=
  (congrArg (· + (a + y)) (Nat.add_add_add_comm s d p x)).trans
    ((Nat.add_add_add_comm (s + p) (d + x) a y).trans
      ((Nat.add_comm _ _).trans (congrArg (d + x + y + ·)
        ((Nat.add_comm (s + p) a).trans (Nat.add_assoc a s p).symm))))

/-- Selection within groups and among them, for `k` groups of equal size: the whole's
concordance, with `k` times the groups' own discordance and the discordance among groups, is the
whole's discordance, with `k` times the groups' own concordance and the concordance among groups.
Divided through, the whole's covariance is the mean of the groups' covariances with the
covariance of their means. No premise beyond the equal sizes. -/
theorem levels (gs : List (List α)) (w a : α → Nat) {m : Nat}
    (equal : ∀ g, g ∈ gs → g.length = m) :
    concord (whole gs) w a + (gs.length * discordWithin gs w a + discordAmong gs w a) =
      discord (whole gs) w a + (gs.length * concordWithin gs w a + concordAmong gs w a) :=
  have whole_cov : gs.length * m * (total gs fun g => weighted g w a) + discord (whole gs) w a =
      (total gs fun g => total g w) * (total gs fun g => total g a) + concord (whole gs) w a := by
    have h := covariation (whole gs) w a
    rw [whole_length_of_equal equal, whole_weighted, whole_total, whole_total] at h
    exact h
  have groups : m * (total gs fun g => weighted g w a) + discordWithin gs w a =
      (total gs fun g => total g w * total g a) + concordWithin gs w a :=
    (Naturals.add_congr (total_mul m _ gs).symm rfl).trans ((total_add _ _ gs).symm.trans
      ((total_eq_of_mem fun g mg => by
        have h := covariation g w a
        rw [equal g mg] at h
        exact h).trans (total_add _ _ gs)))
  have scaled : gs.length * m * (total gs fun g => weighted g w a) + gs.length * discordWithin gs w a =
      gs.length * (total gs fun g => total g w * total g a) + gs.length * concordWithin gs w a :=
    (Naturals.add_congr (mul_assoc_nat _ _ _) rfl).trans
      ((Nat.left_distrib _ _ _).symm.trans ((congrArg (gs.length * ·) groups).trans
        (Nat.left_distrib _ _ _)))
  have among : gs.length * (total gs fun g => total g w * total g a) + discordAmong gs w a =
      (total gs fun g => total g w) * (total gs fun g => total g a) + concordAmong gs w a :=
    covariation gs (fun g => total g w) (fun g => total g a)
  have summed :
      (total gs fun g => total g w) * (total gs fun g => total g a) + concord (whole gs) w a +
          (gs.length * m * (total gs fun g => weighted g w a) + gs.length * discordWithin gs w a) +
          (gs.length * (total gs fun g => total g w * total g a) + discordAmong gs w a) =
        gs.length * m * (total gs fun g => weighted g w a) + discord (whole gs) w a +
          (gs.length * (total gs fun g => total g w * total g a) + gs.length * concordWithin gs w a) +
          ((total gs fun g => total g w) * (total gs fun g => total g a) + concordAmong gs w a) := by
    rw [← whole_cov, scaled, among]
  (Nat.add_assoc _ _ _).symm.trans ((Naturals.add_right_cancel
    ((lhs_shape _ _ _ _ _ _).symm.trans (summed.trans (rhs_shape _ _ _ _ _ _)))).trans
    (Nat.add_assoc _ _ _))

/-- The whole selects for the amount exactly where the concordance among groups with `k` times
the groups' concordance exceeds the discordance among groups with `k` times the groups'
discordance. -/
theorem rises_iff (gs : List (List α)) (w a : α → Nat) {m : Nat}
    (equal : ∀ g, g ∈ gs → g.length = m) :
    discord (whole gs) w a < concord (whole gs) w a ↔
      gs.length * discordWithin gs w a + discordAmong gs w a <
        gs.length * concordWithin gs w a + concordAmong gs w a :=
  lt_iff_of_balance (levels gs w a equal)

/-- And selects nothing exactly where they are equal. -/
theorem none_iff (gs : List (List α)) (w a : α → Nat) {m : Nat}
    (equal : ∀ g, g ∈ gs → g.length = m) :
    discord (whole gs) w a = concord (whole gs) w a ↔
      gs.length * discordWithin gs w a + discordAmong gs w a =
        gs.length * concordWithin gs w a + concordAmong gs w a :=
  eq_iff_of_balance (levels gs w a equal)

/-- Where selection within the groups goes against the amount, the whole selects for it only
where selection among the groups goes for it. -/
theorem among_for_of_rises (gs : List (List α)) (w a : α → Nat) {m : Nat}
    (equal : ∀ g, g ∈ gs → g.length = m)
    (against : concordWithin gs w a ≤ discordWithin gs w a)
    (rises : discord (whole gs) w a < concord (whole gs) w a) :
    discordAmong gs w a < concordAmong gs w a :=
  Nat.lt_of_add_lt_add_left (Nat.lt_of_le_of_lt
    (Nat.add_le_add_right (Nat.mul_le_mul_left _ against) _)
    ((rises_iff gs w a equal).mp rises))

/-- And where selection among the groups goes against it, the whole selects for it only where
selection within the groups goes for it. -/
theorem within_for_of_rises (gs : List (List α)) (w a : α → Nat) {m : Nat}
    (equal : ∀ g, g ∈ gs → g.length = m)
    (against : concordAmong gs w a ≤ discordAmong gs w a)
    (rises : discord (whole gs) w a < concord (whole gs) w a) :
    discordWithin gs w a < concordWithin gs w a :=
  lt_of_mul_lt_mul (m := gs.length) (Nat.lt_of_add_lt_add_right (Nat.lt_of_le_of_lt
    (Nat.add_le_add_left against _) ((rises_iff gs w a equal).mp rises)))

/-- Where every group is uniform in amount, nothing is selected within the groups. -/
theorem within_none_of_uniform {gs : List (List α)} {w a : α → Nat}
    (uniform : ∀ g, g ∈ gs → ∃ c, ∀ p, p ∈ g → a p = c) :
    concordWithin gs w a = 0 ∧ discordWithin gs w a = 0 :=
  ⟨total_zero_of fun g mg => match uniform g mg with
      | ⟨_, same⟩ => concord_alike same w,
    total_zero_of fun g mg => match uniform g mg with
      | ⟨_, same⟩ => discord_alike same w⟩

/-- So the whole's selection is selection among groups alone. -/
theorem levels_of_uniform (gs : List (List α)) (w a : α → Nat) {m : Nat}
    (equal : ∀ g, g ∈ gs → g.length = m) (uniform : ∀ g, g ∈ gs → ∃ c, ∀ p, p ∈ g → a p = c) :
    concord (whole gs) w a + discordAmong gs w a = discord (whole gs) w a + concordAmong gs w a := by
  have h := levels gs w a equal
  rw [(within_none_of_uniform uniform).1, (within_none_of_uniform uniform).2, Nat.mul_zero,
    Nat.zero_add, Nat.zero_add] at h
  exact h

/-- Where the groups' totals of amount are all alike, nothing is selected among the groups. -/
theorem among_none_of_alike {gs : List (List α)} {w a : α → Nat} {c : Nat}
    (alike : ∀ g, g ∈ gs → total g a = c) :
    concordAmong gs w a = 0 ∧ discordAmong gs w a = 0 :=
  ⟨concord_alike alike _, discord_alike alike _⟩

/-- So the whole's selection is `k` times selection within the groups. -/
theorem levels_of_alike (gs : List (List α)) (w a : α → Nat) {m c : Nat}
    (equal : ∀ g, g ∈ gs → g.length = m) (alike : ∀ g, g ∈ gs → total g a = c) :
    concord (whole gs) w a + gs.length * discordWithin gs w a =
      discord (whole gs) w a + gs.length * concordWithin gs w a := by
  have h := levels gs w a equal
  rw [(among_none_of_alike alike).1, (among_none_of_alike alike).2, Nat.add_zero, Nat.add_zero] at h
  exact h

/-! ## Over generations -/

/-- Over listed generations with exact transmission, a generation listed as groups of equal size:
its mean amount rises across the step exactly where, read by offspring number, the concordance
among groups with `k` times the groups' own concordance exceeds the discordance among groups with
`k` times the groups' own discordance. -/
theorem rises_exact_iff_levels (G : Generations α) {t m : Nat} (gs : List (List α))
    (listed : whole gs = G.family t) (equal : ∀ g, g ∈ gs → g.length = m)
    (exact : Exact (G.family t) (G.kids t) (G.amount t) (G.amount (t + 1))) :
    G.Raises t ↔
      gs.length * discordWithin gs (G.offspringNumber t) (G.amount t) +
          discordAmong gs (G.offspringNumber t) (G.amount t) <
        gs.length * concordWithin gs (G.offspringNumber t) (G.amount t) +
          concordAmong gs (G.offspringNumber t) (G.amount t) :=
  (G.raises_exact_iff exact).trans (by
    unfold Generations.concordAt Generations.discordAt
    rw [← listed]
    exact rises_iff gs _ _ equal)

/-- So, with exact transmission, where selection within the groups goes against the amount, its
mean rises only where selection among the groups goes for it. -/
theorem among_for_of_raises (G : Generations α) {t m : Nat} (gs : List (List α))
    (listed : whole gs = G.family t) (equal : ∀ g, g ∈ gs → g.length = m)
    (exact : Exact (G.family t) (G.kids t) (G.amount t) (G.amount (t + 1)))
    (against : concordWithin gs (G.offspringNumber t) (G.amount t) ≤
      discordWithin gs (G.offspringNumber t) (G.amount t))
    (raises : G.Raises t) :
    discordAmong gs (G.offspringNumber t) (G.amount t) <
      concordAmong gs (G.offspringNumber t) (G.amount t) :=
  Nat.lt_of_add_lt_add_left (Nat.lt_of_le_of_lt
    (Nat.add_le_add_right (Nat.mul_le_mul_left _ against) _)
    ((rises_exact_iff_levels G gs listed equal exact).mp raises))

/-! ## Witnesses -/

/-- Four members: one holding back, its groupmate, and the two members of the other group. -/
inductive Member where
  | held
  | mate
  | first
  | second

open Member

/-- One at the member holding back, none at the others. -/
def holds : Member → Nat
  | held => 1
  | mate => 0
  | first => 0
  | second => 0

/-- The group with the member holding back, and the group without. -/
def groups : List (List Member) := [[held, mate], [first, second]]

theorem equal : ∀ g, g ∈ groups → g.length = 2
  | _, .head _ => rfl
  | _, .tail _ (.head _) => rfl
  | _, .tail _ (.tail _ mem) => nomatch mem

namespace AmongWins

/-- The member holding back leaves two offspring and its groupmate three; the group without it
leaves none. -/
def offspring : Member → Nat
  | held => 2
  | mate => 3
  | first => 0
  | second => 0

/-- Within the groups, holding back is selected against (discordance one, concordance none);
among them, for (concordance five, discordance none); the whole selects for it (concordance four,
discordance one). -/
theorem among_wins :
    concordWithin groups offspring holds = 0 ∧ discordWithin groups offspring holds = 1 ∧
      concordAmong groups offspring holds = 5 ∧ discordAmong groups offspring holds = 0 ∧
      concord (whole groups) offspring holds = 4 ∧ discord (whole groups) offspring holds = 1 ∧
      discord (whole groups) offspring holds < concord (whole groups) offspring holds :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl, by decide⟩

end AmongWins

namespace WithinWins

/-- The member holding back leaves two offspring and its groupmate three; each member of the
group without it leaves three. -/
def offspring : Member → Nat
  | held => 2
  | mate => 3
  | first => 3
  | second => 3

/-- Within the groups, holding back is selected against; among them, against as well (the group
with it leaves five, the group without six); the whole selects against it (concordance none,
discordance three). -/
theorem within_wins :
    concordWithin groups offspring holds = 0 ∧ discordWithin groups offspring holds = 1 ∧
      concordAmong groups offspring holds = 0 ∧ discordAmong groups offspring holds = 1 ∧
      concord (whole groups) offspring holds = 0 ∧ discord (whole groups) offspring holds = 3 :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩

end WithinWins

end SelectionLevels

end Becoming
