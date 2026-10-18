#!/usr/bin/env python3
"""A2: the text edits outside the chain's data, as exact replacements, so that they can be applied again on a newer
main. Chapter section 8.4: the clause on the generativity chain says the proposal was applied, with links to the chain
and its maintenance record. The decision brief: its opening note and item 19 say the change was applied, and item 19
notes that "memory is not wisdom" is the AI's paraphrase. The chain's maintenance record: the entry of 18 October 2026
(index-entry.txt, next to this script) is appended. Each replacement must match exactly once, and the script refuses
to run twice.

usage (from the repository root): python3 -B apply_text.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
BRIEF = RF + 'READINGS-PENDING-REN.md'
INDEX = RF + 'GENERATIVITY-CHAIN-INDEX-RECORD.md'
ANCHOR = '<a id="learning-and-wisdom-links-18-october-2026"></a>'
SOURCE_16 = '../../../../sources/15-codex-theory-conversations/2026-10-16-selection-through-a-model.md'

EDITS = {
    CHAPTER: [(
        'The chain is Ren\'s curated argument and changes through its maintenance record; applying the proposal there '
        'is a separate step.',
        'The chain is Ren\'s curated argument and changes through its maintenance record, where the proposal has been '
        'applied: `Selection` entered the wisdom entry, and `Observation` and `Parting` the learning entry '
        '([chain](../results/GENERATIVITY-CHAIN.md), [maintenance record](../../../' + INDEX + '#learning-and-wisdom-'
        'links-18-october-2026)).')],
    BRIEF: [(
        'The generativity chain\'s change (item 19) goes through the chain\'s maintenance record, a separate step.',
        'The generativity chain\'s change (item 19) was applied through the chain\'s maintenance record (board item '
        'A2).'), (
        '    - Separately, the chain\'s index record needs an entry for the 78 refreshed fingerprints. That is a process '
        'fix, not a reading.\n',
        '    - **Applied** (board item A2), as Ren took it (D43): `Selection` in the chain\'s wisdom '
        'entry (M15), `Observation` and `Parting` in its learning entry (M26), each with its record\'s scope and in the '
        'naming study\'s coupling vocabulary ([chain](../../../../theories/becoming/results/GENERATIVITY-CHAIN.md), '
        '[maintenance record](GENERATIVITY-CHAIN-INDEX-RECORD.md#learning-and-wisdom-links-18-october-2026)). '
        '"Memory is not wisdom", above and in item 3, is the AI\'s paraphrase of Ren\'s correction, not his words; the '
        'chain quotes his words of 16 October, “it is about the cognitive model, not just record” ([source](' + SOURCE_16
        + ')).\n'
        '    - Separately, the chain\'s index record needed an entry for the 78 refreshed fingerprints, a process fix, '
        'not a reading. That entry was written on 16 October 2026 (`e3b08cda9`, fix-list item 37), and A2\'s entry '
        'covers the sources changed since ([maintenance record](GENERATIVITY-CHAIN-INDEX-RECORD.md#learning-and-wisdom-'
        'links-18-october-2026)).\n')],
}


def main():
    for name, edits in EDITS.items():
        path = ROOT / name
        text = path.read_text()
        for old, new in edits:
            if text.count(new) and not text.count(old):
                raise SystemExit(f'{name} already holds the A2 text')
            if text.count(old) != 1:
                raise SystemExit(f'{name}: the text to replace occurs {text.count(old)} times')
            text = text.replace(old, new)
        path.write_text(text)
    index = ROOT / INDEX
    text = index.read_text()
    if ANCHOR in text:
        raise SystemExit(f'{INDEX} already holds the A2 entry')
    index.write_text(text + (HERE / 'index-entry.txt').read_text())
    print('chapter section 8.4, the brief and the maintenance record edited')


if __name__ == '__main__':
    main()
