#!/usr/bin/env python3
"""RG (19 October 2026): bring the goal record chinese-sources-and-becoming up to RG's landing, on top of RC's version
(the record owner's instruction): python3 -B update_goal.py   (from the checkout root, before rendering)
1. result_ids: RG's record appended.
2. overview.summary (en, zh): `Becoming.Regulation` added to the gap modules that have landed, with its sources.
3. overview.next_step (en, zh): the queued-module sentence dropped, so the next step starts with the open gaps.
The scope, objective, premises and completion are not touched. README's section is generated from this record."""
import json
import re
from pathlib import Path

PATH = Path('_process/goals/chinese-sources-and-becoming.json')
RID = 'two-sided-regulation-and-late-reading'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:100], text.count(old))
    return text.replace(old, new)


d = json.loads(PATH.read_text())
assert RID not in d['result_ids']
d['result_ids'].append(RID)
ov = d['overview']
s = ov['summary']
# The list of landed gap modules, as RC left it: the last item is joined by "and" / "与"; RG's goes after it.
SUMMARY_EN = [('a code formed between formations (约定俗成, `Becoming.SharedCodes`) and capture through the rule (二柄, '
               '据有余而制不足; `Becoming.RuleCapture`) have landed',
               'a code formed between formations (约定俗成, `Becoming.SharedCodes`), capture through the rule (二柄, '
               '据有余而制不足; `Becoming.RuleCapture`) and two-sided regulation of a level and regulation that reads the '
               'level late (中和, 宽猛相济; `Becoming.Regulation`) have landed')]
SUMMARY_ZH = [('，以及经由规则的捕获（二柄、据有余而制不足；`Becoming.RuleCapture`）已落地',
               '，经由规则的捕获（二柄、据有余而制不足；`Becoming.RuleCapture`），以及水平的双向调节与迟到读法下的调节'
               '（中和、宽猛相济；`Becoming.Regulation`）已落地')]
for old, new in SUMMARY_EN:
    s['en'] = once(s['en'], old, new)
for old, new in SUMMARY_ZH:
    s['zh'] = once(s['zh'], old, new)
assert 'Becoming.Regulation' in s['en'] and 'Becoming.Regulation' in s['zh']
n = ov['next_step']
m_en = re.fullmatch(r'Land [^.]*?`Becoming\.Regulation`[^.]*\. Then (the [a-z]+ open gaps?: .*)', n['en'], re.S)
m_zh = re.fullmatch(r'落地[^。]*?`Becoming\.Regulation`[^。]*。然后是(.*)', n['zh'], re.S)
assert m_en and m_zh, n
n['en'] = m_en.group(1)[0].upper() + m_en.group(1)[1:]
n['zh'] = m_zh.group(1)
assert 'Becoming.Regulation' not in n['en'] + n['zh']
PATH.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('goal record:', RID, 'added; next step:', n['en'][:80])
