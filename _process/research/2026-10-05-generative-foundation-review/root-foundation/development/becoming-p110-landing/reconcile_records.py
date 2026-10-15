"""Bring the result records in line with the P110 decisions (DELEGATED-CHOICES).

Usage:
  python3 -B reconcile_records.py ROOT            apply, write the changed records
  python3 -B reconcile_records.py ROOT --dry OUT  write what would still be pending to OUT

Readings and names that the records left to Ren and that DELEGATED-CHOICES decides on
Ren's delegation of 15 October 2026 are rewritten as decided, with the decision's number;
next steps that asked for Ren's judgment on them are closed. What stays Ren's (section 10
of DELEGATED-CHOICES: Ren's own texts and terms, 识 and 理 as Ren's readings, Ren's
testimony on the invariance step, warrant, I4, the representation decisions Ren reserved,
review decisions) is kept. Every changed record gets one paired, dated history note naming
the decisions it applies. Statements, laws' formal content, proofs and bindings are not
touched; reviewed_at_utc is left as it is.

Each specific replacement is asserted to occur exactly once in its record (generic ones
may occur any number of times), so the script fails rather than guess when a record has
changed underneath it; re-read the record and adjust the entry.
"""
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan_pending import PATTERN, walk  # noqa: E402

DC = "DELEGATED-CHOICES"
ZD = "依 Ren 的交托决定"
ED = "decided on Ren's delegation"
ZA = "依 Ren 的交托采用"
EA = "adopted on Ren's delegation"

# Phrases that only mark a reading as the AI's and pending Ren. Every reading they mark is
# one the decisions adopt (the declined ones, D2's activity reading, D9's direct valuation,
# D27's identification with curvature and D31's weakening and link, are rewritten in
# p110_specific); the decision numbers for the history note come from DNUM.
GENERIC = [
    ("（AI 的，待 Ren）", f"（AI 的，{ZA}）"),
    ("(the AI's, pending Ren)", f"(the AI's, {EA})"),
    ("（AI 论证，待 Ren）", f"（AI 论证，{ZA}）"),
    ("(an AI argument, pending Ren)", f"(an AI argument, {EA})"),
    ("（AI，待 Ren）", f"（AI，{ZA}）"),
    ("(AI, pending Ren)", f"(AI, {EA})"),
    ("（读法，AI 的，待 Ren）", f"（读法，AI 的，{ZA}）"),
    ("(a reading, the AI's, pending Ren)", f"(a reading, the AI's, {EA})"),
    ("AI 的，待 Ren；", f"AI 的，{ZA}；"),
    ("the AI's, pending Ren;", f"the AI's, {EA};"),
    ("AI 的读法，待 Ren", f"AI 的读法，{ZA}"),
    ("the AI's reading, pending Ren", f"the AI's reading, {EA}"),
    ("读法由 AI 提出，待 Ren", f"读法由 AI 提出，{ZA}"),
    ("The reading is AI-authored, pending Ren", f"The reading is AI-authored, {EA}"),
    ("读法待 Ren。", f"读法{ZA}。"),
    ("The reading awaits Ren.", f"The reading is {EA}."),
    ("读法是 AI 的，待 Ren。", f"读法是 AI 的，{ZA}。"),
    ("the readings are the AI's, pending Ren.", f"the readings are the AI's, {EA}."),
    ("这一形式化是 AI 的，待 Ren", f"这一形式化是 AI 的，{ZA}"),
    ("this formalization is the AI's, pending Ren", f"this formalization is the AI's, {EA}"),
    ("这一读法仍属 AI，待 Ren", f"这一读法是 AI 的，{ZA}"),
    ("this reading remains the AI's, pending Ren", f"this reading is the AI's, {EA}"),
    ("the other readings are the AI's, pending Ren", f"the other readings are the AI's, {EA}"),
    # Ren confirmed refinement counted as the case of 0 (11 October 2026).
    ("（AI，待 Ren 确认）", "（Ren 已确认）"),
    ("(AI, pending Ren's confirmation)", "(Ren confirmed it)"),
]

# The sentence repeated in the records counting arising and ceasing (D2).
T1_ZH_OLD = ("是否为 Ren 提议中的“生成的”“退化的”由 Ren 选择（Ren 写道“generative和degenerate虽然都在"
             "一个becoming model上，但是他们不overlap吧”，以“吧”预设二者不重叠；若取不重叠，这一读法就"
             "不是其所指，这是 AI 的推论）")
T1_ZH_NEW = ("不是 Ren 提议中的“生成的”“退化的”（Ren 写道“generative和degenerate虽然都在一个becoming "
             "model上，但是他们不overlap吧”，以“吧”预设二者不重叠，所以这一读法不是其所指；二者读作"
             f"对能形成者的扩大与缩小，{DC} D2）")
T1_EN_OLD = ("is the proposal's generative and degenerative is Ren's to choose (Ren wrote ‘generative和"
             "degenerate虽然都在一个becoming model上，但是他们不overlap吧’, a tag question presuming that "
             "they do not overlap; if non-overlap is taken, this reading is not what is meant, the AI's "
             "inference)")
T1_EN_NEW = ("is not the proposal's generative and degenerative (Ren wrote ‘generative和degenerate虽然都在"
             "一个becoming model上，但是他们不overlap吧’, a tag question presuming that they do not overlap, "
             "so this reading is not what is meant; they read as widening and narrowing what can form, "
             f"{DC} D2)")
TEMPLATES = [
    ("它" + T1_ZH_OLD, "它" + T1_ZH_NEW),
    ("这一读法" + T1_ZH_OLD, "这一读法" + T1_ZH_NEW),
    ("whether it " + T1_EN_OLD, "it " + T1_EN_NEW),
    ("whether this reading " + T1_EN_OLD, "this reading " + T1_EN_NEW),
]

from p110_specific import SPECIFIC, DNUM, EXTRA_NOTE, RELATE, RELATE_NOTE, CONTEXTUAL_NOTE  # noqa: E402


def records(root):
    for name in sorted(glob.glob(os.path.join(root, "theories/becoming/results/records/*.json"))):
        yield name, json.load(open(name, encoding="utf-8"))


def fields(record):
    """The (container, key) pairs of every scanned string field."""
    out = []

    def visit(value, top):
        if isinstance(value, dict):
            for key, item in value.items():
                if top and key in SKIP_TOP:
                    continue
                if key in ("path", "anchor", "role"):
                    continue
                if isinstance(item, str):
                    out.append((value, key))
                else:
                    visit(item, False)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                if isinstance(item, str):
                    out.append((value, index))
                else:
                    visit(item, False)

    visit(record, True)
    return out


SKIP_TOP = {"history", "text_versions", "proof_bindings", "canonical_source", "aliases",
            "dependencies", "id", "reviewed_at_utc", "schema_version", "status", "kind",
            "family", "standard_boundaries"}


FAILURES = []

# Readings posed after Ren's reply of 15 October 2026 on the identification line ("reality is
# always situational") and left for Ren by their owner; not within the delegation's list.
EXCLUDE = {"identification-where-runs-part", "typicality-by-counting"}


def apply(record):
    """Apply the replacements to one record in place; return the decisions used."""
    rid = record["id"]
    used = set()
    slots = fields(record)
    for old, new in GENERIC + TEMPLATES:
        for container, key in slots:
            if old in container[key]:
                container[key] = container[key].replace(old, new)
                used.add("generic")
    for old, new in SPECIFIC.get(rid, []):
        hits = [(c, k) for c, k in slots if old in c[k]]
        count = sum(c[k].count(old) for c, k in hits)
        if count != 1:
            FAILURES.append((rid, old[:90], count))
            continue
        container, key = hits[0]
        container[key] = container[key].replace(old, new)
        used.add("specific")
    return used


# Study sections, provisional until landing (the integrator renumbers).
SECTION = {"P110": int(os.environ.get("P110_SECTION", 142)),
           "P111": int(os.environ.get("P111_SECTION", 143)),
           "P112": int(os.environ.get("P112_SECTION", 144))}
MARK = "P110（依 Ren 2026-10-15 的交托"


def note(record, decisions):
    extra_zh, extra_en = EXTRA_NOTE.get(record["id"], ("", ""))
    zh = (f"2026-10-15 {MARK}决定的读法，研究 §{SECTION['P110']}，{DC} {decisions}）："
          "此前留给 Ren 的读法与名称按所列决定改为采用或不采用，要求 Ren 判断这些读法的下一步已删去。"
          f"{extra_zh}陈述、证明与绑定不变；Ren 可改其中任何一项决定。")
    en = (f"15 October 2026, P110 (readings decided on Ren's delegation of 15 October 2026, study "
          f"section {SECTION['P110']}, {DC} {decisions}): readings and names formerly left to Ren are "
          "adopted or declined as those decisions say, and next steps asking for Ren's judgment on "
          f"them are removed.{' ' + extra_en if extra_en else ''} Statements, proofs and bindings "
          "unchanged; Ren can reverse any of the decisions.")
    record.setdefault("history", []).append({"zh": zh, "en": en})


def relate(record):
    """The paired related link for P111 or P112, with its dated note; False where none applies."""
    if record["id"] not in RELATE:
        return False
    target, zh, en = RELATE[record["id"]]
    assert all(x["id"] != target for x in record["related"]), (record["id"], target)
    record["related"].append({"id": target, "detail": {"zh": zh, "en": en}})
    item = "P111" if target == "where-novelty-gain-comes-from" else "P112"
    title_zh, title_en, body_zh, body_en = RELATE_NOTE[target]
    if record["id"] == "contextual-registration":
        body_zh, body_en = CONTEXTUAL_NOTE[0] + body_zh, CONTEXTUAL_NOTE[1] + " " + body_en
    record["history"].append({
        "zh": f"2026-10-15 {item}（{title_zh}，研究 §{SECTION[item]}）：{body_zh}",
        "en": f"15 October 2026, {item} ({title_en}, study section {SECTION[item]}): {body_en}"})
    return True


def residual(record):
    out = []
    for path, text in walk(record, []):
        if PATTERN.search(text):
            out.append((".".join(path), text))
    return out


def main():
    root = sys.argv[1]
    dry = "--dry" in sys.argv
    report = open(sys.argv[sys.argv.index("--dry") + 1], "w", encoding="utf-8") if dry else None
    changed = []
    for name, record in records(root):
        if record["id"] in EXCLUDE:
            continue
        if any(MARK in h.get("zh", "") for h in record.get("history", [])):
            print("already reconciled:", record["id"], file=sys.stderr)
            continue
        before = json.dumps(record, ensure_ascii=False, indent=2) + "\n"
        apply(record)
        if report is not None:
            for path, text in residual(record):
                report.write(f"### {record['id']} | {path} | v{record.get('schema_version')}\n{text}\n\n")
        after = json.dumps(record, ensure_ascii=False, indent=2) + "\n"
        if after == before and record["id"] not in RELATE:
            continue
        decisions = DNUM.get(record["id"])
        changed.append(record["id"])
        if after != before:
            assert decisions, ("no decision numbers for", record["id"])
            note(record, decisions)
        relate(record)
        if not dry:
            open(name, "w", encoding="utf-8").write(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    for failure in FAILURES:
        print("no single match:", failure, file=sys.stderr)
    assert dry or not FAILURES, "specific replacements failed; nothing should be written"
    print(" ".join(changed))
    print(f"{len(changed)} records changed", file=sys.stderr)


if __name__ == "__main__":
    main()
