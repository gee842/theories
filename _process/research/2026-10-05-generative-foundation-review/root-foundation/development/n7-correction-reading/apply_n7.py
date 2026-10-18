#!/usr/bin/env python3
"""N7 (19 October 2026): the reading pass on "correction" (Ren, 19 October 2026: "correct? this is a dualist word, are
we drifting off?"). Replaces each use the naming study's section 9 restates, after checking that its text occurs exactly
once on the tree; updates the live fields of four records; re-points the record references to the changed files, with
a history note. Docs and records only: no Lean, no statement changed. Lands after N6 (the section 3 sentence follows
N6's wording; before N6, its first block still applies and the second reads N6's text) and is independent of M4's
blocks, which restate M4's and M3's sentences (section 7.4 last paragraph, 7.7, 8.2, the 8.4 clause on loops).

usage (from the repository root):
  python3 -B .../n7-correction-reading/apply_n7.py --check    count every block on the tree, change nothing
  python3 -B .../n7-correction-reading/apply_n7.py BASE       apply, then re-point references that matched BASE
  python3 -B .../n7-correction-reading/apply_n7.py --repoint 'SECTION' ID ...
                                              after reading what `make research-render` reports as source_drift
                                              only in SECTION, where N7 restated the word, re-point those records
then: make research-render research-check research-links research-test"""
import glob, hashlib, json, subprocess, sys

CH = 'theories/becoming/chapters/'
EN, ZH = CH + 'THE-THEORY-OF-BECOMING.md', CH + 'THE-THEORY-OF-BECOMING.zh.md'
AD, ADZ = CH + 'ALIGNMENT-DIRECTION.md', CH + 'ALIGNMENT-DIRECTION.zh.md'
OP = 'theories/becoming/OPENING.md'  # its AI-written footnote only, not Ren's body
REC = 'theories/becoming/results/records/'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-19-correct-is-dualist.md'

CLAIM_OLD = 'with effective opportunities to understand, challenge and correct that development'
CLAIM_NEW = 'with effective opportunities to understand, challenge and revise that development'
CLAIM_ZH_OLD = '使这种发展能够被认识、质疑和纠正'
CLAIM_ZH_NEW = '使这种发展能够被认识、质疑和修订'

BLOCKS = {
    EN: [
        # section 3, the boundary condition for 无明 (N6 rewords the first sentence; these substrings hold before and after)
        ('- *Correction.* Losses reach a seeker only through what',
         '- *Beyond its own feedback.* Losses reach a seeker only through what'),
        ('So locked seeking is not corrected by its own feedback.',
         'So the losses locked seeking makes beyond what couples into it do not reach it through its own feedback.'),
        (' corrects it: measurement, a model, or others.',
         ' carries them to it: measurement, a model, or others.'),
        ('Robust judgment, correction under observation and safe choice are therefore one common response.',
         'Robust judgment, a change chosen under observation and safe choice are therefore one common response.'),
        # section 7
        ('and organizes the correction around 明.', 'and organizes its answer around 明.'),
        ('§7.6 keeps the conditions under which a correction can be carried out,',
         '§7.6 keeps the conditions under which a requested change, such as a stop, can reach a system and be carried out,'),
        ('- **Capability widens reach; correction needs coupling.**', '- **Capability widens reach; closing the gap needs coupling.**'),
        ('so locked seeking is not corrected by its own feedback. It is corrected by measurement, a model, or others (§3,',
         'so the losses locked seeking makes beyond that do not reach it through its own feedback. They reach it through '
         'measurement, a model, or others (§3,'),
        ('- **Correction has to reach the rule.** Where the next configuration depends on the rule, a correction that '
         'changes the state alone is re-absorbed from the next step (law 7).',
         '- **A lasting change has to reach the rule.** Where the next configuration depends on the rule, a change to '
         'the state alone is re-absorbed from the next step (law 7).'),
        ('a correction that reaches only states is re-absorbed (law 7).', 'a change that reaches only states is re-absorbed (law 7).'),
        (CLAIM_OLD, CLAIM_NEW),
        ('the claim\'s “effective opportunities to understand, challenge and correct that development”',
         'the claim\'s “effective opportunities to understand, challenge and revise that development”'),
        ('a correction selects what an act does beyond its actor\'s coupling closure only through a coupling that reaches it.',
         'a challenge or a revision selects what an act does beyond its actor\'s coupling closure only through a coupling '
         'that reaches it.'),
        ('### 7.6 Correction must be an executable sequence', '### 7.6 A requested change must be an executable sequence'),
        ('A disposition to accept correction does not by itself mean that correction can reach the system and be completed.',
         'A disposition to accept a requested change, such as a stop or a revision, does not by itself mean that the change '
         'can reach the system and be completed.'),
        ('[recovering evidence after interrupted change, and the bound on reaching correction]',
         '[recovering evidence after interrupted change, and the bound on reaching a stop]'),
        ('§7.3 says what a correction has to couple into; these records state, for their protocols, when it can also be '
         'carried out.',
         '§7.3 says what a change has to couple into to reach what an act does; these records state, for their protocols, '
         'when a requested change can also be carried out.'),
        # sections 8.4 and 8.7
        ('with correction reaching the rule and each law\'s scope kept exact;',
         'with a lasting change reaching the rule and each law\'s scope kept exact;'),
        ('the conditional direction\'s opportunities to correct read as the routes of 明',
         'the conditional direction\'s opportunities to revise read as the routes of 明'),
        ('Whether actual humans and AI form understanding and correction along these routes',
         'Whether actual humans and AI form understanding and revision along these routes'),
    ],
    ZH: [
        ('所以被锁定的寻求不被自身的反馈纠正；识', '所以被锁定的寻求在其所耦合入者之外造成的损失，不经其自身的反馈到达它；识'),
        ('所以被锁定的寻求不被自身的反馈纠正；及于', '所以被锁定的寻求在其所耦合入者之外造成的损失，不经其自身的反馈到达它；及于'),
        ('，即量度、模型或他者，纠正它。', '，即量度、模型或他者，把这些损失带到它那里。'),
        ('稳健判断、观察下的纠正与安全选择因此都是同一个共同回应', '稳健判断、观察下选择的改变与安全选择因此都是同一个共同回应'),
        ('并以明组织纠正。', '并以明组织其回答。'),
        ('§7.6 保留纠正能被执行的条件，', '§7.6 保留所请求的改变（例如停止）能送达系统并被执行的条件，'),
        ('- **能力扩展所及；纠正需要耦合。**', '- **能力扩展所及；合上缺口需要耦合。**'),
        ('所以被锁定的寻求不被自身的反馈纠正；量度、模型或他者纠正它（§3',
         '所以被锁定的寻求在此之外造成的损失，不经其自身的反馈到达它；它们经量度、模型或他者到达它（§3'),
        ('- **纠正须及于规则。** 下一配置取决于规则时，只改变状态的纠正从下一步起被重新吸收（规律 7）。',
         '- **持久的改变须及于规则。** 下一配置取决于规则时，只改变状态的改变从下一步起被重新吸收（规律 7）。'),
        ('只及于状态的纠正被重新吸收（规律 7）', '只及于状态的改变被重新吸收（规律 7）'),
        (CLAIM_ZH_OLD, CLAIM_ZH_NEW),
        ('“能够被认识、质疑和纠正”的机会', '“能够被认识、质疑和修订”的机会'),
        ('动作在行动者耦合闭包之外所做的，纠正只经及于它的耦合才能选择。', '动作在行动者耦合闭包之外所做的，质疑与修订只经及于它的耦合才能选择。'),
        ('### 7.6 纠正须是可执行的序列', '### 7.6 所请求的改变须是可执行的序列'),
        ('接受纠正的倾向，不等于纠正能被送达和完成。', '接受所请求之改变（例如停止或修订）的倾向，不等于这一改变能被送达和完成。'),
        ('被中断变化后的证据恢复与纠正通达的界', '被中断变化后的证据恢复与停止通达的界'),
        ('§7.3 说纠正须耦合入什么；这些记录就其协议说明纠正何时也能被执行。',
         '§7.3 说改变须耦合入什么才及于动作所做的；这些记录就其协议说明所请求的改变何时也能被执行。'),
        ('纠正须及于规则，各规律的范围保持精确', '持久的改变须及于规则，各规律的范围保持精确'),
        ('有条件之方向中纠正的机会读作明之路', '有条件之方向中修订的机会读作明之路'),
        ('实际的人与 AI 是否经这些路线形成其理解与修正', '实际的人与 AI 是否经这些路线形成其理解与修订'),
    ],
    AD: [
        (CLAIM_OLD, CLAIM_NEW),
        ('feasible ways of living and later correction together.', 'feasible ways of living and later revision together.'),
        ('3. **Maintain effective participation, challenge and correction.**', '3. **Maintain effective participation, challenge and revision.**'),
    ],
    ADZ: [
        (CLAIM_ZH_OLD, CLAIM_ZH_NEW),
        ('实际可行的生活方式和之后纠错的条件', '实际可行的生活方式和之后修订的条件'),
        ('3. **保留有效参与、质疑和纠正。**', '3. **保留有效参与、质疑和修订。**'),
        ('申诉、纠正与替换安排', '申诉、修复与替换安排'),
    ],
    OP: [
        ('legitimate participation, and open to correction ([AI alignment]',
         'legitimate participation, and open to revision ([AI alignment]'),
    ],
}
# The two zh section 3 variants: exactly one holds (before or after N6).
ALTERNATIVES = {(ZH, '所以被锁定的寻求不被自身的反馈纠正；识'), (ZH, '所以被锁定的寻求不被自身的反馈纠正；及于')}

# live record fields: (record id, field path, old, new)
RECORDS = [
    ('alignment-direction-g0-j', ('statement', 'en'), 'generative development, correction, transfer and appropriate ending',
     'generative development, revision, transfer and appropriate ending'),
    ('alignment-direction-g0-j', ('statement', 'zh'), '支持生成、纠正、交接与适当结束', '支持生成、修订、交接与适当结束'),
    ('alignment-direction-g0-j', ('overview', 'summary', 'en'), 'aligning learning, action, correction, transfer and appropriate ending',
     'aligning learning, action, revision, transfer and appropriate ending'),
    ('alignment-direction-g0-j', ('overview', 'summary', 'zh'), '使学习、行动、纠正、交接和适当结束', '使学习、行动、修订、交接和适当结束'),
    ('the-gap-for-ones-own-act', ('correspondence', 'en'),
     'correcting an act whose consequences lie beyond takes a coupling that reaches them',
     'responding to an act whose consequences lie beyond takes a coupling that reaches them'),
    ('the-gap-for-ones-own-act', ('correspondence', 'zh'), '纠正后果在闭包之外的动作，需要及于后果的耦合',
     '回应后果在闭包之外的动作，需要及于后果的耦合'),
    ('what-pooled-coupling-reaches', ('does_not_show', 0, 'en'), "that a pool's selection responds to what it separates or corrects anything;",
     "that a pool's selection responds to what it separates or closes any difference;"),
    ('what-pooled-coupling-reaches', ('does_not_show', 0, 'zh'), '一组的选择回应它所分开者或纠正任何东西；', '一组的选择回应它所分开者或闭合任何差别；'),
    ('what-pooled-coupling-reaches', ('next_delta', 'en'), 'which responses to what a pool separates correct the act (',
     'which law closes rather than widens a difference a pool separates ('),
    ('what-pooled-coupling-reaches', ('next_delta', 'zh'), '对一组所分开者的哪些回应纠正动作（', '哪个律闭合而非扩大一组所分开的差别（'),
    ('recoverable-mediated-change', ('title', 'en'), 'Evidence recovery and corrective-access limits after interrupted change',
     'Evidence recovery and the limits of stop access after interrupted change'),
    ('recoverable-mediated-change', ('title', 'zh'), '中断改变后的证据恢复与纠正边界', '中断改变后的证据恢复与停止入口的界'),
]
RECORD_NOTE = {
    'en': '19 October 2026, N7 (the reading pass on "correction"): {what} "Correct" presupposed a standard outside the '
          'relation, a right course and an error to remove (Ren, 19 October 2026: "correct? this is a dualist word, are '
          'we drifting off?"); the field now states the structure meant. The claim is unchanged.',
    'zh': '2026年10月19日，N7（关于“纠正”的读法审读）：{what}“纠正”预设了关系之外的标准，即一条对的进程和一个要去除的错误（Ren，'
          '2026年10月19日：“correct? this is a dualist word, are we drifting off?”）；此字段现陈述所指的结构。论断不变。'}
RECORD_WHAT = {
    'alignment-direction-g0-j': ('statement and overview: "correction" read as revision, as in the restated claim of '
                                 'ALIGNMENT-DIRECTION ("understand, challenge and revise that development"); which '
                                 'revision supports living goes through the stated premises.',
                                 '陈述与概述：“纠正”读作修订，与 ALIGNMENT-DIRECTION 改述后的主张（“能够被认识、质疑和修订”）一致；哪种修订支持生，经所述前提。'),
    'the-gap-for-ones-own-act': ('the AI\'s reading in the correspondence: "correcting an act" read as responding to it.',
                                 '对应中 AI 的读法：“纠正动作”读作回应它。'),
    'what-pooled-coupling-reaches': ('the first non-implication and next_delta: "corrects" read as closing a difference, as M4 states it.',
                                     '第一条非蕴含与 next_delta：“纠正”读作闭合差别，如 M4 所陈述。'),
    'recoverable-mediated-change': ('title: "corrective access" read as access for a stop, which is what the counterexample '
                                    'and next_delta concern (ordinary shutdown blocked during recovery).',
                                    '标题：“纠正入口”读作停止入口，反例与 next_delta 所涉即此（恢复期间普通停机被阻）。'),
}
FILE_WHAT = {
    EN: 'N7 restated the uses of "correction" in sections 3 (the boundary condition for 无明, and the one-step inquiry), '
        '7.0, 7.2, 7.3, 7.4 ("one ground"), 7.5 (the claim and where the two parts meet), 7.6, 8.4 and 8.7',
    ZH: 'N7 restated the uses of 纠正 in the same places of the zh edition',
    AD: 'N7 restated the central claim ("revise" for "correct"), section 2 and the heading of section 4 item 3',
    ADZ: 'N7 restated the central claim (修订 for 纠正), section 2 and section 4 item 3',
    OP: 'N7 restated "open to correction" as "open to revision" in the AI-written footnote on alignment, as in the claim',
}


def check(tree_text):
    bad = []
    for f, blocks in BLOCKS.items():
        t = tree_text[f]
        alts = [old for old, _ in blocks if (f, old) in ALTERNATIVES]
        for old, new in blocks:
            n = t.count(old)
            if (f, old) in ALTERNATIVES:
                if sum(t.count(a) for a in alts) != 1:
                    bad.append((f, old, n))
            elif n != 1:
                bad.append((f, old, n))
    return bad


def get(d, path):
    for k in path:
        d = d[k]
    return d


def put(d, path, v):
    for k in path[:-1]:
        d = d[k]
    d[path[-1]] = v


def repoint(section, ids):
    h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
    for rid in ids:
        f = REC + rid + '.json'
        d = json.load(open(f, encoding='utf-8'))
        files = []
        for r in d['references']:
            if r.get('path') in FILE_WHAT and r.get('sha256') != h(r['path']):
                r['sha256'] = h(r['path'])
                files.append(r['path'].split('/')[-1])
        assert files, rid
        d['history'].append({
            'en': f'19 October 2026, N7 (the reading pass on "correction"): {", ".join(files)} re-pointed. Since this '
                  f'record\'s reviewed hash, the cited text changed only in {section}, where N7 restated "correction" '
                  'by the structure meant. Read before re-pointing. The claim is unchanged.',
            'zh': f'2026年10月19日，N7（关于“纠正”的读法审读）：{"、".join(files)} 重新指向。自本记录所审哈希以来，所引文字只在 {section} '
                  '改动，即 N7 把“纠正”改述为所指结构之处。重新指向前已读。论断不变。'})
        open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        print('re-pointed', rid, files)


def main():
    if sys.argv[1:2] == ['--repoint']:
        return repoint(sys.argv[2], sys.argv[3:])
    text = {f: open(f, encoding='utf-8').read() for f in BLOCKS}
    bad = check(text)
    recs = {}
    for rid, path, old, new in RECORDS:
        d = recs.setdefault(rid, json.load(open(REC + rid + '.json', encoding='utf-8')))
        if get(d, path).count(old) != 1:
            bad.append((rid, path, old))
    for b in bad:
        print('MISMATCH', b)
    if bad:
        sys.exit(1)
    if sys.argv[1:] == ['--check']:
        print('all', sum(len(v) for v in BLOCKS.values()), 'blocks and', len(RECORDS), 'record fields match once')
        return
    base = sys.argv[1]
    for f, blocks in BLOCKS.items():
        t = text[f]
        for old, new in blocks:
            if t.count(old) == 0:
                continue
            t = t.replace(old, new)
        open(f, 'w', encoding='utf-8').write(t)
    for rid, path, old, new in RECORDS:
        put(recs[rid], path, get(recs[rid], path).replace(old, new))
    for rid, d in recs.items():
        en, zh = RECORD_WHAT[rid]
        d['history'].append({'en': RECORD_NOTE['en'].format(what=en[0].upper() + en[1:]),
                             'zh': RECORD_NOTE['zh'].format(what=zh)})
        open(REC + rid + '.json', 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    # re-point references to the four changed files that matched them at BASE (a reference already stale stays)
    h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
    at_base = {p: hashlib.sha256(subprocess.run(['git', 'show', f'{base}:{p}'], capture_output=True, check=True).stdout).hexdigest()
               for p in FILE_WHAT}
    now = {p: h(p) for p in FILE_WHAT}
    n = 0
    for f in sorted(glob.glob(REC + '*.json')):
        d = json.load(open(f, encoding='utf-8'))
        files = []
        for r in d.get('references', []):
            p = r.get('path')
            if p in FILE_WHAT and r.get('sha256') == at_base[p] and now[p] != at_base[p]:
                r['sha256'] = now[p]
                files.append(p)
        if not files:
            continue
        en = '; '.join(f'{p.split("/")[-1]} ({FILE_WHAT[p]})' for p in files)
        d['history'].append({
            'en': f'19 October 2026, N7 (the reading pass on "correction"): re-pointed {en}. Wording only; read before '
                  're-pointing. The claim is unchanged.',
            'zh': '2026年10月19日，N7（关于“纠正”的读法审读）：重新指向 ' + '、'.join(p.split('/')[-1] for p in files)
                  + '。只改措辞（“纠正”改述为所指的结构，见命名研究第 9 节）；重新指向前已读。论断不变。'})
        open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        n += 1
    print('applied; re-pointed', n, 'records')


if __name__ == '__main__':
    main()
