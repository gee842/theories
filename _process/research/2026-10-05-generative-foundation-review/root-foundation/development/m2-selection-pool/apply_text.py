#!/usr/bin/env python3
"""M2 (Becoming.SelectionPool) landing edits. Every edit must match exactly once.

usage (from the repository root; M2_ROOT names another checkout to edit, such as a worktree):
  python3 -B apply_text.py package                          copy the module in; import, doc bullet, CORE entry, scope
                                                             sentence, README row
  python3 -B apply_text.py text RECEIPT BASE AFTER APART    study, chapter (sections 7.3, 7.4, 7.7, 8.2, 9, en; 7.3,
                                                             7.4, 7.7 zh), the selection and gap records' related notes
RECEIPT is the core checker run, BASE the main commit it ran on, AFTER what BASE adds to the last landing (for the
receipt sentence), APART the connectivity check's count of spine theorems apart; the section 9 counts are read from
the receipt itself."""
import json, os, re, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['M2_ROOT']).resolve() if os.environ.get('M2_ROOT') else HERE.parents[5]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


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


DOC_AFTER = ('  `Diversion` is an instance, and its supplying flow, which gains, shows the premise binds.\n')
DOC = (
    '* `Becoming.SelectionPool` (L4): what selection through pooled coupling reaches. A pool\'s\n'
    '  coupling closure is the union of its members\' coupling closures. With the rest of the exchange\n'
    '  fixed, a part beyond it is selected alike by every selection through the pooled coupling of any\n'
    '  group within it. Some pooled selection separates two histories exactly when the members do not\n'
    '  all couple them alike; with the members listed and each member\'s coupling decided, exactly when\n'
    '  some member couples them apart; and the pooled selections are one member\'s exactly when\n'
    '  whatever that member couples alike every member couples alike. Where the rest follows a law of\n'
    '  exchange reading through coupling and a pool\'s act differs only beyond the pool\'s coupling\n'
    '  closure, every selection through the pooled coupling of a group within the closure selects the\n'
    '  flows with and without the act alike, and a formation whose admission the act changes lies\n'
    '  beyond the closure and separates the two through every pool holding it. In `Clearing`, pooling\n'
    '  with the dweller closes the clearer\'s gap.\n')
SCOPE_AFTER = ('    "reaching beyond the coupling; Diversion is an instance, and its supplying flow shows the "\n'
               '    "premise binds. "\n')
SCOPE = (
    '    "SelectionPool: a pool\'s coupling closure is the union of its members\'; with the rest fixed, "\n'
    '    "every selection through the pooled coupling of a group within it selects a part beyond it "\n'
    '    "alike; some pooled selection separates two histories exactly when the members do not all "\n'
    '    "couple them alike, and, with the members listed and each member\'s coupling decided, exactly "\n'
    '    "when some member couples them apart; where the rest follows a law of exchange reading "\n'
    '    "through coupling and a pool\'s act differs only beyond its coupling closure, every selection "\n'
    '    "through the pooled coupling of a group within the closure selects the flows with and without "\n'
    '    "the act alike, while a formation whose admission the act changes separates them through every "\n'
    '    "pool holding it; in Clearing, pooling with the dweller closes the clearer\'s gap. "\n')
README_ROW = (
    '| L4 | [`Becoming.SelectionPool`](Becoming/SelectionPool.lean) | what selection through pooled coupling reaches '
    '(no axiom; the law the rest follows, that it reads through coupling, balance, and for the converse the members '
    'listed and each member\'s coupling decided, are hypotheses of the theorems): a pool\'s coupling closure is the '
    'union of its members\' (`withinClosureOf_iff`, `Flow.WithinPoolCoupling`); with the rest fixed, a part beyond it '
    'is selected alike through the pooled coupling of any group within it (`Flow.unselected_beyond_pool`, of which '
    '`Flow.unselected_beyond_coupling_all` is the case of one formation); some pooled selection separates two '
    'histories exactly when the members do not all couple them alike (`Web.separates_all_iff`), and, the members '
    'listed and decided, exactly when some member couples them apart (`Web.separates_all_iff_member`); the pooled '
    'selections are one member\'s exactly when whatever it couples alike every member couples alike '
    '(`Web.pooled_iff_member`, `Web.pool_adds`); the gap for a pool\'s act (`Flow.act_unselected_pool`, '
    '`act_courses_unselected_pool`), a formation whose admission the act changes lying beyond the closure and '
    'separating the flows through every pool holding it (`Flow.act_selected_by_pool`, '
    '`Flow.separating_member_beyond`); in `Clearing`, pooling with the dweller closes the clearer\'s gap '
    '(`Clearing.pool_closes_gap`), and a part within the clearer\'s closure is not thereby separated through it '
    '(`Clearing.within_closure_unseparated`) ([what-pooled-coupling-reaches](../../../../../../theories/becoming/'
    'results/records/what-pooled-coupling-reaches.md)) |')


def package():
    shutil.copyfile(HERE / 'Becoming/SelectionPool.lean', ROOT / PKG / 'Becoming/SelectionPool.lean')
    print('copied Becoming/SelectionPool.lean')
    edit(f'{PKG}/Becoming.lean', [
        ('import Becoming.SelectionReach\n', 'import Becoming.SelectionReach\nimport Becoming.SelectionPool\n'),
        (DOC_AFTER, DOC_AFTER + DOC),
    ])
    edit(f'{PKG}/check_becoming.py', [
        ('"Becoming.SelectionReach", ', '"Becoming.SelectionReach", "Becoming.SelectionPool", '),
        (SCOPE_AFTER, SCOPE_AFTER + SCOPE),
    ])
    readme = f'{PKG}/README.md'
    text = (ROOT / readme).read_text(encoding='utf-8')
    row = next(line for line in text.split('\n') if line.startswith('| L4 | [`Becoming.SelectionReach`]'))
    edit(readme, [(row + '\n', row + '\n' + README_ROW + '\n')])


CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHAPTER_ZH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
SR = '../../../' + STUDY
MOD = f'../../../{PKG}/Becoming/SelectionPool.lean'
REC = '../results/records/what-pooled-coupling-reaches.md'
RECLINK = f'[what-pooled-coupling-reaches]({REC})'


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
        'pool': int(mods['Becoming.SelectionPool']['theorems']),
        'pool_decls': len(mods['Becoming.SelectionPool']['declarations']),
    }


def n(x):
    return f'{x:,}'


def subn1(pattern, repl, text, what):
    text, k = re.subn(pattern, repl, text)
    if k != 1:
        sys.exit(f'{what}: expected one match, found {k}')
    return text


def replace_line(text, start, new, what):
    lines = text.split('\n')
    idx = [i for i, line in enumerate(lines) if line.startswith(start)]
    if len(idx) != 1:
        sys.exit(f'{what}: expected one line, found {len(idx)}')
    lines[idx[0]] = new
    return '\n'.join(lines)


def insert_after_line(text, start, new, what):
    lines = text.split('\n')
    idx = [i for i, line in enumerate(lines) if line.startswith(start)]
    if len(idx) != 1:
        sys.exit(f'{what}: expected one line, found {len(idx)}')
    lines[idx[0] + 1:idx[0] + 1] = [new]
    return '\n'.join(lines)


# ---------------------------------------------------------------- chapter text, en
SEC3_AFTER = '- *Raising what couples in draws from beyond* ('
SEC3 = (
    '- *What pooled coupling reaches* ([Becoming.SelectionPool]({MOD}), {RECLINK}). A pool\'s coupling closure is the '
    'union of its members\' (`withinClosureOf_iff`). With the rest of the exchange fixed and balance on what the closure '
    'couples into, every selection through the pooled coupling of any group within it selects the levels with and '
    'without a part beyond it alike '
    '(`Flow.unselected_beyond_pool`); the pooled form above is the case of a pool within one formation\'s closure '
    '(`Flow.unselected_beyond_coupling_all_of_pool`). Some pooled selection separates two histories exactly when the '
    'members do not all couple them alike (`Web.separates_all_iff`), and, with the members listed and each member\'s '
    'coupling decided, exactly when some member couples them apart (`Web.separates_all_iff_member`). An act whose '
    'difference stays beyond a pool\'s coupling closure, the pool\'s own joint act included, is selected alike by every '
    'selection through the pooled coupling of any group within the closure (`Flow.act_unselected_pool`, '
    '`act_courses_unselected_pool`); a formation whose admission the act changes lies beyond the closure and separates '
    'the act through every pool holding it (`Flow.act_selected_by_pool`). In `Clearing`, with the rest\'s law derived, '
    'pooling with the dweller closes the clearer\'s gap (`Clearing.pool_closes_gap`). Stated in §7.3 and §7.4. Study: '
    '[section {SEC}]({SR}#{ANCHOR}).')
OTHERS_START = '- **Others: pooled coupling.** '
OTHERS = (
    '- **Others: pooled coupling** ({RECLINK}). A selection through a group\'s pooled coupling selects alike exactly the '
    'histories alike through every member\'s couplings (`Web.SelectsThroughAll`, `Web.selects_alike_all_iff`). Every '
    'member\'s selection is a pooled selection (`Web.SelectsThrough.all`), and pooled selections combine '
    '(`Web.SelectsThroughAll.and`). Some pooled selection separates two histories exactly when the members do not all '
    'couple them alike (`Web.separates_all_iff`); with the members listed and each member\'s coupling of the two '
    'decided, exactly when some member couples them apart (`Web.separates_all_iff_member`). In `Clearing`, that the '
    'clearer and the dweller are both admitted at the third step goes through their pooled coupling: it holds in the '
    'spared world, fails in the cleared one, and goes through neither coupling alone (`Clearing.selected_pooled`). '
    '*Limit:* a pool\'s coupling closure is the union of its members\' (`withinClosureOf_iff`), and with the rest fixed '
    'and balance on what it couples into, every selection through the pooled coupling of any group within it selects the '
    'levels with and without a part '
    'beyond it alike (`Flow.unselected_beyond_pool`; for a pool within one formation\'s closure, '
    '`Flow.unselected_beyond_coupling_all`). So a pool reaches beyond a closure only if not all its members lie within '
    'it. Lying within the closure does not make a difference separated: the clearer\'s own part lies within its '
    'coupling closure, and the clearer couples the levels with and without it alike at every step '
    '(`Clearing.within_closure_unseparated`).')
HOLDING_OLD = ('In `Clearing` that formation is the dweller, the one the clearer\'s act ends '
               '(`Clearing.selected_by_dweller`).')
HOLDING_NEW = (HOLDING_OLD + ' Where the rest follows a law of exchange reading through coupling, such a formation '
               'separates the act through every pool holding it, and no pool within the actor\'s coupling closure does '
               '(`Flow.act_selected_by_pool`, §7.4).')
S74_OLD_READING_START = '*Reading* [AI reading, open]. Alignment, so read, is neither fitting one party'
S74_OLD_DIFF_START = '- **Difference is what a pool adds.** Where every member couples into the same conditions'
S74_NEW = (
    'What a pool\'s selections reach is proved for any pool, with neither the condition of §6.15 nor a practical '
    'premise ({RECLINK}).\n'
    '\n'
    '- **The gap for a pool\'s act.** Let the rest follow one law of exchange reading through coupling, in balanced '
    'flows with the same formations present and a common start, and let an act, which may be a pool\'s own act taken '
    'jointly, have its difference stay beyond the pool\'s coupling closure. Every selection through the pooled coupling '
    'of any group within that closure, the pool among them, then selects the worlds with and without the act alike at '
    'every step (`Flow.act_unselected_pool`), so a consequence of the act is a selection through no such group '
    '(`Flow.consequence_unselected_pool`); where both acts are laws, nothing is supplied '
    '(`act_courses_unselected_pool`).\n'
    '- **What separates the act.** Under the same conditions, a formation that couples the two worlds apart lies beyond '
    'the pool\'s coupling closure (`Flow.apart_beyond_pool`). A formation whose admission the act changes is one: its '
    'admission is a selection through the pooled coupling of every group holding it, from that step on, and of no group '
    'within the closure (`Flow.act_selected_by_pool`). Where a list holds the members of a pool and each member\'s '
    'coupling of the two worlds is decided, a pool that separates them has a member that couples them apart, and that '
    'member lies beyond the closure (`Flow.separating_member_beyond`). In `Clearing`, every selection through the pooled '
    'coupling of the clearer and its source selects the cleared and the spared world alike at every step, and every pool '
    'holding the dweller separates them by its admission at the third step (`Clearing.pool_closes_gap`).\n'
    '- **Difference is what a pool adds.** A pool\'s selections are one member\'s exactly when whatever that member '
    'couples alike every member couples alike (`Web.pooled_iff_member`). Where the members do not all couple alike two '
    'histories that one member couples alike, the pool has a selection that goes through no coupling of that member\'s '
    '(`Web.pool_adds`).\n'
    '\n'
    '*Reading* [AI reading, open]. Alignment, so read, is neither fitting one party to another\'s preferences nor '
    'fitting all to a fixed common utility. It is pooling couplings across intelligences, so that what any member\'s '
    'acts do beyond its own coupling closure couples into some member of the pool and can be corrected there. The laws '
    'above give the reading its exact part. Pooling moves the gap to the pool\'s coupling closure and does not remove '
    'it: what a pool does jointly beyond that closure is separated only through formations beyond it that couple the '
    'difference apart, such as those whose support the act changes. So a pool of intelligences reaches what its acts '
    'do to formations outside it only through members whose couplings reach that difference. That a separated '
    'difference is then corrected is not proved: selection is not response (§7.7). Members correct one another, and no '
    'member\'s couplings are the pool\'s.\n'
    '\n'
    '- **Members who differ.** An AI system may couple into scale, distance and far consequences that a person does '
    'not; a person into a lived situation and its stakes, which a system may not. Neither coupling replaces the other: '
    'a pool holding both separates what either separates (`Web.member_separates_all`).')

# ---------------------------------------------------------------- chapter text, zh
OTHERS_ZH_START = '- **他者：合起来的耦合。** '
OTHERS_ZH = (
    '- **他者：合起来的耦合**（{RECLINK}）。经一组合起来之耦合的选择，恰把经每个成员之耦合都无别的历史选得相同'
    '（`Web.SelectsThroughAll`、`Web.selects_alike_all_iff`）。每个成员的选择都是合起来的选择（`Web.SelectsThrough.all`），'
    '合起来的选择可以结合（`Web.SelectsThroughAll.and`）。某个合起来的选择分开两段历史，恰当并非每个成员都经其耦合使它们'
    '无别（`Web.separates_all_iff`）；成员由一个列表列出、每个成员对两者的耦合已判定时，恰当某个成员经其耦合使它们有别'
    '（`Web.separates_all_iff_member`）。`Clearing` 中，“清除者与栖居者在第三步都被接纳”经两者合起来的耦合：它在不清除的'
    '世界成立，在清除的世界不成立，而不经其中任一者单独的耦合（`Clearing.selected_pooled`）。*界限*：一组的耦合闭包是其'
    '成员耦合闭包的并（`withinClosureOf_iff`）；其余交换固定、并在闭包所耦合入者上平衡时，经此闭包内任一组合起来之耦合的每个选择，'
    '都把有与无闭包之外'
    '一个部分的水平选得相同（`Flow.unselected_beyond_pool`；组在一个形成的闭包之内时，即 '
    '`Flow.unselected_beyond_coupling_all`）。所以一组合起来及于闭包之外，只当并非其成员都在闭包之内。在闭包之内，并不因此'
    '使差别被分开：清除者自己的部分在其耦合闭包之内，而清除者在每一步都把有与无这个部分的水平耦合得无别'
    '（`Clearing.within_closure_unseparated`）。')
HOLDING_ZH_OLD = '`Clearing` 中这个形成是栖居者，即清除者的动作所终结者（`Clearing.selected_by_dweller`）。'
HOLDING_ZH_NEW = (HOLDING_ZH_OLD + '其余遵从一个经耦合而读的交换律时，这样的形成经每个含有它的组分开此动作，而行动者耦合闭包'
                  '之内没有哪个组分开它（`Flow.act_selected_by_pool`，§7.4）。')
S74_ZH_OLD_READING_START = '读法（AI 的，开放）：如此读，对齐既不是使一方适合另一方的偏好'
S74_ZH_OLD_DIFF_START = '- **差别是一组所加的。** 每个成员都以同样方式耦合入同样的条件时'
S74_ZH_NEW = (
    '一组的选择及于什么，对任何一组都已证明，既不用 §6.15 的条件，也不用实践前提（{RECLINK}）。\n'
    '\n'
    '- **一组之动作的缺口。** 设其余遵从一个经耦合而读的交换律，在出现的形成相同、起点相同的平衡的流中；设一个动作的差别'
    '留在一组的耦合闭包之外，这个动作可以是这组合起来的动作。那么经这一闭包内任一组合起来之耦合的每个选择（这组自身在内），'
    '都在每一步把有与无此动作的世界选得相同（`Flow.act_unselected_pool`）；所以此动作的后果不是经任何这样的组的选择'
    '（`Flow.consequence_unselected_pool`）；两个动作都是律时，不另给任何东西（`act_courses_unselected_pool`）。\n'
    '- **什么分开这个动作。** 在同样的条件下，经其耦合使两个世界有别的形成，在这组的耦合闭包之外'
    '（`Flow.apart_beyond_pool`）。接纳被此动作改变的形成就是这样的形成：它在那一步的接纳，从那一步起，是经每个含有它的组'
    '合起来之耦合的选择，而不是经闭包内任何组的选择（`Flow.act_selected_by_pool`）。一组的成员由一个列表列出、每个成员对两个'
    '世界的耦合已判定时，分开它们的组有一个经其耦合使它们有别的成员，且这个成员在闭包之外（`Flow.separating_member_beyond`）。'
    '`Clearing` 中，经清除者与其来源合起来之耦合的每个选择，在每一步都把清除的与不清除的世界选得相同；每个含有栖居者的组，'
    '以栖居者在第三步的接纳分开它们（`Clearing.pool_closes_gap`）。\n'
    '- **差别是一组所加的。** 一组的选择恰是一个成员的选择，当且仅当这个成员经其耦合使之无别的，每个成员都经其耦合使之无别'
    '（`Web.pooled_iff_member`）。一个成员使之无别的两段历史，并非每个成员都使之无别时，这组有一个不经该成员任何耦合的选择'
    '（`Web.pool_adds`）。\n'
    '\n'
    '读法（AI 的，开放）：如此读，对齐既不是使一方适合另一方的偏好，也不是使一切适合一个固定的共同效用。它是跨智能地把耦合'
    '合起来，使任何成员的动作在其自身耦合闭包之外所做的，耦合入组中的某个成员，并能在那里被纠正。上面的规律给出这一读法的'
    '精确部分。合起来把缺口移到这组的耦合闭包，并不消除它：一组合起来在这一闭包之外所做的，只经闭包之外、经其耦合使差别有别'
    '的形成被分开，例如支持被此动作改变的形成。所以一组智能及于其动作对组外形成所做的，只经其耦合及于这一差别的成员。被分开的'
    '差别随后被纠正，并未证明：选择不是回应（§7.7）。成员互相纠正，没有哪个成员的耦合就是这组的耦合。\n'
    '\n'
    '- **相异的成员。** AI 系统可以耦合入人所不耦合入的规模、距离与远处后果；人可以耦合入系统可能不耦合入的生活处境及其'
    '所系。哪一种耦合都不替代另一种：含有两者的组，分开其中任一者所分开的（`Web.member_separates_all`）。')


def replace_74(text, reading_start, diff_start, new, what):
    lines = text.split('\n')
    r = [i for i, line in enumerate(lines) if line.startswith(reading_start)]
    d = [i for i, line in enumerate(lines) if line.startswith(diff_start)]
    if len(r) != 1 or len(d) != 1 or d[0] != r[0] + 2 or lines[r[0] + 1] != '':
        sys.exit(f'{what}: reading {r}, difference bullet {d}')
    lines[r[0]:d[0] + 1] = new.split('\n')
    return '\n'.join(lines)


def text_phase(rid, base, after, apart):
    c = receipt_counts(rid)
    assert (c['pool'], c['pool_decls']) == (33, 37), (c['pool'], c['pool_decls'])
    spine = n(c['spine'])
    # ------------------------------------------------------------ study
    study = (ROOT / STUDY).read_text(encoding='utf-8')
    sec = max(int(x) for x in re.findall(r'^## (\d+)\. ', study, re.M)) + 1
    body = (HERE / 'study_m2.txt').read_text(encoding='utf-8')
    body = body.replace('{N}', str(sec)).replace('{RECEIPT}', rid).replace('{APART}', apart).replace('{SPINE}', spine)
    assert '{' not in body.replace('{N}', ''), 'unfilled placeholder'
    marker = '## Ren’s words quoted in passages that exist only in the Chinese edition'
    assert study.count(marker) == 1
    study = study.replace(marker, body.rstrip('\n') + '\n\n' + marker)
    (ROOT / STUDY).write_text(study, encoding='utf-8')
    print('study section', sec)
    anchor = f'{sec}-what-pooled-coupling-reaches-m2'
    fill = lambda t: (t.replace('{MOD}', MOD).replace('{RECLINK}', RECLINK).replace('{SEC}', str(sec))
                      .replace('{SR}', SR).replace('{ANCHOR}', anchor))
    # ------------------------------------------------------------ chapter, en
    ch = (ROOT / CHAPTER).read_text(encoding='utf-8')
    ch = insert_after_line(ch, SEC3_AFTER, fill(SEC3), 'section 3 bullet')
    ch = replace_line(ch, OTHERS_START, fill(OTHERS), 'section 7.3 others')
    if ch.count(HOLDING_OLD) != 1:
        sys.exit('section 7.3 holding: no single match')
    ch = ch.replace(HOLDING_OLD, HOLDING_NEW)
    ch = replace_74(ch, S74_OLD_READING_START, S74_OLD_DIFF_START, fill(S74_NEW), 'section 7.4')
    # section 8.2, "Selection, causes and experiment"
    lines = ch.split('\n')
    rows = [i for i, line in enumerate(lines) if line.startswith('| Selection, causes and experiment | (Stated: ')]
    assert len(rows) == 1, rows
    row = lines[rows[0]]
    close = row.index('.)')
    row = (row[:close] + '; what a pool\'s selections reach, and the gap for a pool\'s act: `Becoming.SelectionPool`'
           + row[close:])
    g2 = '[raising-what-couples-in-draws-from-beyond](../results/records/raising-what-couples-in-draws-from-beyond.md)'
    assert row.count(g2) == 1
    row = row.replace(g2, g2 + ', ' + RECLINK)
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
    para = subn1(r'It was checked with Lean 4\.29\.1 on main \S+ (?:\(.*?\) )?with .*? in the working tree, and it passed\.',
                 f'It was checked with Lean 4.29.1 on main {base} ({after}) with M2 (`Becoming.SelectionPool`, '
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
    ch = ch[:at] + f' Rerun with M2 (receipt {rid}), it counts {apart} of {spine}, none in `Becoming.SelectionPool`.' + ch[at:]
    (ROOT / CHAPTER).write_text(ch, encoding='utf-8')
    print('edited', CHAPTER)
    # ------------------------------------------------------------ chapter, zh
    zh = (ROOT / CHAPTER_ZH).read_text(encoding='utf-8')
    zh = replace_line(zh, OTHERS_ZH_START, fill(OTHERS_ZH), 'zh section 7.3 others')
    if zh.count(HOLDING_ZH_OLD) != 1:
        sys.exit('zh section 7.3 holding: no single match')
    zh = zh.replace(HOLDING_ZH_OLD, HOLDING_ZH_NEW)
    zh = replace_74(zh, S74_ZH_OLD_READING_START, S74_ZH_OLD_DIFF_START, fill(S74_ZH_NEW), 'zh section 7.4')
    (ROOT / CHAPTER_ZH).write_text(zh, encoding='utf-8')
    print('edited', CHAPTER_ZH)


if __name__ == '__main__':
    if sys.argv[1] == 'package':
        package()
    elif sys.argv[1] == 'text':
        text_phase(*sys.argv[2:6])
    else:
        sys.exit(__doc__)
