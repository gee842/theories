#!/usr/bin/env python3
"""Restate which-links-a-closure-needs for K2 and re-point growth-constrained-fragmentation's Cuts.lean reference:
python3 -B make_record.py CORE_RECEIPT   (from the repository root)

The receipt is checked against the current bytes of Cuts.lean and Feedback.lean, and every declaration cited
against those Lean elaborated, before anything is written. Run after study section 191 is in place."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/Cuts.lean'
FEEDBACK = f'{PKG}/Becoming/Feedback.lean'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RECORDS = ROOT / 'theories/becoming/results/records'
core_id = sys.argv[1]
core_receipt = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


core = json.loads((ROOT / core_receipt).read_text())
assert core['status'] == 'passed'
assert core['source_sha256']['Becoming.Cuts'] == sha(SRC), 'core receipt does not bind Cuts.lean'
assert core['source_sha256']['Becoming.Feedback'] == sha(FEEDBACK)
mod = next(m for m in core['modules'] if m['module'] == 'Becoming.Cuts')
cut_decls = {d['name'] for d in mod['declarations']}
assert not any(mod['axiom_dependencies'].values())
n_decl = len(mod['declarations'])
n_thm = sum(1 for d in mod['declarations'] if d.get('kind') == 'theorem')
assert (n_decl, n_thm) == (60, 51), (n_decl, n_thm)
assert re.search(r'^## 191\. Growth by attachment on the base \(K2\)$', (ROOT / STUDY).read_text(), re.M)


def c(*names):
    out = ['Becoming.' + n for n in names]
    missing = [n for n in out if n not in cut_decls]
    assert not missing, missing
    return out


path = RECORDS / 'which-links-a-closure-needs.json'
r = json.loads(path.read_text())
r['reviewed_at_utc'] = NOW
r['statement'] = {
    'en': 'A cut leaves every closure as it was exactly where each removed link is bypassed, and a join adds exactly what passes through it. In a world grown by attachment every condition is needed; one added condition frees exactly the grown ones it crosses.',
    'zh': '切断使每个闭包保持原样，恰当每条被去掉的联系被绕过；连上一条联系，恰好添上经它通过的。在依附式生长的世界中，每个条件都被需要；多一个条件，恰使它跨过的生长出的条件不再被需要。'}
assert len(r['statement']['en']) <= 300
laws = r['laws']
assert laws[3]['declarations'][-1] == 'Becoming.Cuts.attached_link_separates'
laws[3]['declarations'] += c('Cuts.Attaches.distinct', 'Cuts.links_mem', 'Cuts.links_of_link', 'Cuts.mem_split',
                             'Cuts.mem_widen', 'Cuts.mem_set_apart', 'Cuts.mem_append_cases',
                             'Cuts.mem_append_right', 'Cuts.exists_split', 'Cuts.append_cons_assoc')
assert len(laws) == 7
laws.append({
    'en': 'In a world grown by attachment, each new formation taking part only in a condition exactly one earlier formation takes part in, the systems are the closures of the grown links; each grown condition is attached at one place and is needed, its two takers lying in one system and apart without it; the latest formation is alone without its condition; and what grew up to any stage is grown by attachment beside the later conditions.',
    'zh': '在依附式生长的世界中（每个新形成只参与恰有一个先前形成也参与的条件），系统就是生长出的联系的闭包；每个生长出的条件只在一处接上，并且被需要：它的两个参与者处于同一系统，没有它就分开；最后接上的形成没有它的条件就是孤立的；生长到任何阶段为止的部分，在其后接上的条件之旁，也是依附式生长的。',
    'declarations': c('Flow.SharesOutside', 'Flow.GrownBy', 'Flow.GrownBy.takes_part_of_link',
                      'Flow.GrownBy.link_of_takers', 'Flow.GrownBy.cond_ne', 'Flow.GrownBy.attached_only',
                      'Flow.GrownBy.outside_step', 'Flow.GrownBy.outside_of_link', 'Flow.GrownBy.within_outside_iff',
                      'Flow.GrownBy.within_outside_added_iff', 'Flow.GrownBy.condition_needed',
                      'Flow.GrownBy.every_condition_needed', 'Flow.GrownBy.latest_alone', 'Flow.GrownBy.suffix')})
laws.append({
    'en': 'With one more condition exactly a and b take part in, the takers p and n of the condition that attached n lie in one system through the other conditions, and every system is what it is without it, exactly where p reaches one of a, b and the other reaches n through the conditions other than these two.',
    'zh': '再多一个恰有 a 与 b 参与的条件后，接上 n 的那个条件的参与者 p 与 n 经其余条件处于同一系统、且每个系统没有它仍是原样，恰当经这两个条件以外的条件，p 到达 a、b 之一而另一个到达 n。',
    'declarations': c('Flow.within_of_two_takers', 'Flow.GrownBy.beside_iff', 'Flow.GrownBy.system_iff',
                      'Flow.GrownBy.bypass_iff', 'Flow.GrownBy.cut_unchanged_iff')})
r['hypotheses'] = [{
    'en': 'No axiom and no premise beyond the relation in the general laws. On the base, splitting sharing a condition into sharing c and sharing another needs equality of conditions decided, given as DecidableEq C; withinSystem_two_takers_iff and the join law take the list of a condition\'s takers as a hypothesis; growth by attachment is the hypothesis Flow.GrownBy on a list of entries.',
    'zh': '一般规律除关系本身外不加公理、不加前提。在基上，把共享条件分成共享 c 与共享其他条件，需要条件相等可判定，以 DecidableEq C 给出；withinSystem_two_takers_iff 与连接规律以一个条件的参与者为假设；依附式生长是对一列条目的假设 Flow.GrownBy。'}]
dns = r['does_not_show']
assert dns[1]['en'].startswith('Growth by attachment read on the base')
dns[1] = {
    'en': 'Whether a world grew by attachment, or in which order: Flow.GrownBy takes the list as a hypothesis; nor several added conditions at once, or added conditions with more than two takers.',
    'zh': '一个世界是否依附式生长、以何种次序：Flow.GrownBy 以这列条目为假设；也不涉及同时多加几个条件，或多于两个参与者的新增条件。',
    'kind': 'scope'}
r['validation_scope'] = {
    'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations of Becoming.Cuts, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. The growth-constrained-fragmentation record holds the periphery instances. Author self-review in study sections 190 and 191; not independently reviewed.',
    'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.Cuts 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；检查器并核对核心纯净。外围实例见 growth-constrained-fragmentation。作者自审见研究第 190、191 节；未经独立审查。'}
r['next_delta'] = {
    'en': 'Several joins at once and the cycle law; added conditions with more than two takers; the count of links or conditions a whole needs; how links form and are cut along a run; an independent review.',
    'zh': '同时多处连接与回路规律；多于两个参与者的新增条件；一个整体所需的联系或条件数；联系如何沿一次运行形成与被切断；独立审查。'}
for alias in ['every condition of a world grown by attachment is needed', '依附式生长的世界的每个条件都被需要',
              'Becoming.Flow.GrownBy.condition_needed', 'Becoming.Flow.GrownBy.cut_unchanged_iff']:
    if alias not in r['aliases']:
        r['aliases'].append(alias)
for ref in r['references']:
    if ref['path'] == SRC:
        ref['declarations'] = sorted(cut_decls)
        ref['sha256'] = sha(SRC)
    elif ref['role'] == 'receipt' and 'becoming-checks' in ref['path']:
        ref['path'] = core_receipt
        ref['sha256'] = sha(core_receipt)
    elif ref['path'] in (FEEDBACK, STUDY, CHAPTER):
        ref['sha256'] = sha(ref['path'])
for b in r['proof_bindings']:
    if b['source'] in (SRC, FEEDBACK):
        b['receipt'] = core_receipt
r['history'].append({
    'en': '19 October 2026, K2: growth by attachment read on the base (Flow.GrownBy): every grown condition is needed, and one added condition frees exactly the grown ones it crosses; laws 8 and 9 added, law 4 gains its list lemmas; study section 191. The earlier laws are unchanged.',
    'zh': '2026年10月19日，K2：依附式生长在基上的读法（Flow.GrownBy）：每个生长出的条件都被需要，多一个条件恰使它跨过的生长出的条件不再被需要；新增规律 8、9，规律 4 添上其列表引理；研究第 191 节。原有规律不变。'})
path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')

path = RECORDS / 'growth-constrained-fragmentation.json'
g = json.loads(path.read_text())
for ref in g['references']:
    if ref['path'] == SRC:
        ref['sha256'] = sha(SRC)
if not any(ref['path'] == core_receipt for ref in g['references']):
    at = next(i for i, ref in enumerate(g['references']) if ref['path'] == SRC) + 1
    g['references'].insert(at, {'path': core_receipt, 'role': 'receipt', 'sha256': sha(core_receipt), 'declarations': []})
for b in g['proof_bindings']:
    if b['source'] == SRC:
        b['receipt'] = core_receipt
g['history'].append({
    'en': f'19 October 2026, K2: Cuts.lean gained the laws of growth by attachment on the base (study section 191); the two Cuts declarations this record cites are unchanged, and its binding moves to core receipt {core_id}. The claim is unchanged.',
    'zh': f'2026年10月19日，K2：Cuts.lean 新增依附式生长在基上的规律（研究第 191 节）；本记录所引的两项 Cuts 声明不变，其绑定移到核心回执 {core_id}。论断不变。'})
path.write_text(json.dumps(g, ensure_ascii=False, indent=2) + '\n')
print('written')
