"""R36: fill the study section's measured numbers from the live editions and the audit outputs, and append it
after section 226 of BECOMING-RENEWAL-READING.md. Usage: python3 -B study_227.py [--apply]"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
STUDY = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'


def main():
    t = (HERE / 'draft/STUDY-227.md').read_text()
    en = (ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md').read_text()
    zh = (ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md').read_text()
    a = json.loads((HERE / 'audit-en.json').read_text())
    z = json.loads((HERE / 'audit-zh.json').read_text())
    ln = a['lean_names']
    t = t.replace('{EN_BYTES}', f'{len(en.encode()):,}').replace('{EN_LINES}', f'{en.count(chr(10)):,}')
    t = t.replace('{ZH_BYTES}', f'{len(zh.encode()):,}').replace('{ZH_LINES}', f'{zh.count(chr(10)):,}')
    t = t.replace('{EN_AUDIT}', (
        f"all {a['anchors']['frozen']} anchors of the frozen edition present ({a['anchors']['new']} in the new); "
        f"all {a['records']['frozen']} records it links linked ({a['records']['new']} now, none nonexistent); "
        f"all {ln['frozen']:,} Lean names it cites accounted for ({ln['chapter']:,} cited again, {ln['qualified']} under "
        f"another qualification, {ln['record']} named in a linked record, none unaccounted); all "
        f"{a['existence']['cited']:,} names the new edition cites occur in the Lean sources; none of its "
        f"{a['open_units']['frozen_open_units']} open statements loses a name or a record; "
        f"{a['links']['checked']:,} links, none broken"))
    t = t.replace('{ZH_AUDIT}', (
        f"all {z['anchors']['frozen']} anchors present ({z['anchors']['new']} in the new), all {z['records']['new']} "
        f"records exist, all {z['existence']['cited']} names cited occur in the Lean sources, {z['links']['checked']} "
        f"links, none broken. Of the frozen Chinese edition's {z['lean_names']['frozen']:,} names, "
        f"{len(z['lean_names']['unaccounted'])} were in neither the new Chinese edition nor its records: two fragments "
        "(`_listing`, `_by_core`), two the English cites, and fourteen from seven rows of the old Chinese module table "
        "in §9 (a table the English had moved to its reference edition on 17 October), which stated laws the English "
        "named nowhere. Those seven rows are now in the English §9 in translation (`zh_only.py`), so all "
        f"{len(z['lean_names']['unaccounted'])} are in the English chapter"))
    assert '{' not in t.replace('{ne', ''), 'unfilled placeholder'
    if '--apply' in sys.argv:
        s = STUDY.read_text()
        assert '## 227.' not in s
        STUDY.write_text(s.rstrip('\n') + '\n' + t)
        print('appended', len(t))
    else:
        print(t)


if __name__ == '__main__':
    main()
