import Becoming.Feedback

/-!
# Cuts: which links a closure needs, and how growth by attachment makes every link needed

`Becoming.Feedback` reads a relation among formations through its closures: `g` lies within `f`'s
closure where every region closed under the relation that holds `f` holds `g` (`WithinClosure`),
and a region certifies a closure where it holds the formation, is closed and is reached
(`closure_iff_certified`). This module states, with no premise beyond the hypotheses each statement
names, what removing links and joining links do to closures, and what growth by attachment does to
every link it forms. Every statement holds for any relation on any type of formations.

* **A cut changes no closure exactly where every removed link is bypassed.** Removing the links of
  `added` from a relation leaves every closure as it was exactly where the ends of each removed
  link stay within each other's closure under what remains (`closure_unchanged_iff_bypassed`). For
  one link read both ways, this is that each end stays within the other's closure
  (`link_cut_unchanged_iff`), and under a symmetric relation that one end stays within the other's
  (`link_cut_unchanged_iff_of_symm`).
* **Joining one link.** After a link between `a` and `b` is joined, `g` lies within `f`'s closure
  exactly where it did before, or `f` reaches one end and the other end reaches `g`
  (`within_link_iff`). No symmetry and no decision is used.
* **Attaching a formation that takes part in no link.** Such a formation reaches only itself
  (`within_of_unlinked`) and nothing else reaches it (`not_within_unlinked`). So attaching it by
  one link changes no closure among the other formations (`within_attached_iff`), and the link
  that attaches it is needed: its ends lie apart without it.
* **Every link of a relation grown by attachment separates its ends.** A list of links in which
  each attaches a formation that took part in no earlier link (`Attaches`) grows a relation
  (`Links`). Removing any one of its links leaves that link's ends apart
  (`attached_link_separates`), whatever links came before or after it. The links are each read
  both ways (`links_symm`), and the list's order of growth is not used beyond attachment.
* **After one join, a grown link is bypassed exactly where the join crosses it.** Joining one more
  link between `a` and `b` to a relation grown by attachment, the ends of a grown link are joined
  without it exactly where `a` and `b` lie on its two sides (`joined_bypass_iff`), and cutting it
  then changes no closure exactly there (`joined_cut_unchanged_iff`).
* **Which conditions a system needs.** A formation's system is its closure under sharing a
  condition (`Flow.WithinSystem`). Sharing a condition is sharing one other than `c` or both taking
  part in `c` (`Flow.shares_iff_beside`, with equality of conditions decided). So every system is
  what it is through the other conditions alone exactly where any two formations taking part in
  `c` lie in one system through the other conditions (`Flow.system_unchanged_without_iff`); a
  condition only one formation takes part in is needed by no system
  (`Flow.system_unchanged_of_single`); and a formation that takes part in no condition has only
  itself in its system and lies in no other's (`Flow.withinSystem_of_no_part`). A condition
  exactly two formations take part in joins their systems as one link would
  (`Flow.withinSystem_two_takers_iff`), and a formation that takes part only in `c` is alone
  without it (`Flow.alone_beside_of_only`).

What is not derived: which links form, which are cut, or when; how much a cut or a join takes;
what the formations on either side do afterwards; any count of links or formations. Removing a
link that is bypassed still removes it: the relation is smaller and only its closures stay.
-/

namespace Becoming

namespace Cuts

variable {F : Type}

/-! ## Joining links and cutting them -/

/-- The relation with the links of `added` joined to it. -/
def Joined (rel added : F → F → Prop) (g h : F) : Prop := rel g h ∨ added g h

/-- The single link between `a` and `b`, read both ways. -/
def Link (a b : F) (g h : F) : Prop := (g = a ∧ h = b) ∨ (g = b ∧ h = a)

/-- A link read both ways is symmetric. -/
theorem link_symm {a b g h : F} (link : Link a b g h) : Link a b h g :=
  link.elim (fun ⟨ga, hb⟩ => Or.inr ⟨hb, ga⟩) (fun ⟨gb, ha⟩ => Or.inl ⟨ha, gb⟩)

/-- Relations with the same links have the same closures. -/
theorem within_congr {rel rel' : F → F → Prop} (same : ∀ g h, rel g h ↔ rel' g h) {f g : F} :
    WithinClosure rel f g ↔ WithinClosure rel' f g :=
  ⟨WithinClosure.mono (fun x y r => (same x y).mp r),
   WithinClosure.mono (fun x y r => (same x y).mpr r)⟩

/-- Where each link of one relation lies within a closure under another, so does each closure. -/
theorem within_of_steps {rel rel' : F → F → Prop} (steps : ∀ g h, rel g h → WithinClosure rel' g h)
    {f g : F} (within : WithinClosure rel f g) : WithinClosure rel' f g :=
  within (WithinClosure rel' f)
    (fun _ y reached related => reached.trans (steps _ y related)) (WithinClosure.refl f)

/-- **A cut changes no closure exactly where every removed link is bypassed.** Removing the links of
`added` leaves every closure as it was exactly where each removed link's ends stay within each
other's closure under what remains. -/
theorem closure_unchanged_iff_bypassed {rel added : F → F → Prop} :
    (∀ f g, WithinClosure (Joined rel added) f g ↔ WithinClosure rel f g) ↔
      ∀ g h, added g h → WithinClosure rel g h :=
  ⟨fun same g h link => (same g h).mp (WithinClosure.of_rel (Or.inr link)),
   fun bypassed f _ =>
    ⟨fun within =>
      within (WithinClosure rel f)
        (fun x y reached related => related.elim
          (fun r => reached.trans (WithinClosure.of_rel r))
          (fun l => reached.trans (bypassed x y l)))
        (WithinClosure.refl f),
     WithinClosure.mono (fun _ _ r => Or.inl r)⟩⟩

/-- **Cutting one link changes no closure exactly where its ends stay within each other's
closure.** -/
theorem link_cut_unchanged_iff {rel : F → F → Prop} {a b : F} :
    (∀ f g, WithinClosure (Joined rel (Link a b)) f g ↔ WithinClosure rel f g) ↔
      WithinClosure rel a b ∧ WithinClosure rel b a :=
  closure_unchanged_iff_bypassed.trans
    ⟨fun bypassed => ⟨bypassed a b (Or.inl ⟨rfl, rfl⟩), bypassed b a (Or.inr ⟨rfl, rfl⟩)⟩,
     fun ⟨ab, ba⟩ g h link => link.elim
      (fun ⟨ga, hb⟩ => by subst ga; subst hb; exact ab)
      (fun ⟨gb, ha⟩ => by subst gb; subst ha; exact ba)⟩

/-- **Under a symmetric relation, cutting one link changes no closure exactly where one end stays
within the other's closure.** -/
theorem link_cut_unchanged_iff_of_symm {rel : F → F → Prop} {a b : F}
    (symmetric : ∀ g h, rel g h → rel h g) :
    (∀ f g, WithinClosure (Joined rel (Link a b)) f g ↔ WithinClosure rel f g) ↔
      WithinClosure rel a b :=
  link_cut_unchanged_iff.trans ⟨And.left, fun ab => ⟨ab, WithinClosure.symm symmetric ab⟩⟩

/-- **The closure after joining one link.** `g` lies within `f`'s closure once a link between `a`
and `b` is joined exactly where it did before, or `f` reaches one end and the other end reaches
`g`. -/
theorem within_link_iff {rel : F → F → Prop} {a b f g : F} :
    WithinClosure (Joined rel (Link a b)) f g ↔
      WithinClosure rel f g ∨ (WithinClosure rel f a ∧ WithinClosure rel b g) ∨
        (WithinClosure rel f b ∧ WithinClosure rel a g) := by
  constructor
  · intro within
    refine within (fun y => WithinClosure rel f y ∨ (WithinClosure rel f a ∧ WithinClosure rel b y) ∨
        (WithinClosure rel f b ∧ WithinClosure rel a y)) ?_ (Or.inl (WithinClosure.refl f))
    intro x y reached related
    cases related with
    | inl r =>
      have step : WithinClosure rel x y := WithinClosure.of_rel r
      rcases reached with direct | ⟨fa, bx⟩ | ⟨fb, ax⟩
      · exact Or.inl (direct.trans step)
      · exact Or.inr (Or.inl ⟨fa, bx.trans step⟩)
      · exact Or.inr (Or.inr ⟨fb, ax.trans step⟩)
    | inr l =>
      rcases l with ⟨xa, yb⟩ | ⟨xb, ya⟩
      · subst xa; subst yb
        rcases reached with fa | ⟨fa, _⟩ | ⟨fb, _⟩
        · exact Or.inr (Or.inl ⟨fa, WithinClosure.refl _⟩)
        · exact Or.inr (Or.inl ⟨fa, WithinClosure.refl _⟩)
        · exact Or.inl fb
      · subst xb; subst ya
        rcases reached with fb | ⟨fa, _⟩ | ⟨fb, _⟩
        · exact Or.inr (Or.inr ⟨fb, WithinClosure.refl _⟩)
        · exact Or.inl fa
        · exact Or.inr (Or.inr ⟨fb, WithinClosure.refl _⟩)
  · intro reached
    have lift : ∀ {x y : F}, WithinClosure rel x y → WithinClosure (Joined rel (Link a b)) x y :=
      fun within => WithinClosure.mono (fun _ _ r => Or.inl r) within
    have forth : WithinClosure (Joined rel (Link a b)) a b :=
      WithinClosure.of_rel (Or.inr (Or.inl ⟨rfl, rfl⟩))
    have back : WithinClosure (Joined rel (Link a b)) b a :=
      WithinClosure.of_rel (Or.inr (Or.inr ⟨rfl, rfl⟩))
    rcases reached with direct | ⟨fa, bg⟩ | ⟨fb, ag⟩
    · exact lift direct
    · exact (lift fa).trans (forth.trans (lift bg))
    · exact (lift fb).trans (back.trans (lift ag))

/-! ## Attaching a formation that takes part in no link -/

/-- `n` takes part in no link of the relation. -/
def Unlinked (rel : F → F → Prop) (n : F) : Prop := ∀ g, ¬ rel g n ∧ ¬ rel n g

/-- **An unlinked formation reaches only itself.** -/
theorem within_of_unlinked {rel : F → F → Prop} {n g : F} (unlinked : Unlinked rel n)
    (within : WithinClosure rel n g) : g = n :=
  within (fun x => x = n)
    (fun x y same related => absurd (show rel n y by subst same; exact related) (unlinked y).2) rfl

/-- **Nothing else reaches an unlinked formation.** -/
theorem not_within_unlinked {rel : F → F → Prop} {n f : F} (unlinked : Unlinked rel n)
    (other : f ≠ n) : ¬ WithinClosure rel f n :=
  fun within => within (fun x => x ≠ n)
    (fun g _ _ related same => (unlinked g).1 (by subst same; exact related)) other rfl

/-- **Attaching an unlinked formation changes no closure among the others.** -/
theorem within_attached_iff {rel : F → F → Prop} {p n f g : F} (unlinked : Unlinked rel n)
    (hf : f ≠ n) (hg : g ≠ n) :
    WithinClosure (Joined rel (Link p n)) f g ↔ WithinClosure rel f g :=
  within_link_iff.trans
    ⟨fun reached => reached.elim id (fun via => via.elim
      (fun ⟨_, ng⟩ => absurd (within_of_unlinked unlinked ng) hg)
      (fun ⟨fn, _⟩ => absurd fn (not_within_unlinked unlinked hf))),
     Or.inl⟩

/-! ## Growth by attachment -/

/-- The links listed, each read both ways; the first listed is the latest. -/
def Links : List (F × F) → F → F → Prop
  | [] => fun _ _ => False
  | e :: rest => Joined (Links rest) (Link e.1 e.2)

/-- The listed links are symmetric. -/
theorem links_symm : ∀ {es : List (F × F)} {g h : F}, Links es g h → Links es h g
  | [], _, _, linked => linked.elim
  | _ :: _, _, _, linked => linked.elim (fun r => Or.inl (links_symm r)) (fun l => Or.inr (link_symm l))

/-- **One listed link, set apart from the rest.** -/
theorem links_split {e : F × F} : ∀ {newer : List (F × F)} {older : List (F × F)} {g h : F},
    Links (newer ++ e :: older) g h ↔ Joined (Links (newer ++ older)) (Link e.1 e.2) g h
  | [], _, _, _ => Iff.rfl
  | _ :: _, _, _, _ =>
    ⟨fun linked => linked.elim
      (fun r => (links_split.mp r).elim (fun r' => Or.inl (Or.inl r')) Or.inr)
      (fun l => Or.inl (Or.inr l)),
     fun linked => linked.elim
      (fun r => r.elim (fun r' => Or.inl (links_split.mpr (Or.inl r'))) Or.inr)
      (fun l => Or.inl (links_split.mpr (Or.inr l)))⟩

/-- Grown by attachment: each listed link attaches, to a formation other than itself, a formation
that took part in no earlier link. -/
inductive Attaches : List (F × F) → Prop
  | nil : Attaches []
  | cons {p n : F} {rest : List (F × F)} :
      Attaches rest → Unlinked (Links rest) n → p ≠ n → Attaches ((p, n) :: rest)

/-- A listed link is a link of the listed relation. -/
theorem links_of_mem : ∀ {es : List (F × F)} {e : F × F}, e ∈ es → Links es e.1 e.2
  | _ :: _, _, .head _ => Or.inr (Or.inl ⟨rfl, rfl⟩)
  | _ :: _, _, .tail _ later => Or.inl (links_of_mem later)

/-- Without its latest links, what grew by attachment is grown by attachment. -/
theorem Attaches.suffix : ∀ {newer rest : List (F × F)}, Attaches (newer ++ rest) → Attaches rest
  | [], _, grown => grown
  | _ :: _, _, grown =>
    match grown with
    | .cons earlier _ _ => Attaches.suffix earlier

/-- **Each link grown by attachment is listed once.** -/
theorem Attaches.listed_once {p n : F} : ∀ {newer older : List (F × F)},
    Attaches (newer ++ (p, n) :: older) → ¬ (p, n) ∈ newer ∧ ¬ (p, n) ∈ older
  | [], older, grown =>
    match grown with
    | .cons _ unlinked _ =>
      ⟨fun listed => (nomatch listed),
       fun listed => (unlinked p).1 (links_of_mem (es := older) (e := (p, n)) listed)⟩
  | (q, m) :: newer, older, grown =>
    match (grown : Attaches ((q, m) :: (newer ++ (p, n) :: older))) with
    | .cons rest unlinked _ =>
      ⟨fun listed => by
        cases listed with
        | head => exact (unlinked p).1 (links_split.mpr (Or.inr (Or.inl ⟨rfl, rfl⟩)))
        | tail _ later => exact (Attaches.listed_once rest).1 later,
       (Attaches.listed_once rest).2⟩

/-- **Every link of a relation grown by attachment separates its ends.** Removing any one listed
link leaves its ends apart, whatever links came before or after it. -/
theorem attached_link_separates {p n : F} : ∀ {newer older : List (F × F)},
    Attaches (newer ++ (p, n) :: older) → ¬ WithinClosure (Links (newer ++ older)) p n
  | [], _, grown =>
    match grown with
    | .cons _ unlinked distinct => not_within_unlinked unlinked distinct
  | (q, m) :: newer, older, grown =>
    match (grown : Attaches ((q, m) :: (newer ++ (p, n) :: older))) with
    | .cons rest unlinked _ => by
      have keeps : ∀ {g h : F}, Links (newer ++ older) g h → Links (newer ++ (p, n) :: older) g h :=
        fun r => links_split.mpr (Or.inl r)
      have present : Links (newer ++ (p, n) :: older) p n := links_split.mpr (Or.inr (Or.inl ⟨rfl, rfl⟩))
      have unlinked' : Unlinked (Links (newer ++ older)) m :=
        fun g => ⟨fun r => (unlinked g).1 (keeps r), fun r => (unlinked g).2 (keeps r)⟩
      have pm : p ≠ m := fun same => (unlinked n).2 (by subst same; exact present)
      have nm : n ≠ m := fun same => (unlinked p).1 (by subst same; exact present)
      intro within
      exact attached_link_separates rest ((within_attached_iff unlinked' pm nm).mp within)

/-- **After one join, a grown link is bypassed exactly where the join crosses it.** In a relation
grown by attachment with one more link joined between `a` and `b`, the ends of a grown link are
joined without it exactly where `a` and `b` lie on its two sides. -/
theorem joined_bypass_iff {p n a b : F} {newer older : List (F × F)}
    (grown : Attaches (newer ++ (p, n) :: older)) :
    WithinClosure (Joined (Links (newer ++ older)) (Link a b)) p n ↔
      (WithinClosure (Links (newer ++ older)) p a ∧ WithinClosure (Links (newer ++ older)) b n) ∨
        (WithinClosure (Links (newer ++ older)) p b ∧ WithinClosure (Links (newer ++ older)) a n) :=
  within_link_iff.trans
    ⟨fun reached => reached.elim (fun direct => absurd direct (attached_link_separates grown)) id,
     Or.inr⟩

/-- **After one join, cutting a grown link changes no closure exactly where the join crosses it.** -/
theorem joined_cut_unchanged_iff {p n a b : F} {newer older : List (F × F)}
    (grown : Attaches (newer ++ (p, n) :: older)) :
    (∀ f g, WithinClosure (Joined (Links (newer ++ (p, n) :: older)) (Link a b)) f g ↔
        WithinClosure (Joined (Links (newer ++ older)) (Link a b)) f g) ↔
      (WithinClosure (Links (newer ++ older)) p a ∧ WithinClosure (Links (newer ++ older)) b n) ∨
        (WithinClosure (Links (newer ++ older)) p b ∧ WithinClosure (Links (newer ++ older)) a n) := by
  have regroup : ∀ f g, WithinClosure (Joined (Links (newer ++ (p, n) :: older)) (Link a b)) f g ↔
      WithinClosure (Joined (Joined (Links (newer ++ older)) (Link a b)) (Link p n)) f g :=
    fun _ _ => within_congr fun x y =>
      ⟨fun r => r.elim
        (fun l => (links_split.mp l).elim (fun l' => Or.inl (Or.inl l')) Or.inr)
        (fun j => Or.inl (Or.inr j)),
       fun r => r.elim
        (fun r' => r'.elim (fun l' => Or.inl (links_split.mpr (Or.inl l'))) Or.inr)
        (fun l => Or.inl (links_split.mpr (Or.inr l)))⟩
  have symmetric : ∀ g h, Joined (Links (newer ++ older)) (Link a b) g h →
      Joined (Links (newer ++ older)) (Link a b) h g :=
    fun _ _ r => r.elim (fun l => Or.inl (links_symm l)) (fun l => Or.inr (link_symm l))
  exact (⟨fun same f g => (regroup f g).symm.trans (same f g),
      fun same f g => (regroup f g).trans (same f g)⟩ :
        (∀ f g, WithinClosure (Joined (Links (newer ++ (p, n) :: older)) (Link a b)) f g ↔
            WithinClosure (Joined (Links (newer ++ older)) (Link a b)) f g) ↔
          (∀ f g, WithinClosure (Joined (Joined (Links (newer ++ older)) (Link a b)) (Link p n)) f g ↔
            WithinClosure (Joined (Links (newer ++ older)) (Link a b)) f g)).trans
    ((link_cut_unchanged_iff_of_symm symmetric).trans (joined_bypass_iff grown))

end Cuts

/-! ## Which conditions a system needs -/

namespace Flow

variable {F C : Type} (L : Flow F C) (W : Web F C)

/-- `g` and `h` take part in a common condition other than `c`. -/
def SharesBeside (c : C) (g h : F) : Prop :=
  ∃ d, d ≠ c ∧ L.TakesPart W g d ∧ L.TakesPart W h d

/-- `g` and `h` both take part in `c`. -/
def BothTakePart (c : C) (g h : F) : Prop :=
  L.TakesPart W g c ∧ L.TakesPart W h c

variable {L W}

/-- Sharing a condition is sharing one other than `c`, or both taking part in `c`. -/
theorem shares_iff_beside [DecidableEq C] (c : C) {g h : F} :
    L.Shares W g h ↔ Cuts.Joined (L.SharesBeside W c) (L.BothTakePart W c) g h :=
  ⟨fun ⟨d, gd, hd⟩ =>
    if same : d = c then Or.inr ⟨same ▸ gd, same ▸ hd⟩ else Or.inl ⟨d, same, gd, hd⟩,
   fun shared => shared.elim (fun ⟨d, _, gd, hd⟩ => ⟨d, gd, hd⟩) (fun ⟨gc, hc⟩ => ⟨c, gc, hc⟩)⟩

/-- **Which conditions a system needs.** Every formation's system is what it is through the other
conditions alone exactly where any two formations taking part in `c` lie in one system through the
other conditions (`Cuts.closure_unchanged_iff_bypassed`). -/
theorem system_unchanged_without_iff [DecidableEq C] (c : C) :
    (∀ f g, L.WithinSystem W f g ↔ WithinClosure (L.SharesBeside W c) f g) ↔
      ∀ g h, L.TakesPart W g c → L.TakesPart W h c → WithinClosure (L.SharesBeside W c) g h :=
  (⟨fun same f g => (Cuts.within_congr (fun _ _ => (shares_iff_beside c).symm)).trans (same f g),
    fun same f g => (Cuts.within_congr (fun _ _ => shares_iff_beside c)).trans (same f g)⟩ :
      (∀ f g, L.WithinSystem W f g ↔ WithinClosure (L.SharesBeside W c) f g) ↔
        (∀ f g, WithinClosure (Cuts.Joined (L.SharesBeside W c) (L.BothTakePart W c)) f g ↔
          WithinClosure (L.SharesBeside W c) f g)).trans
    (Cuts.closure_unchanged_iff_bypassed.trans
      ⟨fun bypassed g h gc hc => bypassed g h ⟨gc, hc⟩,
       fun bypassed g h both => bypassed g h both.1 both.2⟩)

/-- **A condition with one formation taking part is not needed by any system.** -/
theorem system_unchanged_of_single [DecidableEq C] {c : C}
    (single : ∀ g h, L.TakesPart W g c → L.TakesPart W h c → g = h) :
    ∀ f g, L.WithinSystem W f g ↔ WithinClosure (L.SharesBeside W c) f g :=
  (system_unchanged_without_iff c).mpr fun g h gc hc => by
    have same := single g h gc hc
    subst same
    exact WithinClosure.refl g

/-- **A formation that takes part in no condition has only itself in its system**, and lies in no
other's (`Cuts.within_of_unlinked`, `Cuts.not_within_unlinked`). -/
theorem withinSystem_of_no_part {n : F} (none : ∀ c, ¬ L.TakesPart W n c) :
    (∀ g, L.WithinSystem W n g ↔ g = n) ∧ ∀ f, f ≠ n → ¬ L.WithinSystem W f n :=
  have unlinked : Cuts.Unlinked (L.Shares W) n :=
    fun _ => ⟨fun ⟨c, _, nc⟩ => none c nc, fun ⟨c, nc, _⟩ => none c nc⟩
  ⟨fun _ => ⟨Cuts.within_of_unlinked unlinked, fun same => by subst same; exact WithinClosure.refl _⟩,
   fun _ other => Cuts.not_within_unlinked unlinked other⟩

/-- **A condition two formations take part in joins their systems as one link would.** Where
exactly `a` and `b` take part in `c`, `g` lies within `f`'s system exactly where it does through the
other conditions, or `f` reaches one of `a`, `b` and the other reaches `g` through them
(`Cuts.within_link_iff`). -/
theorem withinSystem_two_takers_iff [DecidableEq C] {c : C} {a b : F}
    (takers : ∀ g, L.TakesPart W g c ↔ g = a ∨ g = b) {f g : F} :
    L.WithinSystem W f g ↔
      WithinClosure (L.SharesBeside W c) f g ∨
        (WithinClosure (L.SharesBeside W c) f a ∧ WithinClosure (L.SharesBeside W c) b g) ∨
        (WithinClosure (L.SharesBeside W c) f b ∧ WithinClosure (L.SharesBeside W c) a g) := by
  have toLink : ∀ x y, L.Shares W x y →
      WithinClosure (Cuts.Joined (L.SharesBeside W c) (Cuts.Link a b)) x y := fun x y shared =>
    ((shares_iff_beside c).mp shared).elim (fun beside => WithinClosure.of_rel (Or.inl beside))
      fun ⟨xc, yc⟩ => ((takers x).mp xc).elim
        (fun xa => ((takers y).mp yc).elim
          (fun ya => by subst xa; subst ya; exact WithinClosure.refl _)
          (fun yb => WithinClosure.of_rel (Or.inr (Or.inl ⟨xa, yb⟩))))
        (fun xb => ((takers y).mp yc).elim
          (fun ya => WithinClosure.of_rel (Or.inr (Or.inr ⟨xb, ya⟩)))
          (fun yb => by subst xb; subst yb; exact WithinClosure.refl _))
  have fromLink : ∀ x y, Cuts.Joined (L.SharesBeside W c) (Cuts.Link a b) x y → L.Shares W x y :=
    fun x y joined => (shares_iff_beside c).mpr (joined.elim Or.inl fun link => Or.inr (link.elim
      (fun ⟨xa, yb⟩ => ⟨(takers x).mpr (Or.inl xa), (takers y).mpr (Or.inr yb)⟩)
      (fun ⟨xb, ya⟩ => ⟨(takers x).mpr (Or.inr xb), (takers y).mpr (Or.inl ya)⟩)))
  exact (⟨Cuts.within_of_steps toLink, WithinClosure.mono fromLink⟩ :
      L.WithinSystem W f g ↔ WithinClosure (Cuts.Joined (L.SharesBeside W c) (Cuts.Link a b)) f g).trans
    Cuts.within_link_iff

/-- **A formation that takes part only in `c` is alone without it**: through the other conditions
it reaches only itself and nothing else reaches it (`Cuts.within_of_unlinked`,
`Cuts.not_within_unlinked`). So where another formation takes part in `c` too, the systems are not
what they are without `c` (`Flow.system_unchanged_without_iff`). -/
theorem alone_beside_of_only {c : C} {n : F} (only : ∀ d, L.TakesPart W n d → d = c) :
    (∀ g, WithinClosure (L.SharesBeside W c) n g ↔ g = n) ∧
      ∀ f, f ≠ n → ¬ WithinClosure (L.SharesBeside W c) f n :=
  have unlinked : Cuts.Unlinked (L.SharesBeside W c) n :=
    fun _ => ⟨fun ⟨d, other, _, nd⟩ => other (only d nd), fun ⟨d, other, nd, _⟩ => other (only d nd)⟩
  ⟨fun _ => ⟨Cuts.within_of_unlinked unlinked, fun same => by subst same; exact WithinClosure.refl _⟩,
   fun _ other => Cuts.not_within_unlinked unlinked other⟩

end Flow

end Becoming
