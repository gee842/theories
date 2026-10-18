"""Retired words in text a later head added after the readings were written (N6, on rebasing).

usage (from the root of the branch's checkout, after `reading_pass.py apply`):
  python3 -B left_on_head.py [READ_AT]
Lists, per file in the pass's scope, each sentence holding a retired word that the head READ_AT
(default 77733b06b, where the readings were written) did not have. Each is then read by sense.
"""
import glob, json, re, subprocess, sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from reading_pass import prose_of, live_strings, PKG, RECORDS
READ_AT = sys.argv[1] if len(sys.argv) > 1 else '77733b06b'
# the head the edits are applied to: the merge base with main (main itself moves)
HEAD_REV = subprocess.run(['git', 'merge-base', 'HEAD', 'main'], capture_output=True, text=True).stdout.strip()
RX = re.compile(r'regist|refut|learner|belief|\brecords?\b|hypothes|target|identif|登记|识|学习者|信念|否证|假说|目标', re.I)
def old(path):
    r = subprocess.run(['git', 'show', f'{READ_AT}:{path}'], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ''
def units(text):
    return [u.strip() for u in re.split(r'(?<=[.。;；])\s+|\n', text) if u.strip()]
def report(path, now, before, head):
    """Sentences the head added (in head, not before) that still stand unchanged after the pass (in now)."""
    seen, cur = set(units(before)), set(units(now))
    for u in units(head):
        if u not in seen and u in cur and RX.search(u):
            print(f'{path}: {u[:400]}')
def at_head(path):
    r = subprocess.run(['git', 'show', f'{HEAD_REV}:{path}'], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ''
def lean_prose(t):
    return ' \n'.join(x for _, x in prose_of(t)) if t else ''
for f in sorted(glob.glob(PKG + 'Becoming/*.lean')):
    report(f, lean_prose(open(f).read()), lean_prose(old(f)), lean_prose(at_head(f)))
for f in ['theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md']:
    report(f, open(f).read(), old(f), at_head(f))
for f in sorted(glob.glob(RECORDS + '*.json')):
    acc = []
    def g(s, acc=acc):
        acc.append(s); return s
    live_strings(json.load(open(f)), g)
    def strs(t):
        a = []
        if t:
            live_strings(json.loads(t), lambda s: (a.append(s), s)[1])
        return '\n'.join(a)
    report(f, '\n'.join(acc), strs(old(f)), strs(at_head(f)))
