"""R36: set the reviewed hashes of the given sources in every record back to their values at BASE, so that one
run of repoint.py re-points them all after the last edit and writes one log line for the landing (an earlier
run's line was taken back). Touches only `references[].sha256` of the given paths.

Usage: python3 -B unpoint.py BASE PATH ...
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
RECORDS = 'theories/becoming/results/records'


def main():
    base, paths = sys.argv[1], set(sys.argv[2:])
    n = 0
    for p in sorted((ROOT / RECORDS).glob('*.json')):
        rel = f'{RECORDS}/{p.name}'
        run = subprocess.run(['git', 'show', f'{base}:{rel}'], cwd=ROOT, capture_output=True, text=True)
        if run.returncode:
            continue
        old = {(r.get('path'), r.get('role')): r.get('sha256') for r in json.loads(run.stdout).get('references', [])}
        d = json.loads(p.read_text())
        changed = False
        for r in d.get('references', []):
            key = (r.get('path'), r.get('role'))
            if r.get('path') in paths and key in old and r.get('sha256') != old[key]:
                r['sha256'] = old[key]
                changed = True
        if changed:
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
            n += 1
    print('records set back', n)


if __name__ == '__main__':
    main()
