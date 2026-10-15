#!/usr/bin/env python3
"""Rebind records after a landing batch (integration helper; run from the repo root).

usage: rebind_batch.py NOTES.json [--write]

NOTES.json: {"core_receipt": run-folder verification.json,
             "extra_receipts": {"<pointer module>": receipt path, ...},
             "files": {path: {"en": why it changed, "zh": ...}, ...},
             "history": {"en": lead sentence, "zh": ...},
             "scope_old": [[en_old, en_new], [zh_old, zh_new], ...]}
For every record:
- a Markdown reference whose change lies outside what the record cites keeps its hash
  (registry.scoped_drift; the research check accepts it);
- a reference whose file changed and whose path is in "files" gets the current sha256;
  a changed file not in "files" is reported and left alone;
- a proof binding whose receipt does not bind the current source sha is re-pointed to
  the core receipt (or an extra receipt) when that receipt binds it, else reported;
- a record that changed gets one paired history note naming each file and why,
  and validation_scope substitutions from "scope_old" where they apply.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT))
from tools.research import registry  # noqa: E402
registry.ROOT = ROOT
RECORDS = ROOT / 'theories/becoming/results/records'


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def pointer(doc, ptr):
    cur = doc
    for part in ptr.strip('/').split('/'):
        part = part.replace('~1', '/').replace('~0', '~')
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        elif isinstance(cur, list) and part.isdigit() and int(part) < len(cur):
            cur = cur[int(part)]
        else:
            return None
    return cur


def main():
    notes = json.loads(Path(sys.argv[1]).read_text())
    write = '--write' in sys.argv
    receipts = {}

    def receipt(path):
        if path not in receipts:
            receipts[path] = json.loads((ROOT / path).read_text())
        return receipts[path]

    core = notes['core_receipt']
    extras = notes.get('extra_receipts', {})
    report = {'changed': [], 'unhandled_drift': [], 'unbound': [], 'kept': 0}
    for p in sorted(RECORDS.glob('*.json')):
        r = json.loads(p.read_text())
        touched_files = []
        for ref in r.get('references', []):
            path = ref.get('path')
            if not path or 'sha256' not in ref or not (ROOT / path).is_file():
                continue
            cur = sha(path)
            if cur != ref['sha256']:
                # A Markdown reference whose change lies outside what the record cites keeps its
                # hash: the research check accepts it (RESULT-WORKFLOW.md), so the record is not
                # rewritten (as the landing kit's repoint.py does since the landing-speed change).
                if path.endswith('.md') and registry.scoped_drift(r, path, ref['sha256'], ROOT / path) is None:
                    report['kept'] += 1
                    continue
                if path in notes['files']:
                    ref['sha256'] = cur
                    touched_files.append(path)
                else:
                    report['unhandled_drift'].append([r['id'], path])
        rebound = False
        for b in r.get('proof_bindings', []):
            src = b.get('source')
            if not src or not (ROOT / src).is_file():
                continue
            cur = sha(src)
            if pointer(receipt(b['receipt']), b['sha256_pointer']) == cur:
                continue
            mod = b['sha256_pointer'].rsplit('/', 1)[-1]
            for cand in [extras.get(mod), core]:
                if cand and pointer(receipt(cand), b['sha256_pointer']) == cur \
                        and pointer(receipt(cand), b.get('success_pointer', '/status')) == b.get('success_value', 'passed'):
                    b['receipt'] = cand
                    rebound = True
                    if src not in touched_files:
                        touched_files.append(src)
                    break
            else:
                report['unbound'].append([r['id'], src, b['receipt']])
        if not touched_files and not rebound:
            continue
        # every reference to a re-pointed receipt is hashed too
        names = {'en': [], 'zh': []}
        for path in touched_files:
            n = notes['files'].get(path)
            short = path.rsplit('/', 1)[-1]
            if n:
                names['en'].append(f'{short} ({n["en"]})')
                names['zh'].append(f'{short}（{n["zh"]}）')
            else:
                names['en'].append(short)
                names['zh'].append(short)
        h = notes['history']
        entry = {'zh': h['zh'] + '；'.join(names['zh']) + '。',
                 'en': h['en'] + '; '.join(names['en']) + '.'}
        r.setdefault('history', []).append(entry)
        if rebound:
            vs = r.get('validation_scope')
            if isinstance(vs, dict):
                for old, new in notes.get('scope_old', []):
                    for lang in ('en', 'zh'):
                        if old in vs.get(lang, ''):
                            vs[lang] = vs[lang].replace(old, new)
        report['changed'].append([r['id'], touched_files, rebound])
        if write:
            p.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'changed': len(report['changed']), 'unhandled_drift': report['unhandled_drift'],
                      'unbound': report['unbound'], 'kept_outside_cited': report['kept']}, ensure_ascii=False, indent=1))
    if '--list' in sys.argv:
        for x in report['changed']:
            print(x[0], [t.rsplit('/', 1)[-1] for t in x[1]], x[2])


if __name__ == '__main__':
    main()
