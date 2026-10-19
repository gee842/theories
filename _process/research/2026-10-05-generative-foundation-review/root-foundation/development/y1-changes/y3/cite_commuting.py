#!/usr/bin/env python3
"""Where SG's `Becoming.Commuting` has landed before Y3, state Y3's commuting laws as its instances
instead of proving them again: import it, take the runs of the nuclear law under a symmetry from
`Law.Commutes.iterate` (dropping Y3's own `orbit_commutes`), the runs from a configuration and its
complement apart from `Law.Commutes.apart` with `complement_moves`, and drop Y3's `complement_ne`,
which says what `complement_moves` says and nothing else uses then. usage: python3 -B cite_commuting.py MODULE_FILE (edited in place; each edit must
match exactly once)."""
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text()


def once(old, new):
    global text
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    text = text.replace(old, new)


once('import Becoming.HexagramPlaces\n', 'import Becoming.HexagramPlaces\nimport Becoming.Commuting\n')
once("""  run of it to a run of it (`nuclear_run_act`). Changing every line leaves nothing as it is
  (`complement_ne`), so the runs from a configuration and from its complement never meet
  (`run_complement_apart`). A class is named by its member of least binary value (`classOf`), and
  two hexagrams are in one class exactly where a symmetry takes one to the other (`classOf_eq_iff`).""",
     """  run of it to a run of it (`nuclear_run_act`, by `Law.Commutes.iterate`). Changing every line
  leaves nothing as it is (`complement_moves`), so the runs from a configuration and from its
  complement never meet (`run_complement_apart`), the instance of what a commuting law keeps apart
  (`Law.Commutes.apart`). A class is named by its member of least binary value (`classOf`), and
  two hexagrams are in one class exactly where a symmetry takes one to the other (`classOf_eq_iff`).""")
once("""/-- A map that commutes with a law takes its orbits to orbits. -/
theorem orbit_commutes {next f : Hexagram → Hexagram} (comm : ∀ s, next (f s) = f (next s))
    (s : Hexagram) : ∀ n, Law.orbit next (f s) n = f (Law.orbit next s n)
  | 0 => rfl
  | n + 1 => (congrArg next (orbit_commutes comm s n)).trans (comm _)

""", '')
once("""/-- **Changing every line leaves nothing as it is**, so no class has one member. -/
theorem complement_ne : ∀ s : Hexagram, complement s ≠ s
  | ⟨true, _, _, _, _, _⟩ => fun h => Bool.noConfusion (congrArg Hexagram.l1 h)
  | ⟨false, _, _, _, _, _⟩ => fun h => Bool.noConfusion (congrArg Hexagram.l1 h)

""", '')
once("""/-- **So each takes every run of the nuclear law to a run of it.** -/
theorem nuclear_run_act (g : Symmetry) (s : Hexagram) (n : Nat) :
    (Law.run nuclear (g.act s)).state n = g.act ((Law.run nuclear s).state n) :=
  orbit_commutes (nuclear_act g) s n
""", """/-- **So each takes every run of the nuclear law to a run of it** (`Law.Commutes.iterate`). -/
theorem nuclear_run_act (g : Symmetry) (s : Hexagram) (n : Nat) :
    (Law.run nuclear (g.act s)).state n = g.act ((Law.run nuclear s).state n) :=
  Law.Commutes.iterate (nuclear_act g) s n
""")
once("""/-- **The runs from a configuration and from its complement never meet**: at every step they are
each other's complements, and no configuration is its own (`complement_ne`). -/
theorem run_complement_apart (s : Hexagram) (n : Nat) :
    (Law.run nuclear (complement s)).state n ≠ (Law.run nuclear s).state n :=
  fun meet => complement_ne _ ((nuclear_run_act .change s n).symm.trans meet)
""", """/-- **The runs from a configuration and from its complement never meet**: the nuclear law commutes
with the complement, which moves every configuration, so this is what a commuting law keeps apart
(`Law.Commutes.apart`). -/
theorem run_complement_apart (s : Hexagram) (n : Nat) :
    (Law.run nuclear (complement s)).state n ≠ (Law.run nuclear s).state n :=
  Law.Commutes.apart nuclear_complement complement_moves s n
""")
path.write_text(text)
print('cited Becoming.Commuting in', path)
