#!/usr/bin/env python3
"""A4 (19 October 2026): the readings in one account (DELEGATED-CHOICES D45) in the live fields of the records.

Ren, 19 October 2026, answering Parts C and D of the decision brief: "integrate all, the theory is a whole, not stitched
pieces, go ahead" (sources/15-codex-theory-conversations/2026-10-19-integrate-all.md). What this kit changes:

1. R18 (D45 (4)). The eighteenth review counts as the review its records asked for. The records it reviewed and that
   still say "not independently reviewed" say that it reviewed them, as the nine records already do; records it did
   not cover keep the phrase. seeking-boundary and target-capture lose the question they left to Ren; both are
   schema 1, so their text grows no more than the growth ratchet allows (tools/research/style.py).
2. The readings D45 decides: where-a-level-couples (adopted) and the conjecture of observation-is-a-route (D45 (3));
   sensitivity-is-the-least-registration and how-much-difference-arrives (识 answered, D37, D39); axiom-decomposition
   (D21 (4) revised); unceasing-generation-needs-renewal (D3 revised); the four records whose readings chapter section
   7 adopts (D45 (2)); two dependency conditions still saying "pending Ren" for readings D11 and D17 decided.
3. 停息 (D45 (4)). The rest family's Chinese term in every live Chinese field is 停息, as in the chapter. Two named
   objects that never move keep 静止: the still flow (`Flow.still`, where nothing takes part) and the static process
   of DynamicConsequences. A Chinese title that changes keeps its old form as an alias.

Every block must match exactly once in its field, in one of its variants (main's text, or N6's, which lands first);
each record changed gets one history note, and a record already carrying it is skipped. History, aliases (apart from
the added old titles), references, proof bindings, text versions and progress logs are not edited.

usage: python3 -B apply_records.py [--check] [ROOT]    (--check counts every block and writes nothing)
After apply_chapter.py and this kit, rehash_refs.py re-points the references to the changed files."""
import glob, json, os, re, sys

ARGS = [a for a in sys.argv[1:] if not a.startswith('--')]
CHECK = '--check' in sys.argv
ROOT = ARGS[0] if ARGS else '.'
REC = os.path.join(ROOT, 'theories/becoming/results/records/')
NOTE = '19 October 2026, A4 (Ren'
ANSWER_EN = '"integrate all, the theory is a whole, not stitched pieces, go ahead"'
SKIP = {'history', 'aliases', 'references', 'proof_bindings', 'text_versions', 'progress'}

# ----------------------------------------------------------------------------------------------------- 1. R18
R18_CORRECTED = [
    'observation-is-a-route', 'orders-as-a-sum-over-histories', 'premises-read-off-the-exchange',
    'selection-through-a-model-of-the-options', 'sensitivity-is-the-least-registration', 'typicality-by-counting',
    'unity-of-readings', 'weights-count-situations', 'what-a-finite-history-refutes',
    'what-a-law-of-the-whole-and-no-part-takes', 'where-a-run-goes-on', 'where-novelty-gain-comes-from',
]
R18_CONFIRMED = ['returning-novelty-forgetting-on-levels', 'what-a-cut-loses']  # C1 and C6: no correction asked
REVIEWED_EN = 'reviewed by the eighteenth review (AI, read-only, no Lean rebuild), '
REVIEWED_ZH = '经第十八次审查（AI，只读，未重建 Lean）审阅，'
R18_EN = ('the eighteenth review counts as the review this record asked for (DELEGATED-CHOICES D45 (4)), so the '
          'validation scope says that it reviewed the record (AI, read-only, no Lean rebuild), in place of "not '
          'independently reviewed"')
R18_ZH = '第十八次审查算作本记录所要求的审查（DELEGATED-CHOICES D45 (4)），验证范围写明它审阅了本记录（AI，只读，未重建 Lean），代替“未经独立审查”'
QUESTION_EN = ('the question this record left to Ren, whether it needs a review, is answered (DELEGATED-CHOICES D45 '
               '(4)): it needs the review the eighteenth review gave the modules it covered, which no reviewer has '
               'given it yet')
QUESTION_ZH = '本记录留给 Ren 的问题（是否需要审查）已回答（DELEGATED-CHOICES D45 (4)）：它需要第十八次审查给其所覆盖模块的那种审查，尚无审查者给过它'

E = {}  # record id -> [(field path, [old variants], new)]
H = {}  # record id -> [(en, zh)] history parts

for rid in R18_CORRECTED + R18_CONFIRMED:
    tail_en = 'whose corrections are applied.' if rid in R18_CORRECTED else 'which asked no correction.'
    tail_zh = '其更正已处理。' if rid in R18_CORRECTED else '未要求更正。'
    if rid == 'selection-through-a-model-of-the-options':
        en = [(('validation_scope', 'en'), ['Not independently reviewed.'], 'R' + REVIEWED_EN[1:] + tail_en)]
    else:
        en = [(('validation_scope', 'en'), ['not independently reviewed.'], REVIEWED_EN + tail_en)]
    E[rid] = en + [(('validation_scope', 'zh'), ['未经独立审查。'], REVIEWED_ZH + tail_zh)]
    H[rid] = [(R18_EN, R18_ZH)]

for rid in ('seeking-boundary', 'target-capture'):
    E[rid] = [
        (('validation_scope', 'en'), ["not independently reviewed, whether it needs a review is Ren's call."],
         'not independently reviewed; it needs a review such as the eighteenth was (DELEGATED-CHOICES D45 (4)).'),
        (('validation_scope', 'zh'), ['未作独立审查，是否需要交 Ren。'], '未作独立审查；需要如第十八次审查的审查（D45 (4)）。'),
    ]
    H[rid] = [(QUESTION_EN, QUESTION_ZH)]

# ----------------------------------------------------------------------------------------------- 2. readings
ONE = 'by its place in one account'

E['where-a-level-couples'] = [
    (('correspondence', 'en'),
     ['It also answers, for the level branch, the question observation-is-a-route leaves open, whether observation is '
      'a second kind of relation beside dependence: obs marks where a level can couple into a formation by level.'],
     'It also answers, for the level branch, the question observation-is-a-route leaves open, whether observation is '
     'a second kind of relation beside dependence, in the sense that both are coupling: obs marks where a level can '
     'couple into a formation by level, as dependence marks where it couples by threshold; whether obs could be '
     'derived from dependence stays a conjecture there.'),
    (('correspondence', 'en'),
     ["Reading (the AI's, open): registration bounds coupling, and a law's responses are its couplings.",
      "Reading (the AI's, open): what couples in bounds what a law can respond to, and a law's responses are its "
      "couplings."],
     "Reading (the AI's, adopted on 19 October 2026 " + ONE + ", DELEGATED-CHOICES D45): obs and dependence are both "
     "coupling, by level and by threshold; what couples in bounds what a law can respond to without fixing it "
     "(ExchangeLaw.response_not_fixed_by_coupling), and a law's responses are its couplings."),
    (('correspondence', 'zh'),
     ['它也就水平一支回答 observation-is-a-route 留下的问题，即观察是否为依赖之外的第二种关系：obs 标出水平能经水平耦合入形成之处。'],
     '它也就水平一支、在两者都是耦合的意义上，回答 observation-is-a-route 留下的问题，即观察是否为依赖之外的第二种关系：obs '
     '标出水平能经水平耦合入形成之处，如依赖标出经阈耦合之处；obs 能否由依赖推出，在那里仍是猜想。'),
    (('correspondence', 'zh'),
     ['读法（AI 的，未定）：所识界定耦合，律的回应即其耦合。', '读法（AI 的，未定）：耦合入者界定律能回应者，律的回应即其耦合。'],
     '读法（AI 的，2026年10月19日以其在一个说明中的位置采用，DELEGATED-CHOICES D45）：obs 与依赖都是耦合，经水平与经阈；'
     '耦合入者界定律能回应者而不确定它（ExchangeLaw.response_not_fixed_by_coupling），律的回应即其耦合。'),
]
H['where-a-level-couples'] = [(
    'the open reading is adopted ' + ONE + ' (DELEGATED-CHOICES D45 (3)): it and the conjecture of '
    'observation-is-a-route said one thing two ways, and the account keeps both senses apart; observation is no second '
    'relation in the sense that obs and dependence are both coupling, and whether obs could be derived from dependence '
    'stays a conjecture. Before: "{b1}"',
    '开放的读法以其在一个说明中的位置采用（DELEGATED-CHOICES D45 (3)）：它与 observation-is-a-route 的猜想以两种方式说同一件事，'
    '这个说明把两种意义分开；在 obs 与依赖都是耦合的意义上，观察不是第二种关系，obs 能否由依赖推出仍是猜想。原文见英文')]

E['observation-is-a-route'] += [
    (('correspondence', 'en'),
     ['That observation is not a second relation beside dependence goes beyond the theorem, which shows only that '
      'observation does not go beyond dependence, not that it is dependence; it is kept as a conjecture, not a '
      'reading.'],
     'That observation is not a second relation beside dependence, in the sense that obs could be derived from '
     'dependence, goes beyond the theorem, which shows only that observation does not go beyond dependence, not that '
     'it is dependence; it is kept as a conjecture, not a reading. In the sense that obs and dependence are both '
     'coupling, by level and by threshold, it holds (where-a-level-couples, adopted ' + ONE + ', DELEGATED-CHOICES '
     'D45).'),
    (('correspondence', 'zh'),
     ['观察不是依赖之外的第二种关系，超出定理：定理只表明观察不越出依赖，未表明观察就是依赖；它作为猜想保留，不是读法。'],
     '在 obs 能由依赖推出的意义上，观察不是依赖之外的第二种关系，超出定理：定理只表明观察不越出依赖，未表明观察就是依赖；'
     '它作为猜想保留，不是读法。在 obs 与依赖都是耦合（经水平与经阈）的意义上，它成立（where-a-level-couples，以其在一个说明中'
     '的位置采用，DELEGATED-CHOICES D45）。'),
    (('next_delta', 'en'), ['the conjecture that observation is not a second relation beside dependence;'],
     'the conjecture that obs could be derived from dependence;'),
    (('next_delta', 'zh'), ['观察不是依赖之外第二种关系这一猜想；'], 'obs 能由依赖推出这一猜想；'),
]
H['observation-is-a-route'] += [(
    'the conjecture is stated in its exact sense, that obs could be derived from dependence; in the sense that obs '
    'and dependence are both coupling it holds, as where-a-level-couples reads it (DELEGATED-CHOICES D45 (3)). '
    'Before: "That observation is not a second relation beside dependence goes beyond the theorem, which shows only '
    'that observation does not go beyond dependence, not that it is dependence; it is kept as a conjecture, not a '
    'reading"',
    '猜想以其确切意义陈述：obs 能由依赖推出；在 obs 与依赖都是耦合的意义上它成立，如 where-a-level-couples 所读'
    '（DELEGATED-CHOICES D45 (3)）。原文见英文')]

# seeking-boundary keeps its readings: they read 无明 as locked seeking, as D45 does, and 明 as N6 words it; the
# revision of D26 (the position grounds 无明 and is not it) concerns chapter section 7.2, not this record. The record is
# schema 1, so its correspondence may not grow before migration (tools/research/style.py, growth).

SHI_EN = "识 itself, left to Ren, is answered by the naming study's option (b), DELEGATED-CHOICES D45)"
SHI_ZH = '识本身原留给 Ren，由命名研究的选项 (b) 回答，DELEGATED-CHOICES D45）'
SHI_H_EN = ('the reading kept 识 itself for Ren; the naming study\'s option (b) answers it (DELEGATED-CHOICES D45 (3)): 识 is '
            'a formation\'s own further course through the lumping its own couplings make')
SHI_H_ZH = '读法原把识本身留给 Ren；命名研究的选项 (b) 回答了它（DELEGATED-CHOICES D45 (3)）：识是一个形成自身的进一步历程经其自身耦合所成之归并而行'
for rid, dn in (('sensitivity-is-the-least-registration', 'D37'), ('how-much-difference-arrives', 'D39')):
    E.setdefault(rid, []).extend([
        (('correspondence', 'en'),
         [f"DELEGATED-CHOICES {dn}; 识 itself stays Ren's)", f"DELEGATED-CHOICES {dn}; the word 识 itself stays Ren's)"],
         f'DELEGATED-CHOICES {dn}; ' + SHI_EN),
        (('correspondence', 'zh'),
         [f'DELEGATED-CHOICES {dn}；识本身仍是 Ren 的）', f'DELEGATED-CHOICES {dn}；识这个词本身仍是 Ren 的）'],
         f'DELEGATED-CHOICES {dn}；' + SHI_ZH),
    ])
    H.setdefault(rid, []).append((SHI_H_EN, SHI_H_ZH))

E['axiom-decomposition'] = [
    (('correspondence', 'en'),
     ["DELEGATED-CHOICES D21; whether Ren holds the step of invariance stays Ren's to state)"],
     'DELEGATED-CHOICES D21; the step of invariance stays open as a question of warrant, chapter sections 6.11 and '
     '8.5, not as one pending Ren, D45)'),
    (('correspondence', 'zh'), ['DELEGATED-CHOICES D21；Ren 是否持有不变之步仍由 Ren 陈述）'],
     'DELEGATED-CHOICES D21；不变之步作为根据的问题保持开放，见理论 §6.11 与 §8.5，不是待 Ren 的问题，D45）'),
    (('dependencies', {'id': 'held-lives-g0-is-centering'}, 'detail', 'en'), ["(the AI's reading, pending Ren)"],
     "(the AI's reading, adopted on Ren's delegation, DELEGATED-CHOICES D21)"),
    (('dependencies', {'id': 'held-lives-g0-is-centering'}, 'detail', 'zh'), ['（AI 的读法，待 Ren）'],
     '（AI 的读法，依 Ren 的交托采用，DELEGATED-CHOICES D21）'),
]
H['axiom-decomposition'] = [(
    'whether the step of invariance holds is a question of warrant, on which Ren\'s testimony would be provenance '
    '(DELEGATED-CHOICES D21, revised by D45); the dependency on held-lives-g0-is-centering cites D21, which adopted the '
    'reading it called pending. Before: "whether Ren holds the step of invariance stays Ren\'s to state"; "(the AI\'s '
    'reading, pending Ren)"',
    '不变之步是否成立是根据的问题，Ren 的陈述于此是来历（DELEGATED-CHOICES D21，经 D45 修订）；对 held-lives-g0-is-centering 的'
    '依赖引 D21，它采用了此处称为待定的读法。原文见英文')]

E['consumption-ends-with-feeders'] = [
    (('dependencies', {'id': 'derived-extent-limits'}, 'interface', 'conditions', 'en'), ['The reading pending Ren.'],
     "The AI's reading, adopted on Ren's delegation (DELEGATED-CHOICES D17)."),
    (('dependencies', {'id': 'derived-extent-limits'}, 'interface', 'conditions', 'zh'), ['读法待 Ren。'],
     'AI 的读法，依 Ren 的交托采用（DELEGATED-CHOICES D17）。'),
]
H['consumption-ends-with-feeders'] = [(
    'the dependency on derived-extent-limits called its reading pending; D17 (3) adopted it on Ren\'s delegation (a '
    'loss returning through a feeder), and no reading waits on Ren (DELEGATED-CHOICES D45 (1))',
    '对 derived-extent-limits 的依赖称其读法待定；D17 (3) 已依 Ren 的交托采用它（损失经供给者返回），且不再有读法等待 Ren'
    '（DELEGATED-CHOICES D45 (1)）')]

E['one-axiom-yields-g0'] = [
    (('dependencies', {'id': 'held-lives-g0-is-centering'}, 'interface', 'conditions', 'en'),
     ['Holding; the reading pending Ren.'],
     "Holding; the reading of section 6.7 is the AI's, adopted on Ren's delegation (DELEGATED-CHOICES D11)."),
    (('dependencies', {'id': 'held-lives-g0-is-centering'}, 'interface', 'conditions', 'zh'), ['持有；读法待 Ren。'],
     '持有；第 6.7 节的读法是 AI 的，依 Ren 的交托采用（DELEGATED-CHOICES D11）。'),
]
H['one-axiom-yields-g0'] = [(
    'the dependency on held-lives-g0-is-centering called the reading of section 6.7 pending; D11 (1) adopted it on '
    'Ren\'s delegation (S0 as the reading of wanting), and no reading waits on Ren (DELEGATED-CHOICES D45 (1))',
    '对 held-lives-g0-is-centering 的依赖称第 6.7 节的读法待定；D11 (1) 已依 Ren 的交托采用它（S0 读作想要），且不再有读法等待 Ren'
    '（DELEGATED-CHOICES D45 (1)）')]

E['unceasing-generation-needs-renewal'] = [
    (('correspondence', 'en'),
     ['on Ren\'s delegation the second 生 ranges over what can form, and arising on depletion is classed by the '
      'comparison (DELEGATED-CHOICES D3).'],
     'on Ren\'s delegation the second 生 is further generation, what can form together with the conditions and '
     'generators of further forming, and arising on depletion is classed by the comparison, which reads what can form '
     '(DELEGATED-CHOICES D3, revised ' + ONE + ', D45).'),
    (('correspondence', 'zh'), ['依 Ren 的交托，第二个“生”的范围是能形成者，以消耗为条件的生起由比较分类（DELEGATED-CHOICES D3）。'],
     '依 Ren 的交托，第二个“生”是进一步的生成，即能形成者连同进一步形成的条件与生成者，以消耗为条件的生起由比较分类，比较读的是'
     '能形成者（DELEGATED-CHOICES D3，以其在一个说明中的位置修订，D45）。'),
]
H['unceasing-generation-needs-renewal'] = [(
    'the second 生 is further generation, as D1\'s revision makes it part of 生生; what can form stays the part the '
    'comparison reads (DELEGATED-CHOICES D3, revised by D45). Before: "the second 生 ranges over what can form"',
    '第二个“生”是进一步的生成，D1 的修订使之成为生生的一部分；能形成者仍是比较所读的部分（DELEGATED-CHOICES D3，经 D45 修订）。原文见英文')]

SEC7_EN = ("Reading (the AI's, adopted in one account with the scope of chapter section 7, DELEGATED-CHOICES D45):")
SEC7_ZH = '读法（AI 的，以理论第 7 节的范围在一个说明中采用，DELEGATED-CHOICES D45）：'
SEC7_H = ('the reading is adopted with the scope of chapter section 7, whose readings were marked open until 19 October '
          '2026 (DELEGATED-CHOICES D45 (2))',
          '读法以理论第 7 节的范围采用，该节的读法在 2026年10月19日之前标为开放（DELEGATED-CHOICES D45 (2)）')
for rid in ('the-gap-for-ones-own-act', 'raising-what-couples-in-draws-from-beyond', 'what-pooled-coupling-reaches',
            'what-a-pools-acts-respond-to'):
    E.setdefault(rid, []).extend([
        (('correspondence', 'en'), ["Reading (the AI's):"], SEC7_EN),
        (('correspondence', 'zh'), ['读法（AI 的）：'], SEC7_ZH),
    ])
    H.setdefault(rid, []).append(SEC7_H)
E['what-pooled-coupling-reaches'] += [
    (('correspondence', 'en'), ['as an open AI reading,'],
     'as an open AI reading, adopted on 19 October 2026 ' + ONE + ' (DELEGATED-CHOICES D45),'),
    (('correspondence', 'zh'), ['作为开放的 AI 读法；'], '作为开放的 AI 读法（2026年10月19日以其在一个说明中的位置采用，DELEGATED-CHOICES D45）；'),
]

# ----------------------------------------------------------------------------------------------------- 3. 停息
KEEP = re.compile(r'\]\([^)\n]*\)|`[^`\n]*`|https?://\S+|静止的流（Flow\.still）|静止和翻转过程')
SWEEP_EN = ('the rest family\'s Chinese term in the live Chinese fields is now 停息 ({n} uses), as in the chapter '
            '(DELEGATED-CHOICES D45 (4)); the English is unchanged')
SWEEP_ZH = '中文字段中停息家族的用语由“静止”改为“停息”（{n} 处），与理论章一致（DELEGATED-CHOICES D45 (4)）；英文不变'
TITLE_EN = '; the Chinese title changes with it, and the old one is kept as an alias'
TITLE_ZH = '；中文标题随之改动，旧标题保留为别名'


def sweep(s):
    out, last, n = [], 0, 0
    for m in KEEP.finditer(s):
        part = s[last:m.start()]
        n += part.count('静止')
        out += [part.replace('静止', '停息'), m.group(0)]
        last = m.end()
    n += s[last:].count('静止')
    out.append(s[last:].replace('静止', '停息'))
    return ''.join(out), n


def sweep_tree(x, under_zh=False):
    """Sweep every string under a 'zh' key; return the new tree and the count."""
    if isinstance(x, str):
        return sweep(x) if under_zh else (x, 0)
    if isinstance(x, list):
        pairs = [sweep_tree(v, under_zh) for v in x]
        return [p[0] for p in pairs], sum(p[1] for p in pairs)
    if isinstance(x, dict):
        res, n = {}, 0
        for k, v in x.items():
            res[k], m = sweep_tree(v, under_zh or k == 'zh')
            n += m
        return res, n
    return x, 0


# ----------------------------------------------------------------------------------------------------- apply
def locate(d, path):
    for k in path[:-1]:
        if isinstance(k, dict):
            hits = [x for x in d if all(x.get(a) == b for a, b in k.items())]
            if len(hits) != 1:
                raise KeyError(f'{k}: {len(hits)} entries')
            d = hits[0]
        else:
            d = d[k]
    return d, path[-1]


def edit(rid, d, bad):
    matched = []
    for path, olds, new in E.get(rid, []):
        try:
            parent, key = locate(d, path)
        except (KeyError, IndexError) as e:
            bad.append((rid, path, f'no field ({e})'))
            continue
        hits = [o for o in olds if parent[key].count(o)]
        if len(hits) != 1 or parent[key].count(hits[0]) != 1:
            bad.append((rid, path, [parent[key].count(o) for o in olds], olds[0][:80]))
            matched.append('')
            continue
        parent[key] = parent[key].replace(hits[0], new)
        matched.append(hits[0].rstrip('.;'))
    return matched


def main():
    files = sorted(glob.glob(REC + '*.json'))
    known = {os.path.basename(f)[:-5] for f in files}
    missing = sorted(set(E) - known)
    if missing:
        sys.exit(f'records not found: {missing}')
    aliases = {}
    for f in files:
        d = json.load(open(f, encoding='utf-8'))
        for a in [d['id']] + d.get('aliases', []):
            aliases[a.casefold()] = d['id']
    bad, plan, swept = [], [], 0
    for f in files:
        rid = os.path.basename(f)[:-5]
        d = json.load(open(f, encoding='utf-8'))
        if any(h.get('en', '').startswith(NOTE) for h in d.get('history', [])):
            print('already applied', rid)
            continue
        matched = edit(rid, d, bad)
        old_title = d['title'].get('zh', '') if isinstance(d.get('title'), dict) else ''
        n = 0
        for k in list(d):
            if k not in SKIP:
                d[k], m = sweep_tree(d[k], k == 'zh')
                n += m
        parts = []
        for en, zh in H.get(rid, []):
            for i, m in enumerate(matched):
                en = en.replace('{b%d}' % i, m)
            parts.append((en, zh))
        if n:
            en, zh = SWEEP_EN.format(n=n), SWEEP_ZH.format(n=n)
            if isinstance(d.get('title'), dict) and d['title'].get('zh', '') != old_title:
                if aliases.get(old_title.casefold(), rid) != rid:
                    bad.append((rid, 'alias', old_title, 'owned by ' + aliases[old_title.casefold()]))
                elif old_title not in d['aliases']:
                    d['aliases'].append(old_title)
                en, zh = en + TITLE_EN, zh + TITLE_ZH
            parts.append((en, zh))
            swept += n
        if parts:
            plan.append((f, rid, d, parts, n))
    for b in bad:
        print('MISMATCH', b)
    if bad:
        sys.exit(1)
    edited = sum(1 for _, rid, _, _, _ in plan if rid in E)
    print(f'{sum(len(v) for v in E.values())} blocks in {len(E)} records match once; {swept} uses of 静止 -> 停息 in '
          f'{sum(1 for p in plan if p[4])} records; {len(plan)} records change ({edited} with blocks)')
    if CHECK:
        return
    for f, rid, d, parts, _ in plan:
        en = '; '.join(p[0] for p in parts)
        zh = '；'.join(p[1] for p in parts)
        d['history'].append({
            'en': f'{NOTE} 19 October: {ANSWER_EN}): {en[0].upper() + en[1:]}. The claim is unchanged.',
            'zh': f'2026年10月19日，A4（Ren 10月19日的回答：“integrate all, the theory is a whole, not stitched pieces, go '
                  f'ahead”）：{zh}。论断不变。'})
        open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print('applied to', len(plan), 'records')


if __name__ == '__main__':
    main()
