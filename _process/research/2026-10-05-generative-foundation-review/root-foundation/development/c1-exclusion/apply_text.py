#!/usr/bin/env python3
"""C1 (Becoming.Exclusion) landing edits. Every edit must match exactly once.

usage (from the repository root):
  python3 -B apply_text.py package                          copy the module in; import, doc bullet, CORE entry, scope
                                                             sentence, README row
  python3 -B apply_text.py text RECEIPT BASE AFTER APART    study, chapter (section 6.7 bullet, section 8.2, section 9),
                                                             DELEGATED-CHOICES D44, the record derived-extent-limits
RECEIPT is the core checker run, BASE the main commit it ran on, AFTER what BASE adds to the last landing (for the
receipt sentence, e.g. "after L2, `Becoming.Labels`"), APART the connectivity check's count of spine theorems apart;
the section 9 counts are read from the receipt itself."""
import json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
SR = '../../../' + STUDY
MOD = f'../../../{PKG}/Becoming/Exclusion.lean'
REC = '../results/records/what-taking-all-excludes.md'


def append(path, line):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    assert line not in text, path
    p.write_text(text.rstrip('\n') + '\n' + line + '\n', encoding='utf-8')
    print('appended to', path)


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
    '    "Exclusion: where renewal is given only by formations depending on what they renew, a "\n'
    '    "formation taking all that is given to a condition makes every other taker a joint excess, so "\n'
    '    "full taking alongside another taker for as many steps as the level allows ends every "\n'
    '    "formation depending on the condition at such a need, the full taker included; a full taker "\n'
    '    "that continues leaves no other formation taking from the condition through a window as long "\n'
    '    "as the level, a formation active only while it takes from it is not active through such a "\n'
    '    "window, and one whose activity does not resume once it stops ends; taking jointly within what "\n'
    '    "is given keeps the level and, where the formations depend on that condition alone at needs "\n'
    '    "it met at the start, every formation supported; of a renewer and two takers, all end where "\n'
    '    "both take two, the renewer and the first continue where the first takes all and the second "\n'
    '    "ends, the ending also following from the law, and all three continue where each takes one, "\n'
    '    "while the levels of the last two courses admit every member at every step. No ethical "\n'
    '    "predicate occurs. "\n')


def package():
    shutil.copyfile(HERE / 'Becoming/Exclusion.lean', ROOT / PKG / 'Becoming/Exclusion.lean')
    print('copied Becoming/Exclusion.lean')
    edit(f'{PKG}/Becoming.lean', [
        ('import Becoming.Admission\n', 'import Becoming.Admission\nimport Becoming.Exclusion\n'),
        ("  these as Ren's generative, degenerative and neutral is the AI's reading.\n",
         "  these as Ren's generative, degenerative and neutral is the AI's reading.\n"
         '* `Becoming.Exclusion` (L3): what taking all that is given excludes, with no ethical premise.\n'
         '  A formation takes all that is given to a condition across a step where it takes part and\n'
         '  takes from it at least all that the step gives to it; alongside it, any other taker makes\n'
         '  the joint taking exceed what is given. So where renewal is given only by formations\n'
         '  depending on what they renew, full taking alongside another taker for as many steps as the\n'
         '  level allows ends every formation depending on the condition at such a need, the full taker\n'
         '  included; a full taker that continues leaves no other formation taking through such a\n'
         '  window, and a formation living by taking from the condition, whose activity does not resume\n'
         '  once it stops, ends. Taking jointly within what is given keeps the level and every formation\n'
         '  supported. Of a renewer and two takers, the first\'s continuation does not require the\n'
         '  second\'s ending (all three continue where each takes one); taking all that is given does.\n'
         '  The levels admit the second where it ends, so admission does not see the exclusion.\n'),
    ])
    edit(f'{PKG}/check_becoming.py', [
        ('"Becoming.Admission",\n        "Becoming.Regions",', '"Becoming.Admission", "Becoming.Exclusion",\n        "Becoming.Regions",'),
        ('    "occurs. "\n    "Regions: within a region of formations levels admit everything other levels admit there, and "\n',
         '    "occurs. "\n' + SCOPE +
         '    "Regions: within a region of formations levels admit everything other levels admit there, and "\n'),
    ])
    readme = f'{PKG}/README.md'
    text = (ROOT / readme).read_text(encoding='utf-8')
    row = next(line for line in text.split('\n') if line.startswith('| L3 | [`Becoming.Admission`]'))
    new_row = ('| L3 | [`Becoming.Exclusion`](Becoming/Exclusion.lean) | what taking all that is given excludes, with no '
               'ethical premise: a formation takes all that is given to a condition across a step where it takes part and '
               'takes from it at least all that the step gives to it (`Flow.TakesAll`), and any other taker then makes the '
               'joint taking exceed what is given (`Flow.excess_of_takesAll`); where renewal depends on what it renews, full '
               'taking alongside another taker at each of `n` steps from a level below `n + m` ends every formation '
               'depending on the condition at a need of at least `m`, the full taker included (`Flow.full_taking_ends`, '
               '`Flow.full_taking_ends_at`); a full taker that continues leaves no other formation taking at each of the '
               '`W.level T c + 1` steps from any `T` (`Flow.continuing_excludes`), a formation active only while it takes '
               'is not active at each of them (`Flow.continuing_excludes_active`) and, where its activity does not resume '
               'once it stops, ends (`Flow.continuing_ends_taker`); one that continues alongside another taker does not '
               'take all that is given at each of them (`Flow.alongside_not_all`); taking jointly within what is given '
               'keeps the level (`Flow.level_kept`) and every formation supported where the formations depend on that '
               'condition alone at needs it met at the start (`Flow.supported_of_within`); of `Exceeding`\'s members, all '
               'end where both take two, the renewer and the first continue where the first takes all and the second '
               'ends, the ending also following from the law (`Excluding.ends_by_law`), and all three continue within '
               'what is given where each takes one (`Excluding.three_courses`, `Sharing.full_taking_needed`); the levels '
               'of the last two courses admit every member at every step and each level path includes the other '
               '(`Excluding.admission_alike`) ([what-taking-all-excludes](../../../../../../theories/becoming/results/'
               'records/what-taking-all-excludes.md)). |')
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
        'exclusion': int(mods['Becoming.Exclusion']['theorems']),
    }


def n(x):
    return f'{x:,}'


def subn1(pattern, repl, text, what):
    text, k = re.subn(pattern, repl, text)
    if k != 1:
        sys.exit(f'{what}: expected one match, found {k}')
    return text


def text_phase(rid, base, after, apart):
    c = receipt_counts(rid)
    assert c['exclusion'] == 31, c['exclusion']
    spine = n(c['spine'])
    # ------------------------------------------------------------ study
    study = (ROOT / STUDY).read_text(encoding='utf-8')
    sec = max(int(x) for x in re.findall(r'^## (\d+)\. ', study, re.M)) + 1
    body = (HERE / 'study_c1.txt').read_text(encoding='utf-8')
    body = body.replace('{N}', str(sec)).replace('{RECEIPT}', rid).replace('{APART}', apart).replace('{SPINE}', spine)
    marker = '## Ren’s words quoted in passages that exist only in the Chinese edition'
    assert study.count(marker) == 1
    study = study.replace(marker, body.rstrip('\n') + '\n\n' + marker)
    (ROOT / STUDY).write_text(study, encoding='utf-8')
    print('study section', sec)
    anchor = f'{sec}-what-taking-all-that-is-given-excludes-c1'
    # ------------------------------------------------------------ chapter
    ch = (ROOT / CHAPTER).read_text(encoding='utf-8')
    bullet = next(line for line in ch.split('\n') if line.startswith('- **What the derived extent does not reach.**'))
    new_bullet = (
        f'- **What taking all that is given excludes** ([Becoming.Exclusion]({MOD}), [what-taking-all-excludes]({REC})). '
        'A formation takes all that is given to a condition across a step where it takes part and takes from the '
        'condition at least all that the step gives to it (`Flow.TakesAll`); alongside it, any other taker makes the '
        'joint taking exceed what is given (`Flow.excess_of_takesAll`). So where renewal is given only by formations '
        'depending on what they renew, full taking alongside another taker at each of `n` steps, from a level below '
        '`n + m`, ends every formation depending on the condition at a need of at least `m`, the full taker included '
        '(`Flow.full_taking_ends`). A full taker that continues therefore leaves no other formation taking from the '
        'condition at each of the `W.level T c + 1` steps from any `T` (`Flow.continuing_excludes`). A formation active '
        'only while it takes from the condition is not active at each of them, and where its activity does not resume '
        'once it stops, it ends (`Flow.continuing_excludes_active`, `Flow.continuing_ends_taker`): here the ending is '
        'derived, not stipulated. Taking jointly within what is given keeps the level, and keeps every formation '
        'supported where the formations depend on that condition alone at needs it met at the start '
        '(`Flow.level_kept`, `Flow.supported_of_within`). Three courses of `Exceeding`\'s members show what ending '
        'another serves (`Excluding.three_courses`). Where both takers take two, all end. Where the first takes all '
        'that is given and the second ends after the first step, the renewer and the first are active at every step, '
        'and the ending also follows from the law (`Excluding.ends_by_law`). Where each takes one, all three are '
        'supported and active at every step, and neither takes all that is given. So the first\'s continuation does '
        'not require the second\'s ending; taking all that is given does. The levels of the last two courses admit '
        'every member at every step, and each level path includes the other (`Excluding.admission_alike`). The '
        'exclusion acts through the taking, not through the levels the second needs, so a comparison of courses by '
        'admission does not register it, and the loss is the member\'s continuation [AI reading, D44].')
    pairs = [
        (bullet + '\n', bullet + '\n' + new_bullet + '\n'),
        # section 8.2, Continuation (§6.7) and feeding
        ("a witness in which ending another serves the clearer's continuation (a stronger case of the meta-attractor); "
         'forced endings;',
         'how taking all that is given forms, for instance through what it gains (a stronger case of the '
         'meta-attractor; ending another serves taking all that is given, not continuing as such: a full taker that '
         'continues leaves no other formation taking through a window as long as the level, a formation living by '
         'taking from the condition ends, and the same members all continue taking within what is given: '
         '`Becoming.Exclusion`); forced endings in the witnesses of §6.7; a comparison of courses that registers an '
         'ending through exclusion from taking, which admission does not;'),
        ('[consumption-ends-with-feeders](../results/records/consumption-ends-with-feeders.md), '
         '[closure-verdict-meets-axiom](../results/records/closure-verdict-meets-axiom.md) |',
         '[consumption-ends-with-feeders](../results/records/consumption-ends-with-feeders.md), '
         f'[closure-verdict-meets-axiom](../results/records/closure-verdict-meets-axiom.md), [what-taking-all-excludes]({REC}) |'),
    ]
    for old, new in pairs:
        k = ch.count(old)
        if k != 1:
            sys.exit(f'chapter: expected one match, found {k}: {old[:100]!r}')
        ch = ch.replace(old, new)
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
    para = subn1(r'It was checked with Lean 4\.29\.1 on main \S+ (?:\(.*?\) )?with .*? in the working tree, and it passed\.',
                 f'It was checked with Lean 4.29.1 on main {base} ({after}) with C1 (`Becoming.Exclusion`, '
                 f'[study §{sec}]({SR}#{anchor})) in the working tree, and it passed.', para, 'receipt sentence')
    rows = {
        '| Core modules (with the root `Becoming`, 0 theorems) |': f' {c["core"][0]} modules, {n(c["core"][1])} theorems |',
        '| Foundation modules |': f' {c["foundation"][0]} modules, {n(c["foundation"][1])} theorems |',
        '| Core closure |': f' {c["closure"][0]} modules, {n(c["closure"][1])} theorems |',
        '| Spine (core and bridge) |': f' {spine} theorems |',
        '| Audited spine declarations |': f' {n(c["audited"])} |',
        '| Modules in the compile order |': f' {c["compile"]} |',
    }
    lines = para.split('\n')
    for i, line in enumerate(lines):
        for head, tail in rows.items():
            if line.startswith(head):
                lines[i] = head + tail
        if line.startswith('| Bridge modules'):
            assert f'| {c["bridge"][0]} modules, {n(c["bridge"][1])} theorems |' in line, line
        if line.startswith('| Periphery-join modules'):
            assert f'| {c["pj"][0]} modules, {n(c["pj"][1])} theorems,' in line, line
        if line.startswith('| Inherited modules bound'):
            assert f'| {c["inherited"]} (' in line, line
        if line.startswith('| Generated `injEq`'):
            assert f'| {c["injeq"][0]} in the core closure, {c["injeq"][1]} on the bridge side' in line, line
    para = '\n'.join(lines)
    ch = ch[:start] + para + ch[end:]
    reruns = list(re.finditer(r'Rerun with [A-Z0-9]+ \(receipt [^)]*\), it counts [\d,]+ of [\d,]+, none in '
                              r'`Becoming\.[A-Za-z]+`\.', ch))
    assert reruns and len({ch.count('\n', 0, m.start()) for m in reruns}) == 1, 'connectivity reruns'
    at = reruns[-1].end()
    ch = ch[:at] + f' Rerun with C1 (receipt {rid}), it counts {apart} of {spine}, none in `Becoming.Exclusion`.' + ch[at:]
    (ROOT / CHAPTER).write_text(ch, encoding='utf-8')
    print('edited', CHAPTER)
    # ------------------------------------------------------------ DELEGATED-CHOICES D44
    rec = '../../../../theories/becoming/results/records/what-taking-all-excludes.md'
    words = ('“alright, generally agree, please make your own pareto frontier decisions, and push the frontier - words are '
             'important, but i think you are capable”')
    d43_en = (
        '<a id="d44-取尽所给所排除的--what-taking-all-that-is-given-excludes"></a>\n'
        '### What taking all that is given excludes\n\n'
        f'**Decision.** Adopted with exact scope (C1, [record]({rec}), [study section {sec}]'
        f'(BECOMING-RENEWAL-READING.md#{anchor})). (1) Ending another serves taking all that is given, not continuing as '
        'such: alongside a full taker that continues, a formation living by taking from the condition ends '
        '(`Flow.continuing_ends_taker`), while the same members continue together where each takes within what is '
        'given (`Excluding.three_courses`). The open item “a witness in which ending another serves the clearer\'s '
        'continuation” is met only for a full taker. (2) The extent derived from the first\'s want does not separate the '
        'excluding from the sharing course: in both, the first is active and supported at every step. What separates '
        'them is the second\'s continuation, which the continuation condition counts (section 6.15 of the chapter) and '
        'the first\'s derived extent does not reach. (3) A comparison of courses by admission (retaining, D13; the '
        'margin) does not register an ending through exclusion from taking: the levels of the excluding course admit '
        'the second at every step while it ends (`Excluding.admission_alike`). So the full taker\'s taking is not read '
        'as harmless because the levels retain what has significance: the loss is the member\'s continuation, which no '
        'comparison by inclusion licenses (D14). Declined: (a) reading the excluding course as serving the first\'s '
        'continuation apart from its full taking; (b) reading retaining by admission as not harm where an ending acts '
        'through taking; (c) reading taking all as a case of the meta-attractor, a term of Ren\'s corpus, which needs a '
        'law of how taking all forms. The name “competitive exclusion” is the ecological principle\'s, adopted for the '
        'law of `Flow.continuing_excludes` with this scope.\n'
        '**Reasons.** (1) and (2) are the theorems; (3) is the witness, and D14 already counts a member\'s ending as a '
        'loss. The declined readings would add a premise (a), drop a loss the theorem shows (b), or extend Ren\'s term '
        '(c).\n'
        '**What would change it.** A comparison of courses that registers endings through taking (on the flow, not the '
        'levels); a law of how taking all that is given forms.\n\n')
    d43_zh = (
        '<a id="d44-取尽所给所排除的--what-taking-all-that-is-given-excludes"></a>\n'
        '### D44. 取尽所给所排除的\n\n'
        f'所在：理论第 6.7 节“What taking all that is given excludes”一条；[what-taking-all-excludes]({rec}) 的读法；'
        f'研究第 {sec} 节。\n\n'
        '**决定。** 以确切范围采用。一、终结他者服务于取尽所给，而不是延续本身：在持续的取尽者旁，以从该条件取用为生的形成终结'
        '（`Flow.continuing_ends_taker`），而各在所给之内取用时，同样的成员一同持续（`Excluding.three_courses`）。开放项“终结他者'
        '服务于清除者延续的见证”只对取尽者成立。二、由第一个的想要推出的范围不区分排除的进程与分享的进程：两者中第一个每步都活跃且'
        '被支持。区分它们的是第二个的延续，延续条件计入它（本章第 6.15 节），第一个推出的范围不及于它。三、以容纳比较进程（保留，'
        'D13；余量）不记下经由被排除于取用之外的终结：排除的进程中水平每步都容纳第二个，而它终结（`Excluding.admission_alike`）。'
        '所以不因水平保留了有意义者而把取尽者的取用读作无损：损失是该成员的延续，任何以包含的比较都不许可它（D14）。不采用：（a）'
        '把排除的进程读作离开取尽所给也服务于第一个的延续；（b）在终结经由取用起作用之处，把以容纳读的保留读作不损；（c）把取尽所给'
        '读作元吸引子的情形——那是 Ren 语料中的术语，且需要取尽所给如何形成的定律。“竞争排除”之名取自生态学原理，以此范围用于 '
        '`Flow.continuing_excludes` 的定律。\n'
        '**理由。** 一与二是定理；三是见证，D14 已把成员的终结算作损失。不采用的读法会加前提（a），丢掉定理所示的损失（b），或扩展 '
        'Ren 的术语（c）。\n'
        '**会改变它的。** 记下经由取用之终结的进程比较（在流上，而不是在水平上）；取尽所给如何形成的定律。\n\n')
    sec4 = '<a id="4-不用公理的路线反馈与所及--the-route-without-axiom-feedback-and-reach"></a>\n'
    edit(RF + 'DELEGATED-CHOICES.md', [
        ('| D43 | the other pending readings (18 October) | taken by Ren on the decision brief\'s recommendations: kept, '
         'narrowed, weakened or revised, item by item |\n',
         '| D43 | the other pending readings (18 October) | taken by Ren on the decision brief\'s recommendations: kept, '
         'narrowed, weakened or revised, item by item |\n'
         '| D44 | what taking all that is given excludes | adopted with exact scope: ending another serves taking all, not '
         'continuing; admission does not register it |\n'),
        (sec4, d43_en + sec4),
    ])
    append(RF + 'DELEGATED-CHOICES.md',
           f'- Ren\'s words of 18 October 2026, {words}, read as also delegating the choice of the next items: C1 and its '
           f'reading, D44 ([study section {sec}](BECOMING-RENEWAL-READING.md#{anchor})).')
    edit(RF + 'DELEGATED-CHOICES.zh.md', [
        ('| D43 | 其余的待决读法（10-18） | 由 Ren 依决定简报的建议取：逐项保留、收窄、减弱或修订 |\n',
         '| D43 | 其余的待决读法（10-18） | 由 Ren 依决定简报的建议取：逐项保留、收窄、减弱或修订 |\n'
         '| D44 | 取尽所给所排除的 | 以确切范围采用：终结他者服务于取尽所给，而非延续；容纳不记下它 |\n'),
        (sec4, d43_zh + sec4),
    ])
    append(RF + 'DELEGATED-CHOICES.zh.md', f'- Ren 2026-10-18 的话，{words}，也读作交托下一项的选择：C1 及其读法 D44（研究第 {sec} 节）。')
    # ------------------------------------------------------------ the record derived-extent-limits
    p = ROOT / 'theories/becoming/results/records/derived-extent-limits.json'
    d = json.loads(p.read_text())
    old_next = dict(d['next_delta'])
    a_en = ("a witness where ending another serves the clearer's continuation (a stronger case of the meta-attractor); "
            'forced endings (quantifying over active);')
    b_en = ('how taking all that is given forms (a stronger case of the meta-attractor); forced endings in these '
            'witnesses (quantifying over active);')
    a_zh = '终结他者服务于清除者延续的见证（元吸引子的更强情形）；强制形式的终结（对 active 量化）；'
    b_zh = '取尽所给如何形成（元吸引子的更强情形）；这些见证中强制形式的终结（对 active 量化）；'
    assert d['next_delta']['en'].count(a_en) == 1 and d['next_delta']['zh'].count(a_zh) == 1, d['next_delta']
    d['next_delta'] = {'en': d['next_delta']['en'].replace(a_en, b_en), 'zh': d['next_delta']['zh'].replace(a_zh, b_zh)}
    assert all(x['id'] != 'what-taking-all-excludes' for x in d['related'])
    d['related'].append({
        'id': 'what-taking-all-excludes',
        'detail': {'en': 'Here a clearer meeting every requirement derived from its want still ends a dweller, the ending '
                         'stipulated; there ending another serves taking all that is given, not continuing as such, and '
                         'the ending of a formation living by taking alongside a full taker is derived.',
                   'zh': '这里满足由其想要推出的每项要求的清除者仍终结栖居者，终结是规定的；那里终结他者服务于取尽所给，而不是延续本身，'
                         '在取尽者旁以取用为生的形成的终结是推出的。'}})
    d['history'].append({
        'en': '18 October 2026, C1 (Becoming.Exclusion): the witness where ending another serves the clearer\'s '
              'continuation is stated in what-taking-all-excludes (it serves taking all that is given, not continuing as '
              'such, and the ending of a formation living by taking alongside a full taker is derived), so the next step '
              'was narrowed and the record linked. Before: next step "' + old_next['en'] + '". The claim is unchanged.',
        'zh': '2026年10月18日，C1（Becoming.Exclusion）：终结他者服务于清除者延续的见证已在 what-taking-all-excludes 中陈述（它服务于'
              '取尽所给，而不是延续本身；在取尽者旁以取用为生的形成的终结是推出的），所以下一步收窄并链接该记录；原文见英文。论断不变。'})
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print('edited', p.relative_to(ROOT))


if __name__ == '__main__':
    if sys.argv[1] == 'package':
        package()
    elif sys.argv[1] == 'text':
        text_phase(*sys.argv[2:6])
    else:
        sys.exit(__doc__)
