#!/usr/bin/env python3
"""Apply the N4 text to the record, the study and the chapter (18 October 2026), after re-reading them.

usage (from the repository root): python3 -B .../n2-level-coupling/n4_apply.py RECEIPT_ID
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


# Study: section 168 gains the N4 paragraph after the N3 one.
s = (ROOT / STUDY).read_text()
anchor = ("its admission is then a conjunction, which a law would have to decide. Evidence: 22 theorems and 7 "
          "definitions in `Becoming.LevelCoupling`, empty axiom reports; core receipt `20261018T002939.754460Z`.\n")
s = once(s, anchor, anchor + f'''
**A crossing among several conditions (N4, 18 October).** After Ren's "just keep pushing the frontier - 道法自然" ([source](../../../../sources/15-codex-theory-conversations/2026-10-17-registration-dualist-vocabulary.md#rens-go-to-keep-pushing-18-october-2026)), the same module took up the item N3 left open.
- For a law reading through registration, a response to a condition the formation does not observe changes its admission at the step of that level, which is at or before the step of the exchange (`ExchangeLaw.Through.admission_changes_of_unobserved`). Admission is the conjunction of the formation's needs at the step, so the response happens only where its other requirements there are met: that is not refuted (`ExchangeLaw.Through.others_met_of_unobserved`).
- A response by a crossing needs the condition required at that step with a positive need (`ExchangeLaw.RespondsByCrossing.requires_pos`).
- Where the formation's admission at the step is decided, the law that takes one unit wherever the levels at that step admit it reads through registration. It responds to a crossing of every condition required there with a positive need, across every later step and at every condition (`admissionLaw`, `admissionLaw_through`, `admissionLaw_respondsByCrossing`). So a crossing passes exactly where it is required with a positive need (`crossing_passes_iff`). A listed support decides admission (`admitsDecidableOfSupport`, `crossing_passes_of_support`), and N3's one-condition case reads as a list of one (a reading; N3's theorem is not rederived from it).
- The witness has one input, the decision of admission, so the premise is that decision and not a finite world.

What remains is a crossing where admission is not decided. A law that responds to such a crossing tells the two histories apart, but that is not shown to decide admission. Evidence: 30 theorems and 11 definitions in `Becoming.LevelCoupling`, empty axiom reports; core receipt `{rid}`.
''')
(ROOT / STUDY).write_text(s)

# Chapter: the paragraph's "Not shown" sentence.
c = (ROOT / CHAPTER).read_text()
c = once(c, "Not shown: a crossing where the formation requires other conditions at the same step, and whether a given law responds to what it may read.",
         "Among several conditions at one step, such a response changes the formation's admission there, and happens only where its other requirements are met (`ExchangeLaw.Through.admission_changes_of_unobserved`, `ExchangeLaw.Through.others_met_of_unobserved`). Where that admission is decided, for example by a listed support, a crossing of a condition passes into every later exchange exactly where the formation requires the condition there with a positive need (`crossing_passes_iff`, `crossing_passes_of_support`). Not shown: a crossing where admission is not decided, and whether a given law responds to what it may read.")
(ROOT / CHAPTER).write_text(c)

# Record.
d = json.loads((ROOT / REC).read_text())
assert d['laws'][3]['en'].startswith('By threshold, a crossing passes')
d['laws'].insert(4, {
    'en': "Among several conditions, a crossing passes through the conjunction: a response of a law reading through registration to an unobserved condition changes the formation's admission at that step, only where its other requirements there are met; where admission there is decided, some such law responds to a crossing into every later exchange exactly where the condition is required with a positive need.",
    'zh': "多个条件之间，跨越经合取而过：经所识而读的律对不观察之条件的回应改变形成在该步的容许，且只在它那一步的其他所需已满足之处；该步容许可判定时，恰在该条件被需要且所需为正之处，有这样的律对跨越回应，及于之后每一步的交换。",
    'declarations': ["Becoming.ExchangeLaw.Through.admission_changes_of_unobserved",
                     "Becoming.ExchangeLaw.Through.others_met_of_unobserved",
                     "Becoming.ExchangeLaw.RespondsByCrossing.requires_pos", "Becoming.decide_eq_of_iff",
                     "Becoming.admissionLaw", "Becoming.admissionLaw_through", "Becoming.needLoweredAt",
                     "Becoming.admissionLaw_respondsByCrossing", "Becoming.crossing_passes_iff",
                     "Becoming.metAllDec", "Becoming.admitsDecidableOfSupport",
                     "Becoming.crossing_passes_of_support"]})
d['statement'] = {
    'en': "A response of an exchange to one level is a coupling of every strength array of the law. For a law reading through registration only registered levels couple; by threshold only a crossing passes, through the conjunction of the needs, and observing is exactly where a level can couple within its need.",
    'zh': "交换对一个水平的回应是律的每个强度阵列的耦合。对经所识而读的律，只有所识的水平耦合；经阈只有跨越得过，且经所需之合取，观察恰是水平能在所需之内耦合之处。"}
d['hypotheses'].append({
    'en': "For a crossing among several conditions: the formation's admission at the step decided (a listed support decides it), and equality of conditions and of formations decided, for the witness.",
    'zh': "对多个条件之间的跨越：形成在该步的容许可判定（列出的支撑即可判定），且条件与形成的相等可判定，用于见证。"})
assert d['does_not_show'][0]['en'].startswith('A crossing passing where the formation requires other conditions')
d['does_not_show'][0] = {
    'en': "A crossing passing where the formation's admission at the step is not decided: a law responding to it tells the two histories apart, which is not shown to decide admission.",
    'zh': "形成在该步的容许不可判定时跨越得过：回应它的律分开两段历史，但未表明这判定了容许。", 'kind': 'scope'}
d['next_delta'] = {
    'en': "The renames adopted in the naming study (N1), prepared as a dry run and awaiting Ren; a crossing where admission is not decided; an independent review.",
    'zh': "命名研究（N1）采纳的改名，已作试运行，待 Ren；容许不可判定时的跨越；独立审查。"}
d['aliases'] += ["crossing through the conjunction", "经合取而过", "admission law", "容许之律", "decided admission"]
d['history'].append({
    'en': "18 October 2026: a crossing among several conditions added after Ren's \"just keep pushing the frontier - 道法自然\" (N4): a response to an unobserved condition changes admission, only where the other requirements are met, and where admission is decided a crossing passes exactly where required with a positive need; study section 168.",
    'zh': "2026年10月18日：按 Ren 的“just keep pushing the frontier - 道法自然”加入多个条件之间的跨越（N4）：对不观察之条件的回应改变容许，只在其他所需已满足之处；容许可判定时，跨越恰在所需且为正之处得过；研究第 168 节。"})
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
    'en': f"Machine-checked by the consolidated Lean 4.29.1 checker (receipt {rid}): the 41 declarations of Becoming.LevelCoupling, 30 of them theorems, have empty axiom reports; the checker verifies core purity, and THEOREM-CONNECTIVITY.py --check finds none of them apart from the base. Author self-review in study section 168; not independently reviewed.",
    'zh': f"Lean 4.29.1 合并检查器实查（回执 {rid}）：Becoming.LevelCoupling 的 41 项声明（30 项定理）公理报告为空；检查器并核对核心纯净，THEOREM-CONNECTIVITY.py --check 未见其中任何一项离开基底。作者自审见研究 §168；未经独立审查。"}
d['reviewed_at_utc'] = '2026-10-18T09:00:00+00:00'
(ROOT / REC).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('applied')
