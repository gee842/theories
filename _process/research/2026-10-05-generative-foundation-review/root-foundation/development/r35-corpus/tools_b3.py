#!/usr/bin/env python3
"""R35 batch B3 (E2): the four 8 October snapshot pages stop rendering as live pages and the empty bridge group of
the Lean catalogue goes. Patches the shared tools; run once, before the moves of batch B3.

usage (from the checkout root): python3 -B tools_b3.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]


def patch(path, pairs):
    p = ROOT / path
    s = p.read_text()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:80])
        s = s.replace(a, b)
    p.write_text(s)


HA = '../history/ARGUMENTS-A-L-2026-10-08.md'
HM = '../history/ARGUMENTS-M-Z-2026-10-08.md'
HT = '../history/THEORY-MAP-2026-10-08.md'
HS = '../history/SESSION-RESULTS-2026-10-08.md'

patch('tools/research/reading_catalogue.py', [
    ("script owns results/README.md, THEORY-MAP.md and both ARGUMENTS volumes. The pages show",
     "script owns results/README.md and the two stubs ARGUMENTS-A-L.md and ARGUMENTS-M-Z.md. The volumes and the\n"
     "theory map of 8 October 2026 are frozen in theories/becoming/history/ (R35, E2); the index links them there and the\n"
     "stubs keep the old paths for the curated chain's page. The pages show"),
    ("def chapter_link(identifier: str) -> str:\n    volume = 'A-L' if identifier[0].upper() <= 'L' else 'M-Z'\n    return f'ARGUMENTS-{volume}.md#{identifier}'\n",
     "FROZEN = {'A-L': OUT.parent / 'history/ARGUMENTS-A-L-2026-10-08.md', 'M-Z': OUT.parent / 'history/ARGUMENTS-M-Z-2026-10-08.md'}\n"
     "THEORY_MAP = OUT.parent / 'history/THEORY-MAP-2026-10-08.md'\n\n\n"
     "def chapter_link(identifier: str, source: str | None = None) -> str:\n"
     "    \"\"\"The entry's reading in the frozen volume of 8 October 2026 where it has one, else the chapter itself.\"\"\"\n"
     "    volume = 'A-L' if identifier[0].upper() <= 'L' else 'M-Z'\n"
     "    frozen = FROZEN[volume]\n"
     "    if frozen.is_file() and identifier in anchors(frozen):\n"
     "        return f'{rel(str(frozen.relative_to(ROOT)))}#{identifier}'\n"
     "    return rel(source) if source else f'{rel(str(frozen.relative_to(ROOT)))}'\n"),
    ("             '| [Session outcomes and proof reuse](SESSION-RESULTS.md) | Chats mapped to result families, canonical reuse targets, overlap decisions and additional chapters. |',\n"
     "             f'| [Theory map](THEORY-MAP.md) | Accounts of the {len(branches)} branches, with significance, status and next steps; includes the method archive. |',\n"
     "             '| [Arguments A–L](ARGUMENTS-A-L.md) · [Arguments M–Z](ARGUMENTS-M-Z.md) | Chapter readings with argument, significance, scope, next question, source, Lean and evidence. |',\n",
     f"             '| [Session outcomes and proof reuse, 8 October 2026]({HS}) (frozen) | Chats mapped to result families, canonical reuse targets, overlap decisions and additional chapters, as of 8 October 2026. |',\n"
     f"             '| [Theory map, 8 October 2026]({HT}) (frozen) | Accounts of the branches, with significance, status and next steps; includes the method archive. |',\n"
     f"             '| [Arguments A–L]({HA}) · [Arguments M–Z]({HM}) (frozen, 8 October 2026) | Chapter readings with argument, significance, scope, next question, source, Lean and evidence; the registers in data/ keep them. |',\n"),
    ("[Generative grounding](ARGUMENTS-A-L.md#generative-grounding) · [Foundation premises](ARGUMENTS-A-L.md#foundation-premises) · [The whole theory](ARGUMENTS-M-Z.md#theory)",
     f"[Generative grounding]({HA}#generative-grounding) · [Foundation premises]({HA}#foundation-premises) · [The whole theory]({HM}#theory)"),
    ("[Generative development](ARGUMENTS-A-L.md#generative-development) · [Learning-route revision](ARGUMENTS-A-L.md#learning-route-revision) · [Evaluative succession](ARGUMENTS-A-L.md#evaluative-succession)",
     f"[Generative development]({HA}#generative-development) · [Learning-route revision]({HA}#learning-route-revision) · [Evaluative succession]({HA}#evaluative-succession)"),
    ("[Unified ethical grounding](ARGUMENTS-M-Z.md#unified-ethical-grounding) · [Evaluative grounding](ARGUMENTS-A-L.md#evaluative-grounding) · [Liangzhi](ARGUMENTS-A-L.md#liangzhi-evolution)",
     f"[Unified ethical grounding]({HM}#unified-ethical-grounding) · [Evaluative grounding]({HA}#evaluative-grounding) · [Liangzhi]({HA}#liangzhi-evolution)"),
    ("[Lean core](ARGUMENTS-A-L.md#generative-core-lean) · [Mathematical root frontier](ARGUMENTS-M-Z.md#mathematical-root-frontier) · [Conditional universality](ARGUMENTS-A-L.md#conditional-universality)",
     f"[Lean core]({HA}#generative-core-lean) · [Mathematical root frontier]({HM}#mathematical-root-frontier) · [Conditional universality]({HA}#conditional-universality)"),
    ("[Empirical scope](ARGUMENTS-A-L.md#empirical-scope) · [Experimental access](ARGUMENTS-A-L.md#experimental-access) · [Nondual method](ARGUMENTS-M-Z.md#nondual-method)",
     f"[Empirical scope]({HA}#empirical-scope) · [Experimental access]({HA}#experimental-access) · [Nondual method]({HM}#nondual-method)"),
    ("[Theory map](THEORY-MAP.md) · [Dao and generativity](ARGUMENTS-A-L.md#dao-and-generativity) · [Wang Yangming](ARGUMENTS-M-Z.md#wang-yangming)",
     f"[Theory map]({HT}) · [Dao and generativity]({HA}#dao-and-generativity) · [Wang Yangming]({HM}#wang-yangming)"),
    ("Additional chapters, changed source versions and session outcomes also appear in the [checkpoint map](SESSION-RESULTS.md). ",
     f"The session outcomes of 8 October 2026 are in the frozen [checkpoint map]({HS}). "),
    ("        lines.append(f\"| [`{d['id']}`]({chapter_link(d['id'])}) | {titled(d)} | {category(d)} |\")",
     "        lines.append(f\"| [`{d['id']}`]({chapter_link(d['id'], d['source'])}) | {titled(d)} | {category(d)} |\")"),
    ("    return {base + '/README.md': index(chapters, branches, drift),\n"
     "            base + '/THEORY-MAP.md': branch_volume(branches, drift),\n"
     "            base + '/ARGUMENTS-A-L.md': chapter_volume([d for d in chapters if d['id'][0].upper() <= 'L'], 'A–L', drift),\n"
     "            base + '/ARGUMENTS-M-Z.md': chapter_volume([d for d in chapters if d['id'][0].upper() > 'L'], 'M–Z', drift)}\n",
     "    return {base + '/README.md': index(chapters, branches, drift),\n"
     "            base + '/ARGUMENTS-A-L.md': stub('A–L', FROZEN['A-L']),\n"
     "            base + '/ARGUMENTS-M-Z.md': stub('M–Z', FROZEN['M-Z'])}\n\n\n"
     "def stub(volume: str, frozen: Path) -> str:\n"
     "    \"\"\"The page left at a frozen volume's old path, which the curated chain's page links (R35, E2).\"\"\"\n"
     "    target = rel(str(frozen.relative_to(ROOT)))\n"
     "    return finish([heading('#', f'Arguments {volume} (frozen)'), '', MARKER, '',\n"
     "                   f'The chapter readings {volume} of 8 October 2026 and later are frozen at [{frozen.name}]({target}), '\n"
     "                   'unchanged. The readings themselves are kept in the registers in [data/](data/); the live register of '\n"
     "                   'results is the [result register](RESULT-REGISTER.md), and every chapter with its status is in the '\n"
     "                   '[chapter index](../chapters/README.md).', ''])\n"),
])

patch('tools/research/research.py', [
    ("    out.update(session_map.render_output())\n", ""),
])
patch('tools/research/session_map.py', [
    ("nothing; changed live sources are reported separately, never silently certified or\noverwritten. `make research-render` writes SESSION-RESULTS.md (render_output).",
     "nothing; changed live sources are reported separately, never silently certified or\noverwritten. Historical since R35 (20 October 2026, E2): the map of 8 October 2026 and its inputs are frozen in\nhistory, `make research-render` no longer writes it, and the paths below are their history paths."),
    ("HERE = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'",
     "HERE = ROOT / '_process/research/2026-10-05-generative-foundation-review/history/root-foundation'"),
    ("REPORT = OUT / 'SESSION-RESULTS.md'", "REPORT = ROOT / 'theories/becoming/history/SESSION-RESULTS-2026-10-08.md'"),
])
patch('tools/research/registry.py', [
    (" + ' · [Session map](SESSION-RESULTS.md) · [Full catalogue](README.md)'", " + ' · [Full catalogue](README.md)'"),
])
print('patched')
