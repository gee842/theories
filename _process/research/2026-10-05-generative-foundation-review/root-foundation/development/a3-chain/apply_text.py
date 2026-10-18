#!/usr/bin/env python3
"""A3: append the maintenance record's entry of 19 October 2026 (index-entry.txt, next to this script) to
GENERATIVITY-CHAIN-INDEX-RECORD.md. The entry's sentence on the sources read again at landing is filled from
--reread-zh and --reread-en; without them it says that no source changed between A3's reading and its landing. The
script refuses to run twice.

usage (from the repository root): python3 -B apply_text.py [--reread-zh TEXT --reread-en TEXT]
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDEX = HERE.parents[1] / 'GENERATIVITY-CHAIN-INDEX-RECORD.md'
ANCHOR = '<a id="sources-read-again-19-october-2026"></a>'
NONE_ZH = 'A3 读后至落地之间，没有所读的来源变动。'
NONE_EN = 'No source read changed between A3\'s reading and its landing.'


def arg(name, default):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def main():
    record = INDEX.read_text()
    if ANCHOR in record:
        raise SystemExit('the entry of 19 October 2026 is already in the record')
    entry = (HERE / 'index-entry.txt').read_text()
    entry = entry.replace('{reread_zh}', arg('--reread-zh', NONE_ZH)).replace('{reread_en}', arg('--reread-en', NONE_EN))
    INDEX.write_text(record.rstrip('\n') + '\n' + entry)
    print('entry appended to', INDEX.name)


if __name__ == '__main__':
    main()
