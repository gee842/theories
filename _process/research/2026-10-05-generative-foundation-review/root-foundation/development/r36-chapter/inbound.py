"""R36: every link into the canonical chapter (EN, ZH), by referrer role and fragment.

Reads the tree; writes inbound.json beside itself (or the path given as the second argument).
Usage: python3 -B inbound.py ROOT [OUT]
"""
import json, sys, re, subprocess
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(sys.argv[1]).resolve()
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_name('inbound.json')
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools/research"))
import moves, paths  # noqa

CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
ZH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
cls = paths.Classifier(root=ROOT)
files = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True).stdout.split('\n')
out = {CH: defaultdict(list), ZH: defaultdict(list)}
for f in files:
    if not f.endswith(('.md', '.json')):
        continue
    try:
        text = (ROOT / f).read_text(errors='replace')
    except OSError:
        continue
    if 'THE-THEORY-OF-BECOMING' not in text:
        continue
    role = cls.role(f)
    if f.endswith('.md'):
        for _a, _b, raw in moves.links(text):
            parts = moves.split_target(raw)
            if parts is None:
                continue
            p, _q, frag = parts
            tgt = f if not p else moves.resolve(f, p)
            if tgt in out:
                out[tgt][unquote(frag or '')].append([f, role])
    else:
        for raw in re.findall(r'[^"\s()\[\]]*THE-THEORY-OF-BECOMING(?:\.zh)?\.md(?:#[^"\s)\]]*)?', text):
            p, _, frag = raw.partition('#')
            tgt = ZH if p.endswith('THE-THEORY-OF-BECOMING.zh.md') else CH
            if not p.endswith(('chapters/THE-THEORY-OF-BECOMING.md', 'chapters/THE-THEORY-OF-BECOMING.zh.md',
                               'THE-THEORY-OF-BECOMING.md', 'THE-THEORY-OF-BECOMING.zh.md')):
                continue
            if 'history/' in p:
                continue
            out[tgt][unquote(frag)].append([f, role])
res = {}
for tgt, d in out.items():
    anchors = moves.anchors((ROOT / tgt).read_text())
    res[tgt] = {
        'anchors_now': sorted(anchors),
        'fragments': {k: {'count': len(v), 'roles': dict(Counter(r for _f, r in v)),
                          'present': (k == '' or k in anchors or k.lower() in anchors),
                          'files': sorted({x for x, _ in v})} for k, v in sorted(d.items())},
    }
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1))
for tgt, r in res.items():
    fr = r['fragments']
    print(tgt, 'anchors', len(r['anchors_now']), 'fragments linked', len(fr), 'links', sum(v['count'] for v in fr.values()))
    print(' missing now', [k for k, v in fr.items() if not v['present']][:30])
    roles = Counter()
    for v in fr.values():
        roles.update(v['roles'])
    print(' by role', dict(roles))
