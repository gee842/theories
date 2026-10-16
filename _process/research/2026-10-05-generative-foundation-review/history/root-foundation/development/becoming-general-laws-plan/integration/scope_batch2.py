#!/usr/bin/env python3
"""Update validation_scope receipt sentences of records rebound in batch 2 (run from repo root).

usage: scope_batch2.py IDS_FILE [--write]
Replaces in place (no appended paragraph):
- L1's prefix (receipt 20261013T204910.042715Z and its package totals) with the batch-2
  receipt and totals, adding the re-pointed modules to its module list;
- otherwise the older consolidated-check sentence (20261013T094743.528770Z) and its
  package totals, with the module counts that changed in batch 2;
- "scratch build only" sentences of the L2 records with the receipt.
"""
import json
import re
import sys
from pathlib import Path

NEW = '20261013T221720.428753Z'
COMMON = [
    ('consolidated receipt 20261013T204910.042715Z (passed: 85 package modules, 4861 theorems, 6856 declaration audits',
     f'consolidated receipt {NEW} (passed: 91 package modules, 4983 theorems, 7020 declaration audits'),
    ('the 86-module core closure', 'the 90-module core closure'),
    ('合并检查器回执 20261013T204910.042715Z 绑定（通过：包 85 个模块，4861 项定理、6856 项声明审计',
     f'合并检查器回执 {NEW} 绑定（通过：包 91 个模块，4983 项定理、7020 项声明审计'),
    ('核心闭包 86 个模块', '核心闭包 90 个模块'),
    ('(receipt 20261013T204910.042715Z', f'(receipt {NEW}'),
    ('（回执 20261013T204910.042715Z', f'（回执 {NEW}'),
]
OLDER = [
    ('consolidated check (20261013T094743.528770Z)', f'consolidated check ({NEW})'),
    ("the package's 75 modules (including the import-only root and the bridge) with 4518 theorems/6370 declaration audits, and 22 inherited modules",
     "the package's 91 modules (including the import-only root and the four bridge modules) with 4983 theorems/7020 declaration audits, and 39 inherited modules"),
    ('exactly these 77 modules', 'exactly these 90 modules'),
    ('the 48 theorems of Becoming.Continuation', 'the 52 theorems of Becoming.Continuation'),
    ('all 21 theorems of Becoming.Joint', 'all 34 theorems of Becoming.Joint'),
    ('all 7 theorems of Becoming.Substitution', 'all 12 theorems of Becoming.Substitution'),
    ('the 27 theorems of Becoming.Ranking', 'the 39 theorems of Becoming.Ranking'),
    ('合并检查器成功实查（20261013T094743.528770Z）', f'合并检查器成功实查（{NEW}）'),
    ('同一回执覆盖包内 75 个模块（含只作导入的根模块与桥接），共 4518 项定理／6370 项声明审计，22 个继承模块',
     '同一回执覆盖包内 91 个模块（含只作导入的根模块与四个桥接模块），共 4983 项定理／7020 项声明审计，39 个继承模块'),
    ('恰为这 77 个模块', '恰为这 90 个模块'),
    ('Becoming.Continuation 的 48 项定理', 'Becoming.Continuation 的 52 项定理'),
    ('Becoming.Joint 21 项定理', 'Becoming.Joint 34 项定理'),
    ('Becoming.Substitution 的 7 项定理', 'Becoming.Substitution 的 12 项定理'),
    ('Becoming.Ranking 的 27 项定理', 'Becoming.Ranking 的 39 项定理'),
]
SCRATCH = [
    (re.compile(r'have so far a scratch build only \(scratch_build\.py: empty axiom reports; not a receipt\); the consolidated checker runs when they land\.'),
     f'are checked in consolidated receipt {NEW} with empty axiom reports.'),
    (re.compile(r'目前只有 ?scratch_build\.py ?的草稿构建（公理报告为空；不是回执）；合并检查器在合并时运行。'),
     f'由合并检查器回执 {NEW} 检查，公理报告为空。'),
]
MODULES = ['Becoming.Joint', 'Becoming.Continuation', 'Becoming.Substitution', 'Becoming.Ranking', 'Becoming.RenewalBridge']


def main():
    ids = Path(sys.argv[1]).read_text().split()
    write = '--write' in sys.argv
    for ident in ids:
        p = Path(f'theories/becoming/results/records/{ident}.json')
        r = json.loads(p.read_text())
        vs = r['validation_scope']
        before = dict(vs)
        bound = {b['sha256_pointer'].rsplit('/', 1)[-1] for b in r.get('proof_bindings', []) if NEW in b['receipt']}
        new_mods = [m for m in MODULES if m in bound]
        for lang in ('en', 'zh'):
            t = vs[lang]
            if '20261013T204910.042715Z' in t:
                for a, b in COMMON:
                    t = t.replace(a, b)
                if lang == 'en':
                    m = re.search(r'the current bytes of (.*?) are bound to consolidated receipt', t)
                    if m:
                        listed = m.group(1)
                        add = [x for x in new_mods if x not in listed]
                        if add:
                            t = t.replace(m.group(0), f'the current bytes of {listed}, {", ".join(add)} are bound to consolidated receipt')
                else:
                    m = re.search(r'：(.*?) 的当前字节由合并检查器回执', t)
                    if m:
                        listed = m.group(1)
                        add = [x for x in new_mods if x not in listed]
                        if add:
                            t = t.replace(m.group(0), f'：{listed}、{"、".join(add)} 的当前字节由合并检查器回执')
            else:
                for a, b in OLDER:
                    t = t.replace(a, b)
            for rx, b in SCRATCH:
                t = rx.sub(b, t)
            vs[lang] = t
        changed = vs != before
        print(ident, 'changed' if changed else 'UNCHANGED', len(before['en']), '->', len(vs['en']), len(before['zh']), '->', len(vs['zh']),
              'still-old' if ('094743' in vs['en'] and '204910' not in vs['en'] and NEW not in vs['en']) else '')
        if write and changed:
            p.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
