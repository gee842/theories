#!/usr/bin/env python3
"""RC (19 October 2026): the scope record of the Chinese sources after RC lands. Its record joins the results, capture
through the rule joins the gaps that have landed, and the next step keeps RG as the one verified gap module still in
the queue. The README's section on ongoing research is rendered from this record. python3 -B update_goal.py"""
import json

P = '_process/goals/chinese-sources-and-becoming.json'
RID = 'capture-through-the-rule'
raw = open(P).read()
d = json.loads(raw)
assert json.dumps(d, ensure_ascii=False, indent=2) + '\n' == raw


def once(text, old, new):
    assert text.count(old) == 1, old
    return text.replace(old, new)


assert RID not in d['result_ids']
d['result_ids'].append(RID)
o = d['overview']
o['summary']['en'] = once(
    o['summary']['en'],
    'the arrangements of the 傳 (`Becoming.HexagramSequences`) and a code formed between formations, 约定俗成 '
    '(`Becoming.SharedCodes`), have landed',
    'the arrangements of the 傳 (`Becoming.HexagramSequences`), a code formed between formations (约定俗成, '
    '`Becoming.SharedCodes`) and capture through the rule (二柄, 据有余而制不足; `Becoming.RuleCapture`) have landed')
o['summary']['zh'] = once(
    o['summary']['zh'],
    '传之排列（`Becoming.HexagramSequences`）与在形成之间形成的编码、约定俗成（`Becoming.SharedCodes`）已落地',
    '传之排列（`Becoming.HexagramSequences`），在形成之间形成的编码、约定俗成（`Becoming.SharedCodes`），以及经由规则的捕获'
    '（二柄、据有余而制不足；`Becoming.RuleCapture`）已落地')
o['next_step']['en'] = once(
    o['next_step']['en'],
    'Land the two verified gap modules in the queue: two-sided regulation of a level and regulation that reads the '
    'level late (中和, 宽猛相济; `Becoming.Regulation`), and capture through the rule (二柄, 据有余而制不足; '
    '`Becoming.RuleCapture`).',
    'Land the verified gap module in the queue: two-sided regulation of a level and regulation that reads the level '
    'late (中和, 宽猛相济; `Becoming.Regulation`).')
o['next_step']['zh'] = once(
    o['next_step']['zh'],
    '落地队列中两个已验证的缺口模块：水平的双向调节与迟到读法下的调节（中和、宽猛相济；`Becoming.Regulation`），以及经由规则的捕获'
    '（二柄、据有余而制不足；`Becoming.RuleCapture`）。',
    '落地队列中已验证的缺口模块：水平的双向调节与迟到读法下的调节（中和、宽猛相济；`Becoming.Regulation`）。')
open(P, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('goal record updated', len(d['result_ids']), 'results')
