#!/usr/bin/env python3
"""Y2 follow-up (19 October 2026): the earlier work on the places (the 生生不息 repository's HexagramPosition.lean, its
preserved report, item H6 of the review of that repository) is cited in study section 195. This script adds the
provenance references and the census boundary to place-relations-in-context, and re-points every record whose
reference to the study matched it at BASE, with a history note. usage (from the checkout's root):
python3 -B cite_earlier.py BASE"""
import glob, hashlib, json, subprocess, sys

BASE = sys.argv[1]
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
REPORT = 'sources/07-shengsheng-buxi/ssbx-repo/formal-notes/zhouyi-position-operator-report.md'
REVIEW = RF + 'SSBX-REPOSITORY-REVIEW.md'
OWN = 'theories/becoming/results/records/place-relations-in-context.json'
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
base_sha = hashlib.sha256(subprocess.run(['git', 'show', f'{BASE}:{STUDY}'], capture_output=True, check=True).stdout).hexdigest()
assert base_sha != h(STUDY), 'the study is unchanged since BASE'

CENSUS_EN = ' The censuses of the sixty-four by each count, which the earlier repository states.'
CENSUS_ZH = '六十四卦按各计数的普查（早期仓库已陈述）也未重述。'
NOTE_EN = ('19 October 2026, Y2 follow-up: the earlier work on the places, the 生生不息 repository\'s '
           'HexagramPosition.lean (its commit efd892a5; its Lean is not preserved here), its preserved report on places '
           'and operators and item H6 of the review of that repository, is cited in study section 195: where the '
           'definitions agree, where they part (its 比 counts neighbours of one kind), what is proved here that it left '
           'unproved, and the review\'s H6 revised (the pattern of 應 is a lumping, its count is not). The references to '
           'the report and the review are added and the study reference re-pointed. The claim is unchanged.')
NOTE_ZH = ('2026年10月19日，Y2 补记：早期关于爻位的工作，即《生生不息》仓库的 HexagramPosition.lean（其提交 efd892a5；'
           '其 Lean 未保存于本库）、所存的位与算子报告、该仓库审读的 H6 项，在研究第 195 节中注明：定义相合之处、相分之处'
           '（其「比」数同性相邻）、此处证明而彼处未证的、审读 H6 的修订（應的样式是聚合，其数目不是）。新增对报告与审读的'
           '引用，研究的引用重新指向。论断不变。')
REPOINT_EN = ('19 October 2026, Y2 follow-up: BECOMING-RENEWAL-READING.md re-pointed after reading the change (section 195 '
              'gained a paragraph on the earlier work on the places). The claim is unchanged.')
REPOINT_ZH = '2026年10月19日，Y2 补记：读过改动后，BECOMING-RENEWAL-READING.md 重新指向（第 195 节新增早期关于爻位工作的一段）。论断不变。'

count = 0
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    hits = [r for r in d.get('references', []) if r.get('path') == STUDY and r.get('sha256') == base_sha]
    if f == OWN:
        assert hits, 'own record does not reference the study at BASE'
        paths = {r['path'] for r in d['references']}
        assert REPORT not in paths and REVIEW not in paths
        at = next(i for i, r in enumerate(d['references']) if r['role'] == 'provenance')
        d['references'][at:at] = [
            {'path': REPORT, 'role': 'provenance', 'declarations': [], 'sha256': h(REPORT)},
            {'path': REVIEW, 'role': 'review', 'declarations': [], 'sha256': h(REVIEW)}]
        scope = next(x for x in d['does_not_show'] if x['kind'] == 'scope')
        assert CENSUS_EN not in scope['en']
        scope['en'] += CENSUS_EN
        scope['zh'] += CENSUS_ZH
        note = {'en': NOTE_EN, 'zh': NOTE_ZH}
    elif hits:
        note = {'en': REPOINT_EN, 'zh': REPOINT_ZH}
    else:
        continue
    for r in hits:
        r['sha256'] = h(STUDY)
    d['history'].append(note)
    open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    count += 1
    print(f.rsplit('/', 1)[-1])
print(count, 'records written')
