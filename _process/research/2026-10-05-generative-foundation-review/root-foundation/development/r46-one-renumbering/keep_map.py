#!/usr/bin/env python3
"""R46: put back the theorem map (EN, ZH) as committed at HEAD, keeping every other edit of the working chapter.

tmap.py regenerated on R46's tree changes no row of R46's record (the-world-an-interleaving-builds stays at section
1.4, a theorem without premise) and rewrites the premises other sessions wrote by hand into the map's rows (EV2,
EV4, EV5) and their order; those rows are theirs, so the map stays as main has it.

usage (checkout root): python3 -B keep_map.py"""
import re
import subprocess

PAT = re.compile(r'<!-- theorem-map:begin -->.*?<!-- theorem-map:end -->', re.S)
for path in ('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md',
             'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'):
    head = subprocess.run(['git', 'show', 'HEAD:' + path], capture_output=True, text=True, check=True).stdout
    block = PAT.search(head).group(0)
    live = open(path).read()
    assert len(PAT.findall(live)) == 1
    open(path, 'w').write(PAT.sub(lambda _m: block, live))
    print('kept', path)
