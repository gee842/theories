#!/usr/bin/env python3
"""C2 (Becoming.Exhaustion) landing edits. Every edit must match exactly once.

usage (from the repository root):
  python3 -B apply_text.py package                          copy the module in; import, doc bullet, CORE entry, scope
                                                             sentence, README row
  python3 -B apply_text.py text RECEIPT BASE AFTER APART    study, chapter (section 6.7 bullet, the exhaustion passages,
                                                             section 8.2, section 9), and the next steps of the records
                                                             seeking-boundary, what-taking-all-excludes and
                                                             derived-extent-limits
RECEIPT is the core checker run, BASE the main commit it ran on, AFTER what BASE adds to the last landing (for the
receipt sentence), APART the connectivity check's count of spine theorems apart; the section 9 counts are read from
the receipt itself. Run make_record.py after this phase, and the rehash after that."""
import json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
SR = '../../../' + STUDY
MOD = f'../../../{PKG}/Becoming/Exhaustion.lean'
RID = 'where-a-rising-take-ends'
REC = f'../results/records/{RID}.md'
THEOREMS = 23


def edit(path, pairs):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    for old, new in pairs:
        n = text.count(old)
        if n != 1:
            sys.exit(f'{path}: expected one match, found {n}: {old[:100]!r}')
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')
    print('edited', path, len(pairs))


SCOPE = (
    '    "Exhaustion: a take that is more than now at each of n steps has risen by at least n, so from "\n'
    '    "a condition given at most B at each step it takes all that is given after B + 1 steps and "\n'
    '    "takes more than is given; under balance such taking does not last as many steps as the level "\n'
    '    "plus one, so a formation that while active takes part with a take more than now is not active "\n'
    '    "through a window of B + 1 steps and the level plus one, and one whose activity does not resume "\n'
    '    "once it stops ends, with no need supplied; where renewal depends on what it renews and the "\n'
    '    "seeker stays active while the condition meets a need, the level falls below that need within "\n'
    '    "the window and every formation depending on the condition there is inactive from then on; of "\n'
    '    "a renewer and a taker whose take rises by one at each step, the taker takes all that is given "\n'
    '    "from step one and ends at step four while the renewer continues. No ethical predicate occurs. "\n')


def package():
    shutil.copyfile(HERE / 'Becoming/Exhaustion.lean', ROOT / PKG / 'Becoming/Exhaustion.lean')
    print('copied Becoming/Exhaustion.lean')
    edit(f'{PKG}/Becoming.lean', [
        ('import Becoming.Exclusion\n', 'import Becoming.Exclusion\nimport Becoming.Exhaustion\n'),
        ('  The levels admit the second where it ends, so admission does not see the exclusion.\n',
         '  The levels admit the second where it ends, so admission does not see the exclusion.\n'
         '* `Becoming.Exhaustion` (L3): where a take that is more than now ends, with no ethical premise.\n'
         '  Read on what a formation takes from a condition, "more than now" (`Becoming.Seeking`) rises by\n'
         '  at least one at each step, so from a condition given at most `B` at each step the take comes\n'
         '  to take all that is given within `B + 1` steps and then more than is given. Under balance such\n'
         '  taking lasts fewer steps than the level plus one, so a formation that while active takes part\n'
         '  with a take more than now does not stay active, and where its activity does not resume it\n'
         '  ends, with no need supplied. Where renewal depends on what it renews and the seeker stays\n'
         '  active while its need is met, the level falls below the need and every formation depending on\n'
         '  the condition there ends. In `Alone` the same taker, taking all that is given without its take\n'
         '  rising, continues.\n'),
    ])
    edit(f'{PKG}/check_becoming.py', [
        ('"Becoming.Admission", "Becoming.Exclusion",\n', '"Becoming.Admission", "Becoming.Exclusion", "Becoming.Exhaustion",\n'),
        ('    "while the levels of the last two courses admit every member at every step. No ethical "\n'
         '    "predicate occurs. "\n',
         '    "while the levels of the last two courses admit every member at every step. No ethical "\n'
         '    "predicate occurs. "\n' + SCOPE),
    ])
    readme = f'{PKG}/README.md'
    text = (ROOT / readme).read_text(encoding='utf-8')
    row = next(line for line in text.split('\n') if line.startswith('| L3 | [`Becoming.Exclusion`]'))
    new_row = ('| L3 | [`Becoming.Exhaustion`](Becoming/Exhaustion.lean) | where a take that is more than now ends, with no '
               'ethical premise: a quantity more than now at each of `n` steps has risen by at least `n` '
               '(`more_accumulates`), so a take more than now from a condition given at most `B` at each step exceeds '
               'what is given after `B + 1` steps (`Flow.exceeds_of_more`): taking part, it takes all that is given '
               '(`Flow.takesAll_of_more`) and the taking exceeds what is given (`Flow.excess_of_more`); under balance no '
               'formation takes part and takes more than is given at each of `W.level T c + 1` steps '
               '(`Flow.beyond_given_bounded`); so a formation that while active takes part with a take more than now is '
               'not active through the window of `B + 1 + (W.level (T + (B + 1)) c + 1)` steps '
               '(`Flow.seeking_bounded`), does not stay active (`Flow.seeking_not_continues`) and, where its activity '
               'does not resume, ends (`Flow.seeking_ends`), with no need supplied; where renewal depends on what it '
               'renews and the seeker stays active while the condition is at least `m`, the level falls below `m` within '
               'the window and every formation depending on the condition at a need of at least `m` is inactive from '
               'then on (`Flow.seeking_exhausts`); of `Exceeding`\'s members, a taker whose take rises by one at each '
               'step takes all that is given from step one and ends at step four, also by the law, while the renewer '
               'continues (`Seeker.course`, `Seeker.ends_by_law`), and in `Alone` the taker taking all that is given '
               'without a rising take continues (`Alone.takes_all`) ([where-a-rising-take-ends](../../../../../../'
               'theories/becoming/results/records/where-a-rising-take-ends.md)). |')
    edit(readme, [(row + '\n', row + '\n' + new_row + '\n')])


def receipt_counts(rid):
    d = json.loads((ROOT / PKG / 'becoming-checks' / rid / 'verification.json').read_text())
    assert d['status'] == 'passed', d['status']
    mods = {m['module']: m for m in d['modules']}
    th = lambda names: sum(int(mods[n]['theorems']) for n in names)
    return {
        'core': (len(d['core_modules']), th(d['core_modules'])),
        'foundation': (len(d['foundation_modules']), th(d['foundation_modules'])),
        'closure': (len(d['core_closure']), th(d['core_closure'])),
        'bridge': (len(d['bridge_modules']), th(d['bridge_modules'])),
        'spine': th(d['spine_modules']),
        'audited': sum(len(mods[n]['declarations']) for n in d['spine_modules']),
        'pj': (len(d['periphery_join_modules']), th(d['periphery_join_modules'])),
        'inherited': len(d['inherited_receipts']),
        'compile': len(d['compile_order']),
        'injeq': (len(d['generated_axiom_dependencies']), len(d['bridge_generated_axiom_dependencies'])),
        'module': int(mods['Becoming.Exhaustion']['theorems']),
    }


def n(x):
    return f'{x:,}'


def subn1(pattern, repl, text, what):
    text, k = re.subn(pattern, repl, text)
    if k != 1:
        sys.exit(f'{what}: expected one match, found {k}')
    return text


def narrow(rid_, old_en, new_en, old_zh, new_zh, why_en, why_zh, related_en, related_zh):
    p = ROOT / f'theories/becoming/results/records/{rid_}.json'
    d = json.loads(p.read_text())
    before = dict(d['next_delta'])
    assert d['next_delta']['en'].count(old_en) == 1 and d['next_delta']['zh'].count(old_zh) == 1, (rid_, d['next_delta'])
    d['next_delta'] = {'en': d['next_delta']['en'].replace(old_en, new_en), 'zh': d['next_delta']['zh'].replace(old_zh, new_zh)}
    assert len(d['next_delta']['en']) <= 400, (rid_, len(d['next_delta']['en']))
    assert all(x['id'] != RID for x in d['related'])
    d['related'].append({'id': RID, 'detail': {'en': related_en, 'zh': related_zh}})
    d['history'].append({
        'en': f'18 October 2026, C2 (Becoming.Exhaustion): {why_en}, so the next step was narrowed and the record linked. '
              f'Before: next step "{before["en"]}". The claim is unchanged.',
        'zh': f'2026年10月18日，C2（Becoming.Exhaustion）：{why_zh}，所以下一步收窄并链接该记录；原文见英文。论断不变。'})
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print('edited', p.relative_to(ROOT))


def text_phase(rid, base, after, apart):
    c = receipt_counts(rid)
    assert c['module'] == THEOREMS, c['module']
    spine = n(c['spine'])
    # ------------------------------------------------------------ study
    study = (ROOT / STUDY).read_text(encoding='utf-8')
    sec = max(int(x) for x in re.findall(r'^## (\d+)\. ', study, re.M)) + 1
    body = (HERE / 'study_c2.txt').read_text(encoding='utf-8')
    body = body.replace('{N}', str(sec)).replace('{RECEIPT}', rid).replace('{APART}', apart).replace('{SPINE}', spine)
    marker = '## Ren’s words quoted in passages that exist only in the Chinese edition'
    assert study.count(marker) == 1
    study = study.replace(marker, body.rstrip('\n') + '\n\n' + marker)
    (ROOT / STUDY).write_text(study, encoding='utf-8')
    print('study section', sec)
    anchor = f'{sec}-where-a-take-more-than-now-ends-c2'
    # ------------------------------------------------------------ chapter
    ch = (ROOT / CHAPTER).read_text(encoding='utf-8')
    bullet = next(line for line in ch.split('\n') if line.startswith('- **What taking all that is given excludes**'))
    new_bullet = (
        f'- **Where a take more than now ends** ([Becoming.Exhaustion]({MOD}), [{RID}]({REC})). Read “more than now” '
        '(`MoreThanNow` of `Becoming.Seeking`) on what a formation takes from a condition. A take more than now at each '
        'of `n` steps has risen by at least `n` (`more_accumulates`), so from a condition given at most `B` at each '
        'step it exceeds what is given after `B + 1` steps: taking part, the formation takes all that is given, and '
        'more (`Flow.takesAll_of_more`, `Flow.excess_of_more`). This is one way taking all that is given forms. Under '
        'balance, taking more than is given cannot go on for `W.level T c + 1` steps from `T` '
        '(`Flow.beyond_given_bounded`). So a formation that, while active, takes part with a take more than now is not '
        'active through a window of `B + 1` steps and the level plus one (`Flow.seeking_bounded`). Where its activity '
        'does not resume once it stops, it ends (`Flow.seeking_ends`). The ending is derived from balance and the '
        'bound on what is given; neither a need nor a dependence is supplied. Where renewal depends on what it renews '
        'and the seeker stays active while the condition is at least `m`, the level falls below `m` within that window. '
        'From then on every formation depending on the condition at a need of at least `m` is inactive, the renewers '
        'included (`Flow.seeking_exhausts`). Among `Exceeding`\'s members, a taker whose take rises by one at each step '
        'takes all that is given from step one and is inactive from step four, which the law also gives; the renewer '
        'is active at every step (`Seeker.course`, `Seeker.ends_by_law`). In `Alone` the same taker takes all that is '
        'given at every step without its take rising, and is active at every step (`Alone.takes_all`). So what ends '
        'the seeker is that its take rises, not that it takes all.')
    exhaust = ('the pursuit ends by exhaustion, not by reaching enough (`Flow.more_exhausted`).')
    exhaust_new = (exhaust + ' Read on what a seeker takes from a condition given within a bound, exhaustion ends the '
                   'seeker itself: its take comes to take all that is given and then more, which balance does not allow '
                   f'for longer than the level (`Flow.seeking_ends`, [{RID}]({REC})).')
    pairs = [
        (bullet + '\n', bullet + '\n' + new_bullet + '\n'),
        # section 8.2, Seeking, capture and runaway
        ('exhaustion ending the seekers themselves where activity needs support;',
         'exhaustion ending the seekers themselves where the seeking is not a take more than now from a condition '
         'given within a bound (where it is, the seeker ends under balance alone and, where renewal depends on what it '
         'renews, so does every formation at its need: `Becoming.Exhaustion`);'),
        ('| [seeking-boundary](../results/records/seeking-boundary.md), [the-boundary-of-enough-under-undetermined-laws]',
         f'| [seeking-boundary](../results/records/seeking-boundary.md), [{RID}]({REC}), '
         '[the-boundary-of-enough-under-undetermined-laws]'),
        # section 8.2, Continuation (§6.7) and feeding
        ('how taking all that is given forms, for instance through what it gains (a stronger case of the meta-attractor;',
         'how taking all that is given forms other than by a take more than now (a take more than now from a condition '
         'given within a bound takes all that is given within `B + 1` steps, and then ends: `Becoming.Exhaustion`), '
         'for instance through what it gains (a stronger case of the meta-attractor;'),
        (f'[closure-verdict-meets-axiom](../results/records/closure-verdict-meets-axiom.md), '
         '[what-taking-all-excludes](../results/records/what-taking-all-excludes.md) |',
         f'[closure-verdict-meets-axiom](../results/records/closure-verdict-meets-axiom.md), '
         f'[what-taking-all-excludes](../results/records/what-taking-all-excludes.md), [{RID}]({REC}) |'),
    ]
    for old, new in pairs:
        k = ch.count(old)
        if k != 1:
            sys.exit(f'chapter: expected one match, found {k}: {old[:100]!r}')
        ch = ch.replace(old, new)
    # the exhaustion bullet of the seeking passage (the line beginning "- *Exhaustion.* ")
    lines = ch.split('\n')
    hits = [i for i, line in enumerate(lines) if line.startswith('- *Exhaustion.* ')]
    assert len(hits) == 1, hits
    assert lines[hits[0]].endswith(exhaust), lines[hits[0]][-120:]
    lines[hits[0]] = lines[hits[0]][:-len(exhaust)] + exhaust_new
    ch = '\n'.join(lines)
    ch = subn1(r'finds [\d,]+ of the [\d,]+ spine theorems apart from both base families at the last rerun',
               f'finds {apart} of the {spine} spine theorems apart from both base families at the last rerun', ch,
               'section 9 connectivity')
    ch = subn1(r'\d+ modules counting the root `Becoming`, and \d+ in the core closure with the foundation',
               f'{c["core"][0]} modules counting the root `Becoming`, and {c["closure"][0]} in the core closure with the '
               'foundation', ch, 'section 9 module counts')
    start = ch.index('**The current receipt.**')
    end = ch.index('Further facts about the receipt:', start)
    para = ch[start:end]
    old_rid = re.search(r'is run `([0-9TZ.]+)`', para).group(1)
    para = para.replace(old_rid, rid)
    para = subn1(r'It was checked with Lean 4\.29\.1 on main \S+ .*?(?:, and it passed\.|\. It passed\.)',
                 f'It was checked with Lean 4.29.1 on main {base} ({after}) with C2 (`Becoming.Exhaustion`, '
                 f'[study §{sec}]({SR}#{anchor})) in the working tree. It passed.', para, 'receipt sentence')
    rows = {
        '| Core modules (with the root `Becoming`, 0 theorems) |': f' {c["core"][0]} modules, {n(c["core"][1])} theorems |',
        '| Foundation modules |': f' {c["foundation"][0]} modules, {n(c["foundation"][1])} theorems |',
        '| Core closure |': f' {c["closure"][0]} modules, {n(c["closure"][1])} theorems |',
        '| Spine (the core; no bridge since the F3 sweep) |': f' {spine} theorems |',
        '| Audited spine declarations |': f' {n(c["audited"])} |',
        '| Modules in the compile order |': f' {c["compile"]} |',
    }
    lines = para.split('\n')
    for i, line in enumerate(lines):
        for head, tail in rows.items():
            if line.startswith(head):
                lines[i] = head + tail
        assert not line.startswith(('| Bridge modules', '| Periphery-join modules')), line
        if line.startswith('| Inherited modules bound'):
            assert f'| {c["inherited"]} (' in line, line
        if line.startswith('| Generated `injEq`'):
            assert f'| {c["injeq"][0]} in the core closure' in line and c['bridge'][0] == 0, line
    para = '\n'.join(lines)
    ch = ch[:start] + para + ch[end:]
    reruns = list(re.finditer(r'Rerun with [^()]+ \(receipt [^)]*\), it counts [\d,]+ of [\d,]+[^.]*\.', ch))
    assert reruns and len({ch.count('\n', 0, m.start()) for m in reruns}) == 1, 'connectivity reruns'
    at = reruns[-1].end()
    ch = ch[:at] + f' Rerun with C2 (receipt {rid}), it counts {apart} of {spine}, none in `Becoming.Exhaustion`.' + ch[at:]
    (ROOT / CHAPTER).write_text(ch, encoding='utf-8')
    print('edited', CHAPTER)
    # ------------------------------------------------------------ records whose next step C2 narrows
    narrow('seeking-boundary',
           'exhaustion ending the seekers themselves where activity needs support;',
           'exhaustion ending the seekers where the seeking is not a take more than now from a bounded giving;',
           '耗尽在活动需要支持之处终结寻求者自身；', '寻求不是对有界所给的多于此刻的取用之处，耗尽终结寻求者；',
           'exhaustion ending the seeker is derived in where-a-rising-take-ends where the seeking is a take more than '
           'now from a condition given within a bound',
           '在 where-a-rising-take-ends 中，寻求是对所给有界的条件的多于此刻的取用之处，耗竭终结寻求者已推出',
           'There, where what stands runs down, the rises of more than now do not recur; here, read on what a seeker '
           'takes from a bounded giving, the seeker itself ends under balance alone.',
           '那里所立者衰减之处，多于此刻的上升不再出现；这里读在寻求者从有界所给中所取上，寻求者本身仅在平衡下终结。')
    narrow('what-taking-all-excludes',
           'how taking all that is given forms;',
           'how taking all that is given forms other than by a rising take;',
           '取尽所给如何形成；', '取尽所给如何以上升的取用以外的方式形成；',
           'one way taking all that is given forms is stated in where-a-rising-take-ends: a take more than now from a '
           'bounded giving',
           '取尽所给的一种形成方式已在 where-a-rising-take-ends 中陈述：对有界所给的多于此刻的取用',
           'There a full taker that continues excludes every other taker; here a take more than now comes to take all '
           'that is given and does not continue.',
           '那里持续的取尽者排除每个其他取用者；这里多于此刻的取用达到取尽所给，且不持续。')
    narrow('derived-extent-limits',
           'how taking all that is given forms (a stronger case of the meta-attractor);',
           'how taking all forms other than by a rising take (a stronger case of the meta-attractor);',
           '取尽所给如何形成（元吸引子的更强情形）；', '取尽所给如何以上升的取用以外的方式形成（元吸引子的更强情形）；',
           'one way taking all that is given forms is stated in where-a-rising-take-ends: a take more than now from a '
           'bounded giving',
           '取尽所给的一种形成方式已在 where-a-rising-take-ends 中陈述：对有界所给的多于此刻的取用',
           'There the clearer\'s ending of the dweller is stipulated; here a seeker\'s ending is derived from balance '
           'and a bound on what is given.',
           '那里清除者对栖居者的终结是规定的；这里寻求者的终结由平衡与所给之界推出。')



if __name__ == '__main__':
    if sys.argv[1] == 'package':
        package()
    elif sys.argv[1] == 'text':
        text_phase(*sys.argv[2:6])
    else:
        sys.exit(__doc__)
