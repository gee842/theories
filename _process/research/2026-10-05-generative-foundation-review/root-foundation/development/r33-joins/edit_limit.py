import sys
p = sys.argv[1]
s = open(p).read()
old = '''/-- A guess of values identifies the hypothesis `H` in the limit where on each run it is `H`'s value
from some horizon on. -/
def Identifies (g : Nat → Run P → V) (H : Run P → V) : Prop :=
  ∀ r, ∃ n, ∀ k, n ≤ k → g k r = H r
'''
new = '''/-- A guess of values tracks the target `h` in the limit where on each run, from some horizon on,
it is the target's value at the horizon. The target may change with the horizon. -/
def Tracks (g : Nat → Run P → V) (h : Nat → Run P → V) : Prop :=
  ∀ r, ∃ n, ∀ k, n ≤ k → g k r = h k r

/-- A guess of values identifies the hypothesis `H` in the limit where on each run it is `H`'s value
from some horizon on: it tracks the target that is `H` at every horizon. -/
def Identifies (g : Nat → Run P → V) (H : Run P → V) : Prop :=
  Tracks g fun _ r => H r

/-- **Identification is tracking a target that does not change with the horizon.** -/
theorem identifies_iff_tracks {g : Nat → Run P → V} {H : Run P → V} :
    Identifies g H ↔ Tracks g fun _ r => H r :=
  Iff.rfl

/-- **Tracked by the same guess, two targets agree from some horizon on**, on every run. -/
theorem Tracks.agree {g : Nat → Run P → V} {h h' : Nat → Run P → V} (tracks : Tracks g h)
    (tracks' : Tracks g h') (r : Run P) : ∃ n, ∀ k, n ≤ k → h k r = h' k r :=
  match tracks r, tracks' r with
  | ⟨n, at_h⟩, ⟨n', at_h'⟩ => ⟨n + n', fun k le =>
    (at_h k (Nat.le_trans (Nat.le_add_right n n') le)).symm.trans
      (at_h' k (Nat.le_trans (Nat.le_add_left n' n) le))⟩
'''
assert s.count(old) == 1
s = s.replace(old, new)
old2 = '''**Identification.** A guess of values that converges on each run to the run's hypothesis verifies
and refutes in the limit each reading "the hypothesis is `v`" (`identifies_verifies`,
`identifies_refutes`): identification in the limit decides each hypothesis in the limit.'''
new2 = '''**Identification.** A guess of values tracks a target in the limit where on each run, from some
horizon on, it is the target's value at the horizon (`Tracks`); it identifies a hypothesis where it
tracks a target that does not change with the horizon (`Identifies`, `identifies_iff_tracks`), and
two targets the same guess tracks agree from some horizon on (`Tracks.agree`). A guess that
identifies the run's hypothesis verifies and refutes in the limit each reading "the hypothesis is
`v`" (`identifies_verifies`, `identifies_refutes`): identification in the limit decides each
hypothesis in the limit. Learning through a map (`Becoming.Learnable`, `Becoming.LearnableRuns`) is
the case of a guess fixed by the record through the map that tracks a feature along the run
(`LearnableRuns.learnable_iff_tracks`); it is identification where the feature does not change along
the run (`LearnableRuns.learnable_iff_identifies`), and not otherwise
(`LearnableRuns.Merge.not_identifies`).'''
assert s.count(old2) == 1
s = s.replace(old2, new2)
open(p, 'w').write(s)
