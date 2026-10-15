#!/usr/bin/env python3
"""I4a step 4: python3 -B table.py DIR [--write]

DIR holds connect.json from inventory.py, connect.py and similar.py. The rows proposed for every module are in
rows/*.jsonl beside this script. Checks every row against RUBRIC.md: every stem exactly once, a known category and
basis, `statements read` for an earlier version or a join candidate, reasons within length, and no market word
outside backticks. Prints the counts as JSON. With --write, renders MODULE-CLASSIFICATION.md in the study folder:
- the counts;
- the earlier versions, and the join candidates grouped by the themes in themes.json (what Ren decides on);
- every module by family.
"""
import collections
import json
import re
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent
THEMES = json.loads((KIT / 'themes.json').read_text())['themes']
STUDY_DIR = KIT.parents[1]
OUT = STUDY_DIR / 'MODULE-CLASSIFICATION.md'
# The P3 classification of the ethics modules (9 October), for the modules it shares with this table.
P3 = STUDY_DIR / 'BECOMING-INSTANCE-CLASSIFICATION.md'
P3_DATA = STUDY_DIR / 'BECOMING-INSTANCE-CHECKS.json'
P3_NAMES = {'interface': 'interface instantiated', 'core': 'already on the core', 'history': 'polymorphic over histories',
            'renewal': 'renewal bounds on runs', 'mathlib': 'Mathlib leaf', 'model': 'concrete model', 'bridge': 'bridge'}
UP = '../../../../'
L = 'experiments/integrated-correction/general-framework/generative-basis/'
CATEGORIES = {
    'joined': ('已接入', 'joined'),
    'earlier-version': ('较早的版本', 'earlier version'),
    'join-candidate': ('待接入的律', 'join candidate'),
    'application': ('应用', 'application'),
    'artifact': ('工作证据', 'working artifact'),
    'snapshot': ('仅存快照', 'snapshot only'),
}
BASES = {'statements read', 'header read'}
MARKET = re.compile(r'\b(budget|price|priced|cost|costs|costly|pay|paid|payment|credit|profit|market)\b', re.I)
REACH = {'core/bridge': ('核心或桥接', 'core or bridge'), 'inherited': ('继承模块', 'inherited module'),
         'foundation only': ('只到基础', 'foundation only'), 'none': ('不及运行', 'none'), 'snapshot': ('快照', 'snapshot')}


def family(path):
    if path.startswith(L + 'lean/'):
        parts = path[len(L + 'lean/'):].split('/')
        return 'lean/' + (parts[0] if len(parts) > 1 else '(root)')
    if path.startswith(L):
        return path[len(L):].split('/')[0]
    if path.startswith('_process/'):
        return '_process'
    return '/'.join(path.split('/')[:2])


def load(directory):
    signals = {r['stem']: r for r in json.loads((Path(directory) / 'connect.json').read_text())}
    rows, problems = {}, []
    for f in sorted((KIT / 'rows').glob('*.jsonl')):
        for n, line in enumerate(f.read_text().splitlines(), 1):
            if not line.strip():
                continue
            r = json.loads(line)
            where = f'{f.name}:{n} {r.get("stem")}'
            if r.get('stem') in rows:
                problems.append(f'{where}: duplicate stem')
            rows[r.get('stem')] = r
            if r.get('stem') not in signals:
                problems.append(f'{where}: unknown stem')
            if r.get('category') not in CATEGORIES:
                problems.append(f'{where}: category {r.get("category")!r}')
            if r.get('basis') not in BASES:
                problems.append(f'{where}: basis {r.get("basis")!r}')
            if r.get('category') in ('earlier-version', 'join-candidate') and r.get('basis') != 'statements read':
                problems.append(f'{where}: {r["category"]} needs statements read')
            if r.get('category') == 'earlier-version' and not r.get('spine'):
                problems.append(f'{where}: earlier version names no spine declaration')
            # English in words; Chinese in Chinese characters (identifiers in backticks or Latin script not counted).
            for key, limit in (('reason_en', 60), ('reason_zh', 75)):
                text = r.get(key) or ''
                size = len(text.split()) if key == 'reason_en' else len(re.findall(r'[\u4e00-\u9fff]', text))
                if not text or size > limit:
                    problems.append(f'{where}: {key} missing or {size} long')
                if MARKET.search(re.sub(r'`[^`]*`', '', text)):
                    problems.append(f'{where}: market word in {key}')
    themed = collections.Counter(x for t in THEMES.values() for x in t['stems'])
    for k, r in rows.items():
        if (r.get('category') == 'join-candidate') != (themed[k] == 1):
            problems.append(f'{k}: {r.get("category")} with {themed[k]} themes')
    missing = sorted(set(signals) - set(rows))
    return signals, rows, problems, missing


def reach(s):
    return 'snapshot' if s['snap'] else s.get('reach_kind') or ('none' if not s['reach_run'] else 'foundation only')


def cell(text):
    return (text or '').replace('|', '\\|').replace('\n', ' ')


def render(signals, rows):
    p3 = {k: v['category'] for k, v in json.loads(P3_DATA.read_text())['modules'].items()}
    merged = [(signals[k], rows[k]) for k in sorted(rows, key=lambda k: (family(rows[k]['path']), k.lower()))]
    by_cat = collections.Counter(r['category'] for _, r in merged)
    by_reach = collections.Counter((reach(s), r['category']) for s, r in merged)
    theorems = collections.Counter()
    for s, r in merged:
        theorems[r['category']] += s['theorems']
    lines = ['# 脊柱运行之外的模块归类（草稿）/ Modules outside the spine run, classified (draft)', '',
             '生成：`development/integration-i4a/table.py`。Ren 2026-10-15 选择“Draft the table first”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-15-i4-classification-table.md)）：这是只读的草稿，每行的类别是 AI 的读法，Ren 决定之前不标注、不移动、不删除任何文件。归类规则见 [RUBRIC.md](development/integration-i4a/RUBRIC.md)。',
             '',
             'Generated by `development/integration-i4a/table.py`. Ren chose “Draft the table first” on 15 October 2026 ([source](../../../../sources/15-codex-theory-conversations/2026-10-15-i4-classification-table.md)). This is a read-only draft. Each row’s category is an AI reading, and nothing is marked, moved or deleted before Ren decides. The rules are in [RUBRIC.md](development/integration-i4a/RUBRIC.md).',
             '', '## 总数 / Totals', '',
             '| 类别 / Category | 模块 / Modules | 定理 / Theorems |', '|---|---:|---:|']
    for c, (zh, en) in CATEGORIES.items():
        lines.append(f'| {zh} / {en} | {by_cat[c]} | {theorems[c]} |')
    lines += [f'| 合计 / Total | {len(merged)} | {sum(theorems.values())} |', '',
              '| 经导入所及 / Reaches the run through imports | ' + ' | '.join(f'{CATEGORIES[c][1]}' for c in CATEGORIES) + ' |',
              '|---|' + '---:|' * len(CATEGORIES)]
    for k, (zh, en) in REACH.items():
        lines.append(f'| {zh} / {en} | ' + ' | '.join(str(by_reach[(k, c)]) for c in CATEGORIES) + ' |')
    def decision_table(picked):
        out = ['| 模块 / Module | 脊柱 / Spine | 关系 / Relation | 理由 / Reason |', '|---|---|---|---|']
        for s, r in picked:
            out.append(f'| [{s["stem"]}]({UP}{r["path"]}) | ' + ', '.join(f'`{x}`' for x in r.get('spine', [])) +
                       f' | {r.get("relation") or "—"} | {cell(r["reason_zh"])} / {cell(r["reason_en"])} |')
        return out
    zh, en = CATEGORIES['earlier-version']
    picked = [(s, r) for s, r in merged if r['category'] == 'earlier-version']
    lines += ['', f'## {zh} / {en} ({len(picked)})', ''] + decision_table(picked)
    zh, en = CATEGORIES['join-candidate']
    picked = [(s, r) for s, r in merged if r['category'] == 'join-candidate']
    lines += ['', f'## {zh} / {en} ({len(picked)})', '',
              '按主题分组（AI 的分组，见 `development/integration-i4a/themes.json`）。 / Grouped by theme (an AI grouping, in `development/integration-i4a/themes.json`).']
    for t in THEMES.values():
        group = [(s, r) for s, r in picked if s['stem'] in t['stems']]
        lines += ['', f'### {t["zh"]} / {t["en"]} ({len(group)})', ''] + decision_table(group)
    shared = sorted(k for k in p3 if k in rows)
    lines += ['', '## 与 P3 分类的对照 / Against the P3 classification', '',
              f'[P3 的分类](BECOMING-INSTANCE-CLASSIFICATION.md)（10 月 9 日）归类了 46 个含类型多态定理的伦理模块；其中 {len(shared)} 个在脊柱运行之外，见于本表，逐行标出其 P3 类别。P3 的“已在核心上”指陈述直接写在基础的 `Process`／`Trace` 上，不指某条脊柱律陈述了它；本表给这些模块补上所及的脊柱声明。',
              '',
              f'[The P3 classification](BECOMING-INSTANCE-CLASSIFICATION.md) (9 October) sorted the 46 ethics modules with type-polymorphic theorems. {len(shared)} of them lie outside the spine run and appear here, each row naming its P3 category. P3’s “already on the core” means stated directly on the foundation’s `Process` and `Trace`, not that a spine law states it; this table adds the spine declarations those modules reach.']
    lines += ['', '## 逐模块 / Every module', '']
    for fam, group in collections.OrderedDict((f, [x for x in merged if family(x[1]['path']) == f])
                                             for f in dict.fromkeys(family(r['path']) for _, r in merged)).items():
        lines += [f'### {fam} ({len(group)})', '',
                  '| 模块 / Module | 定理 / Thms | 所及 / Reaches | 类别 / Category | 脊柱 / Spine | 依据 / Basis | 理由 / Reason |',
                  '|---|---:|---|---|---|---|---|']
        for s, r in group:
            others = f' (+{len(s["others"])})' if s.get('others') else ''
            spine = ', '.join(f'`{x}`' for x in r.get('spine', [])[:4]) + (f' ({r["relation"]})' if r.get('relation') else '')
            earlier = f' (P3: {P3_NAMES.get(p3[s["stem"]], p3[s["stem"]])})' if s['stem'] in p3 else ''
            lines.append(f'| [{s["stem"]}]({UP}{r["path"]}){others} | {s["theorems"]} | {REACH[reach(s)][1]} | '
                         f'{CATEGORIES[r["category"]][1]}{earlier} | {spine or "—"} | {r["basis"]} | {cell(r["reason_zh"])} / {cell(r["reason_en"])} |')
        lines.append('')
    OUT.write_text('\n'.join(lines).rstrip('\n') + '\n')


def main():
    signals, rows, problems, missing = load(sys.argv[1])
    print(json.dumps({'rows': len(rows), 'stems': len(signals), 'missing': len(missing),
                      'categories': collections.Counter(r['category'] for r in rows.values()),
                      'problems': problems[:40], 'problem_count': len(problems)}, ensure_ascii=False, indent=1))
    if '--write' in sys.argv:
        assert not missing and not problems, 'rows incomplete or invalid'
        render(signals, rows)
        print('wrote', OUT)


if __name__ == '__main__':
    main()
