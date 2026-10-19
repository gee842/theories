#!/usr/bin/env python3
"""RC (19 October 2026): re-point the chapter reference of records that `make research-render` reports as drifting only
in section 8 because RC rewrote the collective continuation row that links them (RC adds its clause, its open item
and its record link to that row; the change was read before re-pointing). Every rewritten line bearing on such a record
must be that row and nothing else, and the record must be linked from it; any other drift stops the script.
python3 -B repoint_drift.py RENDER_LOG BASE"""
import hashlib, json, subprocess, sys

sys.path.insert(0, '.')
from tools.research import registry  # noqa: E402

C = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
ROW = '| Collective continuation |'
log, base = sys.argv[1], sys.argv[2]
t = open(log).read()
drift = json.loads(t[t.index('{'):t.rindex('}') + 1]).get('source_drift') or []


def row(text):
    rows = [line for line in text.splitlines() if line.startswith(ROW)]
    assert len(rows) == 1, len(rows)
    return rows[0]


now = open(C).read()
old_row = row(subprocess.check_output(['git', 'show', f'{base}:{C}']).decode())
new_row = row(now)
assert old_row != new_row and 'records/capture-through-the-rule.md' in new_row
h = hashlib.sha256(now.encode()).hexdigest()
other = [e for e in drift if e['path'] != C or e['changed_sections'] != ['## 8. Open programme']]
assert not other, other
for e in drift:
    i = e['id']
    assert f'records/{i}.md' in old_row, (i, 'not linked from the collective continuation row')
    f = f'theories/becoming/results/records/{i}.json'
    d = json.load(open(f))
    bearing = [(head, removed, added) for head, removed, added in registry.changed_lines(C, e['reviewed_sha256'], now)
               if registry.links_record(d, '\n'.join(removed + added))]
    assert bearing == [('## 8. Open programme', [old_row], [new_row])], (i, bearing)
    n = 0
    for r in d['references']:
        if r['path'] == C and r['sha256'] != h:
            r['sha256'] = h
            n += 1
    assert n == 1, (i, n)
    d['history'].append({
        'en': '19 October 2026, RC (capture through the rule): THE-THEORY-OF-BECOMING.md re-pointed. Since this record\'s '
              'reviewed hash, the cited text changed only in the collective continuation row of section 8, where RC added '
              'capture through the rule (Becoming.RuleCapture) to what is stated, rules that read more than the share to '
              'what is open, and its record to the links. Read before re-pointing. The claim is unchanged.',
        'zh': '2026年10月19日，RC（经由规则的捕获）：THE-THEORY-OF-BECOMING.md 重新指向。自本记录所审哈希以来，所引文字只在第 8 节集体延续一行'
              '改动：RC 把经由规则的捕获（Becoming.RuleCapture）加入已陈述者，把读出多于份额的规则加入未决者，并加入其记录的链接。'
              '重新指向前已读。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(i)
print(len(drift), 'records re-pointed for the collective continuation row')
