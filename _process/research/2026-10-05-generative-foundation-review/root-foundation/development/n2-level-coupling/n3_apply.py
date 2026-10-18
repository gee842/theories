#!/usr/bin/env python3
"""Apply the N3 text to the record, the study and the chapter (18 October 2026), after re-reading them.

usage (from the repository root): python3 -B .../n2-level-coupling/n3_apply.py RECEIPT_ID
Each edit asserts that its anchor is present exactly once, so a concurrent change stops it instead of overwriting.
"""
import hashlib, json, sys
from pathlib import Path

rid = sys.argv[1]
ROOT = Path(__file__).resolve().parents[6]
B = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
REC = 'theories/becoming/results/records/where-a-level-couples.json'
h = lambda p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def once(text, old, new):
    assert text.count(old) == 1, old[:80]
    return text.replace(old, new)


# Study: section 168 gains the N3 paragraph.
s = (ROOT / STUDY).read_text()
s = once(s, "\n<a id=\"168-where-a-level-couples-into-a-formation-n2\"></a>", "\n<a id=\"168-where-a-level-couples-into-a-formation-n2\"></a>")
anchor = "The first receipt is kept as evidence of the superseded run.\n"
s = once(s, anchor, anchor + f'''
**The positive half of the threshold grain (N3, 18 October).** After Ren's "please continue" ([source](../../../../sources/15-codex-theory-conversations/2026-10-17-registration-dualist-vocabulary.md#rens-go-to-continue-18-october-2026)), the same module gained the half that N2 left unwitnessed.
- A response by a crossing changes the level across the formation's need: met under one history, not under the other (`ExchangeLaw.RespondsByCrossing`).
- For a law reading through registration, a response to a condition the formation does not observe is a crossing: the formation is not refuted to require the condition at that step, and the two levels do not meet its need alike (`ExchangeLaw.Through.crosses_of_unobserved`).
- Where the formation requires at a step exactly that one condition, with a positive need, the law taking one unit across that step only, where the need is met, reads through registration and responds to the crossing at every condition (`thresholdLaw`, `thresholdLaw_through`, `thresholdLaw_respondsByCrossing`, `crossing_passes`).
- A first version needed the support to be the one condition at every step. Making the law act at the crossing step only weakened the hypothesis to that step.
- The first checker run (receipt `20261018T002542.282895Z`, kept) failed on a name clash: the module had its own `beq_self`, which `Becoming.OrderNormal` also declares. The module now uses `Loops.beq_self`, one proof for one law.

So both grains of "couples into" are exact: by level the level passes, by threshold a crossing passes. What remains is a crossing where the formation requires other conditions at the same step: its admission is then a conjunction, which a law would have to decide. Evidence: 22 theorems and 7 definitions in `Becoming.LevelCoupling`, empty axiom reports; core receipt `{rid}`.
''')
(ROOT / STUDY).write_text(s)

# Chapter: the paragraph's "Not shown" sentence.
c = (ROOT / CHAPTER).read_text()
c = once(c, "Not shown: that a crossing of the need passes through some law (a witness would need the whole support decided), and whether a given law responds to what it may read.",
         "A response to a condition not observed is a crossing of its need (`ExchangeLaw.Through.crosses_of_unobserved`), and where the formation requires at a step exactly that condition, with a positive need, some law reading through registration responds to a crossing there (`crossing_passes`): by threshold a crossing passes. Not shown: a crossing where the formation requires other conditions at the same step, and whether a given law responds to what it may read.")
(ROOT / CHAPTER).write_text(c)

# Record.
d = json.loads((ROOT / REC).read_text())
d['laws'].insert(3, {
    'en': "By threshold, a crossing passes: for a law reading through registration, a response to a condition the formation does not observe is a crossing of its need (the requirement not refuted, the two levels not meeting it alike); where the formation requires at a step exactly that condition, with a positive need, a law reading through registration responds to a crossing there, at every condition.",
    'zh': "经阈则跨越得过：对经所识而读的律，对形成不观察之条件的回应是其所需的跨越（所需不被否定，两个水平不同样满足它）；形成在一步恰只需要该条件且所需为正时，有经所识而读的律在那里对跨越回应，于每个条件。",
    'declarations': ["Becoming.ExchangeLaw.RespondsByCrossing", "Becoming.ExchangeLaw.RespondsByCrossing.respondsTo",
                     "Becoming.ExchangeLaw.Through.crosses_of_unobserved", "Becoming.ble_eq_of_iff",
                     "Becoming.Web.admits_iff_of_sole", "Becoming.thresholdLaw",
                     "Becoming.thresholdLaw_through", "Becoming.loweredAt", "Becoming.thresholdLaw_respondsByCrossing",
                     "Becoming.crossing_passes"]})
d['statement'] = {
    'en': "A response of an exchange to one level is a coupling of every strength array of the law. For a law reading through registration only registered levels couple; by threshold a crossing of the need passes and nothing else, and observing is exactly where a level can couple within its need.",
    'zh': "交换对一个水平的回应是律的每个强度阵列的耦合。对经所识而读的律，只有所识的水平耦合；经阈只有所需的跨越得过，观察恰是水平能在所需之内耦合之处。"}
d['does_not_show'][0] = {
    'en': "A crossing passing where the formation requires other conditions at the same step: its admission is then a conjunction a law would have to decide.",
    'zh': "形成在同一步还需要别的条件时跨越得过：其容许是一个合取，律须判定它。", 'kind': 'scope'}
d['next_delta'] = {
    'en': "A crossing where the formation requires several conditions at one step (a decided support); the renames adopted in the naming study (N1), prepared as a dry run and awaiting Ren; an independent review.",
    'zh': "形成在一步需要多个条件时的跨越（支撑可判定）；命名研究（N1）采纳的改名，已作试运行，待 Ren；独立审查。"}
d['aliases'] += ["a crossing passes", "跨越得过", "crossing passes", "threshold law", "阈之律"]
d['history'].append({
    'en': "18 October 2026: the positive half of the threshold grain added after Ren's \"please continue\" (N3): a response to an unobserved condition is a crossing, and where the support at a step is the one condition a crossing passes; study section 168.",
    'zh': "2026年10月18日：按 Ren 的“please continue”加入阈粒度的正面一半（N3）：对不观察之条件的回应是跨越，一步的支撑只是该条件时跨越得过；研究第 168 节。"})
rec = B + 'becoming-checks/' + rid + '/verification.json'
for b in d['proof_bindings']:
    b['receipt'] = rec
refs = []
for r in d['references']:
    if r['role'] == 'receipt':
        continue
    if r['path'] == B + 'Becoming/LevelCoupling.lean':
        r['declarations'] = [x for l in d['laws'] for x in l['declarations']]
    r['sha256'] = h(r['path'])
    refs.append(r)
refs.append({'path': rec, 'role': 'receipt', 'sha256': h(rec)})
d['references'] = refs
d['validation_scope'] = {
    'en': f"Machine-checked by the consolidated Lean 4.29.1 checker (receipt {rid}): the 29 declarations of Becoming.LevelCoupling, 22 of them theorems, have empty axiom reports; the checker verifies core purity, and THEOREM-CONNECTIVITY.py --check finds none of them apart from the base. Author self-review in study section 168; not independently reviewed.",
    'zh': f"Lean 4.29.1 合并检查器实查（回执 {rid}）：Becoming.LevelCoupling 的 29 项声明（22 项定理）公理报告为空；检查器并核对核心纯净，THEOREM-CONNECTIVITY.py --check 未见其中任何一项离开基底。作者自审见研究 §168；未经独立审查。"}
d['reviewed_at_utc'] = '2026-10-18T06:00:00+00:00'
(ROOT / REC).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('applied')
