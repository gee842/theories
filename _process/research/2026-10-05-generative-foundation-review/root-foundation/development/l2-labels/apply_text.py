#!/usr/bin/env python3
"""L2 (Becoming.Labels) landing edits. Every edit must match exactly once.

usage (from the repository root):
  python3 -B apply_text.py package                          copy the module in; import, doc bullet, CORE entry, scope
                                                             sentences, README row
  python3 -B apply_text.py text RECEIPT BASE AFTER APART    study, chapter (bullet, D40 reading, section 8.2, section 9),
                                                             DELEGATED-CHOICES D40, the L1 record
RECEIPT is the core checker run, BASE the main commit it ran on, AFTER what BASE adds to the last landing (for the
receipt sentence, e.g. "after G3, `Becoming.LawAlongRun`"), APART the connectivity check's count of spine theorems
apart; the section 9 counts are read from the receipt itself."""
import json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
SR = '../../../' + STUDY
MOD = f'../../../{PKG}/Becoming/Labels.lean'
REC = '../results/records/what-finitely-many-labels-fix.md'
L1REC = '../results/records/what-an-extrapolation-given-nothing-fixes.md'


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


SCOPE_LEARNING = (
    '    "Unrolling: given nothing, a prefix fixes the whole future through the map in every world a list "\n'
    '    "holds: unrolled on its own proposals, the extrapolation by elimination over the lasso candidates "\n'
    '    "proposes the value through the map at every step ahead from the identification bound on; a "\n'
    '    "feature is learnable exactly where it is, from some step on, a reading of that future, and given "\n'
    '    "nothing no extrapolation learns every learnable feature. "\n'
    '    "Labels: in a world a list of N holds, a feature is learnable through the map exactly where the "\n'
    '    "extrapolation given some table of at most N labelled names of N - 1 values learns it, the table "\n'
    '    "of the world being one; every value the feature takes once that extrapolation rests is a label; "\n'
    '    "where the map also carries the feature, the extrapolation given nothing learns it and the labels "\n'
    '    "before the bound fix every later one. "\n')
SCOPE_SEEKING = (
    '    "Enough: under an undetermined law some run comes to rest with its target met exactly where a "\n'
    '    "reachable configuration stays and meets it, and every run does exactly where every reachable "\n'
    '    "configuration with a step that stays meets it and every run settles; under a determined law the "\n'
    '    "two are one. "\n'
    '    "Settling: in a world a list holds, some run keeps changing exactly where a reachable change can "\n'
    '    "be undone; not changing for ever is not settling, which is the limited principle of omniscience "\n'
    '    "already for two configurations. "\n'
    '    "LastChange: along a run a list of N holds, with no change within a loop, there are fewer than N "\n'
    '    "changes, and with decidable configurations the run is not not settled; settling every run from a "\n'
    '    "configuration with no reachable change that can be undone, for every process of decidable "\n'
    '    "configurations in a world a list holds, is exactly the limited principle of omniscience, and "\n'
    '    "with it assured enough is every reachable stay meeting the target and no reachable change "\n'
    '    "undoable. "\n')


def package():
    shutil.copyfile(HERE / 'Becoming/Labels.lean', ROOT / PKG / 'Becoming/Labels.lean')
    print('copied Becoming/Labels.lean')
    edit(f'{PKG}/Becoming.lean', [
        ('import Becoming.Unrolling\n', 'import Becoming.Unrolling\nimport Becoming.Labels\n'),
        ('  of that future, and the extrapolation given the reading learns it; given nothing, no\n'
         '  extrapolation learns every learnable feature.\n',
         '  of that future, and the extrapolation given the reading learns it; given nothing, no\n'
         '  extrapolation learns every learnable feature.\n'
         '* `Becoming.Labels` (L4): what finitely many labelled names fix, with no premise beyond a list.\n'
         '  The extrapolation given a table of labelled names (a name a finite future through the map, a\n'
         '  label a value of the feature) unrolls the extrapolation given nothing and proposes the label of\n'
         '  the first name its proposed future begins with. In a world a list of `N` holds, the table of\n'
         '  the `N` configurations, each named by `N - 1` values, learns every learnable feature, so a\n'
         '  feature is learnable exactly where the extrapolation given some table of at most `N` names of\n'
         '  `N - 1` values learns it; its labels include every value the feature takes once it rests.\n'
         '  Where the map also carries the feature, the labels before the bound fix every later one.\n'),
    ])
    edit(f'{PKG}/check_becoming.py', [
        ('"Becoming.Unrolling", "Becoming.ParityReadings"', '"Becoming.Unrolling", "Becoming.Labels", "Becoming.ParityReadings"'),
        ('    "learnable along every run exactly where runs beginning alike have targets that agree from "\n'
         '    "some step on. "\n',
         '    "learnable along every run exactly where runs beginning alike have targets that agree from "\n'
         '    "some step on. "\n' + SCOPE_LEARNING),
        ('    "SeekingRuns: the boundary of enough on the unfolding. "\n',
         '    "SeekingRuns: the boundary of enough on the unfolding. "\n' + SCOPE_SEEKING),
    ])
    readme = f'{PKG}/README.md'
    text = (ROOT / readme).read_text(encoding='utf-8')
    row = next(line for line in text.split('\n') if line.startswith('| L4 | [`Becoming.Unrolling`]'))
    new_row = ('| L4 | [`Becoming.Labels`](Becoming/Labels.lean) | What finitely many labelled names fix (no premise beyond '
               'a list): the extrapolation given a table of labelled names, a name a finite future through the map and a '
               'label a value of the feature, unrolls the extrapolation given nothing and proposes the label of the first '
               'name its proposed future begins with (`Learnable.byTable`); in a world a list of `N` holds, where '
               'configurations with the same future through the map have features agreeing from some step on, the table '
               'of the `N` configurations as many steps on as the list is long, each named by its first `N - 1` values '
               '(Moore\'s bound) and labelled with its feature, rests in accord with the feature from the bound of the '
               'extrapolation given nothing on (`Learnable.table_rests`); so a feature is learnable exactly where the '
               'extrapolation given some table of at most `N` labelled names of `N - 1` values learns it '
               '(`Learnable.learnable_iff_table`); every value the feature takes once it rests is a label '
               '(`Learnable.label_of_rests`, `Learnable.labels_of_still`); where the map also carries the feature, the '
               'extrapolation given nothing learns it and the labels before the bound fix every later one '
               '(`Learnable.rests_with_labels`, `Learnable.ahead_with_labels`); the same along the runs of the law '
               '(`LearnableRuns.table_rests`, `LearnableRuns.learnable_iff_table`, `LearnableRuns.labels_of_still`, '
               '`LearnableRuns.rests_with_labels`, `LearnableRuns.ahead_with_labels`) '
               '([what-finitely-many-labels-fix](../../../../../../theories/becoming/results/records/'
               'what-finitely-many-labels-fix.md)). |')
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
        'labels': int(mods['Becoming.Labels']['theorems']),
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
    assert c['labels'] == 20, c['labels']
    spine = n(c['spine'])
    # ------------------------------------------------------------ study
    study = (ROOT / STUDY).read_text(encoding='utf-8')
    sec = max(int(x) for x in re.findall(r'^## (\d+)\. ', study, re.M)) + 1
    body = (HERE / 'study_l2.txt').read_text(encoding='utf-8')
    body = body.replace('{N}', str(sec)).replace('{RECEIPT}', rid).replace('{APART}', apart).replace('{SPINE}', spine)
    marker = '## Ren’s words quoted in passages that exist only in the Chinese edition'
    assert study.count(marker) == 1
    study = study.replace(marker, body.rstrip('\n') + '\n\n' + marker)
    (ROOT / STUDY).write_text(study, encoding='utf-8')
    print('study section', sec)
    anchor = f'{sec}-what-finitely-many-labels-fix-l2'
    # ------------------------------------------------------------ chapter
    ch = (ROOT / CHAPTER).read_text(encoding='utf-8')
    bullet = next(line for line in ch.split('\n') if line.startswith('- *Given nothing, not every learnable target.*'))
    new_bullet = (
        f'- *What finitely many labels fix* ([Becoming.Labels]({MOD}), [what-finitely-many-labels-fix]({REC})). A table '
        'of labelled names is finite: a name is a finite future through the map, as `Law.name` writes it, and a label '
        'is a value of the feature. The extrapolation given a table unrolls the extrapolation given nothing and '
        'proposes the label of the first name its proposed future begins with (`Learnable.byTable`). It is given '
        'neither the configurations, nor how many there are, nor the law. In a world a list of N holds, take each '
        'configuration as many steps on as the list is long, name it by its first N − 1 values through the map '
        '(Moore\'s bound, `Law.sameFuture_iff_within`) and label it with its feature. This table of the world rests in '
        'accord with every learnable feature from the bound of the extrapolation given nothing on '
        '(`Learnable.table_rests`). So a feature is learnable exactly where the extrapolation given some table of at '
        'most N labelled names of N − 1 values learns it (`Learnable.learnable_iff_table`). Every value the feature '
        'takes once it rests is a label (`Learnable.label_of_rests`). Where the map also carries the feature, the '
        'extrapolation given nothing learns it, and the labels before the bound fix every later one '
        '(`Learnable.rests_with_labels`, `Learnable.ahead_with_labels`). The same holds along the runs of the law '
        '(`LearnableRuns.table_rests`, `LearnableRuns.learnable_iff_table`, `LearnableRuns.labels_of_still`, '
        '`LearnableRuns.rests_with_labels`, `LearnableRuns.ahead_with_labels`).')
    pairs = [
        (bullet + '\n', bullet + '\n' + new_bullet + '\n'),
        # the reading D40, extended
        (f'over every course, no prefix fixes the next value. Record: [what-an-extrapolation-given-nothing-fixes]({L1REC}). '
         f'Study: [section 173]({SR}#173-what-an-extrapolation-given-nothing-fixes-l1).',
         'over every course, no prefix fixes the next value. That reading is a finite object: at most N labelled names '
         'of N − 1 values, whose labels are values the feature takes. Records: '
         f'[what-an-extrapolation-given-nothing-fixes]({L1REC}), [what-finitely-many-labels-fix]({REC}). Study: '
         f'[section 173]({SR}#173-what-an-extrapolation-given-nothing-fixes-l1), [section {sec}]({SR}#{anchor}).'),
        # section 8.2, Learning
        ('learning a target from finitely many of its values, given part of a reading of the future rather than the '
         'whole (given nothing, no learner rests on every learnable target; a target is learnable exactly where it is, '
         'from some step on, a reading of the future through the map, which the prefix fixes given nothing: '
         '`Becoming.Unrolling`); ',
         'a table of labelled names found rather than given, and whether fewer than N names of N − 1 values can be '
         'enough (given nothing, no extrapolation rests in accord with every learnable feature; a feature is learnable '
         'exactly where it is, from some step on, a reading of the future through the map, which the prefix fixes '
         'given nothing: `Becoming.Unrolling`; that reading is at most N labelled names of N − 1 values, and where the '
         'map carries the feature the labels before the bound fix every later one: `Becoming.Labels`); '),
        (f'[what-an-extrapolation-given-nothing-fixes]({L1REC}) |',
         f'[what-an-extrapolation-given-nothing-fixes]({L1REC}), [what-finitely-many-labels-fix]({REC}) |'),
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
                 f'It was checked with Lean 4.29.1 on main {base} ({after}) with L2 (`Becoming.Labels`, '
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
    ch = ch[:at] + f' Rerun with L2 (receipt {rid}), it counts {apart} of {spine}, none in `Becoming.Labels`.' + ch[at:]
    (ROOT / CHAPTER).write_text(ch, encoding='utf-8')
    print('edited', CHAPTER)
    # ------------------------------------------------------------ DELEGATED-CHOICES D40, extended with L2
    rec = '../../../../theories/becoming/results/records/what-finitely-many-labels-fix.md'
    edit(RF + 'DELEGATED-CHOICES.md', [
        ('| D40 | what an extrapolation given nothing fixes | adopted with exact scope: worlds a list holds; a reading is '
         'a function, not a model held |',
         '| D40 | what an extrapolation given nothing fixes | adopted with exact scope: worlds a list holds; a reading is '
         'a function, not a model held; extended with L2 |'),
        ('**What would change it.** A form of the fixing beyond worlds a list holds (for instance with a bound on what is '
         'registered); a better name than `reading`.\n',
         '**What would change it.** A form of the fixing beyond worlds a list holds (for instance with a bound on what is '
         'registered); a better name than `reading`.\n\n'
         f'**Extended with L2 (18 October 2026, `Becoming.Labels`, [record]({rec}), [study section {sec}]'
         f'(BECOMING-RENEWAL-READING.md#{anchor})).** The reading is a finite object. In a world a list of N holds, the '
         'extrapolation given at most N labelled names learns every learnable feature: each name is a future of N − 1 '
         'values through the map, each label a value of the feature. So a feature is learnable exactly where some such '
         'table learns it (`Learnable.table_rests`, `Learnable.learnable_iff_table`). Its labels include every value '
         'the feature takes once it rests (`Learnable.label_of_rests`). Where the map also carries the feature, the '
         'labels before the bound fix every later one (`Learnable.ahead_with_labels`). Read: what the prefix does not '
         'supply is finitely many values of the feature, attached to names. The table is still given, not found, and '
         'is not read as a model a formation holds (declined reading (2) stands). Adopted with the same scope; decided '
         'by the AI on the same words of Ren.\n'),
    ])
    edit(RF + 'DELEGATED-CHOICES.zh.md', [
        ('| D40 | 不被给予任何东西的外推所确定者 | 以确切范围采用：由一个列表容纳的世界；读法是函数，不是被持有的模型 |',
         '| D40 | 不被给予任何东西的外推所确定者 | 以确切范围采用：由一个列表容纳的世界；读法是函数，不是被持有的模型；以 L2 扩展 |'),
        ('**会改变它的。** 在列表容纳的世界之外的确定形式（例如对所识者给一个界）；比 `reading` 更好的名称。\n',
         '**会改变它的。** 在列表容纳的世界之外的确定形式（例如对所识者给一个界）；比 `reading` 更好的名称。\n\n'
         f'**以 L2 扩展（2026-10-18，`Becoming.Labels`，[记录]({rec})，研究第 {sec} 节）。** 读法是有限的对象。在由 N 个构形的'
         '列表容纳的世界中，被给予至多 N 个带标签名字的外推学得每个可学特征：每个名字是 N − 1 个经映射之值的未来，每个标签是特征的'
         '一个值。所以一个特征可学，恰当某张这样的表学得它（`Learnable.table_rests`、`Learnable.learnable_iff_table`）。其标签含'
         '特征在它静止后所取的每个值（`Learnable.label_of_rests`）。映射也带着特征之处，界之前的标签确定此后的每一个'
         '（`Learnable.ahead_with_labels`）。读作：前缀不提供的，是附在名字上的有限多个特征之值。表仍是被给予的，不是找到的，'
         '也不读作某个构成所持有的模型（不采用的读法（2）仍成立）。以同样的范围采用；由 AI 依 Ren 的同一段话决定。\n'),
    ])
    # ------------------------------------------------------------ the L1 record: what L2 now states
    p = ROOT / 'theories/becoming/results/records/what-an-extrapolation-given-nothing-fixes.json'
    d = json.loads(p.read_text())
    old_dns = d['does_not_show'][1]['en']
    old_next = d['next_delta']['en']
    assert old_dns.startswith('Learning a feature from finitely many of its values;'), old_dns
    assert old_next.startswith('Learning from finitely many values of the feature'), old_next
    d['does_not_show'][1] = {
        'en': 'Undetermined processes; rates beyond the stated bound (learning from finitely many labelled values of the '
              'feature is in what-finitely-many-labels-fix).',
        'zh': '不确定的过程；超出所述之界的速率（从特征的有限多个带标签的值学习，见 what-finitely-many-labels-fix）。',
        'kind': 'scope'}
    d['next_delta'] = {'en': 'An extrapolation that finds the reading, or a table of it; an independent review.',
                       'zh': '找到读法或其表的外推；独立审查。'}
    d['history'].append({
        'en': '18 October 2026, L2 (Becoming.Labels): learning from finitely many values of the feature is stated in '
              'what-finitely-many-labels-fix, and the enough of seeking under undetermined laws landed as S1 '
              '(the-boundary-of-enough-under-undetermined-laws), so one item of does_not_show and the next step were '
              'narrowed. Before: does_not_show "' + old_dns + '"; next step "' + old_next + '". The claim is unchanged.',
        'zh': '2026年10月18日，L2（Becoming.Labels）：从特征的有限个值学习已在 what-finitely-many-labels-fix 中陈述，不确定律下'
              '寻求之足够已作为 S1 落地（the-boundary-of-enough-under-undetermined-laws），所以“未表明”的一项与下一步收窄；'
              '原文见英文。论断不变。'})
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print('edited', p.relative_to(ROOT))


if __name__ == '__main__':
    if sys.argv[1] == 'package':
        package()
    elif sys.argv[1] == 'text':
        text_phase(*sys.argv[2:6])
    else:
        sys.exit(__doc__)
