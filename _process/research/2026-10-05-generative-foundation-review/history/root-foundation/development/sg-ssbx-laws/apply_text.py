#!/usr/bin/env python3
"""SG landing text: the study section and the readings entry (both numbered next at landing), chapter §1, §3,
§8.2, §8.3, §9 and the glossary (en, zh), X1's 护闭 rows where present, the apart register, and the board row moved
to the history file with the queue sentence. Every edit must match exactly once.

usage (from the checkout root to edit): python3 -B apply_text.py RECEIPT BASE CONNECTIVITY_LOG [--board]
RECEIPT is the core checker run, BASE the main commit it ran on, CONNECTIVITY_LOG the --check output on the
landing tree. The §9 counts are read from the receipt. --board also moves the board row (at landing only).
Writes sg-numbers.json (study section, readings entry) for make_records.py."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
DC = f'{RF}/DELEGATED-CHOICES.md'
DCZ = f'{RF}/DELEGATED-CHOICES.zh.md'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHZ = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
MODS = ['Undecided', 'Junctures', 'Commuting']
TITLE = 'Junctures, what a commuting law keeps apart, and the third value (SG)'
receipt_id, base, conn_log = sys.argv[1], sys.argv[2], sys.argv[3]
board_too = '--board' in sys.argv[4:]


PENDING = {}   # every edit is held here and written only once all of them matched


def read(path):
    return PENDING[path] if path in PENDING else (ROOT / path).read_text(encoding='utf-8')


def write(path, text):
    PENDING[path] = text


def once(text, old, new, where):
    k = text.count(old)
    if k != 1:
        sys.exit(f'{where}: expected one match, found {k}: {old[:100]!r}')
    return text.replace(old, new)


def after_line(text, prefix, insert, where):
    """Insert `insert` (a block) after the one line starting with `prefix`, separated by a blank line."""
    lines = text.split('\n')
    hits = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(hits) != 1:
        sys.exit(f'{where}: expected one line starting {prefix[:60]!r}, found {len(hits)}')
    lines[hits[0] + 1:hits[0] + 1] = [''] + insert.strip('\n').split('\n')
    return '\n'.join(lines)


def row_after(text, prefix, rows, where):
    lines = text.split('\n')
    hits = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(hits) != 1:
        sys.exit(f'{where}: expected one row starting {prefix[:60]!r}, found {len(hits)}')
    lines[hits[0] + 1:hits[0] + 1] = rows.strip('\n').split('\n')
    return '\n'.join(lines)


def slug(heading):
    s = heading.strip().lower()
    s = re.sub(r'[^\w\- ]', '', s)
    return s.replace(' ', '-')


# Receipt and connectivity.
rec = json.loads((ROOT / PKG / 'becoming-checks' / receipt_id / 'verification.json').read_text())
core = [m for m in rec['modules'] if m['layer'] == 'core']
assert rec['status'] == 'passed' and rec['core_compiles_from_prelude'] and rec['source_unchanged_during_check']
assert not any(v for m in core for v in m['axiom_dependencies'].values())
spine = {m['module']: m['theorems'] for m in core}
n_mod = len(rec['core_modules'])
n_thm = sum(spine.values())
found = {m: spine[f'Becoming.{m}'] for m in MODS}
total = sum(found.values())
closure = len(rec['core_closure'])
assert closure == len(rec['compile_order'])
audits = sum(len(m['declarations']) for m in rec['modules'] if m['spine'])
inj = len(rec['generated_axiom_dependencies'])
ran, reused = len(rec['lean_steps']['ran']), len(rec['lean_steps']['reused'])
t = Path(conn_log).read_text() if conn_log.startswith('/') else read(conn_log)
conn = json.loads(t[t.index('{'):t.rindex('}') + 1])
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
assert conn['spine_theorems'] == n_thm, (conn['spine_theorems'], n_thm)
assert not conn['apart_roots_unclassified'] and not conn['register_entries_not_apart_roots']
assert 'Becoming.Junctures' not in conn['apart_by_module'] and 'Becoming.Commuting' not in conn['apart_by_module']
und_apart = conn['apart_by_module'].get('Becoming.Undecided', [0])[0]
assert und_apart == 2, und_apart
comps = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = conn['classes']['statement on both families']
fmt = lambda n: f'{n:,}'

# Numbers: the next study section and the next readings entry.
study_text = read(STUDY)
assert f'. {TITLE}' not in study_text, 'study section already applied'
S = max(int(n) for n in re.findall(r'^## (\d+)\. ', study_text, re.M)) + 1
dc_text = read(DC)
D = max(int(n) for n in re.findall(r'<a id="d(\d+)-', dc_text)) + 1
assert D == max(int(n) for n in re.findall(r'<a id="d(\d+)-', read(DCZ))) + 1, 'en and zh readings entries differ'
SANCHOR = slug(f'{S}. {TITLE}')
(HERE / 'sg-numbers.json').write_text(json.dumps({'study_section': S, 'readings': D, 'study_anchor': SANCHOR}) + '\n')


def fill(text):
    return text.replace('{D}', str(D)).replace('{S}', str(S)).replace('{SANCHOR}', SANCHOR)


# Study section.
study = fill((HERE / 'study_sg.txt').read_text(encoding='utf-8')).replace('{N}', str(S)).replace(
    '{RECEIPT}', receipt_id).replace(
    '{APART}', f'{apart} apart of {fmt(n_thm)}; in SG only Undecided.incomplete (registered as general structure) and\n'
               '          the lemma it uses')
write(STUDY, study_text.rstrip('\n') + '\n\n' + study.rstrip('\n') + '\n')
print('study section', S)

# Readings entry, en and zh: the table row, the provenance line, the entry.
ROW_EN = (f'| D{D} | junctures, commuting laws and the third value (19 October) | adopted with exact scope: 机 a juncture; '
          '护闭 keeping and 成闭 losing at a juncture, with no valuation; finding the juncture is deciding reach (LPO for '
          'every process); a law keeping a symmetry never merges what it tells apart; 疑 what revision has not decided |')
ROW_ZH = (f'| D{D} | 关节、交换之律与第三值（10-19） | 以确切范围采用：机为关节；护闭为关节处的保持，成闭为失去，不带估值；'
          '找到关节即判定可达（对每个过程为 LPO）；保持对称的律从不合并其所分开者；疑为修正尚未决定者 |')
LINE_EN = ('- Ren\'s request of 19 October 2026 that the earlier 生生不息 repository be read for what can be integrated, '
           '"please take a look of this … many insights can be integrated" (abridged, as quoted with the '
           f'[review](SSBX-REPOSITORY-REVIEW.md)): D{D} ([study section {S}](BECOMING-RENEWAL-READING.md#{SANCHOR})).')
LINE_ZH = ('- Ren 2026-10-19 要求审读早期《生生不息》仓库中可并入者，“please take a look of this … many insights can be '
           f'integrated”（节录，随[审读](SSBX-REPOSITORY-REVIEW.md)引用）：D{D}（研究第 {S} 节）。')
SEC13 = '<a id="13-一个说明--one-account"></a>'
# X1's D49 says 护闭 waits on the juncture law; where X1 has landed, it is anchored to Becoming.Junctures (X1's request).
JD = ('`Branching.loss_passes_juncture`, `Branching.keeping_greatest`, `Branching.keeping_removes_at_juncture`')
X1_DC = [
    ('护闭 not yet proved;', f'护闭 keeping at a juncture (D{D});'),
    ("That law, the juncture law, is not proved (the review's §3.2, G1 there), and the chapter says so; on this reading",
     f'That law, the juncture law, is proved in `Becoming.Junctures` ({JD}; SG, D{D}); on this reading'),
    ('A proof of the juncture law (claimed on the work board as SG, module `Becoming.Junctures`), which gives 护闭 its '
     'anchor, or a counterexample to it;',
     "A reading of 护闭, argued from Ren's texts, other than keeping at a juncture (the juncture law, proved in "
     f'`Becoming.Junctures`, SG, D{D}, gives 护闭 its anchor);'),
]
X1_DCZ = [
    ('护闭尚未证明；', f'护闭为关节处的保持（D{D}）；'),
    ('这条律即关节律尚未证明（审读第 3.2 节，其中的 G1），章节如实写明；',
     f'这条律即关节律已在 `Becoming.Junctures` 中证明（{JD.replace(", ", "、")}；SG，D{D}）；'),
    ('关节律的证明（工作板上认领为 SG，模块 `Becoming.Junctures`；护闭由此有其锚点），或它的反例；',
     f'由 Ren 的文本论证、不同于关节处之保持的护闭读法（关节律已在 `Becoming.Junctures` 中证明，SG，D{D}，护闭由此有其锚点）；'),
]
for path, row, line, entry in ((DC, ROW_EN, LINE_EN, 'd_sg.txt'), (DCZ, ROW_ZH, LINE_ZH, 'd_sg.zh.txt')):
    text = read(path)
    lines = text.split('\n')
    last = max(i for i, x in enumerate(lines) if re.match(r'\| D\d+ \|', x))
    lines.insert(last + 1, row)
    text = '\n'.join(lines)
    text = once(text, '\n' + SEC13, '\n' + line + '\n\n' + SEC13, path)
    text = text.rstrip('\n') + '\n' + fill((HERE / entry).read_text(encoding='utf-8')).rstrip('\n') + '\n'
    swaps = X1_DC if path == DC else X1_DCZ
    done = [o for o, _ in swaps if o in text]
    for o, n in swaps:
        if o in text:
            text = once(text, o, n, path)
    write(path, text)
    print('readings entry', path, D, '; X1 (D49) items anchored:', len(done), 'of', len(swaps))

# Chapter, English.
ch = read(CH)
ch = after_line(ch, '*Readings* [AI reading, D32]. Not derived: being drawn in within a bound', fill((HERE / 'ch_junctures.txt').read_text(encoding='utf-8')), CH)
ch = after_line(ch, '*Readings* [AI reading, D47].', fill((HERE / 'ch_commuting.txt').read_text(encoding='utf-8')), CH)
liar = '- *The liar.* Read as revision, the liar never rests;'
ch = row_after(ch, liar, fill((HERE / 'ch_liar.txt').read_text(encoding='utf-8')), CH)
ch = row_after(ch, '| possibly / necessarily drawn (可能／必然被吸入) |', (HERE / 'ch_glossary.txt').read_text(encoding='utf-8'), CH)
REC = '../results/records/'
lines = ch.split('\n')
for area, add_open, recs in (
        ('| When the course branches | ',
         ' Junctures for a set of configurations and for profiles of several possibilities at once; which junctures and '
         'symmetries actual unfoldings have; groups of symmetries (the four-group of 錯 and 綜).',
         ['every-loss-passes-a-juncture', 'what-a-commuting-law-keeps-apart']),
        ('| What a description keeps and loses | ',
         ' Revision with an undecided value over infinitely many sentences, where the least fixed point needs a limit '
         'stage.', ['revision-with-an-undecided-value'])):
    hits = [i for i, x in enumerate(lines) if x.startswith(area)]
    assert len(hits) == 1, (area, hits)
    cells = lines[hits[0]].split(' | ')
    assert len(cells) == 3, (area, len(cells))
    cells[1] = cells[1] + add_open
    cells[2] = cells[2][:-2] + ''.join(f', [{r}]({REC}{r}.md)' for r in recs) + ' |'
    lines[hits[0]] = ' | '.join(cells)
ch = '\n'.join(lines)
B83 = (f'- Junctures, commuting laws and the third value (D{D}). 机 is a juncture, where one step keeps a configuration to '
       'be had again and another loses it; 护闭 is keeping and 成闭 losing at a juncture, with no valuation; finding the '
       'juncture of a loss is deciding whether the configuration can still be had, which asked of every process is the '
       'limited principle of omniscience. A law keeping a symmetry never merges what it tells apart: 消息 never merges 陰 '
       'and 陽 changed line for line, and the waning into 坤 breaks 錯. The third value 疑 is what revision has not '
       'decided, not a third truth, and the diagonal\'s gap reappears as undecidedness (§1, §3).')
ch = once(ch, '\n- One account (D45).', '\n' + B83 + '\n- One account (D45).', CH)
# X1's 护闭 row and §8.3 item, where X1 has landed.
X1_EN = [
    ('**Not yet proved.** The candidate is the juncture law of the review (§3.2, G1 there).',
     f'Proved as keeping at a juncture (`Becoming.Junctures`, D{D}; §1, “Where a configuration is lost”).'),
    ('What has landed: a configuration possibly drawn in', 'Also landed: a configuration possibly drawn in'),
    ('| none yet; compare `Branching.possiblyDrawn_iff`,',
     '| `Branching.Juncture`, `Branching.keeping`, `Branching.keeping_greatest`, `Branching.keeping_removes_at_juncture`; '
     'compare `Branching.possiblyDrawn_iff`,'),
    ('护闭 is the juncture law, not yet proved', f'护闭 is keeping at a juncture (D{D})'),
]
x1 = [old for old, _ in X1_EN if old in ch]
for old, new in X1_EN:
    if old in ch:
        ch = once(ch, old, new, CH)
print('X1 rows updated (en):', len(x1), 'of', len(X1_EN))

# §9: receipt, counts, compile order, reuse, integration.
m = re.search(r'There are (\d+) dependency components, with (\d+) spine theorems outside the main one; (\d+) statements use both families\.', ch)
assert m, 'components sentence'
NEWINT = (f'Rerun with SG (receipt {receipt_id}), it counts {apart} of {fmt(n_thm)}: none of the theorems of '
          '`Becoming.Junctures` and `Becoming.Commuting` stands apart, their laws stated on processes, traces and runs '
          '(`Law.run`), and of the 64 of `Becoming.Undecided` two do, `Undecided.incomplete`, a law of every family of '
          'three-valued readings registered as general structure, and the lemma it uses; revision is stated on its run. '
          f'There are {comps} dependency components, with {outside} spine theorems outside the main one; '
          f'{both} statements use both families.')
ch = ch.replace(m.group(0), NEWINT, 1)
m = re.search(r'\*\*The current receipt\.\*\* The \[current receipt\]\([^)]*\) is run `([^`]+)`, frozen in .*?It passed\. Its counts:', ch, re.S)
assert m and '\n' not in m.group(0), 'receipt sentence'
NEWREC = (f'**The current receipt.** The [current receipt](../../../{PKG}/becoming-verification.json) is run '
          f'`{receipt_id}`, frozen in [`becoming-checks/{receipt_id}/`](../../../{PKG}/becoming-checks/{receipt_id}/'
          f'verification.json). It was checked with Lean 4.29.1 on main {base} with SG '
          '(`Becoming.Undecided`, `Becoming.Junctures`, `Becoming.Commuting`, '
          f'[study §{S}](../../../{STUDY}#{SANCHOR})) in the working tree. It passed. Its counts:')
ch = ch.replace(m.group(0), NEWREC, 1)
table = re.search(r'\| Core modules \(with the root `Becoming`, 0 theorems\) \| (\d+) modules, ([\d,]+) theorems \|\n'
                  r'\| Foundation modules \| 3 modules, 74 theorems \|\n'
                  r'\| Core closure \| (\d+) modules, ([\d,]+) theorems \|\n'
                  r'\| Spine \(the core; no bridge since the F3 sweep\) \| ([\d,]+) theorems \|\n'
                  r'\| Audited spine declarations \| ([\d,]+) \|\n', ch)
assert table, 'counts table'
NEWTABLE = (f'| Core modules (with the root `Becoming`, 0 theorems) | {n_mod} modules, {fmt(n_thm)} theorems |\n'
            '| Foundation modules | 3 modules, 74 theorems |\n'
            f'| Core closure | {closure} modules, {fmt(n_thm + 74)} theorems |\n'
            f'| Spine (the core; no bridge since the F3 sweep) | {fmt(n_thm)} theorems |\n'
            f'| Audited spine declarations | {fmt(audits)} |\n')
ch = ch.replace(table.group(0), NEWTABLE, 1)
mo = re.search(r'\| Modules in the compile order \| (\d+) \|\n\| Generated `injEq` lemmas on `propext` \| (\d+) in the core closure \|', ch)
assert mo, 'compile order'
ch = ch.replace(mo.group(0), f'| Modules in the compile order | {closure} |\n| Generated `injEq` lemmas on `propext` | {inj} in the core closure |', 1)
mr = re.search(r'That run reused ([\d,]+) cached Lean steps from `~/.cache/becoming-lean` and ran (\d+)\.', ch)
assert mr, 'reuse sentence'
ch = ch.replace(mr.group(0), f'That run reused {fmt(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran}.', 1)
write(CH, ch)
print('chapter (en)')

# Chapter, Chinese edition.
z = read(CHZ)
z = after_line(z, '**路径分支时。**', fill((HERE / 'ch_junctures.zh.txt').read_text(encoding='utf-8')), CHZ)
z = after_line(z, '**周易的构形。**', fill((HERE / 'ch_commuting.zh.txt').read_text(encoding='utf-8')), CHZ)
z = after_line(z, '**在所读之中的读法族。**', fill((HERE / 'ch_liar.zh.txt').read_text(encoding='utf-8')), CHZ)
GLOSS_ZH = (
    '| 关节（机，AI 读法） | juncture | 有一步之后某配置仍可得、又有一步之后它不可得的配置。返回之配置的每次失去都经过一个，以双重否定的形式；'
    '找到它就是判定该配置是否仍可再得，一般即有限全知原理。 | `Branching.Juncture`、`Branching.loss_passes_juncture`、'
    '`Branching.lpo_of_junctures_found` |\n'
    '| 保持／失去（关节处的护闭／成闭，AI 读法） | keeping / losing | 之后某配置仍可得之步构成的子过程，与其余之步构成的子过程。'
    '保持保住该配置，在自己的路径上是保住它的最大子过程；失去从不回到它。都不是估值。 | `Branching.keeping`、'
    '`Branching.keeping_greatest`、`Branching.losing_not_returns` |\n'
    '| 交换之律 | commuting law | 对每个 x 有 T (σ x) = σ (T x) 的律 T。σ 移动每个配置时，律从 x 与从 σ x 出发的运行在同一步从不在同一配置。'
    ' | `Law.Commutes`、`Law.Commutes.apart`、`Law.Commutes.breaks` |\n'
    '| 未定（第三值；早期文本的疑） | undecided | 信息序上低于真与假的值：修正尚未决定者。只彼此言说的有限个句子的修正停于最小不动点；'
    '二值修正没有不动点时，有句子保持未定。 | `Undecided.Value`、`Undecided.least_fixed`、`Undecided.undecided_of_moves` |')
z = row_after(z, '| 可能／必然被吸入 |', GLOSS_ZH, CHZ)
lines = z.split('\n')
for area, add in (
        ('| 路径分支时 | ', f'；配置在何处失去与交换之律保持什么分开已陈述（[every-loss-passes-a-juncture]({REC}every-loss-passes-a-juncture.md)、'
                       f'[what-a-commuting-law-keeps-apart]({REC}what-a-commuting-law-keeps-apart.md)），一组配置的关节与对称群开放'),
        ('| 描述保留什么、失去什么 | ', f'；第三值下的修正已陈述（[revision-with-an-undecided-value]({REC}revision-with-an-undecided-value.md)），'
                                f'无穷多个句子开放')):
    hits = [i for i, x in enumerate(lines) if x.startswith(area)]
    assert len(hits) == 1, (area, hits)
    assert lines[hits[0]].endswith(' |')
    lines[hits[0]] = lines[hits[0]][:-2] + add + ' |'
z = '\n'.join(lines)
X1_ZH = [
    ('**尚未证明。** 候选是审读中的关节律（第 3.2 节，其中的 G1）：',
     f'已证明为关节处的保持（`Becoming.Junctures`，D{D}；§1“配置在何处失去”）：'),
    ('已落地的：可能被吸入的配置', '另已落地的：可能被吸入的配置'),
    ('| 尚无；对照 `Branching.possiblyDrawn_iff`',
     '| `Branching.Juncture`、`Branching.keeping`、`Branching.keeping_greatest`、`Branching.keeping_removes_at_juncture`；'
     '对照 `Branching.possiblyDrawn_iff`'),
    ('护闭是关节律，尚未证明', f'护闭是关节处的保持（D{D}）'),
]
x1z = [old for old, _ in X1_ZH if old in z]
for old, new in X1_ZH:
    if old in z:
        z = once(z, old, new, CHZ)
print('X1 rows updated (zh):', len(x1z), 'of', len(X1_ZH))
B83Z = (f'- 关节、交换之律与第三值（D{D}）：机是关节，一步保住某配置仍可再得，另一步失去它；护闭是关节处的保持，成闭是失去，不带估值；'
        '找到一次失去的关节，就是判定该配置是否仍可再得，对每个过程都这样问即有限全知原理。保持对称的律从不合并其所分开者：消息从不合并逐爻相反的'
        '阴阳，尽归坤之消破错。第三值疑是修正尚未决定者，不是第三种真；对角线的缺口表现为未定（§1、§3）。')
zl = z.split('\n')
hits = [i for i, x in enumerate(zl) if x.startswith('- 一个说明（D45）')]
if len(hits) == 1:
    zl.insert(hits[0], B83Z)
    z = '\n'.join(zl)
    print('zh §8.3 item added')
else:
    print('zh §8.3: no single "- 一个说明（D45）" line; item not added', len(hits))
write(CHZ, z)
print('chapter (zh)')

# Board: the row moves to the history file; the queue sentence names the landing.
if board_too:
    board = read(BOARD)
    history = read(HISTORY)
    lines = board.split('\n')
    rows = [i for i, line in enumerate(lines) if line.startswith('| **SG: ')]
    assert len(rows) == 1, rows
    row = lines.pop(rows[0])
    cells = row.split(' | ')
    assert len(cells) == 5, len(cells)
    cells[2] = (f'landed 2026-10-19, core receipt `{receipt_id}`; {total} theorems in three core modules '
                f'(`Becoming.Undecided` {found["Undecided"]}, `Becoming.Junctures` {found["Junctures"]}, '
                f'`Becoming.Commuting` {found["Commuting"]}), empty axiom reports; records every-loss-passes-a-juncture, '
                f'what-a-commuting-law-keeps-apart, revision-with-an-undecided-value; study §{S}; readings D{D}')
    row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
    hist = history.split('\n')
    stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
    last = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
    hist.insert(last + 1, row)
    board = '\n'.join(lines)
    board = once(board, '): W2 (this re-rooting', f'; SG landed, core receipt `{receipt_id}`, ahead of W2): W2 (this re-rooting', BOARD)
    write(BOARD, board)
    write(HISTORY, '\n'.join(hist))
    print('board row moved')
for path, text in PENDING.items():
    (ROOT / path).write_text(text, encoding='utf-8')
print('written:', ', '.join(sorted(PENDING)))
print('receipt', receipt_id, 'apart', apart, 'theorems', n_thm, 'modules', n_mod, 'closure', closure, 'S', S, 'D', D)
