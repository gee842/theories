#!/usr/bin/env python3
"""R25 (20 October 2026), the twentieth review's step 1, docs now: re-point the result records after reading the
change. Usage (from the checkout root): python3 -B repoint_drift.py BASE [RENDER_LOG]

BASE is the main commit R25 was rebased on. For every record, a reference to a file R25 changed whose hash
matched the file at BASE follows the file; with a `make research-render` log, a record reported as drifting in
a file R25 changed is re-pointed too (its reference was already behind BASE in sections R25 did not change, or
cites a section R25 rewrote, which was read). No Lean changed, so no proof binding moves. A history note says
what changed; the three records whose text R25 corrected say so. Modelled on R21's repoint_drift.py."""
import glob, hashlib, json, subprocess, sys

BASE = sys.argv[1]
DRIFT = {}
if len(sys.argv) > 2:
    _log = open(sys.argv[2]).read()
    _dec = json.JSONDecoder()
    for _k in range(len(_log)):
        if _log[_k] == '{':
            try:
                _o, _ = _dec.raw_decode(_log[_k:])
            except ValueError:
                continue
            if isinstance(_o, dict) and 'source_drift' in _o:
                for _x in _o['source_drift']:
                    DRIFT.setdefault(_x['path'], set()).add(_x['id'])
                break
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING'
WHAT = {
    CH + '.md': (
        'the twentieth review\'s step 1 (R25): the ethics\' scope (the continuation condition) and order (C) stated apart '
        '(status, §6.8, §6.12, §6.13, §6.15, §7.5, §8.3, §8.5, the theory stated whole); the two presentations of the base '
        'stated exactly (§1, §9); rising_recurs, falls_not_recurring and Flow.excess_bounded tagged as natural-number facts '
        '(block A, §1, §2, §4); §8 rewritten as twelve ranked open items, its targets and area table moved verbatim to '
        'theories/becoming/history/THE-THEORY-OF-BECOMING-open-programme-2026-10-20.md and its connectivity log to '
        'THEOREM-CONNECTIVITY.md §10; item 11 qualified',
        '第二十次审查第一步（R25）：伦理的范围（延续条件）与次序（C）分开陈述（现状、§6.8、§6.12、§6.13、§6.15、§7.5、§8.3、§8.5、'
        '完整陈述）；基底的两种呈现确切陈述（§1、§9）；rising_recurs、falls_not_recurring 与 Flow.excess_bounded 标为自然数之量的事实'
        '（A 块、§1、§2、§4）；§8 重写为依次排列的十二项，原目标与领域表原样移至 '
        'theories/becoming/history/THE-THEORY-OF-BECOMING-open-programme-2026-10-20.md，连通度量的记录移至 THEOREM-CONNECTIVITY.md §10；'
        '第 11 条加限定'),
    CH + '.zh.md': ('the same changes in the Chinese edition', '中文版的同样改动'),
    RF + 'DELEGATED-CHOICES.md': ('a dated paragraph on what widening counts (a type of formations given in advance; widening over a grown world open); the decisions unchanged',
                                  '一段注明日期的说明：扩大计入什么（事先给定的形成类型；在生长的世界上的扩大开放）；各决定不变'),
    RF + 'DELEGATED-CHOICES.zh.md': ('the same paragraph in Chinese', '同一段（中文）'),
    RF + 'THEOREM-CONNECTIVITY.md': ('section 10 added, the reruns logged in the chapter moved there unchanged; earlier sections unchanged',
                                     '新增第 10 节，章中记下的历次重跑原样移入；前面各节不变'),
    RF + 'BECOMING-RENEWAL-READING.md': ('section 218 added (R25); earlier sections unchanged', '新增第 218 节（R25）；前面各节不变'),
    'AGENTS.md': ('the ethics sentence: the continuation condition fixes scope, only C orders, both premises named', '伦理一句：延续条件定范围，只有 C 定次序，两个前提都写明'),
    '_process/navigation/README-LEAD.md': ('both premises of the ethics named', '伦理的两个前提都写明'),
    'theories/becoming/OPENING.md': ('the AI-written footnote [^axiom] only: scope and order named, the warrant of C open; the body unchanged',
                                     '只改 AI 所写的脚注 [^axiom]：写明范围与次序，C 的根据开放；正文不变'),
    'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md': (
        'the paragraph on the four layers: the two presentations of the base stated exactly', '四层一段：基底的两种呈现确切陈述'),
}
CLAIM = {
    'one-axiom-yields-g0': ('Its hypotheses and one does_not_show item were restated (twentieth review F5): the condition fixes scope, and C, the only premise that orders, is a separate premise; under the condition C on level paths is `Web.widens_iff_retains_adds`.',
                            '其假设与一条 does_not_show 已重述（第二十次审查 F5）：条件定范围，C 是唯一定次序的前提，另行给出；在条件之下，水平路径上的 C 即 `Web.widens_iff_retains_adds`。'),
    'own-count-misses-joint-excess': ('Its statement now says that the amounts are natural numbers (twentieth review D5).',
                                      '其陈述现在写明量是自然数（第二十次审查 D5）。'),
    'reserve-defers-ending': ('One dependency interface now says that the principle is for an amount counted in whole units (twentieth review D5).',
                              '一条依赖接口现在写明这条原则适用于以整单位计的量（第二十次审查 D5）。'),
}
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
base = {p: hashlib.sha256(subprocess.run(['git', 'show', f'{BASE}:{p}'], capture_output=True, check=True).stdout).hexdigest() for p in WHAT}
n = 0
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    rid = f.rsplit('/', 1)[-1][:-5]
    touched = set()
    for r in d.get('references', []):
        p = r['path']
        if p in WHAT and (r.get('sha256') == base[p] or rid in DRIFT.get(p, ())) and r.get('sha256') != h(p):
            r['sha256'] = h(p)
            touched.add(p)
    if not touched and rid not in CLAIM:
        continue
    ps = sorted(touched)
    d['history'].append({
        'en': '20 October 2026, R25 (the twentieth review\'s step 1, docs now): '
              + (', '.join(p.rsplit('/', 1)[-1] for p in ps) + ' re-pointed. R25 changed the cited files as follows: '
                 + '; '.join(p.rsplit('/', 1)[-1] + ', ' + WHAT[p][0] for p in ps) + '. Read before re-pointing; no Lean changed. ' if ps else '')
              + CLAIM.get(rid, ('The claim is unchanged.',))[0],
        'zh': '2026年10月20日，R25（第二十次审查第一步，现在改文本）：'
              + ('、'.join(p.rsplit('/', 1)[-1] for p in ps) + ' 重新指向。R25 对所引文件的改动：'
                 + '；'.join(p.rsplit('/', 1)[-1] + '，' + WHAT[p][1] for p in ps) + '。重新指向前已读；Lean 未改。' if ps else '')
              + CLAIM.get(rid, (None, '论断不变。'))[1]})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(ps))
print(n, 'records changed')
