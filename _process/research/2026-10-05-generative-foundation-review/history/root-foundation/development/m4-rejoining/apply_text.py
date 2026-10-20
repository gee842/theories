#!/usr/bin/env python3
"""M4 (Becoming.Rejoining) landing edits. Every edit must match exactly once.

usage (from the repository root; M4_ROOT names another checkout to edit, such as a worktree):
  python3 -B apply_text.py package                          copy the module in; import, doc bullet, CORE entry, scope
                                                             sentence, README row
  python3 -B apply_text.py text RECEIPT BASE AFTER APART    study, chapter (sections 3, 7.4, 7.7, 8.2, 8.4, 9, en;
                                                             7.4, 7.7, 8 zh)
RECEIPT is the core checker run, BASE the main commit it ran on, AFTER what BASE adds to the last landing (for the
receipt sentence), APART the connectivity check's count of spine theorems apart; the section 9 counts are read from
the receipt itself."""
import json, os, re, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['M4_ROOT']).resolve() if os.environ.get('M4_ROOT') else HERE.parents[5]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
MODULE = 'Becoming.Rejoining'
THEOREMS, DECLARATIONS = 20, 32


def edit(path, pairs):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    for old, new in pairs:
        k = text.count(old)
        if k != 1:
            sys.exit(f'{path}: expected one match, found {k}: {old[:100]!r}')
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')
    print('edited', path, len(pairs))


DOC_AFTER = ('  separates goes unresponded outside the clearer\'s part; in `Loop` a response returns through the\n'
             '  actor\'s coupling closure.\n')
DOC = (
    '* `Becoming.Rejoining` (L4): where the courses with and without an act rejoin. A difference\n'
    '  between the two courses opens or closes at a condition only across a step at which the two\n'
    '  flows exchange with it differently, and where they rejoin, what they exchanged with it makes up\n'
    '  the gap exactly. Where the rest follows a law reading through its coupling and the part acts\n'
    '  alike after the act, a difference changes only through a formation outside the part that\n'
    '  exchanges with the condition differently and couples the two courses apart; what nothing within\n'
    '  the responsive reach exchanges with stays as it was. In `Replenishing` a responder reading the\n'
    '  level gives back what the act took and the courses rejoin. The course without the act is a\n'
    '  comparison, not a standard.\n')
SCOPE_AFTER = '    "and in Loop a response returns through the actor\'s coupling closure. "\n'
SCOPE = (
    '    "Rejoining: a difference between the courses with and without an act opens or closes at a "\n'
    '    "condition only across a step at which the flows exchange with it differently, and where they "\n'
    '    "rejoin, what they exchanged makes up the gap exactly; where the rest reads through its coupling "\n'
    '    "and the part acts alike after the act, it changes only through a formation outside the part "\n'
    '    "that couples the two courses apart; what nothing within the responsive reach exchanges with "\n'
    '    "stays; in Replenishing a responder reading the level gives back what the act took. "\n')
README_ROW = (
    '| L4 | [`Becoming.Rejoining`](Becoming/Rejoining.lean) | where the courses with and without an act rejoin (no '
    'axiom; balance, the same formations present, the law the rest follows and that it reads through coupling, and the '
    'hypotheses of `Flow.alike_beyond_response` are hypotheses of the theorems): a difference opens or closes at a '
    'condition only across a step at which the two flows exchange with it differently (`Flow.level_alike_succ_iff`, '
    '`Flow.exchange_apart_of_change`, `Flow.formation_apart_of_exchange_apart`); where they rejoin, what they '
    'exchanged makes up the gap exactly (`Flow.level_steps`, `Flow.gap_made_up`); whatever closes it couples the two '
    'courses apart (`Flow.closer_couples_apart`, `Flow.changes_through_coupling_apart`, '
    '`Flow.closes_through_coupling_apart`); beyond the responsive reach a difference stays '
    '(`Flow.stays_beyond_response`); in `Replenishing` a responder gives back what the act took (`Replenishing.closes`, '
    '`Replenishing.made_up`, `Replenishing.closes_through`) ([where-two-courses-rejoin](../../../../../../theories/'
    'becoming/results/records/where-two-courses-rejoin.md)) |')


def package():
    shutil.copyfile(HERE / 'Becoming/Rejoining.lean', ROOT / PKG / 'Becoming/Rejoining.lean')
    print('copied Becoming/Rejoining.lean')
    edit(f'{PKG}/Becoming.lean', [
        ('import Becoming.PoolResponse\n', 'import Becoming.PoolResponse\nimport Becoming.Rejoining\n'),
        (DOC_AFTER, DOC_AFTER + DOC),
    ])
    edit(f'{PKG}/check_becoming.py', [
        ('"Becoming.PoolResponse", ', '"Becoming.PoolResponse", "Becoming.Rejoining", '),
        (SCOPE_AFTER, SCOPE_AFTER + SCOPE),
    ])
    readme = f'{PKG}/README.md'
    text = (ROOT / readme).read_text(encoding='utf-8')
    row = next(line for line in text.split('\n') if line.startswith('| L4 | [`Becoming.PoolResponse`]'))
    edit(readme, [(row + '\n', row + '\n' + README_ROW + '\n')])


CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHAPTER_ZH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
SR = '../../../' + STUDY
MOD = f'../../../{PKG}/Becoming/Rejoining.lean'
REC = '../results/records/where-two-courses-rejoin.md'
RECLINK = f'[where-two-courses-rejoin]({REC})'
M3LINK = '[what-a-pools-acts-respond-to](../results/records/what-a-pools-acts-respond-to.md)'


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
        'own': int(mods[MODULE]['theorems']),
        'ran': len(d['lean_steps']['ran']),
        'reused': len(d['lean_steps']['reused']),
        'own_decls': len(mods[MODULE]['declarations']),
    }


def n(x):
    return f'{x:,}'


def subn1(pattern, repl, text, what):
    text, k = re.subn(pattern, repl, text)
    if k != 1:
        sys.exit(f'{what}: expected one match, found {k}')
    return text


def replace_once(text, old, new, what):
    if text.count(old) != 1:
        sys.exit(f'{what}: expected one match, found {text.count(old)}')
    return text.replace(old, new)


def insert_after_line(text, start, new, what):
    lines = text.split('\n')
    idx = [i for i, line in enumerate(lines) if line.startswith(start)]
    if len(idx) != 1:
        sys.exit(f'{what}: expected one line, found {len(idx)}')
    lines[idx[0] + 1:idx[0] + 1] = new.split('\n')
    return '\n'.join(lines)


def replace_line(text, start, new, what):
    lines = text.split('\n')
    idx = [i for i, line in enumerate(lines) if line.startswith(start)]
    if len(idx) != 1:
        sys.exit(f'{what}: expected one line, found {len(idx)}')
    lines[idx[0]:idx[0] + 1] = new.split('\n')
    return '\n'.join(lines)


# ---------------------------------------------------------------- chapter text, en
# ---------------------------------------------------------------- chapter text, en
SEC3_AFTER = '- *What a pool\'s acts respond to* ('
SEC3 = (
    '- *Where two courses rejoin* ([Becoming.Rejoining]({MOD}), {RECLINK}). A difference between the courses with '
    'and without an act opens or closes at a condition only across a step at which the two flows exchange with it '
    'differently (`Flow.exchange_apart_of_change`), and where the courses rejoin, what they exchanged with it makes up '
    'the gap exactly (`Flow.gap_made_up`). Where the rest follows a law reading through its coupling and the part acts '
    'alike after the act, a difference closes only through a formation outside the part that exchanges with it '
    'differently and couples the two courses apart (`Flow.closes_through_coupling_apart`), and a difference that '
    'nothing within the responsive reach exchanges with stays as it was (`Flow.stays_beyond_response`). In '
    '`Replenishing` a responder that reads the level gives back what the act took (`Replenishing.closes_through`). '
    'The course without the act is a comparison, not a standard. Stated in §7.7. Study: [section {SEC}]({SR}#{ANCHOR}).')
# sentences M3 added, restated without "correct" (Ren, 19 October 2026: "correct? this is a dualist word, are we
# drifting off?")
S74_PAIRS = [
    ('such as a reward, a vote or a correction it gives', 'such as a reward, a vote or a revision it gives'),
    ('and correction and escalation share that structure, a loop through another\'s coupling and response. Which loops '
     'correct is not proved (§7.7). Members correct one another, if at all, through such loops,',
     'and a response that closes the difference an act made and one that widens it share that structure, a loop '
     'through another\'s coupling and response; which of the two a loop does is decided by the laws followed, not by '
     'the loop (§7.7). Members change what one another\'s acts did, if at all, through such loops,'),
]
S77_START = '- **Which responses correct.** A response reaches an actor\'s own act only through the actor\'s coupling'
S77_NEW = (
    '- **What a response does to an act\'s difference.** The course without an act is a comparison, not a standard: '
    'the laws state when the course with the act and the course without it, having parted at a condition, rejoin '
    'there, and do not say that rejoining is better than keeping or widening the difference; which of these supports '
    '生生 goes through the comparison and the condition of §6.15. A difference opens or closes at a condition only '
    'across a step at which the two flows exchange with it differently, and where the courses rejoin, what they '
    'exchanged with it makes up the gap exactly (`Flow.exchange_apart_of_change`, `Flow.gap_made_up`). Where the rest '
    'follows a law reading through its coupling and the acting part acts alike after the act, a difference closes only '
    'through a formation outside the part that exchanges with it differently and couples the two courses apart '
    '(`Flow.closes_through_coupling_apart`): rejoining is a response, through a coupling that carries the difference. '
    'A difference that nothing within the responsive reach exchanges with stays as it was '
    '(`Flow.stays_beyond_response`). In `Replenishing` a responder that reads the level gives back what the act took '
    'and the courses rejoin (`Replenishing.closes_through`); in `Loop` the response ends the actor\'s support instead '
    '(§7.4, `Loop.response_returns`). Which law closes rather than widens a difference, how a member\'s law comes to, '
    'differences at many conditions at once, and members that read one another\'s coupling directly are open (§8.2, '
    '“Selection, causes and experiment”).')
S82_OPEN_OLD = ('.) Which responses to what a pool\'s acts separate correct the act, and how a member\'s law comes to '
                'respond to what it couples into;')
S82_OPEN_NEW = ('.) Which law closes rather than widens a difference a pool\'s acts separate, and how a member\'s law '
                'comes to; differences at many conditions at once;')
S84_OLD = 'with correction and escalation read as one loop through another\'s coupling and response; '
S84_NEW = ('with a response that closes a difference and one that widens it read as one loop through another\'s coupling '
           'and response, the course without the act as a comparison rather than a standard; ')

# ---------------------------------------------------------------- chapter text, zh
S74_ZH_PAIRS = [
    ('例如它给出的奖励、表决或纠正', '例如它给出的奖励、表决或修订'),
    ('纠正与升级共有这一结构，即经他者的耦合与回应的回路。哪些回路纠正，并未证明（§7.7）。成员若互相纠正，也只经这样的回路；',
     '闭合动作所造成之差别的回应与扩大它的回应共有这一结构，即经他者的耦合与回应的回路；回路做哪一种，由所遵从的律决定，不由回路决定'
     '（§7.7）。成员若改变彼此动作所做的，也只经这样的回路；'),
]
S77_ZH_START = '- **哪些回应纠正。** 回应只经行动者的耦合闭包及于其自身的动作'
S77_ZH_NEW = (
    '- **回应对动作之差别做什么。** 无动作的进程是比较，不是标准：这些规律陈述有动作与无动作的两个进程在一个条件处分开之后何时'
    '在那里重合，并不说重合优于保持或扩大差别；其中哪个支持生生，经 §6.15 的比较与条件。差别只在两个流与该条件交换不同的那一步'
    '开合，两个进程重合时，两流与它所交换的恰好补足差距（`Flow.exchange_apart_of_change`，`Flow.gap_made_up`）。其余遵从经其'
    '耦合而读的律、行动部分在动作之后行动相同时，差别只经部分之外、与它交换不同并把两个进程耦合得有别的形成而闭合'
    '（`Flow.closes_through_coupling_apart`）：重合是一种回应，经承载该差别的耦合。回应所及之内无物与之交换的差别保持原样'
    '（`Flow.stays_beyond_response`）。`Replenishing` 中，读取水平的回应者归还动作所取，两个进程重合'
    '（`Replenishing.closes_through`）；`Loop` 中回应反而终结行动者的支持（§7.4，`Loop.response_returns`）。哪个律闭合而非'
    '扩大差别、成员的律如何变成这样、多个条件上同时的差别，以及成员直接读彼此的耦合，仍开放（§8“进一步的证明”）。')
S84_ZH_OLD = '纠正与升级读作同一种经他者耦合与回应的回路；'
S84_ZH_NEW = '闭合差别的回应与扩大差别的回应读作同一种经他者耦合与回应的回路，无动作的进程是比较而非标准；'


def text_phase(rid, base, after, apart):
    c = receipt_counts(rid)
    assert (c['own'], c['own_decls']) == (THEOREMS, DECLARATIONS), (c['own'], c['own_decls'])
    spine = n(c['spine'])
    # ------------------------------------------------------------ study
    study = (ROOT / STUDY).read_text(encoding='utf-8')
    sec = max(int(x) for x in re.findall(r'^## (\d+)\. ', study, re.M)) + 1
    body = (HERE / 'study_m4.txt').read_text(encoding='utf-8')
    body = body.replace('{N}', str(sec)).replace('{RECEIPT}', rid).replace('{APART}', apart).replace('{SPINE}', spine)
    assert '{' not in body, 'unfilled placeholder'
    marker = '## Ren’s words quoted in passages that exist only in the Chinese edition'
    assert study.count(marker) == 1
    study = study.replace(marker, body.rstrip('\n') + '\n\n' + marker)
    (ROOT / STUDY).write_text(study, encoding='utf-8')
    print('study section', sec)
    anchor = f'{sec}-where-two-courses-rejoin-m4'
    fill = lambda t: (t.replace('{MOD}', MOD).replace('{RECLINK}', RECLINK).replace('{SEC}', str(sec))
                      .replace('{SR}', SR).replace('{ANCHOR}', anchor))
    # ------------------------------------------------------------ chapter, en
    ch = (ROOT / CHAPTER).read_text(encoding='utf-8')
    ch = insert_after_line(ch, SEC3_AFTER, fill(SEC3), 'section 3 bullet')
    for old, new in S74_PAIRS:
        ch = replace_once(ch, old, new, 'section 7.4 (M3 sentences)')
    ch = replace_line(ch, S77_START, S77_NEW, 'section 7.7 bullet')
    ch = replace_once(ch, S84_OLD, S84_NEW, 'section 8.4 open readings')
    lines = ch.split('\n')
    rows = [i for i, line in enumerate(lines) if line.startswith('| Selection, causes and experiment | (Stated: ')]
    assert len(rows) == 1, rows
    row = lines[rows[0]]
    close = row.index('.)')
    row = row[:close] + '; where two courses rejoin: `Becoming.Rejoining`' + row[close:]
    row = replace_once(row, S82_OPEN_OLD, S82_OPEN_NEW, 'section 8.2 open item')
    row = replace_once(row, M3LINK, M3LINK + ', ' + RECLINK, 'section 8.2 record link')
    lines[rows[0]] = row
    ch = '\n'.join(lines)
    # section 9
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
    para = subn1(r'It was checked with Lean 4\.29\.1 on main \S+ (?:\(.*?\) )?with .*? in the working tree\. It passed\.',
                 f'It was checked with Lean 4.29.1 on main {base} ({after}) with M4 (`Becoming.Rejoining`, '
                 f'[study §{sec}]({SR}#{anchor})) in the working tree. It passed.', para, 'receipt sentence')
    # since the F3 sweep the core is the whole spine: no bridge or periphery-join rows
    assert c['bridge'] == (0, 0) and c['pj'][0] == 0 and c['injeq'][1] == 0, (c['bridge'], c['pj'], c['injeq'])
    assert c['spine'] == c['core'][1], (c['spine'], c['core'])
    rows = {
        '| Core modules (with the root `Becoming`, 0 theorems) |': f' {c["core"][0]} modules, {n(c["core"][1])} theorems |',
        '| Foundation modules |': f' {c["foundation"][0]} modules, {n(c["foundation"][1])} theorems |',
        '| Core closure |': f' {c["closure"][0]} modules, {n(c["closure"][1])} theorems |',
        '| Spine (the core; no bridge since the F3 sweep) |': f' {spine} theorems |',
        '| Audited spine declarations |': f' {n(c["audited"])} |',
        '| Modules in the compile order |': f' {c["compile"]} |',
        '| Generated `injEq` lemmas on `propext` |': f' {c["injeq"][0]} in the core closure |',
    }
    lines = para.split('\n')
    for i, line in enumerate(lines):
        for head, tail in rows.items():
            if line.startswith(head):
                lines[i] = head + tail
        if line.startswith('| Inherited modules bound'):
            assert f'| {c["inherited"]} (' in line, line
    for head in rows:
        assert sum(line.startswith(head) for line in lines) == 1, head
    para = '\n'.join(lines)
    ch = ch[:start] + para + ch[end:]
    ch = subn1(r'That run reused [\d,]+ cached Lean steps from `~/\.cache/becoming-lean` and ran [\d,]+\.',
               f'That run reused {n(c["reused"])} cached Lean steps from `~/.cache/becoming-lean` and ran {n(c["ran"])}.',
               ch, 'section 9 steps')
    last = list(re.finditer(r'Rerun with \w+ \(receipt [0-9TZ.]+\), it counts \d+ of [\d,]+, none in `[^`]+`\.', ch))[-1]
    assert 'Rerun with G5 (receipt 20261019T003752.845229Z)' in last.group(0), last.group(0)
    ch = ch[:last.end()] + f' Rerun with M4 (receipt {rid}), it counts {apart} of {spine}, none in `{MODULE}`.' + ch[last.end():]
    (ROOT / CHAPTER).write_text(ch, encoding='utf-8')
    print('edited', CHAPTER)
    # ------------------------------------------------------------ chapter, zh
    zh = (ROOT / CHAPTER_ZH).read_text(encoding='utf-8')
    for old, new in S74_ZH_PAIRS:
        zh = replace_once(zh, old, new, 'zh section 7.4 (M3 sentences)')
    zh = replace_line(zh, S77_ZH_START, S77_ZH_NEW, 'zh section 7.7 bullet')
    zh = replace_once(zh, S84_ZH_OLD, S84_ZH_NEW, 'zh section 8 open readings')
    (ROOT / CHAPTER_ZH).write_text(zh, encoding='utf-8')
    print('edited', CHAPTER_ZH)


if __name__ == '__main__':
    if sys.argv[1:2] == ['package']:
        package()
    elif sys.argv[1:2] == ['text'] and len(sys.argv) == 6:
        text_phase(*sys.argv[2:6])
    else:
        sys.exit(__doc__)
