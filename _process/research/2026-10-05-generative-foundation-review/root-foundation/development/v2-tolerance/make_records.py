#!/usr/bin/env python3
"""Write V2's two records: python3 -B make_records.py CORE_RECEIPT   (from the checkout root, after apply_text.py)

Every declaration cited is resolved against the receipt's audited declarations of its module (a short name must
match exactly one declaration by suffix), and the receipt must bind each module's current bytes."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-19-collective-continuation.md'
RECORDS = ROOT / 'theories/becoming/results/records'
MOD = 'Tolerance'
core_id = sys.argv[1]
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
assert re.search(r'^## 194\. Thresholds of waiting and the laws that restore giving \(V2\)$', (ROOT / STUDY).read_text(), re.M)


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def src(mod):
    return f'{PKG}/Becoming/{mod}.lean'


def decls(mod):
    m = next(m for m in core['modules'] if m['module'] == f'Becoming.{mod}')
    assert core['source_sha256'][f'Becoming.{mod}'] == sha(src(mod)), ('receipt does not bind', mod)
    return m


def resolve(mod, names):
    full = [d['name'] for d in decls(mod)['declarations']]
    out = []
    for n in names:
        hits = [f for f in full if f == 'Becoming.' + n or f.endswith('.' + n)]
        assert len(hits) == 1, (mod, n, hits)
        out.append(hits[0])
    return out


def counts(mod):
    m = decls(mod)
    assert not any(m['axiom_dependencies'].values()), mod
    return len(m['declarations']), sum(1 for d in m['declarations'] if d.get('kind') == 'theorem')


BOUNDS = ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical', 'names-provisional',
          'omission-not-refutation']


def dep(rid, relation, en, zh, out_en, out_zh, in_en, in_zh, cond_en, cond_zh, evidence):
    return {'id': rid, 'relation': relation, 'detail': {'en': en, 'zh': zh},
            'interface': {'output': {'en': out_en, 'zh': out_zh}, 'input': {'en': in_en, 'zh': in_zh},
                          'conditions': {'en': cond_en, 'zh': cond_zh}, 'evidence': evidence}}


def record(rid, title, statement, laws, hypotheses, dns, counterexamples, nxt, corr, aliases, deps, related,
           extra_refs):
    n_decl, n_thm = counts(MOD)
    aliases = [resolve(MOD, [a[len('Becoming.'):]])[0] if a.startswith('Becoming.') else a for a in aliases]
    cited = {src(MOD)} | {p for p, _ in extra_refs}
    extra_refs = list(extra_refs) + [(d['interface']['evidence'], None) for d in deps
                                     if d['interface']['evidence'] not in cited]
    assert len(statement['en']) <= 300, (rid, len(statement['en']))
    r = {
        'schema_version': 2, 'id': rid, 'title': title, 'kind': 'theorem', 'status': 'recorded-checked',
        'family': 'F01', 'reviewed_at_utc': NOW, 'statement': statement,
        'laws': [{'en': en, 'zh': zh, 'declarations': resolve(MOD, names)} for en, zh, names in laws],
        'hypotheses': hypotheses, 'does_not_show': dns, 'counterexamples': counterexamples,
        'standard_boundaries': BOUNDS,
        'validation_scope': {
            'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {n_decl} declarations '
                  f'of Becoming.{MOD}, {n_thm} of them theorems, have empty axiom reports; the checker verifies core purity. '
                  'Built and reviewed in one session, with no separate reviewer; author review in study section 194; not '
                  'independently reviewed by a person.',
            'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.{MOD} 的 {n_decl} 项声明（{n_thm} 项定理）公理报告为空；'
                  '检查器并核对核心纯净。在一个会话中构建并审查，没有另设审查者；作者审查见研究第 194 节；未经人的独立审查。'},
        'next_delta': nxt, 'correspondence': corr, 'canonical_source': src(MOD), 'aliases': aliases,
        'dependencies': deps, 'related': related,
        'references': [{'path': src(MOD), 'role': 'proof', 'declarations': sorted(d['name'] for d in decls(MOD)['declarations']),
                        'sha256': sha(src(MOD))}]
        + [dict({'path': p, 'role': 'proof'}, **({'declarations': ds} if ds else {}), sha256=sha(p)) for p, ds in extra_refs]
        + [{'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
           {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
           {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
           {'path': SOURCE, 'role': 'provenance', 'sha256': sha(SOURCE)}],
        'proof_bindings': [{'source': src(MOD), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{MOD}',
                            'success_pointer': '/status', 'success_value': 'passed'}],
        'history': [{
            'en': '19 October 2026: added (V2), taking two items of the open remainder that V (study section 193) named in '
                  'chapter section 8.2, "Collective continuation": thresholds of waiting with the laws that restore giving '
                  'in a general family, and fault tolerance joined to Becoming.FaultEnvelopes; study section 194.',
            'zh': '2026年10月19日：新增（V2），承接 V（研究第 193 节）在第 8.2 节“集体延续”中列出的开放余项中的两项：等待的阈值与一般族中'
                  '恢复给出的律，以及与 Becoming.FaultEnvelopes 相接的容错；研究第 194 节。'}],
    }
    path = RECORDS / f'{rid}.json'
    assert not path.exists(), ('record exists', rid)
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('written', rid)


CORR_EN = ('An account of social viability Ren brought on 19 October 2026 lists eight constraints and a unifying ninth; '
           'V carried the fourth, cooperation among strangers, by Becoming.Withholding and left {gap} open. Ren\'s words '
           'are provenance, not warrant; the reading onto collectives is the AI\'s (D48).')
CORR_ZH = ('Ren 于 2026年10月19日带来的一段社会可存续性文字列出八条约束与统一它们的第九条；V 以 Becoming.Withholding 承载第四条'
           '（陌生人之间的合作），留下{gap}待解。Ren 的话是出处，不是依据；读到集体上是 AI 的（D48）。')
REC_DEP = dep('recurrence-without-premise', 'formal-reuse',
              'Reuses Law.orbit and the run of a determined law, Law.run, whose states are the orbit.',
              '复用 Law.orbit 与决定性律的运行 Law.run，其状态即轨道。',
              'The course of a determined law as a run of the spine.', '决定性律的进程作为脊柱的运行。',
              'The courses the laws are stated on.', '诸定律所陈述的进程。', 'None.', '无。', src('Recurrence'))
WITH_DEP = dep('giving-that-waits-on-giving', 'formal-reuse',
               'Reuses the laws waitsAll, answers and givesFirst, chains of waits and their closed form answers_closed, '
               'and the ring of three.',
               '复用 waitsAll、answers 与 givesFirst 三条律、等待链及其闭式 answers_closed，以及三元环。',
               'The laws of giving that waits on giving, their chains and the ring.', '等待给出的给出之律、其链与环。',
               'The family whose restoring is characterized; the ring restated as an instance.',
               '其恢复被刻画的族；环被重述为实例。', 'None.', '无。', src('Withholding'))

# The worst start.
record(
    'restoring-giving-from-the-worst-start',
    {'en': 'Restoring giving from the worst start', 'zh': '从最坏的开始恢复给出'},
    {'en': 'For every law of giving that keeps inclusion, giving at step n from every start is giving at n from total '
           'withholding, from which giving only grows. Where a formation gives first, restoring by n is exactly no chain '
           'of n waits clear of sources.',
     'zh': '对每条保持包含的给出之律，从每个开始在第 n 步给出即从全部扣留开始在第 n 步给出，而从全部扣留出发给出只增不减。一个形成先给出时，恢复到第 n 步恰当没有 n 次避开来源的等待链。'},
    [('A law keeping inclusion keeps it along its courses; the four laws waitsAll, answers, givesFirst and the '
      'tolerating law keep inclusion.',
      '保持包含的律沿其进程保持包含；waitsAll、answers、givesFirst 与容忍律四条律保持包含。',
      ['KeepsInclusion', 'KeepsInclusion.course', 'waitsAll_keeps', 'answers_keeps', 'givesFirst_keeps',
       'tolerating_keeps']),
     ('The worst start is total withholding: a formation gives at step n from every start exactly where it gives at n '
      'from the start at which nothing gives; from that start giving only grows, so restoring by n is restoring at every '
      'later step; where no formation gives at the step after total withholding, none gives at any step.',
      '最坏的开始是全部扣留：一个形成从每个开始在第 n 步给出，恰当它从无一给出的开始在第 n 步给出；从该开始给出只增不减，故恢复到第 n 步即此后每一步都恢复；全部扣留后的下一步无一给出时，任何一步都无一给出。',
      ['allWithheld', 'worst_start', 'rises_from_withheld', 'rises_le', 'restored_stays', 'withheld_kept']),
     ('Under givesFirst, a clear chain of n waits into a formation (none of its formations after the first a source) '
      'makes it withhold at n from total withholding; with the sources decided, it gives at n from every start exactly '
      'where no clear chain of n waits leads into it, and where no clear chain is L long every formation gives from L '
      'on; a clear loop is never restored.',
      '在 givesFirst 下，通入一个形成的 n 次避开来源的等待链（首个之后无一是来源）使它从全部扣留开始在第 n 步扣留；来源可判定时，它从每个开始在第 n 步给出，恰当没有 n 次避开来源的链通入它；没有 L 长的避开来源的链时，每个形成从第 L 步起给出；避开来源的回路永不恢复。',
      ['Clear', 'Clear.last', 'Clear.chain', 'Clear.iterate', 'clear_withholds', 'gives_of_no_clear', 'restores_iff',
       'restores_from', 'clear_loop_withholds']),
     ('Without memory, a formation gives at n from every start exactly where no chain of n waits leads into it, so '
      'giving first never restores later than waiting on all; with memory no step restores giving.',
      '无记忆时，一个形成从每个开始在第 n 步给出，恰当没有 n 次等待链通入它，故先给出从不比等待全部更晚恢复；有记忆时没有一步恢复给出。',
      ['answers_restores_iff', 'givesFirst_restores_of_answers', 'waitsAll_never_restores']),
     ('The ring of Becoming.Withholding has no clear chain of three waits, so its restoring from step 3 is an instance.',
      'Becoming.Withholding 的环没有三次避开来源的等待链，故其从第 3 步起的恢复是一个实例。',
      ['Ring.no_clear_three', 'Ring.isFirst_decided', 'Ring.restores_from_three'])],
    [{'en': 'No axiom and no premise about the formations or the relation of waiting: no finiteness and no decision of '
            'giving. The converse of restores_iff, and restores_from, take the decision of which formations are sources '
            '(∀ a, src a ∨ ¬ src a) as a hypothesis. Every main law is stated on runs Law.run.',
      'zh': '不加公理，对形成与等待关系不加前提：不要求有限，不要求给出可判定。restores_iff 的逆向与 restores_from 以“哪些形成是来源可判定”'
            '（∀ a, src a ∨ ¬ src a）为假设。每条主要定律都陈述在运行 Law.run 上。'}],
    [{'en': 'How a law that gives first forms, or which formations come to be sources.',
      'zh': '先给出的律如何形成，或哪些形成成为来源。', 'kind': 'scope'},
     {'en': 'That restoring giving is good, or that a source should give.', 'zh': '恢复给出是好的，或来源应当给出。',
      'kind': 'non-implication'}],
    [],
    {'en': 'How a restoring law forms from the relations; the worst start for laws that do not keep inclusion; an '
           'independent review.', 'zh': '恢复之律如何从关系中形成；不保持包含的律的最坏开始；独立审查。'},
    {'en': CORR_EN.format(gap='which laws restore giving in a general family'),
     'zh': CORR_ZH.format(gap='一般族中哪些律恢复给出')},
    ['restoring giving from the worst start', '从最坏的开始恢复给出', 'Becoming.worst_start', 'Becoming.restores_iff',
     'institutions that act whatever was last received (reading)'],
    [REC_DEP, WITH_DEP],
    [{'id': 'target-capture', 'detail': {
        'en': 'As a perturbed state is re-absorbed under one rule, giving is regained only under another law; here exactly '
              'where every chain of waits passes a source.',
        'zh': '如同受扰状态在一条规则下被重新吸收，给出只在另一条律下恢复；这里恰在每条等待链都经过来源处。'}}],
    [])

# Thresholds.
record(
    'thresholds-of-waiting',
    {'en': 'Thresholds of waiting', 'zh': '等待的阈值'},
    {'en': 'Where a formation gives as all but its tolerance of what it waits on gave, a set relying on at most its '
           'tolerance outside it keeps giving and a thin withholding passes out in one step; restoring needs a formation '
           'sparing all it waits on.',
     'zh': '一个形成在所等待者中除其容忍数之外都给出时给出，则在集合外至多依赖其容忍数的集合保持给出，稀疏的扣留一步消散；恢复需要一个容忍其全部等待者的形成。'},
    [('All but f members of a list hold s: with f = 0 every member, with f at least the length always; it grows with s '
      'and f, finds a member that holds or a list at most f long, and holds of nothing exactly where the list is at most '
      'f long.',
      '列表中除至多 f 个外都满足 s：f = 0 时为每个成员，f 不小于长度时总成立；它随 s 与 f 增大，找到一个满足者或列表长至多 f，对“无一”成立恰当列表长至多 f。',
      ['AllBut', 'AllBut.mono_set', 'AllBut.mono_count', 'AllBut.of_length', 'AllBut.of_length_le', 'AllBut.zero_all',
       'AllBut.zero_iff', 'AllBut.found', 'AllBut.withheld_iff']),
     ('The tolerating law: a formation gives where all but its tolerance of what it waits on gave; with every tolerance '
      '0 its course is that of answers on the listed waits.',
      '容忍律：一个形成在所等待者中除其容忍数之外都给出时给出；容忍数全为 0 时其进程即所列等待上 answers 的进程。',
      ['tolerating', 'Listed', 'tolerating_zero']),
     ('Restoring needs a formation sparing all it waits on: from total withholding a giving formation finds one; such a '
      'formation gives at every step after the start; without one, total withholding stays.',
      '恢复需要一个容忍其全部等待者的形成：从全部扣留出发，一个给出的形成找到这样一个；这样的形成在开始之后每一步给出；没有这样的形成时全部扣留保持。',
      ['gives_needs_sparing', 'sparing_gives', 'total_stays']),
     ('A set giving at the start, each member waiting on at most its tolerance outside it, gives at every step whatever '
      'the rest does; where the start gives outside W and every formation waits on at most its tolerance inside W, every '
      'formation gives from step 1 on.',
      '开始时给出、每个成员在集合外至多等待其容忍数的集合，不论其余如何每一步都给出；开始在 W 之外给出且每个形成在 W 内至多等待其容忍数时，每个形成从第 1 步起给出。',
      ['kept_set', 'thin_absorbed']),
     ('The certificate of Becoming.FaultEnvelopes read as a law of giving keeps a covered set giving under separated '
      'envelopes, is available at step 1 exactly where the envelope is separated, and without separation a withholding '
      'within an admitted fault set stops a domain.',
      'Becoming.FaultEnvelopes 的证书读作给出之律：在分隔的包络下保持被覆盖的集合给出；恰在包络分隔处第 1 步可用；不分隔时，落在一个被容许故障集之内的扣留使一个域停止。',
      ['certified', 'certified_kept', 'certified_available_iff', 'certified_blocked']),
     ('In three formations each waiting on the other two, one withholding spreads to all from step 2 with tolerance 0 '
      '(at step 1 first still gives), passes out at step 1 with tolerance 1, and with tolerance 1 total withholding is '
      'kept at every step.',
      '在三个各等待另外两个的形成中，一处扣留在容忍 0 时从第 2 步起扩散到全部（第 1 步 first 仍给出），在容忍 1 时于第 1 步消散，而容忍 1 下全部扣留在每一步保持。',
      ['Triad.spreads', 'Triad.absorbed', 'Triad.total_kept', 'Triad.total_at_two'])],
    [{'en': 'No axiom and no premise about the formations: what each waits on is a given list, so a formation waiting twice '
            'on one counts it twice; tolerances are given numbers. The certificate law takes rosters and envelopes as given, '
            'as Becoming.FaultEnvelopes does. Every main law is stated on runs Law.run.',
      'zh': '不加公理，对形成不加前提：每个形成所等待者是给定的列表，故两次等待同一者计两次；容忍数是给定的数。证书律如 Becoming.FaultEnvelopes 一样以名册与包络为给定。每条主要定律都陈述在运行 Law.run 上。'}],
    [{'en': 'Amounts of giving; thresholds with memory; how tolerances form.',
      'zh': '给出的数量；有记忆的阈值；容忍数如何形成。', 'kind': 'scope'},
     {'en': 'That tolerance is good, or how much a collective should tolerate.', 'zh': '容忍是好的，或一个集体应容忍多少。',
      'kind': 'non-implication'}],
    [],
    {'en': 'Amounts of giving and thresholds with memory; the tolerating law as an instance of an envelope law; an '
           'independent review.', 'zh': '给出的数量与有记忆的阈值；容忍律作为包络律的实例；独立审查。'},
    {'en': CORR_EN.format(gap='amounts of giving, thresholds of waiting and fault tolerance as an instance'),
     'zh': CORR_ZH.format(gap='给出的数量、等待的阈值与作为实例的容错')},
    ['thresholds of waiting', '等待的阈值', 'tolerance', 'Becoming.kept_set', 'Becoming.thin_absorbed',
     'fault tolerance in giving (reading)'],
    [REC_DEP, WITH_DEP],
    [{'id': 'restoring-giving-from-the-worst-start', 'detail': {
        'en': 'The tolerating law keeps inclusion, so its restoring is read off the course from total withholding.',
        'zh': '容忍律保持包含，故其恢复由全部扣留出发的进程读出。'}}],
    [(src('FaultEnvelopes'), ['Becoming.FaultEnvelopes.certificate_available',
                              'Becoming.FaultEnvelopes.availability_iff_separated',
                              'Becoming.FaultEnvelopes.correlated_three_blocks'])])
print('done')
