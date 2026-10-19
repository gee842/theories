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
  `added` from a relation leaves every closure as it was exactly where the target of each removed
  link stays within its source's closure under what remains (`closure_unchanged_iff_bypassed`). For
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

* **Which conditions a world grown by attachment needs.** A world is grown by attachment
  (`Flow.GrownBy`) where a list of entries, latest first, says how its conditions grew: the entry
  `(p, n)` attaches the formation `n` to the earlier formation `p` by a condition exactly `p` and
  `n` take part in, and `n` took part in no earlier condition. Its systems are the closures of the
  listed links (`Flow.GrownBy.within_outside_added_iff`), and without one grown condition they are
  the closures of the other links (`Flow.GrownBy.within_outside_iff`), so each grown condition is
  attached at one place (`Flow.GrownBy.cond_ne`) and is needed: its two takers lie in one system
  and apart without it (`Flow.GrownBy.condition_needed`, `Flow.GrownBy.every_condition_needed`,
  from `Cuts.attached_link_separates`). The latest formation is alone without its condition
  (`Flow.GrownBy.latest_alone`, from `Flow.alone_beside_of_only`), and what grew up to any stage
  is grown by attachment beside the conditions attached later (`Flow.GrownBy.suffix`). With one
  more condition exactly two formations take part in, a grown condition is bypassed, and every
  system is what it is without it, exactly where the new condition's takers lie on its two sides
  through the other conditions (`Flow.GrownBy.bypass_iff`, `Flow.GrownBy.cut_unchanged_iff`, from
  `Cuts.joined_bypass_iff` and `Cuts.joined_cut_unchanged_iff`).

What is not derived: which links form, which are cut, or when; how much a cut or a join takes;
what the formations on either side do afterwards; any count of links or formations; whether a
world grew by attachment, or in which order (`Flow.GrownBy` is a hypothesis on the list). Removing a
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
`added` leaves every closure as it was exactly where each removed link's target stays within its
source's closure under what remains. -/
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

/-! ## Places in a list of links -/

/-- A listed entry other than the one set apart is listed among the rest. -/
theorem mem_split {e : F × F} : ∀ {newer older : List (F × F)} {e' : F × F},
    e' ∈ newer ++ e :: older → e' = e ∨ e' ∈ newer ++ older
  | [], _, _, .head _ => Or.inl rfl
  | [], _, _, .tail _ listed => Or.inr listed
  | _ :: _, _, _, .head _ => Or.inr (.head _)
  | _ :: _, _, _, .tail _ listed => (mem_split listed).elim Or.inl (fun rest => Or.inr (.tail _ rest))

/-- An entry listed among the rest stays listed with one more entry set between them. -/
theorem mem_widen {e : F × F} : ∀ {newer older : List (F × F)} {e' : F × F},
    e' ∈ newer ++ older → e' ∈ newer ++ e :: older
  | [], _, _, listed => .tail _ listed
  | _ :: _, _, _, .head _ => .head _
  | _ :: _, _, _, .tail _ listed => .tail _ (mem_widen listed)

/-- The entry set apart is listed. -/
theorem mem_set_apart {e : F × F} : ∀ {newer older : List (F × F)}, e ∈ newer ++ e :: older
  | [], _ => .head _
  | _ :: _, _ => .tail _ mem_set_apart

/-- An entry of two lists joined is an entry of the first or of the second. -/
theorem mem_append_cases : ∀ {newer older : List (F × F)} {e : F × F},
    e ∈ newer ++ older → e ∈ newer ∨ e ∈ older
  | [], _, _, listed => Or.inr listed
  | _ :: _, _, _, .head _ => Or.inl (.head _)
  | _ :: _, _, _, .tail _ listed =>
    (mem_append_cases listed).elim (fun newer => Or.inl (.tail _ newer)) Or.inr

/-- An entry of the later list is an entry of the two joined. -/
theorem mem_append_right : ∀ {newer older : List (F × F)} {e : F × F},
    e ∈ older → e ∈ newer ++ older
  | [], _, _, listed => listed
  | _ :: _, _, _, listed => .tail _ (mem_append_right listed)

/-- A listed entry splits the list into the entries before it and after it. -/
theorem exists_split : ∀ {es : List (F × F)} {e : F × F}, e ∈ es → ∃ newer older, es = newer ++ e :: older
  | _ :: older, _, .head _ => ⟨[], older, rfl⟩
  | x :: _, _, .tail _ listed =>
    let ⟨newer, older, split⟩ := exists_split listed
    ⟨x :: newer, older, congrArg (x :: ·) split⟩

/-- Regrouping a list split at an entry and joined to another. -/
theorem append_cons_assoc : ∀ {front : List (F × F)} {e : F × F} {back rest : List (F × F)},
    (front ++ e :: back) ++ rest = front ++ e :: (back ++ rest)
  | [], _, _, _ => rfl
  | x :: _, _, _, _ => congrArg (x :: ·) append_cons_assoc

/-- A link of the listed relation is a listed link, read one way or the other. -/
theorem links_mem : ∀ {es : List (F × F)} {g h : F}, Links es g h → ∃ e, e ∈ es ∧ Link e.1 e.2 g h
  | [], _, _, linked => linked.elim
  | _ :: _, _, _, linked => linked.elim
    (fun r => let ⟨e, listed, link⟩ := links_mem r; ⟨e, .tail _ listed, link⟩)
    (fun l => ⟨_, .head _, l⟩)

/-- A listed link, read either way, is a link of the listed relation. -/
theorem links_of_link {es : List (F × F)} {e : F × F} (listed : e ∈ es) {g h : F}
    (link : Link e.1 e.2 g h) : Links es g h :=
  link.elim (fun ⟨ga, hb⟩ => by subst ga; subst hb; exact links_of_mem listed)
    (fun ⟨gb, ha⟩ => by subst gb; subst ha; exact links_symm (links_of_mem listed))

/-- Each link grown by attachment joins two formations. -/
theorem Attaches.distinct : ∀ {es : List (F × F)} {e : F × F}, Attaches es → e ∈ es → e.1 ≠ e.2
  | _, _, .cons _ _ distinct, .head _ => distinct
  | _, _, .cons earlier _ _, .tail _ listed => Attaches.distinct earlier listed

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

/-! ## Which conditions a world grown by attachment needs -/

section Grown

variable (L W)

/-- `g` and `h` take part in a common condition outside `cut`. -/
def SharesOutside (cut : C → Prop) (g h : F) : Prop :=
  ∃ d, ¬ cut d ∧ L.TakesPart W g d ∧ L.TakesPart W h d

/-- **A world grown by attachment.** The entries of `es` list, latest first, how the conditions
outside `added` grew: the entry `(p, n)` attaches the formation `n` to the earlier formation `p`
by the condition `cond n`, in which exactly `p` and `n` take part; the entries attach, each new
formation taking part in no earlier link (`Cuts.Attaches`); every condition some formation takes
part in is attached by an entry or lies in `added`; and no attached condition lies in `added`. -/
structure GrownBy (added : C → Prop) (es : List (F × F)) (cond : F → C) : Prop where
  attaches : Cuts.Attaches es
  takers : ∀ e, e ∈ es → ∀ g, L.TakesPart W g (cond e.2) ↔ g = e.1 ∨ g = e.2
  listed : ∀ g d, L.TakesPart W g d → added d ∨ ∃ e, e ∈ es ∧ cond e.2 = d
  fresh : ∀ e, e ∈ es → ¬ added (cond e.2)

end Grown

/-- Two formations taking part in a condition exactly `a` and `b` take part in lie in one
closure once the link between `a` and `b` is joined to any relation. -/
theorem within_of_two_takers {R : F → F → Prop} {j : C} {a b : F}
    (takers : ∀ g, L.TakesPart W g j ↔ g = a ∨ g = b) {x y : F}
    (xj : L.TakesPart W x j) (yj : L.TakesPart W y j) :
    WithinClosure (Cuts.Joined R (Cuts.Link a b)) x y :=
  ((takers x).mp xj).elim
    (fun xa => ((takers y).mp yj).elim
      (fun ya => by subst xa; subst ya; exact WithinClosure.refl _)
      (fun yb => WithinClosure.of_rel (Or.inr (Or.inl ⟨xa, yb⟩))))
    (fun xb => ((takers y).mp yj).elim
      (fun ya => WithinClosure.of_rel (Or.inr (Or.inr ⟨xb, ya⟩)))
      (fun yb => by subst xb; subst yb; exact WithinClosure.refl _))

namespace GrownBy

variable {added : C → Prop} {es : List (F × F)} {cond : F → C}

/-- Both ends of a grown link take part in the condition that attached it. -/
theorem takes_part_of_link (grown : L.GrownBy W added es cond) {e : F × F} (listed : e ∈ es)
    {x y : F} (link : Cuts.Link e.1 e.2 x y) :
    L.TakesPart W x (cond e.2) ∧ L.TakesPart W y (cond e.2) :=
  link.elim
    (fun ⟨xa, yb⟩ =>
      ⟨(grown.takers e listed x).mpr (Or.inl xa), (grown.takers e listed y).mpr (Or.inr yb)⟩)
    (fun ⟨xb, ya⟩ =>
      ⟨(grown.takers e listed x).mpr (Or.inr xb), (grown.takers e listed y).mpr (Or.inl ya)⟩)

/-- Two formations taking part in a grown condition are one, or the ends of the link that
attached it. -/
theorem link_of_takers (grown : L.GrownBy W added es cond) {e : F × F} (listed : e ∈ es)
    {x y : F} (xc : L.TakesPart W x (cond e.2)) (yc : L.TakesPart W y (cond e.2)) :
    x = y ∨ Cuts.Link e.1 e.2 x y :=
  ((grown.takers e listed x).mp xc).elim
    (fun xa => ((grown.takers e listed y).mp yc).elim
      (fun ya => Or.inl (xa.trans ya.symm))
      (fun yb => Or.inr (Or.inl ⟨xa, yb⟩)))
    (fun xb => ((grown.takers e listed y).mp yc).elim
      (fun ya => Or.inr (Or.inr ⟨xb, ya⟩))
      (fun yb => Or.inl (xb.trans yb.symm)))

/-- **Each grown condition is attached at one place.** No entry other than `(p, n)` attaches the
condition `cond n`: its two takers would be `p` and `n`. An entry `(p, n)` again would list it twice
(`Cuts.Attaches.listed_once`), and an entry `(n, p)` would join what
`Cuts.attached_link_separates` keeps apart without `(p, n)`. -/
theorem cond_ne (grown : L.GrownBy W added es cond) {p n : F} {newer older : List (F × F)}
    (split : es = newer ++ (p, n) :: older) {e : F × F} (listed : e ∈ newer ++ older) :
    cond e.2 ≠ cond n := by
  subst split
  intro same
  have here : (p, n) ∈ newer ++ (p, n) :: older := Cuts.mem_set_apart
  have there : e ∈ newer ++ (p, n) :: older := Cuts.mem_widen listed
  have pTakes : L.TakesPart W p (cond n) := (grown.takers (p, n) here p).mpr (Or.inl rfl)
  have nTakes : L.TakesPart W n (cond n) := (grown.takers (p, n) here n).mpr (Or.inr rfl)
  apply Cuts.attached_link_separates grown.attaches
  rcases grown.link_of_takers there (same ▸ pTakes) (same ▸ nTakes) with one | ⟨pe, ne⟩ | ⟨pe, ne⟩
  · exact absurd one (Cuts.Attaches.distinct grown.attaches here)
  · obtain ⟨notNewer, notOlder⟩ := Cuts.Attaches.listed_once grown.attaches
    have again : (p, n) = e := by rw [pe, ne]
    subst again
    exact (Cuts.mem_append_cases listed).elim (fun later => absurd later notNewer)
      (fun earlier => absurd earlier notOlder)
  · exact WithinClosure.of_rel (Cuts.links_of_link listed (Or.inr ⟨pe, ne⟩))

/-- **What every formation attached takes part in.** The formation `n` attached by `(p, n)` takes
part only in its own condition, in a condition attached later, or in one in `added`. -/
theorem attached_only (grown : L.GrownBy W added es cond) {p n : F} {newer older : List (F × F)}
    (split : es = newer ++ (p, n) :: older) {d : C} (takes : L.TakesPart W n d) :
    added d ∨ d = cond n ∨ ∃ e, e ∈ newer ∧ cond e.2 = d := by
  rcases grown.listed n d takes with extra | ⟨e, listed, attached⟩
  · exact Or.inl extra
  · subst attached
    subst split
    rcases Cuts.mem_split listed with here | rest
    · subst here
      exact Or.inr (Or.inl rfl)
    · rcases Cuts.mem_append_cases rest with later | earlier
      · exact Or.inr (Or.inr ⟨e, later, rfl⟩)
      · have stage : Cuts.Attaches ((p, n) :: older) := Cuts.Attaches.suffix grown.attaches
        cases stage with
        | cons _ unlinked _ =>
          rcases (grown.takers e listed n).mp takes with first | second
          · exact absurd (first ▸ Cuts.links_of_mem earlier) (unlinked e.2).2
          · exact absurd (second ▸ Cuts.links_of_mem earlier) (unlinked e.1).1

/-- Sharing a condition outside `added` and outside the one `(p, n)` attached is sharing a link
grown without `(p, n)`, up to closure. -/
theorem outside_step (grown : L.GrownBy W added es cond) {p n : F} {newer older : List (F × F)}
    (split : es = newer ++ (p, n) :: older) {x y : F}
    (shared : L.SharesOutside W (fun d => d = cond n ∨ added d) x y) :
    WithinClosure (Cuts.Links (newer ++ older)) x y := by
  obtain ⟨d, outside, xd, yd⟩ := shared
  rcases grown.listed x d xd with extra | ⟨e, listed, attached⟩
  · exact absurd (Or.inr extra) outside
  · subst attached
    have apart : e ∈ newer ++ (p, n) :: older := split ▸ listed
    rcases Cuts.mem_split apart with here | rest
    · subst here
      exact absurd (Or.inl rfl) outside
    · rcases grown.link_of_takers listed xd yd with one | link
      · subst one
        exact WithinClosure.refl _
      · exact WithinClosure.of_rel (Cuts.links_of_link rest link)

/-- A link grown without `(p, n)` is a condition shared outside `added` and outside the one
`(p, n)` attached. -/
theorem outside_of_link (grown : L.GrownBy W added es cond) {p n : F} {newer older : List (F × F)}
    (split : es = newer ++ (p, n) :: older) {x y : F} (linked : Cuts.Links (newer ++ older) x y) :
    L.SharesOutside W (fun d => d = cond n ∨ added d) x y := by
  obtain ⟨e, listed, link⟩ := Cuts.links_mem linked
  have there : e ∈ es := split ▸ Cuts.mem_widen listed
  have takes := grown.takes_part_of_link there link
  exact ⟨cond e.2, fun cut => cut.elim (grown.cond_ne split listed) (grown.fresh e there),
    takes.1, takes.2⟩

/-- **The systems without a grown condition are the closures of the links grown without it.**
Beside `added`, sharing a condition other than the one `(p, n)` attached has the closures of the
listed links other than `(p, n)`. -/
theorem within_outside_iff (grown : L.GrownBy W added es cond) {p n : F}
    {newer older : List (F × F)} (split : es = newer ++ (p, n) :: older) {f g : F} :
    WithinClosure (L.SharesOutside W (fun d => d = cond n ∨ added d)) f g ↔
      WithinClosure (Cuts.Links (newer ++ older)) f g :=
  ⟨Cuts.within_of_steps (fun _ _ shared => grown.outside_step split shared),
   WithinClosure.mono (fun _ _ linked => grown.outside_of_link split linked)⟩

/-- **The systems of a grown world are the closures of its links.** Beside `added`, sharing a
condition has the closures of the listed links. -/
theorem within_outside_added_iff (grown : L.GrownBy W added es cond) {f g : F} :
    WithinClosure (L.SharesOutside W added) f g ↔ WithinClosure (Cuts.Links es) f g :=
  ⟨Cuts.within_of_steps (fun x y ⟨d, outside, xd, yd⟩ =>
      (grown.listed x d xd).elim (fun extra => absurd extra outside) fun ⟨e, listed, attached⟩ => by
        subst attached
        rcases grown.link_of_takers listed xd yd with one | link
        · subst one
          exact WithinClosure.refl _
        · exact WithinClosure.of_rel (Cuts.links_of_link listed link)),
   WithinClosure.mono (fun _ _ linked =>
      let ⟨e, listed, link⟩ := Cuts.links_mem linked
      let takes := grown.takes_part_of_link listed link
      ⟨cond e.2, grown.fresh e listed, takes.1, takes.2⟩)⟩

/-- **In a world grown by attachment, every grown condition is needed.** The two formations taking
part in the condition that attached `n` to `p` lie in one system, and without that condition they
lie apart (`Cuts.attached_link_separates`). -/
theorem condition_needed (grown : L.GrownBy W (fun _ => False) es cond) {p n : F}
    {newer older : List (F × F)} (split : es = newer ++ (p, n) :: older) :
    L.WithinSystem W p n ∧ ¬ WithinClosure (L.SharesBeside W (cond n)) p n := by
  have here : (p, n) ∈ es := split ▸ Cuts.mem_set_apart
  have attaches : Cuts.Attaches (newer ++ (p, n) :: older) := split ▸ grown.attaches
  refine ⟨WithinClosure.of_rel ⟨cond n, (grown.takers (p, n) here p).mpr (Or.inl rfl),
    (grown.takers (p, n) here n).mpr (Or.inr rfl)⟩, fun within => ?_⟩
  have outside : WithinClosure (L.SharesOutside W (fun d => d = cond n ∨ False)) p n :=
    WithinClosure.mono (fun _ _ ⟨d, other, gd, hd⟩ => ⟨d, fun cut => cut.elim other id, gd, hd⟩)
      within
  exact Cuts.attached_link_separates attaches ((grown.within_outside_iff split).mp outside)

/-- **Every condition of a world grown by attachment is needed by the systems.** Where every
condition some formation takes part in was attached, no system is what it is without any of
them (the left side of `Flow.system_unchanged_without_iff` fails for each). -/
theorem every_condition_needed (grown : L.GrownBy W (fun _ => False) es cond) {g : F} {d : C}
    (takes : L.TakesPart W g d) :
    ¬ ∀ f h, L.WithinSystem W f h ↔ WithinClosure (L.SharesBeside W d) f h := by
  rcases grown.listed g d takes with none | ⟨⟨p, n⟩, listed, attached⟩
  · exact none.elim
  · subst attached
    obtain ⟨newer, older, split⟩ := Cuts.exists_split listed
    exact fun same =>
      (grown.condition_needed split).2 ((same p n).mp (grown.condition_needed split).1)

/-- **The latest formation is alone without its condition.** In a world grown by attachment, the
formation attached last takes part only in the condition that attached it, so through the other
conditions it reaches only itself and nothing else reaches it (`Flow.alone_beside_of_only`). -/
theorem latest_alone {p n : F} {older : List (F × F)}
    (grown : L.GrownBy W (fun _ => False) ((p, n) :: older) cond) :
    (∀ g, WithinClosure (L.SharesBeside W (cond n)) n g ↔ g = n) ∧
      ∀ f, f ≠ n → ¬ WithinClosure (L.SharesBeside W (cond n)) f n :=
  alone_beside_of_only fun _ takes =>
    (grown.attached_only (newer := []) rfl takes).elim False.elim
      fun rest => rest.elim id fun ⟨_, nothing, _⟩ => nomatch nothing

/-- **What grew up to any stage is grown by attachment**, beside the conditions attached later
(`Cuts.Attaches.suffix`). -/
theorem suffix {newer older : List (F × F)} (grown : L.GrownBy W added (newer ++ older) cond) :
    L.GrownBy W (fun d => added d ∨ ∃ e, e ∈ newer ∧ cond e.2 = d) older cond := by
  refine ⟨Cuts.Attaches.suffix grown.attaches,
    fun e listed => grown.takers e (Cuts.mem_append_right listed),
    fun g d takes => (grown.listed g d takes).elim (fun extra => Or.inl (Or.inl extra))
      fun ⟨e, listed, attached⟩ => (Cuts.mem_append_cases listed).elim
        (fun later => Or.inl (Or.inr ⟨e, later, attached⟩)) (fun earlier => Or.inr ⟨e, earlier, attached⟩),
    fun e listed extra => ?_⟩
  rcases extra with extra | ⟨⟨q, m⟩, later, same⟩
  · exact grown.fresh e (Cuts.mem_append_right listed) extra
  · obtain ⟨front, back, split⟩ := Cuts.exists_split later
    subst split
    exact grown.cond_ne Cuts.append_cons_assoc
      (Cuts.mem_append_right (Cuts.mem_append_right listed)) same.symm

variable [DecidableEq C] {j : C} {a b : F}

/-- With one more condition `j` exactly `a` and `b` take part in, sharing a condition other than
the one `(p, n)` attached is, up to closure, a link grown without `(p, n)` or the link between `a`
and `b`. -/
theorem beside_iff (grown : L.GrownBy W (fun d => d = j) es cond)
    (takers : ∀ g, L.TakesPart W g j ↔ g = a ∨ g = b) {p n : F} {newer older : List (F × F)}
    (split : es = newer ++ (p, n) :: older) {f g : F} :
    WithinClosure (L.SharesBeside W (cond n)) f g ↔
      WithinClosure (Cuts.Joined (Cuts.Links (newer ++ older)) (Cuts.Link a b)) f g := by
  have here : (p, n) ∈ es := split ▸ Cuts.mem_set_apart
  refine ⟨Cuts.within_of_steps fun x y shared => ?_, WithinClosure.mono fun x y joined => ?_⟩
  · obtain ⟨d, other, xd, yd⟩ := shared
    exact if dj : d = j then within_of_two_takers takers (dj ▸ xd) (dj ▸ yd)
      else WithinClosure.mono (fun _ _ r => Or.inl r)
        (grown.outside_step split ⟨d, fun cut => cut.elim other dj, xd, yd⟩)
  · rcases joined with linked | link
    · obtain ⟨d, outside, xd, yd⟩ := grown.outside_of_link split linked
      exact ⟨d, fun same => outside (Or.inl same), xd, yd⟩
    · refine ⟨j, fun same => grown.fresh (p, n) here same.symm, ?_⟩
      exact link.elim (fun ⟨xa, yb⟩ => ⟨(takers x).mpr (Or.inl xa), (takers y).mpr (Or.inr yb)⟩)
        (fun ⟨xb, ya⟩ => ⟨(takers x).mpr (Or.inr xb), (takers y).mpr (Or.inl ya)⟩)

/-- With one more condition `j` exactly `a` and `b` take part in, the systems of a grown world are
the closures of its links with the link between `a` and `b` joined. -/
theorem system_iff (grown : L.GrownBy W (fun d => d = j) es cond)
    (takers : ∀ g, L.TakesPart W g j ↔ g = a ∨ g = b) {f g : F} :
    L.WithinSystem W f g ↔ WithinClosure (Cuts.Joined (Cuts.Links es) (Cuts.Link a b)) f g := by
  refine ⟨Cuts.within_of_steps fun x y shared => ?_, WithinClosure.mono fun x y joined => ?_⟩
  · obtain ⟨d, xd, yd⟩ := shared
    exact if dj : d = j then within_of_two_takers takers (dj ▸ xd) (dj ▸ yd)
      else WithinClosure.mono (fun _ _ r => Or.inl r)
        ((grown.within_outside_added_iff).mp (WithinClosure.of_rel ⟨d, dj, xd, yd⟩))
  · rcases joined with linked | link
    · obtain ⟨e, listed, link⟩ := Cuts.links_mem linked
      have takes := grown.takes_part_of_link listed link
      exact ⟨cond e.2, takes.1, takes.2⟩
    · exact ⟨j, link.elim (fun ⟨xa, yb⟩ => ⟨(takers x).mpr (Or.inl xa), (takers y).mpr (Or.inr yb)⟩)
        (fun ⟨xb, ya⟩ => ⟨(takers x).mpr (Or.inr xb), (takers y).mpr (Or.inl ya)⟩)⟩

/-- **After one more condition, a grown condition is bypassed exactly where the new one crosses
it.** In a world grown by attachment with one more condition `j` exactly `a` and `b` take part in,
the takers `p` and `n` of the condition that attached `n` lie in one system through the other
conditions exactly where `a` and `b` lie on its two sides: one with `p`, the other with `n`,
through the conditions other than `cond n` and `j` (`Cuts.joined_bypass_iff`). -/
theorem bypass_iff (grown : L.GrownBy W (fun d => d = j) es cond)
    (takers : ∀ g, L.TakesPart W g j ↔ g = a ∨ g = b) {p n : F} {newer older : List (F × F)}
    (split : es = newer ++ (p, n) :: older) :
    WithinClosure (L.SharesBeside W (cond n)) p n ↔
      (WithinClosure (L.SharesOutside W (fun d => d = cond n ∨ d = j)) p a ∧
          WithinClosure (L.SharesOutside W (fun d => d = cond n ∨ d = j)) b n) ∨
        (WithinClosure (L.SharesOutside W (fun d => d = cond n ∨ d = j)) p b ∧
          WithinClosure (L.SharesOutside W (fun d => d = cond n ∨ d = j)) a n) := by
  have attaches : Cuts.Attaches (newer ++ (p, n) :: older) := split ▸ grown.attaches
  exact (grown.beside_iff takers split).trans ((Cuts.joined_bypass_iff attaches).trans
    (or_congr (and_congr (grown.within_outside_iff split).symm (grown.within_outside_iff split).symm)
      (and_congr (grown.within_outside_iff split).symm (grown.within_outside_iff split).symm)))

/-- **After one more condition, a grown condition stops being needed exactly where the new one
crosses it.** Every system is what it is without the condition that attached `n` to `p` exactly
where the takers of `j` lie on its two sides (`Cuts.joined_cut_unchanged_iff`). -/
theorem cut_unchanged_iff (grown : L.GrownBy W (fun d => d = j) es cond)
    (takers : ∀ g, L.TakesPart W g j ↔ g = a ∨ g = b) {p n : F} {newer older : List (F × F)}
    (split : es = newer ++ (p, n) :: older) :
    (∀ f g, L.WithinSystem W f g ↔ WithinClosure (L.SharesBeside W (cond n)) f g) ↔
      (WithinClosure (L.SharesOutside W (fun d => d = cond n ∨ d = j)) p a ∧
          WithinClosure (L.SharesOutside W (fun d => d = cond n ∨ d = j)) b n) ∨
        (WithinClosure (L.SharesOutside W (fun d => d = cond n ∨ d = j)) p b ∧
          WithinClosure (L.SharesOutside W (fun d => d = cond n ∨ d = j)) a n) := by
  have attaches : Cuts.Attaches (newer ++ (p, n) :: older) := split ▸ grown.attaches
  have system : ∀ f g, L.WithinSystem W f g ↔
      WithinClosure (Cuts.Joined (Cuts.Links (newer ++ (p, n) :: older)) (Cuts.Link a b)) f g :=
    fun _ _ => split ▸ grown.system_iff takers
  have beside : ∀ f g, WithinClosure (L.SharesBeside W (cond n)) f g ↔
      WithinClosure (Cuts.Joined (Cuts.Links (newer ++ older)) (Cuts.Link a b)) f g :=
    fun _ _ => grown.beside_iff takers split
  exact (⟨fun same f g => ((system f g).symm.trans (same f g)).trans (beside f g),
      fun same f g => ((system f g).trans (same f g)).trans (beside f g).symm⟩ :
        (∀ f g, L.WithinSystem W f g ↔ WithinClosure (L.SharesBeside W (cond n)) f g) ↔
          ∀ f g, WithinClosure (Cuts.Joined (Cuts.Links (newer ++ (p, n) :: older)) (Cuts.Link a b)) f g ↔
            WithinClosure (Cuts.Joined (Cuts.Links (newer ++ older)) (Cuts.Link a b)) f g).trans
    ((Cuts.joined_cut_unchanged_iff attaches).trans
      (or_congr (and_congr (grown.within_outside_iff split).symm (grown.within_outside_iff split).symm)
        (and_congr (grown.within_outside_iff split).symm (grown.within_outside_iff split).symm)))

end GrownBy

end Flow

end Becoming
