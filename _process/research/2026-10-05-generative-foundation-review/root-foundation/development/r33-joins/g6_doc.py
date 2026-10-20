#!/usr/bin/env python3
"""R33 (G6): LoopReturn's header says what the join with Becoming.Loops states."""
from pathlib import Path
B = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
p = B / 'LoopReturn.lean'
s = p.read_text()
old = """is one number, a simplification of Rejoining's levels at many conditions; no theorem here reads a
loop of Rejoining as a return map.
"""
new = """is one number, a simplification of Rejoining's levels at many conditions; no theorem here reads a
loop of Rejoining as a return map. A link's *factor* is what one turn makes of the difference it
receives; a *strength* is only a coupling strength of `Becoming.Propagation`, and around a cycle the
product of the coupling strengths (`Loops.product`). The last section joins the two.
"""
assert s.count(old) == 1
s = s.replace(old, new)
old = """  gradually needs a link that is not a multiplication.

What is not derived:"""
new = """  gradually needs a link that is not a multiplication.
* **The return map is the carried amount of `Becoming.Loops`.** For one condition returning its
  current level to itself with coupling strength `M` (`Loops.SelfLoop.strengths`), the carried
  amount from a starting gap `D` is, at every step, the course from `D` of the loop of one link with
  factor `1 + M`, one turn a step (`LoopReturn.selfLoop_carried`, through
  `LoopReturn.geomBound_eq_course`). The carried amount is attained by the course the carrying law
  generates, against the quiet course (`carried_attained`), so where the actual response attains the
  carrying bound the gap itself is that course (`LoopReturn.selfLoop_gap`). Around every cycle of
  `m + 1` couplings holding at every step, the carried amount after `R` times around is at least the
  course after `R` turns of the loop of one link with factor one plus the product of the coupling
  strengths around the cycle (`LoopReturn.carried_around_course`, from `carried_runaway`). The one is
  the holding: the carrying law takes nothing, so a condition keeps what it had while the cycle
  returns more. A positive whole-number strength gives a factor of at least `2`, the doubling of
  `carried_doubles_around`.

What is not derived:"""
assert s.count(old) == 1
s = s.replace(old, new)
old = """and which of keeping, closing or widening a difference supports the generation of life in the
whole, which goes through the comparison and the condition of the chapter's §6.15."""
new = """the carried amount around a cycle of more than one condition as a return map (intermediate
conditions hold and keep giving, so a turn is not a map of one number; the bound above is what
holds); and which of keeping, closing or widening a difference supports the generation of life in
the whole, which goes through the comparison and the condition of the chapter's §6.15."""
assert s.count(old) == 1
s = s.replace(old, new)
p.write_text(s)
