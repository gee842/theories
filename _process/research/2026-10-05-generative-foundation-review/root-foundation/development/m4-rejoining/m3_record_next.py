#!/usr/bin/env python3
"""M4 (19 October 2026): what-a-pools-acts-respond-to named "which responses to what a pool separates correct the
act, and toward what" as a next step; M4 states where the courses with and without an act rejoin. Update that record's next_delta and related
list, with a history note, before rehash_refs.py runs. usage (from the repository root): python3 -B m3_record_next.py"""
import json

PATH = 'theories/becoming/results/records/what-a-pools-acts-respond-to.json'
d = json.load(open(PATH))
OLD_EN = 'Which responses to what a pool separates correct the act, and toward what; '
OLD_ZH = '对一组所分开者的哪些回应纠正动作，朝向什么；'
assert d['next_delta']['en'].count(OLD_EN) == 1 and d['next_delta']['zh'].count(OLD_ZH) == 1
d['next_delta']['en'] = d['next_delta']['en'].replace(
    OLD_EN, 'Which law closes rather than widens a difference a pool separates (where the two courses rejoin, and '
            'through whom, is stated in where-two-courses-rejoin); ')
d['next_delta']['zh'] = d['next_delta']['zh'].replace(
    OLD_ZH, '哪个律闭合而非扩大一组所分开的差别（两个进程在何处、经谁重合，见 where-two-courses-rejoin）；')
assert all(r['id'] != 'where-two-courses-rejoin' for r in d['related'])
d['related'].append({
    'id': 'where-two-courses-rejoin',
    'detail': {'en': 'States what a response must do for the two courses to rejoin: a difference closes only through a different exchange '
                     'with the condition, by exactly the gap, and where the rest reads through its coupling, through a '
                     'formation that couples the two courses apart.',
               'zh': '陈述回应要使两个进程重合须做什么：差别只经与该条件的不同交换而闭合，所交换的恰是差距；其余经其耦合而读时，经一个把两个进程'
                     '耦合得有别的形成。'}})
d['history'].append({
    'en': '19 October 2026, M4 (Becoming.Rejoining): next_delta updated, since where-two-courses-rejoin states when '
          'the courses with and without an act rejoin (only through a different exchange with the condition, and '
          'where the rest reads through its coupling, through a formation coupling the courses apart); which law '
          'closes rather than widens a difference stays open. "Correct" is no longer used for this: the course without '
          'the act is a comparison, not a standard (Ren, 19 October 2026: "correct? this is a dualist word, are we '
          'drifting off?"); the reading and the first boundary are worded likewise. The claim is unchanged.',
    'zh': '2026年10月19日，M4（Becoming.Rejoining）：next_delta 更新，因为 where-two-courses-rejoin 陈述了有动作与无动作的进程'
          '何时重合（只经与该条件的不同交换；其余经其耦合而读时，经把进程耦合得有别的形成）；哪个律闭合而非扩大差别仍开放。此处不再'
          '用“纠正”：无动作的进程是比较，不是标准（Ren，2026年10月19日：“correct? this is a dualist word, are we drifting off?”）。'
          '读法与第一条界限照此措辞。论断不变。'})
# M3's own wording of its reading and boundary, restated without "correct" (Ren, 19 October 2026)
for item in d['does_not_show']:
    for lang, old, new in (('en', "That a pool's response corrects anything, or which responses do;",
                            "That a pool's response closes any difference, or which responses do;"),
                           ('zh', '一组的回应纠正任何东西，或哪些回应纠正；', '一组的回应闭合任何差别，或哪些回应如此；')):
        item[lang] = item[lang].replace(old, new)
for lang, old, new in (('en', 'the structure correction and escalation share.',
                        'the structure that closing a difference and widening it share.'),
                       ('zh', '这是纠正与升级共有的结构。', '这是闭合差别与扩大差别共有的结构。')):
    assert d['correspondence'][lang].count(old) == 1, (lang, old)
    d['correspondence'][lang] = d['correspondence'][lang].replace(old, new)
assert sum("corrects anything" in i['en'] for i in d['does_not_show']) == 0
open(PATH, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', PATH)
