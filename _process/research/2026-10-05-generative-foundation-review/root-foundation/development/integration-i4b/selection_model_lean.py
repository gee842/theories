#!/usr/bin/env python3
"""I4b-2 follow-up (Ren, 16 October 2026: “go ahead with the reframing, first title”): Becoming.Selection's
section “Selection by the record alone” becomes “Selection through a model of the options”. Comments only: every
replacement is asserted to apply once, and the code outside comments is asserted unchanged.
Run from the repository root: python3 -B selection_model_lean.py
"""
import re
from pathlib import Path

PATH = Path('experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Selection.lean')

EDITS = [
("""* **By the record alone.** Options are told apart only by what a record holds of each. A
  selection reads the record alone when exchanging two options' entries exchanges what it
  selects (`Relabel.Equivariant`). Two options are selected alike by every such selection exactly
  when the record ties them (`Relabel.selected_alike_iff`), as a selection through registration
  reaches exactly what registers. One selecting at most one option singles out exactly the
  options whose entry no other option shares (`Relabel.singled_iff_untied`, the selection
  `Relabel.Alone`), and at a full tie of two or more options it selects none
  (`Relabel.Equivariant.none_of_full_tie`). A valuation reading the record alone, such as a
  weight on each option, gives tied options equal values (`Relabel.EquivariantValue.tied`,
  `Relabel.valued_alike_iff`), and a choice of one option chooses no tied option and withholds at
  a full tie (`Relabel.EquivariantChoice.untied`, `Relabel.EquivariantChoice.withholds_of_full_tie`).
  Exchanging two options tells them apart: their equality is decided, a condition each statement
  names. Reading (the AI's, pending Ren): which option is which is not part of the record's
  relations; to part what the record ties takes a further recorded relation, such as an order of
  arrival or an agreement.
""",
"""* **Through a model of the options.** A selector tells options apart only through its model of
  them: an entry for each option, of any kind; options given one entry are tied, lumped together
  by the model. A selection is through the model when exchanging two options' entries exchanges
  what it selects (`Relabel.Equivariant`). Two options are selected alike by every such selection
  exactly when the model ties them (`Relabel.selected_alike_iff`), as a selection through
  registration reaches exactly what registers. One selecting at most one option singles out
  exactly the options whose entry no other option shares (`Relabel.singled_iff_untied`, the
  selection `Relabel.Alone`), and at a full tie of two or more options it selects none
  (`Relabel.Equivariant.none_of_full_tie`). A valuation through the model, such as a weight on
  each option, gives tied options equal values (`Relabel.EquivariantValue.tied`,
  `Relabel.valued_alike_iff`), and a choice of one option chooses no tied option and withholds at
  a full tie (`Relabel.EquivariantChoice.untied`, `Relabel.EquivariantChoice.withholds_of_full_tie`).
  Exchanging two options tells them apart: their equality is decided, a condition each statement
  names. The model is a lumping (`Lumped` of `Becoming.Learning`), and a selection through it is
  right about what matters only where what matters goes alike across the lumping
  (`Learning.selects_right_through`, `Learning.selects_not_right_of_parted`). Reading (the AI's
  reading of Ren's correction of 16 October 2026, which Ren approved the same day): what a model
  lumps, no selection through it can separate; separating them takes a finer model, and whether
  that model is right is its fit to what matters, which a longer memory does not supply: memory
  gives distinctions, not their relevance.
"""),
("that reaching beyond is chosen, that a selection reads the record alone, and how an option it\n",
 "that reaching beyond is chosen, that a selection is through a given model, and how an option it\n"),
("""/-! ## Selection by the record alone

Options are told apart only by what a record holds of each: an entry per option, of any kind. A
selection among them reads the record alone when exchanging two options' entries exchanges what it
selects (`Relabel.Equivariant`); a valuation of the options, such as a weight on each, reads the
record alone when it exchanges their values (`Relabel.EquivariantValue`); a choice of at most one
option does when it exchanges the choice (`Relabel.EquivariantChoice`). As a selection through
registration reaches exactly what registers (`Web.selects_alike_iff`), a selection by the record
alone reaches exactly what the record parts. -/""",
"""/-! ## Selection through a model of the options

A selector tells options apart only through its model of them: an entry per option, of any kind,
the options given one entry being tied, lumped together by the model (`Lumped` of
`Becoming.Learning`). A selection among them is through the model when exchanging two options'
entries exchanges what it selects (`Relabel.Equivariant`); a valuation of the options, such as a
weight on each, is through the model when it exchanges their values (`Relabel.EquivariantValue`);
a choice of at most one option is when it exchanges the choice (`Relabel.EquivariantChoice`). As a
selection through registration reaches exactly what registers (`Web.selects_alike_iff`), a
selection through a model separates exactly what the model separates. -/"""),
("/-- A selection reads the record alone: where `r'` is `r` with the entries of `a` and `b`\n",
 "/-- A selection is through the model: where `r'` is `r` with the entries of `a` and `b`\n"),
("/-- A valuation of the options reads the record alone: exchanging two options' entries exchanges\n",
 "/-- A valuation of the options is through the model: exchanging two options' entries exchanges\n"),
("/-- A choice of at most one option reads the record alone: exchanging two options' entries\n",
 "/-- A choice of at most one option is through the model: exchanging two options' entries\n"),
("/-- Exchanging two tied options leaves the record as it was. -/",
 "/-- Exchanging two tied options leaves the model as it was. -/"),
("""/-- **A selection by the record alone reaches exactly what the record parts.** Two options are
selected alike by every selection reading the record alone exactly when the record ties them. -/""",
"""/-- **A selection through a model separates exactly what the model separates.** Two options are
selected alike by every selection through the model exactly when the model ties them. -/"""),
("""/-- **What is singled out is untied.** A selection reading the record alone that selects at most
one option""",
"""/-- **What is singled out is untied.** A selection through the model that selects at most one
option"""),
("""/-- At a full tie of two or more options, a selection reading the record alone that selects at
most one option selects none. -/""",
"""/-- At a full tie of two or more options, a selection through the model that selects at most one
option selects none. -/"""),
("/-- The option holding `v` alone in the record. -/", "/-- The option holding `v` alone in the model. -/"),
("/-- Holding an entry alone is read off the record alone. -/", "/-- Holding an entry alone is read through the model. -/"),
("""/-- **An option is singled out exactly where the record parts it.** Some selection reading the
record alone, selecting at most one option at each record, selects""",
"""/-- **An option is singled out exactly where the model separates it.** Some selection through the
model, selecting at most one option at each model, selects"""),
("/-- The options taking a given value form a selection reading the record alone. -/",
 "/-- The options taking a given value form a selection through the model. -/"),
("/-- A constant valuation, the same weight on every option, reads the record alone. -/",
 "/-- A constant valuation, the same weight on every option, is through the model. -/"),
("/-- The entry itself is a valuation reading the record alone. -/",
 "/-- The entry itself is a valuation through the model. -/"),
("""/-- Two options are valued alike by every valuation reading the record alone exactly when the
record ties them. -/""",
"""/-- Two options are valued alike by every valuation through the model exactly when the model
ties them. -/"""),
("/-- A choice reading the record alone selects, reading the record alone, the option it chooses. -/",
 "/-- A choice through the model selects, through the model, the option it chooses. -/"),
("/-- **A choice reading the record alone chooses no tied option.** -/",
 "/-- **A choice through the model chooses no tied option.** -/"),
("/-- **At a full tie of two or more options a choice reading the record alone withholds.** -/",
 "/-- **At a full tie of two or more options a choice through the model withholds.** -/"),
]


def code(text):
    """The text outside comments: block comments (nested) and line comments removed, whitespace collapsed."""
    out, i, depth = [], 0, 0
    while i < len(text):
        if text.startswith('/-', i):
            depth += 1
            i += 2
        elif depth and text.startswith('-/', i):
            depth -= 1
            i += 2
        elif depth:
            i += 1
        elif text.startswith('--', i):
            i = text.find('\n', i)
            i = len(text) if i < 0 else i
        else:
            out.append(text[i])
            i += 1
    return re.sub(r'\s+', ' ', ''.join(out))


before = PATH.read_text()
after = before
for old, new in EDITS:
    assert after.count(old) == 1, old[:80]
    after = after.replace(old, new)
assert code(after) == code(before), 'code outside comments changed'
long = lambda text: {line for line in text.splitlines() if len(line) > 100}
assert long(after) <= long(before), long(after) - long(before)  # no new line past 100 columns
assert 'record alone' not in after and 'reading the record' not in after and 'reads the record' not in after
PATH.write_text(after)
print(PATH)
