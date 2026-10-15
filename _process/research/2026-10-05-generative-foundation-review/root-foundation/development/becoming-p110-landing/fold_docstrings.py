"""Fold the P110 decisions into the Lean docstrings of the Becoming package.

Usage:
  python3 -B fold_docstrings.py ROOT          apply, write the changed modules
  python3 -B fold_docstrings.py ROOT --dry    report only

Docstrings that mark a reading "the AI's, pending Ren", or leave a choice of reading to Ren
that DELEGATED-CHOICES decides on Ren's delegation of 15 October 2026, are rewritten as
decided, with the decision's number in the module docstrings (the root module's bullets name
no number; each module's own docstring does). Readings Ren adopted earlier say so (the
re-founding, 14 October 2026). What stays Ren's (section 10 of DELEGATED-CHOICES) is not
touched, and nothing outside comments changes: for every file, the text with comments and
docstrings removed is asserted to be identical before and after, so no statement, proof or
name can change. Each replacement is asserted to occur exactly once, matching across line
breaks; where the original phrase wrapped, the line break is kept after the same word.
"""
import re
import sys
from pathlib import Path

LEAN = Path("experiments/integrated-correction/general-framework/generative-basis/lean/becoming")
DC = "DELEGATED-CHOICES"
DEL = "adopted on Ren's delegation of 15 October 2026"


def readings(d):
    return ("**Readings (the AI's, pending Ren).**", f"**Readings (the AI's, {DEL}, {DC} {d}).**")


def ai_reading(d):
    return ("**AI reading, pending Ren.**", f"**AI reading, {DEL} ({DC} {d}).**")


def tail(d, plural=True):
    noun = "readings are" if plural else "reading is"
    return (f"The {noun} the AI's, pending Ren.", f"The {noun} the AI's, {DEL} ({DC} {d}).")


MODULES = {
    "Admission": [ai_reading("D2, D22, D35")],
    "Attraction": [readings("D25")],
    "Boundaries": [
        ai_reading("D21"),
        ("(`Flow.presupposition_order`). Whether this direction fits is Ren's to judge.",
         "(`Flow.presupposition_order`). This direction is adopted as the reading of Ren's order "
         f"of levels on Ren's delegation of 15 October 2026 ({DC} D21)."),
    ],
    "Branching": [readings("D32")],
    "Capture": [readings("D26")],
    "Composition": [tail("D33")],
    "Counterfactual": [readings("D25")],
    "Coupling": [("which carry it to the move, are the AI's, pending Ren.",
                  f"which carry it to the move, are the AI's, {DEL}, with their qualifiers ({DC} D24).")],
    "Decidedness": [ai_reading("D30")],
    "Distinguishing": [("The readings are the AI's, pending Ren: what tells",
                        f"The readings are the AI's, {DEL} ({DC} D34): what tells")],
    "Experiment": [readings("D25")],
    "Feedback": [ai_reading("D20")],
    "Feeding": [ai_reading("D17")],
    "Granularity": [("The readings of these results are the AI's, pending Ren.",
                     f"The readings of these results are the AI's, {DEL} ({DC} D33).")],
    "GranularityBridge": [("The readings of these results are the AI's, pending Ren.",
                           f"The readings of these results are the AI's, {DEL} ({DC} D33).")],
    "Histories": [("**Readings.** The AI's, pending Ren.", f"**Readings.** The AI's, {DEL} ({DC} D32).")],
    "Imbalance": [
        ("**AI reading, pending Ren.**", "**AI reading, adopted by Ren with the re-founding on 14 October 2026.**"),
        ("Whether to adopt the re-founding is Ren's; the laws",
         "Ren adopted the re-founding on 14 October 2026 (“please, finish all”); the laws"),
    ],
    "Interdependence": [ai_reading("D17")],
    "Joining": [("The readings of these results are the AI's, pending Ren.",
                 f"The readings of these results are the AI's, {DEL} ({DC} D33).")],
    "JoiningBridge": [("The readings of these results are the AI's, pending Ren.",
                       f"The readings of these results are the AI's, {DEL} ({DC} D33).")],
    "Learning": [
        ("- (The AI's, pending Ren.) Induction is resolved",
         f"- (The AI's, {DEL}, {DC} D26.) Induction is resolved"),
        ("- (The AI's, pending Ren.) For a trained network",
         f"- (The AI's, {DEL}, {DC} D26.) For a trained network"),
        ("- (The AI's, pending Ren.) The meta level",
         f"- (The AI's, {DEL}, {DC} D26.) The meta level"),
    ],
    "Likeness": [tail("D23")],
    "Listing": [ai_reading("D30")],
    "Mechanism": [readings("D25")],
    "Metaethics": [("This is the working stepwise candidate, pending Ren's choice of the reading.",
                    "This is the stepwise reading, kept beside the whole-run and relation-level "
                    f"readings on Ren's delegation of 15 October 2026; no comparison uses it ({DC} D1, D10).")],
    "Novelty": [readings("D27")],
    "Order": [("Reading (the AI's, pending Ren): for the laws",
               f"Reading (the AI's, {DEL}, {DC} D30): for the laws")],
    "OrderNormal": [("Reading (the AI's, pending Ren): the order",
                     f"Reading (the AI's, {DEL}, {DC} D30): the order")],
    "Persistence": [("Readings (the AI's, pending Ren): that what holds",
                     f"Readings (the AI's, {DEL}, {DC} D5): that what holds")],
    "Ranking": [("the working candidate after review pending Ren's choice: an event is living",
                 "kept beside the whole-run reading on Ren's delegation of 15 October 2026, with no "
                 f"comparison using it ({DC} D1, D10): an event is living")],
    "Reading": [readings("D27, D28")],
    "Readings": [readings("D23")],
    "Refinement": [tail("D34")],
    "Regions": [ai_reading("D20")],
    "Relevance": [ai_reading("D1, D16")],
    "Response": [readings("D25")],
    "Runaway": [readings("D26")],
    "Seeking": [readings("D26")],
    "Selection": [readings("D25")],
    # Registration formally as the law's sensitivity; 识 itself stays Ren's reading (D37).
    "Sensitivity": [("**Readings (the AI's, pending Ren).**",
                     f"**Readings (the AI's, {DEL}, {DC} D37; 识 itself stays Ren's reading).**")],
    "Significance": [ai_reading("D16")],
    "Space": [
        ("Which parts Ren's \"generative\" and \"degenerative\" name is Ren's to choose. Ren wrote,",
         "On Ren's delegation of 15 October 2026, Ren's \"generative\" and \"degenerative\" read as "
         "widening and narrowing what can form, and at the level of formations as renewing and "
         f"consuming ({DC} D2). Ren wrote,"),
        ("coincide in finite worlds. This module states the second.",
         "coincide in finite worlds, so this reading is not what the pair names (D2). This module "
         "states the second."),
        ("only on the stepwise verdict about drawing on a self-bearing relatum at its ending, which is Ren's to choose. The grazer's event lies outside that choice as worded,",
         "only on the stepwise verdict about drawing on a self-bearing relatum at its ending, a "
         f"theorem of that reading which no comparison uses ({DC} D6). The grazer's event lies "
         "outside that verdict as worded,"),
        ("Whether undermining that co-occurs with the relatum depending not being active after the step counts against living, and for which drawers, is a question of the same kind.",
         "Undermining that co-occurs with the relatum depending not being active after the step is "
         "a verdict of the same kind, for every drawer, and values no drawer: whether a course is "
         "worse is for the comparison on possibilities (D6)."),
        ("Whether such drawing at an ending counts as not living is Ren's to choose.",
         "On the stepwise reading such drawing at an ending is not living, for every drawer, and the "
         f"verdict values no drawer ({DC} D6)."),
    ],
    "Standpoints": [("is the AI's reading of Ren's proposal, pending Ren.",
                     f"is the AI's reading of Ren's proposal, {DEL} ({DC} D11)."),
                    ("Whether conveyance counts as a formed relation is Ren's choice, as for interaction, living on and descent.",
                     "On Ren's delegation of 15 October 2026 conveyance counts as a formed relation, as "
                     f"interaction, living on and descent do ({DC} D9, D12).")],
    "Succession": [("Read (the AI's, pending Ren): the dependence",
                    f"Read (the AI's, {DEL}, {DC} D12): the dependence")],
    "Transmission": [tail("D31")],
    "Unfolding": [
        ("there are no two realities\". The rest are the AI's, pending Ren.",
         f"there are no two realities\". The rest are the AI's, {DEL} ({DC} D23)."),
        ("- `World` is where the core begins;",
         "- (Superseded: on 14 October 2026 Ren asked “why do we need \"World\"?” and approved the "
         "readings in context as the general case, `World` being the case where they glue, "
         "`Becoming.Readings`; DELEGATED-CHOICES D23.) `World` is where the core begins;"),
    ],
    "Weighted": [("**Readings.** The AI's, pending Ren.", f"**Readings.** The AI's, {DEL} ({DC} D30).")],
    "Wholes": [("At which level 生生不息 is read is Ren's.",
                f"On Ren's delegation of 15 October 2026 生生不息 is read at the level of the whole, as "
                "arising that recurs through renewal, lineages and members being levels within it "
                f"({DC} D5).")],
    "Descent": [("Whether living on a relatum and descent count as formed relations for N_rel, so that",
                 "On Ren's delegation of 15 October 2026 living on a relatum and descent count as formed "
                 "relations of continuation for N_rel, not as direct valuations, so that"),
                ("a parent reaches its offspring, is a correspondence choice and Ren's.",
                 f"a parent reaches its offspring ({DC} D9).")],
    "Generation": [("which 生 the second 生 names, and whether an arising on a consumed condition is 生成 at all, are Ren's to say.",
                    "on Ren's delegation of 15 October 2026 the second 生 ranges over what can form, active "
                    f"or not, and arising on a consumed condition is classed by the comparison ({DC} D3).")],
    "Roles": [("whatever ends it; whether it should, and for which drawers, belongs to the reading of 生生, which is Ren's.",
               "whatever ends it; on Ren's delegation of 15 October 2026 this stays a verdict of the "
               f"stepwise reading, for every drawer, valuing no drawer ({DC} D6).")],
    "Gain": [("**Readings (the AI's, decided on Ren's delegation of 15 October 2026; P110).**",
              f"**Readings (the AI's, {DEL}, {DC} D7, D27).**"),
             ("`Becoming.Coupling` (P109) states the counterpart", "`Becoming.Coupling` states the counterpart")],
}

ROOT_DEL = "adopted on Ren's delegation of 15 October 2026"
ROOT = [
    # Specific bullets first; the generic sentence follows.
    ("English names of this reading; which parts Ren's generative and degenerative name is Ren's to choose.",
     "English names of this reading; Ren's generative and degenerative read, on Ren's delegation of "
     "15 October 2026, as widening and narrowing what can form, which this reading is not "
     "(DELEGATED-CHOICES D2)."),
    ("condition read as the rest idle. The readings are the AI's, pending Ren.",
     "condition read as the rest idle. The readings are the AI's, adopted with the re-founding."),
    ("are connected by descent alone. Whether these readings count as formed relations is Ren's choice.",
     "are connected by descent alone. On Ren's delegation of 15 October 2026 these readings count as "
     "formed relations of continuation, not as direct valuations (DELEGATED-CHOICES D9)."),
    ("is the AI's reading of Ren's proposal of 10 October 2026, pending Ren.",
     f"is the AI's reading of Ren's proposal of 10 October 2026, {ROOT_DEL}."),
    ("The readings are the AI's, narrowed by the independent review, pending Ren.",
     f"The readings are the AI's, narrowed by the independent review and {ROOT_DEL} as narrowed."),
    ("the other readings are the AI's, pending Ren.", f"the other readings are the AI's, {ROOT_DEL}."),
]
ROOT_GENERIC = [
    ("The readings are the AI's, pending Ren.", f"The readings are the AI's, {ROOT_DEL}."),
    ("The readings are the AI’s, pending Ren.", f"The readings are the AI’s, {ROOT_DEL}."),
    ("The reading is the AI's, pending Ren.", f"The reading is the AI's, {ROOT_DEL}."),
]

README = LEAN / "README.md"
README_SPECIFIC = [
    ("Ren 的“生成的”“退化的”指哪些部分由 Ren 定；",
     "Ren 的“生成的”“退化的”依 Ren 的交托读作对能形成者的扩大与缩小，不是这一读法（DELEGATED-CHOICES D2）；"),
    ("and which parts Ren's generative and degenerative name is Ren's to choose;",
     "and Ren's generative and degenerative read, on Ren's delegation, as widening and narrowing what "
     "can form, which this reading is not (DELEGATED-CHOICES D2);"),
    ("采用之后，核心现有的规律仍以平衡为局部条件陈述；读法是 AI 的，待 Ren",
     "采用之后，核心现有的规律仍以平衡为局部条件陈述；读法是 AI 的，随这一重建采用"),
    ("in their statements; the readings are the AI's, pending Ren",
     "in their statements; the readings are the AI's, adopted with the re-founding"),
    ("这些读法是否算作已形成的关系，由 Ren 选择",
     "依 Ren 的交托，这些读法算作延续的已形成关系，不是直接的估值（DELEGATED-CHOICES D9）"),
    ("whether these readings count as formed relations is Ren's choice",
     "on Ren's delegation these readings count as formed relations of continuation, not as direct "
     "valuations (DELEGATED-CHOICES D9)"),
    ("是 AI 对 Ren 提议的读法，待 Ren 判断",
     "是 AI 对 Ren 提议的读法，依 Ren 的交托采用（DELEGATED-CHOICES D11）"),
    ("is the AI's reading of Ren's proposal, pending Ren",
     "is the AI's reading of Ren's proposal, adopted on Ren's delegation (DELEGATED-CHOICES D11)"),
    ("读法是 AI 的，经审查收窄，待 Ren", "读法是 AI 的，经审查收窄，依 Ren 的交托按收窄后采用"),
    ("the readings are the AI's, narrowed by review, pending Ren",
     "the readings are the AI's, narrowed by review and adopted as narrowed on Ren's delegation"),
]
README_GENERIC = [
    ("读法是 AI 的，待 Ren", "读法是 AI 的，依 Ren 的交托采用"),
    ("the readings are the AI's, pending Ren", "the readings are the AI's, adopted on Ren's delegation"),
    ("the reading is the AI's, pending Ren", "the reading is the AI's, adopted on Ren's delegation"),
    ("the other readings are the AI's, pending Ren", "the other readings are the AI's, adopted on Ren's delegation"),
]

PENDING = re.compile(r"pending\s+Ren|Ren's\s+to\s+(?:choose|judge|decide|say)|Ren's\s+choice|待 Ren|由 Ren (?:选择|判断|定)")


def flexible(phrase):
    """A pattern matching the phrase with any run of whitespace between its words."""
    return re.compile(r"\s+".join(re.escape(w) for w in phrase.split()))


def replace(text, old, new, exactly_once=True):
    pattern = flexible(old)
    hits = list(pattern.finditer(text))
    if exactly_once and len(hits) != 1:
        raise AssertionError(f"{len(hits)} matches for {old[:80]!r}")
    out, at = [], 0
    for m in hits:
        out.append(text[at:m.start()])
        out.append(rewrap(m.group(0), new))
        at = m.end()
    out.append(text[at:])
    return "".join(out), len(hits)


def rewrap(matched, new):
    """Keep a line break of the matched text after the same word of the new text."""
    gaps = re.findall(r"\s+", matched)
    words = new.split(" ")
    for index, gap in enumerate(gaps):
        if "\n" in gap and index < len(words) - 1:
            return " ".join(words[:index + 1]) + gap + " ".join(words[index + 1:])
    return new


def code_only(text):
    """The text with Lean comments and docstrings removed, strings kept, whitespace folded."""
    out, i, n = [], 0, len(text)
    while i < n:
        if text.startswith("--", i):
            j = text.find("\n", i)
            i = n if j < 0 else j
        elif text.startswith("/-", i):
            depth, i = 1, i + 2
            while i < n and depth:
                if text.startswith("/-", i):
                    depth, i = depth + 1, i + 2
                elif text.startswith("-/", i):
                    depth, i = depth - 1, i + 2
                else:
                    i += 1
            out.append(" ")
        elif text[i] == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == "\\" else 1
            out.append(text[i:j + 1])
            i = j + 1
        else:
            out.append(text[i])
            i += 1
    return " ".join("".join(out).split())


def main():
    root = Path(sys.argv[1])
    dry = "--dry" in sys.argv
    changed, failures = [], []
    jobs = [(LEAN / "Becoming" / f"{name}.lean", MODULES[name], []) for name in sorted(MODULES)]
    jobs.append((LEAN / "Becoming.lean", ROOT, ROOT_GENERIC))
    jobs.append((README, README_SPECIFIC, README_GENERIC))
    for rel, specific, generic in jobs:
        path = root / rel
        before = path.read_text(encoding="utf-8")
        text = before
        try:
            for old, new in specific:
                text, _ = replace(text, old, new)
            for old, new in generic:
                text, _ = replace(text, old, new, exactly_once=False)
        except AssertionError as error:
            failures.append((rel.name, str(error)))
            continue
        if rel.suffix == ".lean":
            assert code_only(text) == code_only(before), ("code outside comments changed", rel)
        left = [m.group(0) for m in PENDING.finditer(text)]
        if left:
            print(f"{rel.name}: still {left}", file=sys.stderr)
        if text != before:
            changed.append(rel.name)
            if not dry:
                path.write_text(text, encoding="utf-8")
    for name, error in failures:
        print(f"no single match in {name}: {error}", file=sys.stderr)
    assert dry or not failures, "replacements failed; nothing should be written"
    print(f"{len(changed)} modules changed: " + " ".join(changed))


if __name__ == "__main__":
    main()
