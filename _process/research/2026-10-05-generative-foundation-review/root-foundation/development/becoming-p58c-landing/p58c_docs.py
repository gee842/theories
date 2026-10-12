#!/usr/bin/env python3
"""P58c documents: python3 -B p58c_docs.py ROOT
Run in the landing worktree after both checkers, before the records (p58c_records.py ROOT SECTION, given the section
printed here). Reads this run's receipts and HEAD's. Chapter (names, the prose for the non-recurring theorems, glossary,
section 9 counts, totals), Lean README, zero-premise plan status, unification plan row and bullet, study section and
English block with the closing totals, the reading entry and its chapter hash. History keeps the old names."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import p58c_names as N  # noqa: E402

ROOT = Path(sys.argv[1]).resolve()
LB = 'experiments/integrated-correction/general-framework/generative-basis/lean'
CORE_R = f'{LB}/becoming/becoming-verification.json'
PERI_R = f'{LB}/universal-ethics/generative-capacity/correction-inquiry-verification.json'
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
CHAPTER = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
README = ROOT / f'{LB}/becoming/README.md'
PLAN, ZERO, STUDY = RF / 'BECOMING-UNIFICATION-PLAN.md', RF / 'ZERO-PREMISE-PLAN.md', RF / 'BECOMING-RENEWAL-READING.md'
DATA = ROOT / 'theories/becoming/results/data/arguments-m-z.json'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-12-rest-family-strengths.md'


def head(path):
    return json.loads(subprocess.run(['git', '-C', str(ROOT), 'show', f'HEAD:{path}'], check=True,
                                     capture_output=True, text=True).stdout)


core, peri, old = json.loads((ROOT / CORE_R).read_text()), json.loads((ROOT / PERI_R).read_text()), head(CORE_R)
assert core['status'] == 'passed' and peri['status'] == 'passed' and core['utc'] != old['utc']


def totals(r):
    spine = [m for m in r['modules'] if m['spine']]
    assert all(not v for m in spine for v in m['axiom_dependencies'].values())
    return (sum(m['theorems'] for m in spine), sum(len(m['declarations']) for m in spine), len(r['core_closure']),
            len(spine), {m['module']: m['theorems'] for m in r['modules']})


TH, AU, CL, PK, COUNT = totals(core)
OTH, OAU, OCL, OPK, OCOUNT = totals(old)
assert (CL, PK) == (OCL, OPK)
RUN, PERI = core['utc'], peri['utc']
CHANGED = {m: (OCOUNT[m], n) for m, n in COUNT.items() if OCOUNT.get(m) != n}
assert set(CHANGED) == {'Becoming.Space', 'Becoming.Locality', 'Becoming.Resolution'}, CHANGED
s0 = STUDY.read_text()
SEC = max(int(x) for x in re.findall(r'^## (\d+)\. ', s0, re.M)) + 1
REN = len(N.MAP['renames'])
UNREF = sorted(n for _, _, n in N.MAP['renames'] if n.split('.')[-1].endswith('_unrefuted') or '_unrefuted_' in n)
NOTREC = sorted(n for _, _, n in N.MAP['renames'] if n not in UNREF)


def once(text, old_, new, where, count=1):
    n = text.count(old_)
    assert n == count, (where, n, old_[:100])
    return text.replace(old_, new)


# ---------------------------------------------------------------- chapter
c = N.rename(CHAPTER.read_text())
for old_, new, *k in [
    # non-recurrence said as such
    ('从某步起不再上升的可观测量，只能下降有限次。**', '从某步起不再上升的可观测量，不在任意晚的步下降。**'),
    ('- 无更新汲取：汲取者的活跃只有有限次。', '- 无更新汲取：汲取者不在任意晚的步活跃。'),
    ('an observable that never rises from some step on falls only finitely often.**',
     'an observable that never rises from some step on does not fall at arbitrarily late steps.**'),
    ('以不被更新的条件为条件的生起停止；', '以不被更新的条件为条件的生起不复现；'),
    ('Arising on a consumed condition ceases, and', 'Arising on a consumed condition does not recur, and'),
    ('关系项总共有限时它终将停止（`generation_opens`、`generation_not_recurring`）',
     '关系项总共有限时它不复现（`generation_opens`、`generation_not_recurring`）'),
    ('and with finitely many relata in all it stops.', 'and with finitely many relata in all it does not recur.'),
    ('在储备之下醒来只有有限多次，', '在储备之下醒来不在任意晚的步发生，'),
    ('under a reserve, waking recurs only finitely often,', 'under a reserve, waking does not recur at arbitrarily late steps,'),
    ('交换也归于静止', '交换也不复现', 2),
    ('the exchange comes to rest too', 'the exchange does not recur either', 2),
    ('满足它们而每步都被围住的互利者归于静止，每个前提都起约束的 `hatch` 也在一次生起与一次止息之后归于静止',
     '满足它们而每步都被围住的互利者生起不复现，每个前提都起约束的 `hatch` 在一次生起与一次止息之后归于静止'),
    ('and mutualists meeting them with every step enclosed come to rest, as does `hatch`, with every premise binding, after '
     'one arising and one ceasing,',
     'and mutualists meeting them with every step enclosed do not keep arising, while `hatch`, with every premise binding, '
     'comes to rest after one arising and one ceasing,'),
    # stopping that cannot be refuted, the glossary's term
    ('生起停止（`World.arising_stops_unrefuted`），再有活动的普查，止息也停止，',
     '生起从某步起停止不能被否证（`World.arising_stops_unrefuted`），再有活动的普查，止息亦然，'),
    ('arising stops once every step from some step on is enclosed around what stands (`World.arising_stops_unrefuted`), '
     'and with a census of what is active ceasing stops too and',
     'that arising stops cannot be refuted once every step from some step on is enclosed around what stands '
     '(`World.arising_stops_unrefuted`), and with a census of what is active the same holds of ceasing and'),
    ('生起与止息都不再复现，世界归于静止，不用判定程序（`World.rests_unrefuted`，P58）',
     '生起与止息都不再复现，世界归于静止，不用判定程序（`World.rests_unrefuted`，P58；所证强度见术语表，P58c）'),
    ('neither recurs and the world comes to rest, with no decision procedure (`World.rests_unrefuted`, P58)',
     'neither recurs and the world comes to rest, with no decision procedure (`World.rests_unrefuted`, P58; the strength '
     'proved is in the glossary, P58c)'),
]:
    c = once(c, old_, new, 'chapter prose', *k)
GLOSS_OLD = ('| 归于静止 | coming to rest | 生起与止息都不再复现。静止定理：')
GLOSS_NEW = ('| 归于静止 | coming to rest | 从某步起生起与止息都不再发生（`World.RestsFrom`）；找出那一步需要全知原则'
             '（`World.lpo_of_finite_ends`）。定理所证有两种强度，名称随之：从某步起静止不能被否证（名称带 `unrefuted`，'
             '如 `World.rests_unrefuted`），由它生起与止息都不复现（`World.not_recurring_of_rests_unrefuted`）；只证不复现的，'
             '名称带 `not_recurring`；本章说一个定理“归于静止”时指它所证的强度（P58c；中文术语与“静止定理”这一标题由 Ren 定）。'
             '静止定理：')
c = once(c, GLOSS_OLD, GLOSS_NEW, 'glossary')
c = once(c, '| `World.comes_to_rest_unrefuted`、`World.arising_stops_unrefuted`、`World.rest_needs_standing`、`World.rests_unrefuted`、`World.rest_few` |',
         '| `World.RestsFrom`、`World.comes_to_rest_unrefuted`、`World.arising_stops_unrefuted`、`World.rest_needs_standing`、'
         '`World.rests_unrefuted`、`World.not_recurring_of_rests_unrefuted`、`World.rest_few` |', 'glossary names')
lines = c.split('\n')
for mod, (o, n) in CHANGED.items():
    i = next(i for i, l in enumerate(lines) if re.match(r'\| L\d+ \| \[' + re.escape(mod) + r'\]\(', l))
    m = re.search(r'\| (\d+) \|$', lines[i])
    if int(m.group(1)) != o:      # a row stale before this landing is set from the receipt, and reported
        print(f'note: {mod} row said {m.group(1)}, HEAD receipt {o}; now {n}')
    lines[i] = lines[i][:m.start()] + f'| {n} |'
c = '\n'.join(lines)
c = once(c, f'覆盖 {OTH} 项定理、{OAU} 项声明审计', f'覆盖 {TH} 项定理、{AU} 项声明审计', 'zh totals')
c = once(c, f'cover {OTH} theorems and {OAU} declaration audits', f'cover {TH} theorems and {AU} declaration audits', 'en totals')
assert not N.old_left(c), N.old_left(c)
CHAPTER.write_text(c)
print('chapter')

# ---------------------------------------------------------------- Lean README
r = N.rename(README.read_text())
for old_, new in [
    ('取用封闭家族与不被支持的形成的活跃也在那里停止', '取用封闭家族与不被支持的形成的活跃也在那里不复现'),
    ('单位固定时取用封闭家族停止（Flow.taking_not_recurring）', '单位固定时取用封闭家族不复现（Flow.taking_not_recurring）'),
    ('and the activity of an unsupported formation also stop (', 'and the activity of an unsupported formation also do not recur ('),
    ('with the unit fixed, taking from a closed family stops (Flow.taking_not_recurring)',
     'with the unit fixed, taking from a closed family does not recur (Flow.taking_not_recurring)')]:
    r = once(r, old_, new, 'README')
assert not N.old_left(r)
README.write_text(r)
print('README')

# ---------------------------------------------------------------- zero-premise plan: current names, status line
z = N.rename(ZERO.read_text())
ZH = (f'\n\n**现状（P58c）。** 静止一族按所证强度命名（Ren 2026-10-12：“agree with you”，[原话](../../../../{SOURCE})，研究 §{SEC}）：'
      f'从某步起静止不能被否证（`World.RestsFrom`，`World.rests_unrefuted` 等，陈述加强）与只证不复现（`…_not_recurring`）分开；'
      '前者也不用判定程序，止息一半在双重否定之内用有限鸽巢（`Covers.ceasing_stops_unrefuted`）。表中名称为现名。')
EN = (f'\n\n**Status (P58c).** The rest family is named by the strength proved (Ren, 12 October 2026: “agree with you”, '
      f'[source](../../../../{SOURCE}), study section {SEC}): that resting from some step on cannot be refuted '
      '(`World.RestsFrom`, `World.rests_unrefuted` and others, statements strengthened) is kept apart from non-recurrence only '
      '(`…_not_recurring`); the former needs no decision procedure either, the ceasing half using a finite pigeonhole '
      'inside the double negation (`Covers.ceasing_stops_unrefuted`). The tables use the current names.')
z = re.sub(r'(\n\*\*现状（P58、P59）。\*\*[^\n]*)', lambda m: m.group(1) + ZH, z, count=1)
z = re.sub(r'(\n\*\*Status \(P58, P59\)\.\*\*[^\n]*)', lambda m: m.group(1) + EN, z, count=1)
assert ZH in z and EN in z and not N.old_left(z)
ZERO.write_text(z)
print('zero-premise plan')

# ---------------------------------------------------------------- unification plan
ANCHOR = f'{SEC}-静止一族按强度命名p58c'
ROW = (f'| P58c 静止一族按强度命名 ✓ | Ren 2026-10-12（“agree with you”，[来源](../../../../{SOURCE})）：{REN} 个名称改为所证的强度；'
       f'{len(UNREF)} 个陈述加强为从某步起静止（或停止）不能被否证，名带 `unrefuted`；其余只证不复现，名带 `not_recurring`；新增 '
       '`World.RestsFrom`、`World.rests_unrefuted_iff`、`World.not_recurring_of_rests_unrefuted`、`World.restsFrom_of_after`、'
       '`ceasing_steps_unrefuted`、`Covers.ceasing_stops_unrefuted` | 回执 {RUN}（{TH} 项定理、{AU} 项声明审计），外围回执 {PERI}；'
       f'[研究 §{SEC}](BECOMING-RENEWAL-READING.md#{ANCHOR})；尚未经独立审查 |').replace('{RUN}', RUN).replace('{TH}', str(TH)) \
    .replace('{AU}', str(AU)).replace('{PERI}', PERI)
BULLET = (f'- **P58c:** the rest family named by strength (Ren, 12 October 2026: “agree with you”): {REN} names now say the '
          f'strength proved; {len(UNREF)} statements strengthened to resting (or stopping) from some step on being unrefutable, '
          'named with `unrefuted`; the rest prove only non-recurrence and are named with `not_recurring`; new '
          '`World.RestsFrom`, `World.rests_unrefuted_iff`, `World.not_recurring_of_rests_unrefuted`, '
          '`World.restsFrom_of_after`, `ceasing_steps_unrefuted`, `Covers.ceasing_stops_unrefuted`. '
          f'Receipt {RUN}; study section {SEC}. Not yet independently reviewed.')
p = PLAN.read_text().split('\n')
p.insert(max(i for i, l in enumerate(p) if re.match(r'\| P\d', l)) + 1, ROW)
p.insert(max(i for i, l in enumerate(p) if re.match(r'- \*\*P\d', l)) + 1, BULLET)
PLAN.write_text('\n'.join(p))
print('plan')

# ---------------------------------------------------------------- study
def table(rows):
    return '\n'.join(['| 原名 / before | 现名 / now |', '|---|---|'] + [f'| `{o}` | `{n}` |' for o, n in rows])


ren = [(o, n) for _, o, n in N.MAP['renames']]
TAB_U = table([(o, n) for o, n in ren if n in UNREF])
TAB_N = table([(o, n) for o, n in ren if n in NOTREC])
SECTION = f'''## {SEC}. 静止一族按强度命名（P58c）

2026-10-12。Ren 对 AI 的分析答：“agree with you”（[原话](../../../../{SOURCE})）。AI 的建议（Ren 所同意的）：在 Lean 中查哪些静止定理在“停止不能被否证”的形式下成立，成立处如此陈述，名带 unrefuted；只有不复现成立处改名为 …_not_recurring；“在某步停止”“从某步起静止”只留给说出那一步的陈述（需要可判定）。中文术语（归于静止或停）与“静止定理”这一标题仍由 Ren 定；在此之前保留，各 Lean 名称说其确切强度。

“它停止”有三种强度，每种强于下一种：(a) 从某步起不再发生（`World.RestsFrom` 是世界的这一形式）；(b) 这一点不能被否证（`¬¬∃N, RestsFrom N`）；(c) 不复现（并非在任意晚的步发生）。对有限的、满足前提的世界，(a) 蕴含有限全知原则（`World.lpo_of_finite_ends`），所以核心证 (b) 与 (c)。

```text
Result(s): 改名与加强，不是新结果；space-and-its-parts（RestsFrom、rests_unrefuted_iff、not_recurring_of_rests_unrefuted）、
           laws-of-one-step（ceasing_steps_unrefuted、Covers.ceasing_stops_unrefuted）、rest-with-refinement-counted
           （restsFrom_of_after）加入新声明；17 项记录改用新名
Delta: {REN} 个名称；{len(UNREF)} 个陈述由 (c) 加强为 (b)，名带 unrefuted；其余陈述不变，名带 not_recurring。双重否定移不过
       全称量词，所以止息一半在双重否定之内作有限鸽巢（Covers.ceasing_stops_unrefuted，由 ceasing_steps_unrefuted）；生起与止息两
       半在共同的一步合起（World.rests_unrefuted_iff）
Supplied premises / correspondence: 无新前提；各定理的前提不变
Evidence: 合并检查器回执 {RUN}（{TH} 项定理、{AU} 项声明审计，全部源声明公理报告为空；核心闭包 {CL} 个模块，包 {PK} 个），外围回执 {PERI}
Boundary: (a) 需要全知原则，不证；交换一族（经 exchange_recurs_iff）、分辨率的量子路线、Recurrence、Reserve、Dissipation、Renewal、
          Change 仍为 (c)，其 (b) 形式尚未证，是后续；见证 rests_needs、rest_needs_census、rest_needs_standing、rest_needs_quantum 的
          名称不变，复现驳倒每一种强度；继承模块（RelationalRenewal 的 unrenewed_drawdown_finite）保留其范围；尚无独立审查
Integration: 核心 Space、Locality、Openness、Resolution、Premises、Sampling、Counting、Decidedness 的陈述与名称，Change、Dissipation、
             Flow、Generation、Interdependence、Recurrence、Renewal、Reserve、Roles、Units 的名称与文档字符串；章节术语表、§9 计数与
             总数；Lean README；零前提计划；统一计划；阅读条目；17 项记录；工作板 P58c
```

**加强为不能被否证（名带 unrefuted）。**

{TAB_U}

**只证不复现（名带 not_recurring）。**

{TAB_N}

**证明。** 生起一半用 P58b 的 `Flow.change_stops_unrefuted`（不上升的量的下降从某步起停止不能被否证）。止息一半：在覆盖列表之下，止息若在此后每一步之后都不能被否证，则在双重否定之内可以造出任意长的、不重复的止息之步列表（`ceasing_steps_unrefuted`，递归），每个止息之前须有生起，鸽巢使生起在任意晚处不能被否证，与生起一半矛盾（`Covers.ceasing_stops_unrefuted`）。目标是 False，所以在双重否定之内构造是可行的；双重否定移位（DNS）不可用，这一步不能省。两半各给一个起点，取二者之和即共同的一步（`World.rests_unrefuted_iff`）。

**作者反审。**
1. **陈述是否只加强，从不减弱？** 是：每个改了陈述的定理，旧陈述是新陈述的推论（`World.not_recurring_of_rests_unrefuted`），原来用旧陈述的地方都经它改写，检查器通过。
2. **(b) 是否真比 (c) 强？** 在构造逻辑中，(b) 推出 (c)；反过来需要双重否定移位，不可用。
3. **为什么不陈述 (a)？** 对每个有限的满足前提的世界陈述 (a) 就蕴含 LPO（`World.lpo_of_finite_ends`）。
4. **“归于静止”仍在章节文字中。** 术语由 Ren 定；术语表说明本章说一个定理归于静止时指它所证的强度。“只有有限次”“停止”说不复现的定理处已改为“不在任意晚的步”“不复现”。
5. **名称冲突。** `Flow.exchanges_finitely` 改名为 `Flow.exchange_not_recurring_around`，因为 Resolution 已有 `Flow.exchange_not_recurring`（取用至少 1/p 单位）。

**边界。** 历史文字（此前各节、工作板、冻结的落地包、来源、审查、记录的历史与验证范围）保留当时的名称；OPENING 的脚注引 `World.rests_enclosed`，只与 Ren 一起改，留给 Ren。尚无独立审查。

'''
s = once(s0, '\n## English summary\n', '\n' + SECTION + '## English summary\n', 'study zh')
EN_BLOCK = f'''**The rest family by strength (P58c).** To the AI's analysis Ren answered “agree with you” on 12 October 2026 ([source](../../../../{SOURCE})): check in Lean which rest theorems hold in the form that the stopping cannot be refuted, state them so with “unrefuted” in the name, rename those proving only non-recurrence to `…_not_recurring`, and keep “stops at” or “rests from” for statements naming a step, which need decidedness. The Chinese term (归于静止 or 停) and the heading “the rest theorem” stay Ren's; until then each Lean name states its exact strength.
- **Three strengths.** (a) From some step on nothing happens (`World.RestsFrom` for a world); (b) that cannot be refuted (`¬¬∃N, RestsFrom N`); (c) it does not recur. (a) for every finite world meeting the premises gives the limited principle of omniscience (`World.lpo_of_finite_ends`), so the core proves (b) and (c).
- **What changed.** {REN} names; {len(UNREF)} statements strengthened from (c) to (b), named with `unrefuted` (among them `World.rests_unrefuted`, `World.comes_to_rest_unrefuted`, `World.premised_rests_unrefuted`, `World.sample_rests_unrefuted`, `World.rests_unrefuted_enclosed`); the rest keep their statements and are named with `not_recurring`. The ceasing half is a finite pigeonhole built inside the double negation (`ceasing_steps_unrefuted`, `Covers.ceasing_stops_unrefuted`), since the double negation shift is not available; the halves join at a common step (`World.rests_unrefuted_iff`).
- **Boundary.** The exchange family, the quantum routes of Resolution, Recurrence, Reserve, Dissipation, Renewal and Change stay at (c) for now; the witnesses keep their names, recurrence refuting every strength. History keeps the old names; the OPENING footnote's `World.rests_enclosed` is Ren's to change.

Receipt {RUN}. Not yet independently reviewed; the author's counterreview is in section {SEC}.

'''
last = s.rindex('\nThe package now has ') + 1
hd, tl = s[:last], s[last:]
tl = once(tl, f'The package now has {OTH} theorems and {OAU} declaration audits', f'The package now has {TH} theorems and {AU} declaration audits', 'study totals')
assert len(re.findall(r'sections 63 to 69, 71 to \d+ \(', tl)) == 1
tl = re.sub(r'(sections 63 to 69, 71 to )\d+( \()', r'\g<1>' + str(SEC) + r'\2', tl)
assert len(re.findall(r'The periphery bridge passed against this core \(receipt \d{8}T\d{6}\.\d+Z\)', tl)) == 1
tl = re.sub(r'(The periphery bridge passed against this core \(receipt )\d{8}T\d{6}\.\d+Z\)', r'\g<1>' + PERI + ')', tl)
STUDY.write_text(hd + EN_BLOCK + tl)
assert re.search(rf'^## {SEC}\. 静止一族按强度命名（P58c）$', STUDY.read_text(), re.M)
print('study section', SEC)

# ---------------------------------------------------------------- reading entry
raw = DATA.read_text()
rows = json.loads(raw)
e = next(x for x in rows if x['id'] == 'the-theory-of-becoming')
headc = subprocess.run(['git', '-C', str(ROOT), 'show', 'HEAD:theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'],
                       check=True, capture_output=True).stdout
assert e['source_sha256'] == hashlib.sha256(headc).hexdigest(), 'reading entry stale before P58c: reread first'
e['argument_zh'] = once(e['argument_zh'], '不上升的量的下降从某步起停止不能被否证；',
                        '不上升的量的下降从某步起停止不能被否证；静止定理所证为世界从某步起静止不能被否证，只证不复现者名为不复现（P58c）；', 'cat zh')
e['argument_en'] = once(e['argument_en'], 'stops falling from some step on;',
                        'stops falling from some step on; what the rest theorems prove is that the world resting from some step on '
                        'cannot be refuted, and those proving only non-recurrence are named so (P58c);', 'cat en')
e['source_sha256'] = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
indent = 2 if raw.startswith('[\n  {') else 1
out = json.dumps(rows, ensure_ascii=False, indent=indent) + ('\n' if raw.endswith('\n') else '')
assert json.loads(out) == rows
DATA.write_text(out)
print('reading entry; hash', e['source_sha256'][:12])
print('SECTION', SEC)
