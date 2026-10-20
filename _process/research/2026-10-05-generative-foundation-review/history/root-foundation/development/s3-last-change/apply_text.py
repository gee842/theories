#!/usr/bin/env python3
"""S3 (Becoming.LastChange) landing edits. Every edit must match exactly once.

usage (from the repository root):
  python3 -B apply_text.py package                      copy the module in; import, doc bullet, CORE entry, README row
  python3 -B apply_text.py text RECEIPT BASE APART      study, chapter (bullet, section 8.2, readings, section 9),
                                                         DELEGATED-CHOICES D42, the S2 record, the board row
RECEIPT is the core checker run, BASE the main commit it ran on, APART the connectivity check's count of spine
theorems apart; the section 9 counts are read from the receipt itself."""
import json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
SR = '../../../' + STUDY
MOD = f'../../../{PKG}/Becoming/LastChange.lean'
REC = '../results/records/the-last-change-of-a-run.md'


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


def package():
    shutil.copyfile(HERE / 'Becoming/LastChange.lean', ROOT / PKG / 'Becoming/LastChange.lean')
    print('copied Becoming/LastChange.lean')
    edit(f'{PKG}/Becoming.lean', [
        ('import Becoming.Settling\n', 'import Becoming.Settling\nimport Becoming.LastChange\n'),
        ('  settling: in a process of two configurations, every run settling is the limited principle of\n'
         '  omniscience.\n',
         '  settling: in a process of two configurations, every run settling is the limited principle of\n'
         '  omniscience.\n'
         '* `Becoming.LastChange` (L4): how often a run changes and what it takes to know it has stopped,\n'
         '  with no premise beyond a list, and decidable configurations, where stated. Along a run a list of\n'
         '  `N` holds, with no change within a loop, there are fewer than `N` changes; such a run settles\n'
         '  exactly where, at every step, whether it changes again is decided, and with decidable\n'
         '  configurations it is not not settled. With the limited principle of omniscience it settles, and\n'
         '  that every run with no reachable change that can be undone settles, for every process of\n'
         '  decidable configurations in a world a list holds, is exactly that principle. With it, assured\n'
         '  enough is every reachable stay meeting the target and no reachable change undoable.\n'),
    ])
    edit(f'{PKG}/check_becoming.py', [('"Becoming.Settling", ', '"Becoming.Settling", "Becoming.LastChange", ')])
    readme = f'{PKG}/README.md'
    text = (ROOT / readme).read_text(encoding='utf-8')
    row = next(line for line in text.split('\n') if line.startswith('| L4 | [`Becoming.Settling`]'))
    new_row = ('| L4 | [`Becoming.LastChange`](Becoming/LastChange.lean) | How often a run changes and what it takes to know '
               'it has stopped (no premise beyond a list, and decidable configurations, where stated): along a run a '
               'list of `N` holds, with no change within a loop, there are fewer than `N` changes (`LastChange.changes_lt`, '
               'through `LastChange.atChanges`); such a run settles where at every step it is decided whether it changes '
               'again, with decidable configurations exactly (`LastChange.settles_of_decided`, '
               '`LastChange.settles_iff_decided`), and with decidable configurations alone it is not not settled '
               '(`LastChange.not_not_settles`); with `LPO` it settles, and in a world a list holds every run from a '
               'configuration with no reachable undoable change settles (`LastChange.settles_of_lpo`, '
               '`LastChange.settles_of_no_undoable`); that this holds for every process of decidable configurations in '
               'such a world is exactly `LPO` (`LastChange.lpo_iff_settles`, through `Settling.OneWay`); with `LPO`, '
               'assured enough is every reachable stay meeting the target and no reachable change undoable '
               '(`LastChange.assured_iff_of_lpo`), and with decided configurations alone each run then does not not '
               'rest (`LastChange.not_not_rests`) ([the-last-change-of-a-run](../../../../../../theories/becoming/'
               'results/records/the-last-change-of-a-run.md)). |')
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
        'lastchange': int(mods['Becoming.LastChange']['theorems']),
    }


def n(x):
    return f'{x:,}'


def text_phase(rid, base, apart):
    c = receipt_counts(rid)
    assert c['lastchange'] == 20, c['lastchange']
    spine = n(c['spine'])
    # ------------------------------------------------------------ study
    study = (ROOT / STUDY).read_text(encoding='utf-8')
    sec = max(int(x) for x in re.findall(r'^## (\d+)\. ', study, re.M)) + 1
    body = (HERE / 'study_s3.txt').read_text(encoding='utf-8')
    body = body.replace('{N}', str(sec)).replace('{RECEIPT}', rid).replace('{APART}', apart).replace('{SPINE}', spine)
    marker = '## Ren’s words quoted in passages that exist only in the Chinese edition'
    assert study.count(marker) == 1
    study = study.replace(marker, body.rstrip('\n') + '\n\n' + marker)
    (ROOT / STUDY).write_text(study, encoding='utf-8')
    print('study section', sec)
    anchor = f'{sec}-the-last-change-of-a-run-s3'
    # ------------------------------------------------------------ chapter
    ch = (ROOT / CHAPTER).read_text(encoding='utf-8')
    bullet = next(line for line in ch.split('\n') if line.startswith('- *When the runs settle*'))
    new_bullet = (
        f'- *The last change* ([Becoming.LastChange]({MOD}), [the-last-change-of-a-run]({REC})). Along a run a list of '
        'N configurations holds, with no change within a loop, there are fewer than N changes '
        '(`LastChange.changes_lt`). Such a run settles exactly where, at every step, it is decided whether it changes '
        'again (`LastChange.settles_iff_decided`, with decidable configurations), and with no premise beyond decidable '
        'configurations it is not not settled (`LastChange.not_not_settles`). With the limited principle of '
        'omniscience it settles, and in a world a list holds every run from a configuration with no reachable change '
        'that can be undone settles; that this holds for every process of decidable configurations in such a world is '
        'exactly the limited principle of omniscience (`LastChange.settles_of_no_undoable`, '
        '`LastChange.lpo_iff_settles`). With that principle, every run from a configuration comes to rest with its '
        'target met exactly where every reachable configuration with a step that stays meets the target and no '
        'reachable change can be undone (`LastChange.assured_iff_of_lpo`).')
    pairs = [
        (bullet + '\n', bullet + '\n' + new_bullet + '\n'),
        ('whether, with the limited principle of omniscience, no reachable change that can be undone gives settling '
         '(possible and assured enough under undetermined laws: `Becoming.Enough`; in a world a list holds, some run '
         'keeps changing exactly where a reachable change can be undone, while every run settling needs `LPO` already '
         'for two configurations: `Becoming.Settling`); ',
         'settling decided under a premise the core accepts, short of the limited principle of omniscience (possible '
         'and assured enough under undetermined laws: `Becoming.Enough`; in a world a list holds, some run keeps '
         'changing exactly where a reachable change can be undone: `Becoming.Settling`; with no such change a run '
         'changes fewer than N times and, with decidable configurations, is not not settled, and every such run '
         'settling, for every process of decidable configurations, is exactly `LPO`: '
         '`Becoming.LastChange`); '),
        ('[when-the-runs-of-a-process-settle](../results/records/when-the-runs-of-a-process-settle.md), '
         '[target-capture](../results/records/target-capture.md)',
         '[when-the-runs-of-a-process-settle](../results/records/when-the-runs-of-a-process-settle.md), '
         f'[the-last-change-of-a-run]({REC}), [target-capture](../results/records/target-capture.md)'),
        ('but knowing that a run will not change for ever is not knowing when it has stopped. Records: '
         '[the-boundary-of-enough-under-undetermined-laws](../results/records/the-boundary-of-enough-under-undetermined-'
         'laws.md), [when-the-runs-of-a-process-settle](../results/records/when-the-runs-of-a-process-settle.md). Study: '
         f'[section 174]({SR}#174-the-boundary-of-enough-under-undetermined-laws-s1), [section 175]({SR}#175-when-the-'
         'runs-of-a-process-settle-s2).',
         'but knowing that a run will not change for ever is not knowing when it has stopped: the count of its changes '
         'is bounded, the step of its last change is not. Records: [the-boundary-of-enough-under-undetermined-laws]'
         '(../results/records/the-boundary-of-enough-under-undetermined-laws.md), [when-the-runs-of-a-process-settle]'
         f'(../results/records/when-the-runs-of-a-process-settle.md), [the-last-change-of-a-run]({REC}). Study: '
         f'[section 174]({SR}#174-the-boundary-of-enough-under-undetermined-laws-s1), [section 175]({SR}#175-when-the-'
         f'runs-of-a-process-settle-s2), [section {sec}]({SR}#{anchor}).'),
        ('the [theorem-connectivity measure](../../../_process/research/2026-10-05-generative-foundation-review/'
         'root-foundation/THEOREM-CONNECTIVITY.md#7-落地头上的重跑--the-rerun-on-the-landing-head) still finds 1,019 of '
         'the 7,214 spine theorems apart from both base families (§8.2, Integration of the spine).',
         'the [theorem-connectivity measure](../../../_process/research/2026-10-05-generative-foundation-review/'
         'root-foundation/THEOREM-CONNECTIVITY.md#9-u2-the-periphery-measured-and-joined), rerun on each landing, '
         f'finds {apart} of the {spine} spine theorems apart from both base families at the last rerun (§8.2, '
         'Integration of the spine).'),
        ('129 modules counting the root `Becoming`, and 132 in the core closure with the foundation',
         f'{c["core"][0]} modules counting the root `Becoming`, and {c["closure"][0]} in the core closure with the '
         'foundation'),
    ]
    for old, new in pairs:
        k = ch.count(old)
        if k != 1:
            sys.exit(f'chapter: expected one match, found {k}: {old[:100]!r}')
        ch = ch.replace(old, new)
    start = ch.index('**The current receipt.**')
    end = ch.index('Further facts about the receipt:', start)
    para = ch[start:end]
    old_rid = re.search(r'is run `([0-9TZ.]+)`', para).group(1)
    para = para.replace(old_rid, rid)
    para, k = re.subn(r'It was checked with Lean 4\.29\.1 on main \S+ (?:\(.*?\) )?with .*? in the working tree, and it passed\.',
                      f'It was checked with Lean 4.29.1 on main {base} (after G2, `Becoming.SelectionReach`, and the S3 and G3 claims) with S3 '
                      f'(`Becoming.LastChange`, [study §{sec}]({SR}#{anchor})) in the working tree, and it passed.', para)
    assert k == 1, 'receipt sentence'
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
    m = list(re.finditer(r'Rerun with G2 \(receipt [^)]*\), it counts [\d,]+ of [\d,]+, none in `Becoming\.SelectionReach`\.', ch))
    assert len(m) == 1, 'G2 connectivity sentence'
    at = m[0].end()
    ch = ch[:at] + f' Rerun with S3 (receipt {rid}), it counts {apart} of {spine}, none in `Becoming.LastChange`.' + ch[at:]
    (ROOT / CHAPTER).write_text(ch, encoding='utf-8')
    print('edited', CHAPTER)
    # ------------------------------------------------------------ DELEGATED-CHOICES D42, extended with S3
    rec = '../../../../theories/becoming/results/records/the-last-change-of-a-run.md'
    edit(RF + 'DELEGATED-CHOICES.md', [
        ('| D42 | when the runs of a process settle | adopted with exact scope: not changing for ever is not settling; the '
         'analogy with D34 of form only |',
         '| D42 | when the runs of a process settle | adopted with exact scope: not changing for ever is not settling; the '
         'analogy with D34 of form only; extended with S3 |'),
        ('**What would change it.** A constructive settling theorem under a premise the core accepts; a name Ren prefers '
         'for settling.\n',
         '**What would change it.** A constructive settling theorem under a premise the core accepts; a name Ren prefers '
         'for settling.\n\n'
         f'**Extended with S3 (18 October 2026, `Becoming.LastChange`, [record]({rec}), [study section {sec}]'
         f'(BECOMING-RENEWAL-READING.md#{anchor})).** The likeness is now exact in form: along a run a list holds, with '
         'no change within a loop, there are fewer than N changes and, with decidable configurations alone, the run is '
         'not not settled, while settling every run from a configuration with no reachable change that can be undone, '
         'for every process of decidable configurations in a world a list holds, is exactly the limited principle of '
         'omniscience '
         '(`LastChange.not_not_settles`, `LastChange.lpo_iff_settles`). Read: the count of changes is bounded, the step '
         'of the last change is not; knowing that a run will not change again is a question about its whole future. '
         'With that principle, assured enough is stated on the process: every reachable stay meets the target, and no '
         'reachable change can be undone (`LastChange.assured_iff_of_lpo`). Adopted with the same scope; decided by '
         'the AI on the same words of Ren.\n'),
    ])
    edit(RF + 'DELEGATED-CHOICES.zh.md', [
        ('| D42 | 过程的运行何时安定 | 以确切范围采用：不永远变化不是安定；与 D34 的相似只在形式上 |',
         '| D42 | 过程的运行何时安定 | 以确切范围采用：不永远变化不是安定；与 D34 的相似只在形式上；以 S3 扩展 |'),
        ('**会改变它的。** 在核心接受的前提下的构造性安定定理；Ren 对安定更喜欢的名称。\n',
         '**会改变它的。** 在核心接受的前提下的构造性安定定理；Ren 对安定更喜欢的名称。\n\n'
         f'**以 S3 扩展（2026-10-18，`Becoming.LastChange`，[记录]({rec})，研究第 {sec} 节）。** 这一相似现在在形式上是精确的：'
         '沿由列表容纳、在回路之内没有变化的运行，变化少于 N 次；只要构形可判定，运行不是不安定的；而对由一个列表容纳的世界中每个构形可判定的过程，使从没有可达的可撤回变化的构形出发的'
         '每次运行都安定，恰是有限全知原理（`LastChange.not_not_settles`、`LastChange.lpo_iff_settles`）。读作：变化的次数有界，最后一次变化的步'
         '不是；知道一次运行不会再变化，是关于其整个未来的问题。在这一原理之下，确保之够在过程上陈述：每个可达的停留满足目标，'
         '且没有可达的变化可被撤回（`LastChange.assured_iff_of_lpo`）。以同样的范围采用；由 AI 依 Ren 的同一段话决定。\n'),
    ])
    # ------------------------------------------------------------ the S2 record: what S3 now states
    p = ROOT / 'theories/becoming/results/records/when-the-runs-of-a-process-settle.json'
    d = json.loads(p.read_text())
    old_dns = [x['en'] for x in d['does_not_show']]
    old_next = d['next_delta']['en']
    assert old_dns[0].startswith('The positive form: when every run settles.'), old_dns[0]
    assert old_dns[1].startswith('How many times a run changes;'), old_dns[1]
    d['does_not_show'][0] = {
        'en': 'Settling without the limited principle of omniscience: with no reachable undoable change, every run '
              'settling is exactly LPO for every process of decidable configurations in a world a list holds '
              '(the-last-change-of-a-run).',
        'zh': '没有有限全知原理的安定：没有可达的可撤回变化时，对由一个列表容纳的世界中每个构形可判定的过程，每次运行都安定恰是 LPO'
              '（the-last-change-of-a-run）。',
        'kind': 'scope'}
    d['does_not_show'][1] = {
        'en': 'Worlds no list holds, where change can recur without a loop (how many times a run changes within a list '
              'is in the-last-change-of-a-run).',
        'zh': '没有列表容纳的世界，那里变化可无回路而反复出现（列表之内一次运行变化多少次，见 the-last-change-of-a-run）。',
        'kind': 'scope'}
    d['next_delta'] = {'en': 'Settling under a premise the core accepts, short of LPO; an independent review.',
                       'zh': '在核心接受、弱于 LPO 的前提下的安定；独立审查。'}
    d['history'].append({
        'en': '18 October 2026, S3 (Becoming.LastChange): the positive form under LPO and how many times a run changes '
              'are stated in the-last-change-of-a-run, so two items of does_not_show and the next step were narrowed. '
              'Before: does_not_show "' + old_dns[0] + '" and "' + old_dns[1] + '"; next step "' + old_next + '". The '
              'claim is unchanged.',
        'zh': '2026年10月18日，S3（Becoming.LastChange）：LPO 下的正面形式与一次运行变化多少次已在 the-last-change-of-a-run 中陈述，'
              '所以“未表明”的两项与下一步收窄；原文见英文。论断不变。'})
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print('edited', p.relative_to(ROOT))


if __name__ == '__main__':
    if sys.argv[1] == 'package':
        package()
    elif sys.argv[1] == 'text':
        text_phase(*sys.argv[2:5])
    else:
        sys.exit(__doc__)
