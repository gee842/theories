#!/usr/bin/env python3
"""W2 (19 October 2026): re-point the chapter reference of records that `make research-render` reports as drifting
only in sections W2 changed, after reading the change: python3 -B repoint_drift_w2.py RENDER_LOG

RENDER_LOG is the render's JSON report; every drifting record must cite the chapter and drift only in the sections
below, which W2 alone changed since the render last passed on main."""
import hashlib, json, sys

C = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
WHAT = {
    '## 1. Becoming: one unfolding': 'W2 extended the sentence on the import tree: no module free of the labelled '
                                     'process imports the frame, and the readings of a module holding both are in '
                                     'Becoming.Labelled, Becoming.LabelledRoles, Becoming.ValuationFrames or the run '
                                     'and trace module that reads it',
    '## 9. The formal spine': 'W2 revised the module counts of the two rings, the L3 and L4 bullets (Becoming.JointPlans, '
                              'Becoming.ValuationFrames), the receipt sentence and counts',
}
WHAT_ZH = {
    '## 1. Becoming: one unfolding': '第 1 节（W2 扩充导入树一句：不含带标签过程的模块都不导入框架，兼含两者的模块的读法所在）',
    '## 9. The formal spine': '第 9 节（W2 更新两环的模块数、L3 与 L4 两条、回执句与计数）',
}
text = open(sys.argv[1]).read()
report = json.loads(text[text.index('{'):text.rindex('}') + 1])
h = hashlib.sha256(open(C, 'rb').read()).hexdigest()
for drift in report['source_drift']:
    i, secs = drift['id'], drift['changed_sections']
    assert drift['path'] == C and secs and all(s in WHAT for s in secs), (i, drift['path'], secs)
    f = f'theories/becoming/results/records/{i}.json'
    d = json.load(open(f))
    n = 0
    for r in d['references']:
        if r['path'] == C and r['sha256'] != h:
            r['sha256'] = h
            n += 1
    assert n == 1, (i, n)
    d['history'].append({
        'en': '19 October 2026, W2 (the re-rooting, second batch): THE-THEORY-OF-BECOMING.md re-pointed. In the sections '
              'this record cites, the only change bearing on it since the render last passed on main is W2\'s: '
              + '; '.join(WHAT[s] for s in secs) + '. Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，W2（重新定根第二批）：THE-THEORY-OF-BECOMING.md 重新指向。本记录所引各节中，自主线上次通过渲染以来，与本记录相关的改动只有 W2 的：'
              + '；'.join(WHAT_ZH[s] for s in secs) + '。重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i, secs)
