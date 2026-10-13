#!/usr/bin/env python3
"""Step 3 of a landing, after the checkers: the documentation of the run's packages in a checkout W.
Usage: python3 -B land_docs.py RUN_DIR W S [BASE]

S is the study section of the first package; the others follow in the order of the config's PACKAGES.
From W's receipts, which must cover every package's module:

- the study: each package's section (`docs/study/<prefix>_zh.md`, headed `## {S}. `) before the English summary,
  and its English block (`<prefix>_en.md`) before the last closing count, which is then updated;
- the unification plan: config.PLAN_ZH rows at the end of the table of items, config.PLAN_EN bullets after the
  last item bullet;
- the chapter: config.CHAPTER_EDITS, as (kind, anchor, text) with kind 'before' (a blank line after a paragraph,
  none before a list item or table row), 'after_line' or 'replace'; then the totals of section 9;
- the reading entry of the chapter: config.READING's sentences after the given anchors and the modules' Lean
  files after config.READING['lean_after'].

Placeholders: {RECEIPT}, {PERIPHERY}, {N_THM}, {N_DECL}, {N_CORE}, {N_PKG}, {LEAN}; per package with key K
{S_K}, {N_K}, {ANCHOR_K}, {STUDY_K}; in a package's own study text {S} and {N_MODULE}; and config.VALUES.
"""
import json
import re
import hashlib
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kit  # noqa: E402

RUN = Path(sys.argv[1]).resolve()
W = Path(sys.argv[2]).resolve()
S = int(sys.argv[3])
BASE = sys.argv[4] if len(sys.argv) > 4 else 'HEAD'
config = kit.load_config(RUN)
R = kit.Receipts(W)
print('totals', R.n_thm, R.n_decl, R.n_core, R.n_pkg)

# Validate the existing reading entry before any document is changed.
cat = W / 'theories/becoming/results/data/arguments-m-z.json'
data = json.loads(cat.read_text())
entry = next(d for d in data if d['id'] == 'the-theory-of-becoming')
base_chapter = subprocess.run(['git', 'show', f'{BASE}:{kit.CHAPTER}'], cwd=W,
                             capture_output=True, check=True).stdout
assert entry['source_sha256'] == hashlib.sha256(base_chapter).hexdigest(), \
    'reading entry was stale at BASE; read and reconcile its chapter before refreshing the hash'

STUDY_LINK = f'../../../{kit.STUDY}'
VALUES = {
    '{RECEIPT}': R.run,
    '{PERIPHERY}': R.peri_run,
    '{N_THM}': str(R.n_thm),
    '{N_DECL}': str(R.n_decl),
    '{N_CORE}': str(R.n_core),
    '{N_PKG}': str(R.n_pkg),
    '{LEAN}': f'../../../{kit.D}/Becoming',
    **getattr(config, 'VALUES', {}),
}
SECTIONS = []
for i, p in enumerate(config.PACKAGES):
    sec, key = str(S + i), p['key']
    docs = W / kit.DEV / p['package'] / 'docs/study'
    zh = (docs / f'{p["prefix"]}_zh.md').read_text()
    en = (docs / f'{p["prefix"]}_en.md').read_text()
    if 'study_heading' in p:
        assert not zh.startswith('## '), 'study_heading would duplicate an existing section heading'
        zh = f'## {{S}}. {p["study_heading"]}\n\n' + zh
    heading = zh.split('\n', 1)[0].replace('{S}', sec)
    assert heading.startswith(f'## {sec}. '), heading
    n = str(R.theorems(p['module']))
    VALUES.update({f'{{S_{key}}}': sec, f'{{N_{key}}}': n, f'{{ANCHOR_{key}}}': kit.anchor(heading),
                   f'{{STUDY_{key}}}': f'{STUDY_LINK}#{kit.anchor(heading)}'})
    SECTIONS.append((sec, n, zh, en))


def fill(text, sec=None, n_module=None):
    if sec is not None:
        text = text.replace('{S}', sec).replace('{N_MODULE}', n_module)
    for k, v in VALUES.items():
        text = text.replace(k, v)
    left = re.findall(r'\{[A-Z_]+\}', text)
    assert not left, left
    return text


def change(path, fn):
    p = W / path
    s = p.read_text()
    s2 = fn(s)
    assert s2 != s, path
    p.write_text(s2)
    print('edited', path)


TOTALS_EN = r'The package now has \d+ theorems and \d+ declaration audits, over a core closure of \d+ modules and a package of \d+'


def study(s):
    assert f'\n## {S}. ' not in s, f'the study already has a section {S}'
    for sec, n, zh, en in SECTIONS:
        s = kit.insert_before_line(s, '## English summary', fill(zh, sec, n).rstrip('\n') + '\n', True)
        s = kit.insert_before_line(s, 'The package now has ', fill(en, sec, n).rstrip('\n'), True, last=True)
    last = list(re.finditer(TOTALS_EN, s))[-1]
    end = s.find('\n', last.end())
    if end == -1:
        end = len(s)
    paragraph = (f'The package now has {R.n_thm} theorems and {R.n_decl} declaration audits, over a core '
                 f'closure of {R.n_core} modules and a package of {R.n_pkg}' + s[last.end():end])
    # These packages retain their own review statements; this summary describes their
    # unreviewed integration text. Do not change earlier review evidence.
    paragraph, n = re.subn(r', 71 to \d+ \(72 and 73',
                           f', 71 to {S + len(SECTIONS) - 1} (72 and 73', paragraph)
    assert n == 1, 'the review summary changed; reconcile it before landing'
    paragraph, n = re.subn(r'(The periphery bridge passed against this core \(receipt )\d{8}T\d{6}\.\d+Z\)',
                           r'\g<1>' + R.peri_run + ')', paragraph)
    assert n == 1, 'the periphery summary changed; reconcile it before landing'
    return s[:last.start()] + paragraph + s[end:]


change(kit.STUDY, study)


def plan(s):
    i = kit.line_start(s, '**P36b 入口与标题。**')
    assert s[i - 2:i] == '\n\n' and s[:i - 2].rsplit('\n', 1)[1].startswith('| P'), 'the table of items moved'
    s = s[:i - 1] + fill(config.PLAN_ZH).strip('\n') + '\n' + s[i - 1:]
    return kit.insert_after_line(s, '- **P', fill(config.PLAN_EN).strip('\n'), last=True)


change(kit.PLAN, plan)


def sub1(s, pattern, repl):
    s2, n = re.subn(pattern, repl, s)
    assert n == 1, (pattern, n)
    return s2


def chapter(s):
    for kind, anchor_text, text in config.CHAPTER_EDITS:
        text = fill(text)
        if kind == 'before':
            s = kit.insert_before_line(s, anchor_text, text, not text.startswith(('- ', '| ')))
        elif kind == 'after_line':
            s = kit.insert_after_line(s, anchor_text, text)
        else:
            assert kind == 'replace' and s.count(anchor_text) == 1, (kind, anchor_text[:80], s.count(anchor_text))
            s = s.replace(anchor_text, text)
    s = sub1(s, r'覆盖 \d+ 项定理、\d+ 项声明审计，源声明的公理报告全部为空；核心闭包共 \d+ 个模块（包 \d+ 个模块',
             f'覆盖 {R.n_thm} 项定理、{R.n_decl} 项声明审计，源声明的公理报告全部为空；核心闭包共 {R.n_core} 个模块（包 {R.n_pkg} 个模块')
    return sub1(s, r'cover \d+ theorems and \d+ declaration audits, all source declarations with empty axiom reports; the core '
                   r'closure has \d+ modules \(the package \d+',
                f'cover {R.n_thm} theorems and {R.n_decl} declaration audits, all source declarations with empty axiom '
                f'reports; the core closure has {R.n_core} modules (the package {R.n_pkg}')


change(kit.CHAPTER, chapter)

r = config.READING
for lang in ('en', 'zh'):
    field, after, text = f'argument_{lang}', r[f'after_{lang}'], fill(r[lang])
    assert entry[field].count(after) == 1 and text not in entry[field], (lang, entry[field].count(after))
    entry[field] = entry[field].replace(after, after + text)
lean = entry['lean']
at = lean.index(f'{kit.D}/Becoming/{r["lean_after"]}') + 1
for p in config.PACKAGES:
    path = f'{kit.D}/Becoming/{p["module"]}.lean'
    assert path not in lean
    lean.insert(at, path)
    at += 1
entry['source_sha256'] = kit.sha(W, kit.CHAPTER)
cat.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print('reading entry: sentences and', len(lean), 'Lean files')
