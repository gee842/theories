#!/usr/bin/env python3
"""R30 (20 October 2026), one notion, one name: rename, rebind and re-point the records.

Usage (from the checkout root): python3 -B rebind.py BASE RECEIPT_ID [RENDER_LOG]

BASE is the main commit R30 was built on; RECEIPT_ID the passing core receipt of R30's checker run.

* Live fields (everything but `history`, `text_versions` and hashes) follow the table by text.py's rule for
  records (a declaration list entry by its full name; text by qualified suffixes and, outside backticks, by
  one-component names that cannot be English words); paths and binding pointers follow the module renames
  (`paths`, `modules`). Record IDs and slugs are stable IDs and do not change. Aliases follow the new names, as in N5:
  the registry requires an alias to be an elaborated declaration of the bound receipt, and the old name is not one
  (the table is the lookup for every old name). Every renamed name is checked against the receipt.
* Proof bindings to the Lean files R30 changed are rebound to the receipt; references to the files R30 changed
  are re-pointed where they matched BASE (the record was current; for a renamed module, BASE's file at its old
  path), or where the render log reports drift in sections the record cites, after reading the change (WHAT).
* A history note (en, zh) says what was renamed and re-pointed, and that the claim is unchanged.
"""
import glob
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

BASE, RID = sys.argv[1], sys.argv[2]
DRIFT = {}
if len(sys.argv) > 3:
    _log = open(sys.argv[3]).read()
    _dec = json.JSONDecoder()
    for _k in range(len(_log)):
        if _log[_k] == '{':
            try:
                _o, _ = _dec.raw_decode(_log[_k:])
            except ValueError:
                continue
            if isinstance(_o, dict) and 'source_drift' in _o:
                for _x in _o['source_drift']:
                    DRIFT.setdefault(_x['path'], set()).add(_x['id'])
                break
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('r30text', HERE / 'text.py')
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
TABLE = json.load(open(HERE / 'RENAME-TABLE.json'))
REN, PATHS = TABLE['declarations'], TABLE['paths']
OLDPATH = {n: o for o, n in PATHS.items()}

LEANDIR = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
PKG = LEANDIR + 'becoming/'
B = PKG + 'Becoming/'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
receipt = json.load(open(RECEIPT))
assert receipt['status'] == 'passed'
assert not any(v for m in receipt['modules'] if m.get('layer') == 'core' for v in m['axiom_dependencies'].values()), 'core axiom report not empty'
elaborated = {x['name'] if isinstance(x, dict) else x for m in receipt['modules'] if m.get('layer') == 'core'
              for x in m.get('declarations', [])}
for o, n in REN.items():
    assert n in elaborated and o not in elaborated, (o, n)
path_of = {m: LEANDIR + p for m, p in receipt['source_paths'].items()}
module_of = {p: m for m, p in path_of.items()}

RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
STUDY = RF + 'BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/'
NAMES = ('names follow the R30 rename table', '名称随 R30 改名表')
DOCS = {
    CH + 'THE-THEORY-OF-BECOMING.md': ('names follow the R30 rename table; the retired Lean names of 20 October are in the glossary; §9 (receipt) follows R30',
                                       '名称随 R30 改名表；10月20日退役的 Lean 名列入术语表；§9（回执）随 R30'),
    CH + 'THE-THEORY-OF-BECOMING.zh.md': ('names follow the R30 rename table; the retired Lean names of 20 October are in the glossary; §9 (receipt) follows R30',
                                          '名称随 R30 改名表；10月20日退役的 Lean 名列入术语表；§9（回执）随 R30'),
    CH + 'THE-THEORY-OF-BECOMING-REFERENCE.md': NAMES,
    CH + 'CHINESE-SOURCES-AND-BECOMING.md': ('names follow the R30 rename table; the passage tables are the rebuilt map',
                                             '名称随 R30 改名表；逐句对应表为重建之图'),
    CH + 'YI-ZHUAN-AND-BECOMING.md': ('names follow the R30 rename table; the passage table is the renamed map',
                                      '名称随 R30 改名表；逐句对应表为改名后之图'),
    CH + 'G0-WARRANT.md': NAMES, CH + 'G0-WARRANT.zh.md': NAMES,
    CH + 'WISDOM-AND-CONTEXT.md': NAMES, CH + 'WISDOM-AND-CONTEXT.zh.md': NAMES,
    'theories/becoming/OPENING.md': ('the footnotes name the renamed declarations; the body is unchanged',
                                     '脚注改用改名后的声明名；正文不变'),
    RF + 'DELEGATED-CHOICES.md': NAMES, RF + 'DELEGATED-CHOICES.zh.md': NAMES,
    RF + 'MODULE-CLASSIFICATION.md': NAMES, RF + 'MODULE-CLASSIFICATION.zh.md': NAMES,
    RF + 'DECIDABILITY-INVENTORY.md': NAMES, RF + 'DECIDABILITY-INVENTORY.zh.md': NAMES,
    RF + 'development/ro-relational-sources/passages.json': ('rebuilt: the declarations and the names in the readings follow the R30 table, each so corrected passage marked',
                                                            '重建：声明与读法中的名称随 R30 改名表，每个如此更正的段落有标注'),
    RF + 'development/ro-relational-sources/build_passages.py': ('the R30 table joins the renames applied after FIXES',
                                                                 'R30 改名表并入在 FIXES 之后施行的改名'),
    RF + 'development/y1-changes/passages.json': ('the declarations and the names in four readings follow the R30 table',
                                                  '四个读法中的声明与名称随 R30 改名表'),
    STUDY: ('section 221 added', '新增第 221 节'),
    PKG + 'Becoming.lean': ('imports and notes follow the module renames', '导入与说明随模块改名'),
    PKG + 'README.md': ('module rows, declaration names and the import order follow R30', '模块行、声明名与导入次序随 R30'),
    PKG + 'README.zh.md': ('module rows, declaration names and the import order follow R30', '模块行、声明名与导入次序随 R30'),
    PKG + 'check_becoming.py': ('CORE module names and the SCOPE text follow the module renames, the SecuresNewContent snippet; no logic changed',
                                'CORE 模块名与 SCOPE 文本随模块改名，SecuresNewContent 片段；逻辑不变'),
    PKG + 'becoming-verification.json': ("the current receipt is R30's run", '当前回执为 R30 之运行'),
}
LEAN_WHAT = {
    'Arising.lean': ('the module Generation renamed Arising; Web.generation_* are Web.embodiedArising_*, Web.Regenerating is Web.ActiveRenewer; statements unchanged',
                     '模块 Generation 改名为 Arising；Web.generation_* 现为 Web.embodiedArising_*，Web.Regenerating 现为 Web.ActiveRenewer；陈述不变'),
    'Restoration.lean': ('the module Return renamed Restoration; Web.Returns and Web.ReturnsWithin are Web.Restored and Web.RestoredWithin; statements unchanged',
                         '模块 Return 改名为 Restoration；Web.Returns 与 Web.ReturnsWithin 现为 Web.Restored 与 Web.RestoredWithin；陈述不变'),
    'MoveFormation.lean': ('the module and namespace Coupling renamed MoveFormation; statements unchanged',
                           '模块与命名空间 Coupling 改名为 MoveFormation；陈述不变'),
    'SecuredContent.lean': ('the module and namespace PositiveGround renamed SecuredContent, contingent_generation* contingent_newContent*, the binder positive relevance; statements unchanged',
                            '模块与命名空间 PositiveGround 改名为 SecuredContent，contingent_generation* 现为 contingent_newContent*，约束变量 positive 现为 relevance；陈述不变'),
    'Metaethics.lean': ('G0 is LivingSignificance, g0_* livingSignificance_*, Valuation.SelfGood Valuation.SelfSignificance, SecuresPositiveGround SecuresNewContent, the binder positive relevance; the module header is structural; statements unchanged',
                        'G0 现为 LivingSignificance，g0_* 现为 livingSignificance_*，Valuation.SelfGood 现为 Valuation.SelfSignificance，SecuresPositiveGround 现为 SecuresNewContent，约束变量 positive 现为 relevance；模块标题改为结构性的；陈述不变'),
}
DEFAULT_LEAN = ('declarations, namespaces and uses renamed by the R30 table (one notion, one name); statements and proofs unchanged',
                '声明、命名空间与用法按 R30 改名表改名（一个概念一个名字）；陈述与证明不变')


def h(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


changed = subprocess.run(['git', 'diff', '--name-only', '-M', BASE, '--'], capture_output=True, text=True, check=True).stdout.split()
changed += [n for n in PATHS.values()]
LEAN = {p for p in changed if p.startswith(B) and p.endswith('.lean') and Path(p).exists()}
WHAT = dict(DOCS)
for p in LEAN:
    WHAT[p] = LEAN_WHAT.get(p.rsplit('/', 1)[-1], DEFAULT_LEAN)
base = {}
for p in WHAT:
    out = subprocess.run(['git', 'show', f'{BASE}:{OLDPATH.get(p, p)}'], capture_output=True)
    base[p] = hashlib.sha256(out.stdout).hexdigest() if out.returncode == 0 else None


def short(p):
    return p.rsplit('/', 1)[-1]


def bare(x):
    return x.split('Becoming.', 1)[1] if x.startswith('Becoming.') else x


def walk(x, key, hits):
    if isinstance(x, str):
        if key in ('path', 'source', 'canonical_source'):
            if x in PATHS:
                hits.append((short(x), short(PATHS[x])))
            return PATHS.get(x, x)
        if key in ('receipt', 'id'):
            return x
        if x in REN:
            hits.append((bare(x), bare(REN[x])))
            return REN[x]
        y = T.rewrite_text(x, True)
        if y != x:
            a, b = set(T.IDENT.findall(x)), set(T.IDENT.findall(y))
            for u in sorted(a - b):
                v = T.rewrite_text('`' + u + '`', True)[1:-1]
                hits.append((bare(u), bare(v) if v != u else ''))
        return y
    if isinstance(x, list):
        return [walk(v, key, hits) for v in x]
    if isinstance(x, dict):
        return {k: (v if k in ('history', 'text_versions', 'sha256', 'id') else walk(v, k, hits))
                for k, v in x.items()}
    return x


n = 0
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d0 = json.load(open(f))
    before = json.dumps(d0, ensure_ascii=False)
    hits = []
    d = walk(d0, None, hits)
    rid = d['id']
    for x in d.get('aliases') or []:
        assert x not in REN, (rid, x)
    rebound, touched = [], set()
    for b in d.get('proof_bindings', []):
        if b['source'] in LEAN and b['receipt'] != RECEIPT:
            assert receipt['source_sha256'][module_of[b['source']]] == h(b['source']), b['source']
            assert b['sha256_pointer'] == '/source_sha256/' + module_of[b['source']], (rid, b['sha256_pointer'])
            b['receipt'] = RECEIPT
            rebound.append(short(b['source']))
    refs = d.get('references', [])
    for r in refs:
        p = r['path']
        if p in LEAN and any(b['source'] == p and b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])):
            if r.get('sha256') != h(p):
                r['sha256'] = h(p)
                touched.add(p)
        elif p in WHAT and (r.get('sha256') == base[p] or rid in DRIFT.get(p, ())) and r.get('sha256') != h(p):
            r['sha256'] = h(p)
            touched.add(p)
    if any(b['receipt'] == RECEIPT for b in d.get('proof_bindings', [])) and not any(r['path'] == RECEIPT for r in refs):
        refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    if json.dumps(d, ensure_ascii=False) == before:
        continue
    en = '20 October 2026, R30 (one notion, one name: names that stated a meaning the statement does not have, or collided, renamed by one table, development/r30-names/RENAME-TABLE.json):'
    zh = '2026年10月20日，R30（一个概念一个名字：名字说出陈述所没有的意思或相撞者，按一张表改名，见 development/r30-names/RENAME-TABLE.json）：'
    named = sorted({(a, b) for a, b in hits if b})
    loose = sorted({a for a, b in hits if not b} - {a for a, _ in named})
    if named or loose:
        items = [f'{a} (now {b})' for a, b in named] + loose
        items_zh = [f'{a}（现为 {b}）' for a, b in named] + loose
        en += ' Renamed: ' + '; '.join(items) + '.'
        zh += '改名：' + '；'.join(items_zh) + '。'
    if rebound:
        en += f' Proof bindings ({", ".join(sorted(set(rebound)))}) rebound to core receipt {RID}.'
        zh += f'证明绑定（{"、".join(sorted(set(rebound)))}）改到核心回执 {RID}。'
    ps = sorted(touched)
    if ps:
        en += ' Re-pointed after reading the change: ' + '; '.join(short(p) + ', ' + WHAT[p][0] for p in ps) + '.'
        zh += '读过改动后重新指向：' + '；'.join(short(p) + '，' + WHAT[p][1] for p in ps) + '。'
    en += ' The claim is unchanged.'
    zh += '论断不变。'
    last = d['history'][-1] if d.get('history') else {}
    if last.get('en', '').startswith('20 October 2026, R30'):
        if ps:
            last['en'] = last['en'].replace(' The claim is unchanged.', ' Also re-pointed after reading the change: '
                                            + '; '.join(short(p) + ', ' + WHAT[p][0] for p in ps) + '. The claim is unchanged.')
            last['zh'] = last['zh'].replace('论断不变。', '另读过改动后重新指向：'
                                            + '；'.join(short(p) + '，' + WHAT[p][1] for p in ps) + '。论断不变。')
    else:
        d.setdefault('history', []).append({'en': en, 'zh': zh})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(rid, len(named), len(loose), sorted(set(rebound)), len(ps))
print(n, 'records changed')
