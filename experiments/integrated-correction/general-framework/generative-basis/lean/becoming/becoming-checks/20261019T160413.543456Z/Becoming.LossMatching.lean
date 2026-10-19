import Becoming.Population
import Becoming.Metaethics
import Becoming.Frame
import Becoming.ValuationFrames

/-!
# Strict loss matching: the general laws

`Frame.StrictLossMatch F same better worse` says: every claim lost at `better` has its own
distinct counterpart, of the same content under `same`, lost at `worse`, and `worse` loses one
more claim besides. The repair process of `Becoming.RepairComparison` is an instance. This
module states the laws for every frame:

* composition and monotonicity (`StrictLossMatch.trans`, `StrictLossMatch.mono`);
* a generative extension is a strict loss match by identity, so a commitment making strict
  matching sufficient for strict priority contains comparison principle C
  (`strictLossMatch_of_extension`, `SufficientMatching.comparison`); not conversely;
* the sufficiency commitment is consistent only where matching is asymmetric
  (`SufficientMatching.not_mutual`); with infinitely many losses a configuration can be
  strictly matched against itself (`EndlessLosses`), so finiteness is needed;
* with the losses listed once, a strict match needs strictly more losses at the worse
  configuration (`StrictLossMatch.length_lt`), hence irreflexive and asymmetric;
* **counting law**: where content is a class `κ` and losses are listed once, a strict
  loss match exists exactly when, class by class, the better configuration loses no more
  than the worse, and in all strictly fewer (`strictLossMatch_iff_counts`); within one
  class, exactly when it loses fewer (`strictLossMatch_iff_length_of_alike`);
* blocking: a lost claim whose every same-content counterpart is kept at the worse
  configuration blocks matching (`not_strictLossMatch_of_kept`); where every claim rests on
  one common support and claims are finitely listed, a configuration losing the support is
  strictly better by matching than no configuration (`not_strictLossMatch_of_base_lost`);
* reading claims at their episode time: a frame reads each claim at its time exactly when
  its realization is settled from that time on (`readsAt_iff_settled`); then restored
  support re-realizes no missed claim (`ReadsAt.loss_retained`).

No ethical predicate is used beyond the supplied comparison `Le` of `SufficientMatching`, which
appears only as a hypothesis, and no axiom occurs.
-/

namespace Becoming

namespace LossMatching

variable {α β : Type}

theorem mem_map_inv {g : α → β} {b : β} : ∀ {l : List α}, b ∈ l.map g → ∃ a, a ∈ l ∧ g a = b
  | [], mem => nomatch mem
  | a :: _, mem => match mem_cons_cases mem with
    | .inl same => ⟨a, .head _, same.symm⟩
    | .inr mem => match mem_map_inv mem with
      | ⟨x, inL, same⟩ => ⟨x, .tail a inL, same⟩

/-- Mapping a list by a function one to one on its members keeps it without repetition. -/
theorem distinct_map_on {g : α → β} : ∀ {l : List α},
    (∀ a b, a ∈ l → b ∈ l → g a = g b → a = b) → Distinct l → Distinct (l.map g)
  | [], _, _ => trivial
  | a :: l, inj, ⟨fresh, distinct⟩ =>
    ⟨fun mem => match mem_map_inv mem with
      | ⟨x, inL, same⟩ =>
        fresh (Eq.subst (motive := fun y => y ∈ l) (inj x a (.tail a inL) (.head l) same) inL),
     distinct_map_on (fun x y mx my => inj x y (.tail a mx) (.tail a my)) distinct⟩

theorem map_length_eq (g : α → β) : ∀ l : List α, (l.map g).length = l.length
  | [] => rfl
  | _ :: l => congrArg Nat.succ (map_length_eq g l)

theorem mem_middle_of {a : α} {q : List α} : ∀ p : List α, a ∈ p ++ a :: q
  | [] => .head q
  | x :: p => .tail x (mem_middle_of p)

theorem not_mem_middle {a : α} : ∀ {p q : List α}, Distinct (p ++ a :: q) → ¬ a ∈ p ++ q
  | [], _, ⟨fresh, _⟩, mem => fresh mem
  | _ :: p, q, ⟨fresh, distinct⟩, mem => match mem_cons_cases mem with
    | .inl ax => fresh (Eq.subst (motive := fun y => y ∈ p ++ a :: q) ax (mem_middle_of p))
    | .inr mem => not_mem_middle distinct mem

/-- The total over a list with one member taken out of the middle. -/
theorem total_middle (f : α → Nat) (a : α) (p q : List α) :
    total (p ++ a :: q) f = f a + total (p ++ q) f :=
  (total_append f (a :: q) p).trans
    ((Nat.add_left_comm (total p f) (f a) (total q f)).trans
      (congrArg (f a + ·) (total_append f q p).symm))

/-- Whether a list is without repetition is decided where identity is. -/
def decideDistinct [DecidableEq α] : (l : List α) → Decidable (Distinct l)
  | [] => isTrue trivial
  | a :: l => match @decideSome α (fun x => x = a) (fun _ => inferInstance) l, decideDistinct l with
    | isTrue found, _ => isFalse fun ⟨fresh, _⟩ => match found with
      | ⟨_, mem, same⟩ => fresh (Eq.subst (motive := fun y => y ∈ l) same mem)
    | isFalse absent, isTrue distinct => isTrue ⟨fun mem => absent ⟨a, mem, rfl⟩, distinct⟩
    | isFalse _, isFalse repeated => isFalse fun ⟨_, distinct⟩ => repeated distinct

end LossMatching

open LossMatching

namespace Frame

variable {S A C : Type}

/-- Each lost claim in the better configuration has a distinct corresponding lost
claim in the worse, which has another loss. `same` is a supplied content relation. -/
def StrictLossMatch (F : Frame S A C) (same : C → C → Prop) (better worse : S) : Prop :=
  ∃ image : C → C,
    (∀ c, ¬ F.realized better c → ¬ F.realized worse (image c)) ∧
    (∀ c, ¬ F.realized better c → same c (image c)) ∧
    (∀ c d, ¬ F.realized better c → ¬ F.realized better d → image c = image d → c = d) ∧
    ∃ extra, ¬ F.realized worse extra ∧
      ∀ c, ¬ F.realized better c → image c ≠ extra

/-! ## Composition, monotonicity and generative extension -/

/-- **Strict loss matches compose** where the content relation does. -/
theorem StrictLossMatch.trans {F : Frame S A C} {same : C → C → Prop}
    (chain : ∀ a b c, same a b → same b c → same a c) {x y z : S} :
    F.StrictLossMatch same x y → F.StrictLossMatch same y z → F.StrictLossMatch same x z
  | ⟨i, loss, content, once, e, lostE, freshE⟩, ⟨j, loss', content', once', _, _, _⟩ =>
    ⟨fun c => j (i c),
     fun c lost => loss' (i c) (loss c lost),
     fun c lost => chain _ _ _ (content c lost) (content' (i c) (loss c lost)),
     fun c d lc ld same => once c d lc ld (once' (i c) (i d) (loss c lc) (loss d ld) same),
     j e, loss' e lostE,
     fun c lost same => freshE c lost (once' (i c) e (loss c lost) lostE same)⟩

/-- A wider content relation, fewer losses at the better and more at the worse keep a match. -/
theorem StrictLossMatch.mono {F : Frame S A C} {same same' : C → C → Prop}
    (wider : ∀ a b, same a b → same' a b) {b b' w w' : S}
    (fewer : ∀ c, ¬ F.realized b' c → ¬ F.realized b c)
    (more : ∀ c, ¬ F.realized w c → ¬ F.realized w' c) :
    F.StrictLossMatch same b w → F.StrictLossMatch same' b' w'
  | ⟨i, loss, content, once, e, lostE, freshE⟩ =>
    ⟨i, fun c lost => more _ (loss c (fewer c lost)),
     fun c lost => wider _ _ (content c (fewer c lost)),
     fun c d lc ld same => once c d (fewer c lc) (fewer d ld) same,
     e, more e lostE, fun c lost => freshE c (fewer c lost)⟩

/-- **A generative extension is a strict loss match by identity**: where `t` keeps every
claim of `s` and realizes one more, every loss of `t` is its own counterpart at `s`. -/
theorem strictLossMatch_of_extension {F : Frame S A C} {same : C → C → Prop}
    (refl : ∀ c, same c c) {living : C → Prop} {s t : S} :
    Extension F living s t → F.StrictLossMatch same t s
  | ⟨keeps, c, _, realized, lost⟩ =>
    ⟨id, fun d lostT realS => lostT (keeps d realS), fun d _ => refl d,
     fun _ _ _ _ same => same, c, lost,
     fun _ lostT same => lostT (Eq.subst (motive := fun x => F.realized t x) same.symm realized)⟩

/-- The sufficiency commitment, for any frame: inside `scope`, a strict loss match is
sufficient for strict priority under the supplied comparison `Le`. -/
def SufficientMatching (F : Frame S A C) (same : C → C → Prop) (scope Le : S → S → Prop) :
    Prop :=
  ∀ better worse, scope better worse → F.StrictLossMatch same better worse →
    Le worse better ∧ ¬ Le better worse

/-- **The sufficiency commitment contains C**: with a reflexive content relation and every
extension in scope, the strict comparison satisfies comparison principle C. -/
theorem SufficientMatching.comparison {F : Frame S A C} {same : C → C → Prop}
    (refl : ∀ c, same c c) {scope Le : S → S → Prop}
    (sufficient : F.SufficientMatching same scope Le) {living : C → Prop}
    (inScope : ∀ s t, Extension F living s t → scope t s) :
    Comparison F living (fun s t => Le s t ∧ ¬ Le t s) :=
  fun s t extension =>
    sufficient t s (inScope s t extension) (strictLossMatch_of_extension refl extension)

/-- **Sufficiency needs asymmetric matching**: inside a scope holding both orders, two
configurations cannot each be strictly matched against the other. -/
theorem SufficientMatching.not_mutual {F : Frame S A C} {same : C → C → Prop}
    {scope Le : S → S → Prop} (sufficient : F.SufficientMatching same scope Le) {a b : S}
    (ab : scope a b) (ba : scope b a) (matched : F.StrictLossMatch same a b) :
    ¬ F.StrictLossMatch same b a :=
  fun back => (sufficient a b ab matched).2 (sufficient b a ba back).1

theorem SufficientMatching.not_self {F : Frame S A C} {same : C → C → Prop}
    {scope Le : S → S → Prop} (sufficient : F.SufficientMatching same scope Le) {a : S}
    (aa : scope a a) : ¬ F.StrictLossMatch same a a :=
  fun matched => (sufficient a a aa matched).2 (sufficient a a aa matched).1

/-! ## Counting: listed losses -/

/-- `l` lists the claims lost at `s`, each once. -/
def LossesListed (F : Frame S A C) (s : S) (l : List C) : Prop :=
  Distinct l ∧ ∀ c, ¬ F.realized s c ↔ c ∈ l

/-- **A strict loss match needs strictly more losses at the worse configuration**, for
any content relation. -/
theorem StrictLossMatch.length_lt {F : Frame S A C} {same : C → C → Prop} {b w : S}
    {lb lw : List C} (listedB : F.LossesListed b lb)
    (heldW : ∀ c, ¬ F.realized w c → c ∈ lw) :
    F.StrictLossMatch same b w → lb.length < lw.length
  | ⟨i, loss, _, once, e, lostE, freshE⟩ =>
    have distinctImage : Distinct (lb.map i) :=
      distinct_map_on (fun x y mx my same =>
        once x y ((listedB.2 x).mpr mx) ((listedB.2 y).mpr my) same) listedB.1
    have distinctAll : Distinct (e :: lb.map i) :=
      ⟨fun mem => match mem_map_inv mem with
        | ⟨x, inL, same⟩ => freshE x ((listedB.2 x).mpr inL) same, distinctImage⟩
    have sub : ∀ c, c ∈ e :: lb.map i → c ∈ lw := fun c mem => match mem_cons_cases mem with
      | .inl same => heldW c (Eq.subst (motive := fun y => ¬ F.realized w y) same.symm lostE)
      | .inr mem => match mem_map_inv mem with
        | ⟨x, inL, same⟩ => heldW c (Eq.subst (motive := fun y => ¬ F.realized w y) same
            (loss x ((listedB.2 x).mpr inL)))
    have bound : (lb.map i).length + 1 ≤ lw.length := length_le_of_sub distinctAll sub
    Eq.subst (motive := fun n => n + 1 ≤ lw.length) (map_length_eq i lb) bound

/-- With its losses listed, no configuration is strictly matched against itself. -/
theorem StrictLossMatch.irrefl {F : Frame S A C} {same : C → C → Prop} {s : S} {l : List C}
    (listed : F.LossesListed s l) : ¬ F.StrictLossMatch same s s :=
  fun matched => Nat.lt_irrefl _ (matched.length_lt listed fun c lost => (listed.2 c).mp lost)

/-- With both configurations' losses listed, strict loss matching is asymmetric, whatever
the content relation. -/
theorem StrictLossMatch.asymm {F : Frame S A C} {same : C → C → Prop} {a b : S}
    {la lb : List C} (listedA : F.LossesListed a la) (listedB : F.LossesListed b lb)
    (matched : F.StrictLossMatch same a b) : ¬ F.StrictLossMatch same b a :=
  fun back => Nat.lt_irrefl _ (Nat.lt_trans
    (matched.length_lt listedA fun c lost => (listedB.2 c).mp lost)
    (back.length_lt listedB fun c lost => (listedA.2 c).mp lost))

/-- Equal numbers of listed losses: no strict match in either direction. -/
theorem not_strictLossMatch_of_length_le {F : Frame S A C} {same : C → C → Prop} {b w : S}
    {lb lw : List C} (listedB : F.LossesListed b lb) (heldW : ∀ c, ¬ F.realized w c → c ∈ lw)
    (le : lw.length ≤ lb.length) : ¬ F.StrictLossMatch same b w :=
  fun matched => Nat.lt_irrefl _ (Nat.lt_of_lt_of_le (matched.length_lt listedB heldW) le)

/-! ## Blocking -/

/-- Every loss at the better configuration has a same-content loss at the worse. -/
theorem StrictLossMatch.counterpart {F : Frame S A C} {same : C → C → Prop} {b w : S} :
    F.StrictLossMatch same b w → ∀ c, ¬ F.realized b c → ∃ d, ¬ F.realized w d ∧ same c d
  | ⟨i, loss, content, _⟩, c, lost => ⟨i c, loss c lost, content c lost⟩

/-- **A kept counterpart class blocks matching**: a claim lost at the better configuration
whose every same-content claim is realized at the worse rules out a strict loss match. -/
theorem not_strictLossMatch_of_kept {F : Frame S A C} {same : C → C → Prop} {b w : S} {c : C}
    (lost : ¬ F.realized b c) (kept : ∀ d, same c d → F.realized w d) :
    ¬ F.StrictLossMatch same b w :=
  fun matched => match matched.counterpart c lost with
    | ⟨d, lostW, related⟩ => lostW (kept d related)

/-- **Losing the common support**: where every claim rests on one support claim `base` and
the claims are finitely listed, a configuration that loses `base` is strictly better by
matching than no configuration, under any content relation. -/
theorem not_strictLossMatch_of_base_lost {F : Frame S A C} {same : C → C → Prop} {base : C}
    (rests : ∀ s c, F.realized s c → F.realized s base) {all : List C} (distinct : Distinct all)
    (every : ∀ c, c ∈ all) {b : S} (lost : ¬ F.realized b base) (w : S) :
    ¬ F.StrictLossMatch same b w :=
  fun matched => Nat.lt_irrefl _ (matched.length_lt (lb := all) (lw := all)
    ⟨distinct, fun c => ⟨fun _ => every c, fun _ realized => lost (rests b c realized)⟩⟩
    fun c _ => every c)

/-! ## The counting law -/

section Counting

variable {K : Type} [DecidableEq K]

/-- How many members of `l` lie in content class `k`. -/
def classCount (κ : C → K) (k : K) (l : List C) : Nat :=
  total l fun c => mark (κ c = k)

/-- Necessity, class by class: a class-respecting strict loss match loses no more claims of
any class at the better configuration than at the worse. -/
theorem StrictLossMatch.classCount_le {F : Frame S A C} {κ : C → K} {b w : S}
    {lb lw : List C} (listedB : F.LossesListed b lb) (listedW : F.LossesListed w lw)
    (matched : F.StrictLossMatch (fun c d => κ c = κ d) b w) (k : K) :
    classCount κ k lb ≤ classCount κ k lw :=
  match matched with
  | ⟨i, loss, content, once, _⟩ =>
    have distinctImage : Distinct (lb.map i) :=
      distinct_map_on (fun x y mx my same =>
        once x y ((listedB.2 x).mpr mx) ((listedB.2 y).mpr my) same) listedB.1
    have moved : classCount κ k lb = total (lb.map i) (fun c => mark (κ c = k)) :=
      (total_congr_on (f := fun c => mark (κ c = k)) (g := fun c => mark (κ (i c) = k))
        fun c mem => congrArg (fun x => mark (x = k)) (content c ((listedB.2 c).mpr mem))).trans
        (total_map i (fun c => mark (κ c = k)) lb).symm
    Nat.le_trans (Nat.le_of_eq moved)
      (marks_le_of_sub (q := fun c => κ c = k) (r := fun c => κ c = k) distinctImage listedW.1
        fun c mem has => match mem_map_inv mem with
          | ⟨x, inL, same⟩ => ⟨(listedW.2 c).mp (Eq.subst (motive := fun y => ¬ F.realized w y)
              same (loss x ((listedB.2 x).mpr inL))), has⟩)

/-- Greedy matching: where, class by class, `lb` has no more members than `lw`, some
class-respecting map sends `lb` one to one into `lw`. -/
theorem matching_of_counts [DecidableEq C] (κ : C → K) :
    ∀ (lb lw : List C), Distinct lb → Distinct lw →
      (∀ k, classCount κ k lb ≤ classCount κ k lw) →
      ∃ image : C → C, (∀ c, c ∈ lb → image c ∈ lw ∧ κ c = κ (image c)) ∧
        (∀ c d, c ∈ lb → d ∈ lb → image c = image d → c = d)
  | [], _, _, _, _ => ⟨id, fun _ mem => (nomatch mem), fun _ _ mem => (nomatch mem)⟩
  | c :: lb, lw, ⟨fresh, distinct⟩, distinctW, counts =>
    have first : mark (κ c = κ c) + classCount κ (κ c) lb ≤ classCount κ (κ c) lw :=
      counts (κ c)
    have pos : 0 < total lw (fun x => mark (κ x = κ c)) :=
      Nat.lt_of_lt_of_le (Nat.lt_of_lt_of_le (mark_pos.mpr rfl) (Nat.le_add_right _ _)) first
    match total_pos lw pos with
    | ⟨d, memD, has⟩ =>
      have classD : κ d = κ c := mark_pos.mp has
      match List.append_of_mem memD with
      | ⟨p, q, split⟩ =>
        have middle : Distinct (p ++ d :: q) := Eq.subst (motive := Distinct) split distinctW
        have counts' : ∀ k, classCount κ k lb ≤ classCount κ k (p ++ q) := fun k =>
          have whole : classCount κ k lw = mark (κ c = k) + classCount κ k (p ++ q) :=
            (congrArg (fun l => total l fun x => mark (κ x = k)) split).trans
              ((total_middle (fun x => mark (κ x = k)) d p q).trans
                (congrArg (· + classCount κ k (p ++ q))
                  (congrArg (fun x => mark (x = k)) classD)))
          have here : mark (κ c = k) + classCount κ k lb ≤ classCount κ k lw := counts k
          le_of_add_le_add_right (mark (κ c = k))
            (Nat.le_trans (Nat.le_of_eq (Nat.add_comm _ _)) (Nat.le_trans here
              (Nat.le_of_eq (whole.trans (Nat.add_comm _ _)))))
        match matching_of_counts κ lb (p ++ q) distinct (distinct_remove middle) counts' with
        | ⟨image, maps, once⟩ =>
          have outside : ∀ x, x ∈ lb → ¬ x = c := fun _ mem same =>
            fresh (Eq.subst (motive := fun y => y ∈ lb) same mem)
          have intoW : ∀ y, y ∈ p ++ q → y ∈ lw := fun y mem =>
            Eq.subst (motive := fun l => y ∈ l) split.symm (mem_insert mem)
          have notD : ∀ x, x ∈ lb → ¬ image x = d := fun x mem same =>
            not_mem_middle middle (Eq.subst (motive := fun y => y ∈ p ++ q) same (maps x mem).1)
          ⟨fun x => if x = c then d else image x,
           fun x mem => match mem_cons_cases mem with
            | .inl same => Eq.subst (motive := fun y => y ∈ lw ∧ κ x = κ y) (if_pos same).symm
                ⟨memD, (congrArg κ same).trans classD.symm⟩
            | .inr mem => Eq.subst (motive := fun y => y ∈ lw ∧ κ x = κ y)
                (if_neg (outside x mem)).symm ⟨intoW _ (maps x mem).1, (maps x mem).2⟩,
           fun x y mx my same => match mem_cons_cases mx, mem_cons_cases my with
            | .inl xc, .inl yc => xc.trans yc.symm
            | .inl xc, .inr my' => absurd
                (((if_pos xc).symm.trans same).trans (if_neg (outside y my'))).symm (notD y my')
            | .inr mx', .inl yc => absurd
                (((if_neg (outside x mx')).symm.trans same).trans (if_pos yc)) (notD x mx')
            | .inr mx', .inr my' => once x y mx' my'
                (((if_neg (outside x mx')).symm.trans same).trans (if_neg (outside y my')))⟩

/-- Where `lb` is shorter than `lw` and maps into it, some member of `lw` is no image. -/
theorem exists_fresh [DecidableEq C] {image : C → C} {lb lw : List C} (distinctW : Distinct lw)
    (shorter : lb.length < lw.length) : ∃ e, e ∈ lw ∧ ∀ c, c ∈ lb → image c ≠ e :=
  match @search C (fun e => ∃ a, a ∈ lb.map image ∧ a = e)
      (fun e => @decideSome C (fun a => a = e) (fun _ => inferInstance) (lb.map image)) lw with
  | .inl ⟨e, mem, absent⟩ => ⟨e, mem, fun c inB same => absent ⟨image c, mem_map_of inB, same⟩⟩
  | .inr all => absurd shorter (Nat.not_lt_of_le (Nat.le_trans
      (length_le_of_sub distinctW fun e mem => match all e mem with
        | ⟨_, inMap, same⟩ => Eq.subst (motive := fun y => y ∈ lb.map image) same inMap)
      (Nat.le_of_eq (map_length_eq image lb))))

/-- Sufficiency: the class counts and a strictly longer list of losses give a match. -/
theorem strictLossMatch_of_counts [DecidableEq C] {F : Frame S A C} {κ : C → K} {b w : S}
    {lb lw : List C} (listedB : F.LossesListed b lb) (listedW : F.LossesListed w lw)
    (counts : ∀ k, classCount κ k lb ≤ classCount κ k lw) (shorter : lb.length < lw.length) :
    F.StrictLossMatch (fun c d => κ c = κ d) b w :=
  match matching_of_counts κ lb lw listedB.1 listedW.1 counts with
  | ⟨image, maps, once⟩ =>
    match exists_fresh (image := image) listedW.1 shorter with
    | ⟨e, memE, freshE⟩ =>
      ⟨image, fun c lost => (listedW.2 (image c)).mpr (maps c ((listedB.2 c).mp lost)).1,
       fun c lost => (maps c ((listedB.2 c).mp lost)).2,
       fun c d lc ld same => once c d ((listedB.2 c).mp lc) ((listedB.2 d).mp ld) same,
       e, (listedW.2 e).mpr memE, fun c lost => freshE c ((listedB.2 c).mp lost)⟩

/-- **The counting law of strict loss matching.** With content read as a class `κ` and the
losses of both configurations listed once: a strict loss match exists exactly when, class
by class, the better configuration loses no more claims than the worse, and in all it loses
fewer. -/
theorem strictLossMatch_iff_counts [DecidableEq C] {F : Frame S A C} {κ : C → K} {b w : S}
    {lb lw : List C} (listedB : F.LossesListed b lb) (listedW : F.LossesListed w lw) :
    F.StrictLossMatch (fun c d => κ c = κ d) b w ↔
      (∀ k, classCount κ k lb ≤ classCount κ k lw) ∧ lb.length < lw.length :=
  ⟨fun matched => ⟨matched.classCount_le listedB listedW,
      matched.length_lt listedB fun c lost => (listedW.2 c).mp lost⟩,
   fun ⟨counts, shorter⟩ => strictLossMatch_of_counts listedB listedW counts shorter⟩

end Counting

theorem classCount_unit (l : List C) : classCount (fun _ => ()) () l = l.length :=
  (total_congr (fun _ => mark_one (p := () = ()) rfl) l).trans (total_ones l)

/-- **Within one content class, a strict loss match exists exactly when the better
configuration loses fewer listed claims.** -/
theorem strictLossMatch_iff_length_of_alike [DecidableEq C] {F : Frame S A C}
    {same : C → C → Prop} {b w : S} {lb lw : List C}
    (listedB : F.LossesListed b lb) (listedW : F.LossesListed w lw)
    (alike : ∀ c d, ¬ F.realized b c → ¬ F.realized w d → same c d) :
    F.StrictLossMatch same b w ↔ lb.length < lw.length :=
  ⟨fun matched => matched.length_lt listedB fun c lost => (listedW.2 c).mp lost,
   fun shorter =>
    match strictLossMatch_of_counts (κ := fun _ => ()) listedB listedW
      (fun k => match k with
        | () => Nat.le_of_lt (Eq.subst (motive := fun n => n < classCount (fun _ => ()) () lw)
            (classCount_unit lb).symm
            (Eq.subst (motive := fun n => lb.length < n) (classCount_unit lw).symm shorter)))
      shorter with
    | ⟨i, loss, _, once, e, lostE, freshE⟩ =>
      ⟨i, loss, fun c lost => alike c (i c) lost (loss c lost), once, e, lostE, freshE⟩⟩

/-! ## Finitely listed claims list their losses -/

/-- The claims of `all` lost at `s`. -/
def lostOf (F : Frame S A C) (s : S) [dec : ∀ c, Decidable (F.realized s c)] :
    List C → List C
  | [] => []
  | c :: l => if F.realized s c then lostOf F s l else c :: lostOf F s l

theorem mem_lostOf {F : Frame S A C} {s : S} [dec : ∀ c, Decidable (F.realized s c)] {x : C} :
    ∀ {l : List C}, x ∈ lostOf F s l ↔ x ∈ l ∧ ¬ F.realized s x
  | [] => ⟨fun mem => (nomatch mem), fun ⟨mem, _⟩ => (nomatch mem)⟩
  | c :: l => match dec c with
    | .isTrue realized =>
      have unfold : lostOf F s (c :: l) = lostOf F s l := if_pos realized
      ⟨fun mem => match (mem_lostOf (l := l)).mp (Eq.subst (motive := fun y => x ∈ y) unfold mem) with
        | ⟨inL, lost⟩ => ⟨.tail c inL, lost⟩,
       fun ⟨mem, lost⟩ => Eq.subst (motive := fun y => x ∈ y) unfold.symm
        ((mem_lostOf (l := l)).mpr ⟨match mem_cons_cases mem with
          | .inl same => absurd (Eq.subst (motive := fun y => F.realized s y) same.symm realized) lost
          | .inr inL => inL, lost⟩)⟩
    | .isFalse missed =>
      have unfold : lostOf F s (c :: l) = c :: lostOf F s l := if_neg missed
      ⟨fun mem => match mem_cons_cases (Eq.subst (motive := fun y => x ∈ y) unfold mem) with
        | .inl same => ⟨Eq.subst (motive := fun y => y ∈ c :: l) same.symm (.head l),
            Eq.subst (motive := fun y => ¬ F.realized s y) same.symm missed⟩
        | .inr mem => match (mem_lostOf (l := l)).mp mem with
          | ⟨inL, lost⟩ => ⟨.tail c inL, lost⟩,
       fun ⟨mem, lost⟩ => Eq.subst (motive := fun y => x ∈ y) unfold.symm
        (match mem_cons_cases mem with
          | .inl same => Eq.subst (motive := fun y => y ∈ c :: lostOf F s l) same.symm (.head _)
          | .inr inL => .tail c ((mem_lostOf (l := l)).mpr ⟨inL, lost⟩))⟩

theorem distinct_lostOf {F : Frame S A C} {s : S} [dec : ∀ c, Decidable (F.realized s c)] :
    ∀ {l : List C}, Distinct l → Distinct (lostOf F s l)
  | [], _ => trivial
  | c :: l, ⟨fresh, distinct⟩ => match dec c with
    | .isTrue realized =>
      Eq.subst (motive := Distinct) (if_pos realized : lostOf F s (c :: l) = lostOf F s l).symm
        (distinct_lostOf distinct)
    | .isFalse missed =>
      Eq.subst (motive := Distinct)
        (if_neg missed : lostOf F s (c :: l) = c :: lostOf F s l).symm
        (⟨fun mem => fresh ((mem_lostOf (l := l)).mp mem).1, distinct_lostOf distinct⟩ :
          Distinct (c :: lostOf F s l))

/-- **Every configuration of a frame whose claims are finitely listed, with realization
decided, has its losses listed.** -/
theorem lossesListed_lostOf {F : Frame S A C} {s : S} [∀ c, Decidable (F.realized s c)]
    {all : List C} (distinct : Distinct all) (every : ∀ c, c ∈ all) :
    F.LossesListed s (lostOf F s all) :=
  ⟨distinct_lostOf distinct, fun c => ⟨fun lost => mem_lostOf.mpr ⟨every c, lost⟩,
    fun mem => (mem_lostOf.mp mem).2⟩⟩

/-! ## Claims read at their time -/

/-- Along the run `r`, claim `c` is read at time `τ`: from `τ` on, `c` is realized exactly
where `support` held of it at `τ`. -/
def ReadsAt (F : Frame S A C) (r : Run F.P) (c : C) (τ : Nat) (support : S → C → Prop) :
    Prop :=
  ∀ t, τ ≤ t → (F.realized (r.state t) c ↔ support (r.state τ) c)

/-- **Restored support does not undo a loss**: a claim read at its time and missed then is
realized at no later step, whatever support holds at that step. -/
theorem ReadsAt.loss_retained {F : Frame S A C} {r : Run F.P} {c : C} {τ : Nat}
    {support : S → C → Prop} (reads : F.ReadsAt r c τ support) (missed : ¬ support (r.state τ) c)
    {t : Nat} (le : τ ≤ t) : ¬ F.realized (r.state t) c :=
  fun realized => missed ((reads t le).mp realized)

/-- **A claim is read at its time exactly when its realization is settled from then on.** -/
theorem readsAt_iff_settled {F : Frame S A C} {r : Run F.P} {c : C} {τ : Nat} :
    (∃ support, F.ReadsAt r c τ support) ↔
      ∀ t, τ ≤ t → (F.realized (r.state t) c ↔ F.realized (r.state τ) c) :=
  ⟨fun ⟨_, reads⟩ t le => (reads t le).trans (reads τ (Nat.le_refl τ)).symm,
   fun settled => ⟨fun s c => F.realized s c, settled⟩⟩

/-- A frame reading current support is not read at the earlier time where support fails then
and returns later. -/
theorem not_readsAt_of_recovery {F : Frame S A C} {r : Run F.P} {c : C} {τ t : Nat}
    (le : τ ≤ t) (missed : ¬ F.realized (r.state τ) c) (restored : F.realized (r.state t) c) :
    ¬ ∃ support, F.ReadsAt r c τ support :=
  fun reads => missed ((readsAt_iff_settled.mp reads t le).mp restored)

end Frame

/-! ## Infinitely many losses: a configuration strictly matched against itself -/

namespace EndlessLosses

/-- One configuration at which every natural-number claim is lost. -/
def frame : Frame Unit Unit Nat := ⟨⟨fun _ _ _ => True⟩, fun _ _ => False⟩

/-- Shifting every loss up by one leaves loss `0` over. -/
theorem self_match : frame.StrictLossMatch (fun _ _ => True) () () :=
  ⟨Nat.succ, fun _ _ => id, fun _ _ => trivial, fun _ _ _ _ same => Nat.succ.inj same, 0, id,
   fun _ _ same => Nat.noConfusion same⟩

/-- So the sufficiency commitment fails at once wherever its scope holds such a pair. -/
theorem no_sufficient_matching (Le : Unit → Unit → Prop) :
    ¬ frame.SufficientMatching (fun _ _ => True) (fun _ _ => True) Le :=
  fun sufficient => sufficient.not_self trivial self_match

end EndlessLosses

end Becoming
