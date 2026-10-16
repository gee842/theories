#!/usr/bin/env python3
"""Update only current chapter/study totals from passed receipts; no proof or review claim is added.

Usage: python3 -B totals.py ROOT
Reusable by adjacent landings. Historical totals and review scopes remain untouched. The Lean README
currently contains no numeric verification total. Run before record hashes are bound.
"""
import json
import re
import sys
from pathlib import Path

LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'


def sub1(text, pattern, replacement):
    text, count = re.subn(pattern, replacement, text)
    assert count == 1, (pattern, count)
    return text


def update(root):
    root = Path(root).resolve()
    receipt = json.loads((root / LEAN / 'becoming/becoming-verification.json').read_text())
    periphery = json.loads((root / LEAN / 'universal-ethics/generative-capacity/correction-inquiry-verification.json').read_text())
    assert receipt['status'] == periphery['status'] == 'passed'
    spine = [m for m in receipt['modules'] if m['spine']]
    theorem = sum(m['theorems'] for m in spine)
    declaration = sum(len(m['declarations']) for m in spine)
    core, package = len(receipt['core_closure']), len(spine)
    chapter = root / CHAPTER
    text = chapter.read_text()
    text = sub1(text, r'覆盖 \d+ 项定理、\d+ 项声明审计，源声明的公理报告全部为空；核心闭包共 \d+ 个模块（包 \d+ 个模块',
                f'覆盖 {theorem} 项定理、{declaration} 项声明审计，源声明的公理报告全部为空；核心闭包共 {core} 个模块（包 {package} 个模块')
    text = sub1(text, r'cover \d+ theorems and \d+ declaration audits, all source declarations with empty axiom reports; the core closure has \d+ modules \(the package \d+',
                f'cover {theorem} theorems and {declaration} declaration audits, all source declarations with empty axiom reports; the core closure has {core} modules (the package {package}')
    chapter.write_text(text)
    study = root / STUDY
    text = study.read_text()
    matches = list(re.finditer(r'The package now has \d+ theorems and \d+ declaration audits, over a core closure of \d+ modules and a package of \d+', text))
    assert matches, 'current study total missing'
    match = matches[-1]
    end = text.find('\n', match.start())
    if end == -1:
        end = len(text)
    paragraph = text[match.start():end].replace(match.group(),
        f'The package now has {theorem} theorems and {declaration} declaration audits, over a core closure of {core} modules and a package of {package}', 1)
    paragraph = sub1(paragraph, r'(The periphery bridge passed against this core \(receipt )[^)]+\)',
                     r'\g<1>' + periphery['utc'] + ')')
    study.write_text(text[:match.start()] + paragraph + text[end:])
    print(f'current totals: {theorem} theorems, {declaration} declarations, {core} core modules, {package} package modules')


if __name__ == '__main__':
    update(sys.argv[1])
