#!/usr/bin/env python3
"""Register Becoming.SharedCodes in the package (board item SC); idempotent.

usage: python3 -B register.py [REPO]

Inserts the import and the module-list entry in Becoming.lean, the row of the package README,
and the module in the checker's CORE list and SCOPE text. Each insertion is anchored on the
entry of a module the new one sits beside and is skipped where the text is already present, so
the script can be rerun on a newer main before landing.
"""
from pathlib import Path
import sys

REPO = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[6])
PKG = REPO / "experiments/integrated-correction/general-framework/generative-basis/lean/becoming"

IMPORT = "import Becoming.SharedCodes\n"
IMPORT_AFTER = "import Becoming.PlaceTransitionNets\n"

ENTRY = """* `Becoming.SharedCodes` (L4): a code formed between formations, with no premise beyond what each
  law names. Codes map senses to forms and change only by hearing, a process of the spine. Hearing
  makes no form; a group's agreement is kept exactly through the hearings closed for it, and
  agreement of all is a rest under every rule. After an order of hearings each formation holds
  the start's form of its origin, so an order forms agreement from every start exactly where it
  gives every formation one origin, and the forms an order can make shared are exactly the forms
  in use; where each takes at once the code a pointer gives it, every start agrees exactly where
  the pointer's paths have met, and being joined through couplings is not enough. A formation reads another's form for a sense as that sense exactly where their codes
  agree there; agreement formed sense by sense can merge senses. Hearing keeps every renaming of
  forms, and a law keeping an exchange of formations with a renaming that moves every form never
  brings a symmetric disagreement to agreement (`Law.KeepsRelation`, `Law.Commutes.keeps_fixed`):
  agreement needs a centre, a preferred form or an order of hearing. An imposed code makes all
  agree, its source loses nothing, and what it merges comes back only from a form kept outside
  it. A reading written back into the records later generations read rests at once; later
  records do not recover what came before (`Law.merged_stays`), records kept from before bar a
  different resolution, and where records are only added a resolution can be lost but never
  replaced.
"""
ENTRY_AFTER_START = "* `Becoming.CrossSituational` (L4):"

ROW = ("| L4 | [`Becoming.SharedCodes`](Becoming/SharedCodes.lean) | a code formed between formations "
       "(no premise beyond what each law names): codes map senses to forms and change by hearing "
       "(`process`); hearing makes no form (`run_held`), a group's agreement is kept exactly through "
       "closed hearings (`kept_iff`, `run_agreement_kept`) and agreement of all is a rest "
       "(`all_agree_rest`); the start and the order fix the form reached (`run_origin`), agreement "
       "from every start exactly with one origin (`agrees_every_start_iff`), the forms that can be "
       "shared exactly those in use (`shared_iff_in_use`), following a pointer agreement exactly "
       "where its paths meet and coupling not enough (`follow_agrees_iff`, `Path.never_agree`); reading across exactly where codes agree "
       "(`reads_iff`), and agreement sense by sense can merge senses (`keeps_apart_iff`); no form "
       "privileged (`run_renamed`, `renamed_carries_iff`); agreement needs a broken symmetry "
       "(`never_agrees_of_both`, `pair_never_agrees`, `TwoFormations.three_agree`); an imposed code "
       "stays and its merges return only from forms kept outside (`run_imposed_stays`, "
       "`outside_needed`, `outside_returns`); a reading written back rests, merges the histories "
       "before it and is barred only by records kept from before (`written_rests`, "
       "`resolved_alike_merged`, `omitted_rest`, `kept_bars`); where records are only added a "
       "resolution is lost but never replaced (`added_never_replaced`) |\n")
ROW_AFTER_START = "| L4 | [`Becoming.Commuting`]"

CORE_ITEM = '"Becoming.SharedCodes", '
CORE_AFTER = '"Becoming.CrossSituational", '

SCOPE_TEXT = (
    '    "SharedCodes: codes from senses to forms held by formations change only by hearing; "\n'
    '    "hearing makes no form and keeps a group\'s agreement exactly through closed hearings; "\n'
    '    "after an order each formation holds its origin\'s start form, so an order forms "\n'
    '    "agreement from every start exactly with one origin and can share exactly the forms in "\n'
    '    "use; following a pointer, every start agrees exactly where its paths have met, and "\n'
    '    "being joined through couplings is not enough; reading across holds exactly where codes "\n'
    '    "agree; hearing keeps every renaming of "\n'
    '    "forms, and a law keeping an exchange of formations with a renaming moving every form "\n'
    '    "never resolves a symmetric disagreement; an imposed code stays and its merges return "\n'
    '    "only from forms kept outside; a resolution written back into the records rests, merges "\n'
    '    "the histories before it and is barred only by records kept from before; where records "\n'
    '    "are only added a resolution is lost but never replaced. "\n')
SCOPE_BEFORE = '    "PlaceTransitionNets: a place/transition net, defined by its own rules (pre and post "\n'


def insert_after_line(text, anchor, addition):
    assert text.count(anchor) == 1, anchor
    i = text.index(anchor) + len(anchor)
    return text[:i] + addition + text[i:]


def insert_after_entry(text, start, addition):
    """Insert after the bullet or row that begins with `start` (up to the next one)."""
    assert text.count(start) == 1, start
    i = text.index(start)
    j = text.index("\n", i)
    while True:
        k = text.index("\n", j + 1)
        line = text[j + 1:k]
        if not line.startswith("  ") or line.startswith("* "):
            break
        j = k
    return text[:j + 1] + addition + text[j + 1:]


def main():
    lean = PKG / "Becoming.lean"
    text = lean.read_text(encoding="utf-8")
    if IMPORT not in text:
        text = insert_after_line(text, IMPORT_AFTER, IMPORT)
    if "* `Becoming.SharedCodes`" not in text:
        text = insert_after_entry(text, ENTRY_AFTER_START, ENTRY)
    lean.write_text(text, encoding="utf-8")

    readme = PKG / "README.md"
    text = readme.read_text(encoding="utf-8")
    if "[`Becoming.SharedCodes`]" not in text:
        assert text.count(ROW_AFTER_START) == 1
        i = text.index(ROW_AFTER_START)
        j = text.index("\n", i)
        text = text[:j + 1] + ROW + text[j + 1:]
    readme.write_text(text, encoding="utf-8")

    checker = PKG / "check_becoming.py"
    text = checker.read_text(encoding="utf-8")
    if CORE_ITEM not in text:
        text = insert_after_line(text, CORE_AFTER, CORE_ITEM)
    if '"SharedCodes: ' not in text:
        assert text.count(SCOPE_BEFORE) == 1
        i = text.index(SCOPE_BEFORE)
        text = text[:i] + SCOPE_TEXT + text[i:]
    checker.write_text(text, encoding="utf-8")
    print("registered Becoming.SharedCodes in", PKG)


if __name__ == "__main__":
    main()
