import re, sys
from pathlib import Path
root = Path(sys.argv[1]); mods = sys.argv[2].split(",")
token = "Distinct"
KW = re.compile(r'^(?:private |protected |noncomputable |@\[[^\]]*\] )*(theorem|def|lemma|structure|abbrev|instance|inductive|example)\s+([^\s:({\[]*)')
for mod in mods:
    path = root / f"Becoming/{mod}.lean"
    lines = path.read_text().split("\n")
    starts = [i for i, ln in enumerate(lines) if KW.match(ln)]
    for j, s in enumerate(starts):
        nxt = starts[j+1] if j+1 < len(starts) else len(lines)
        body = lines[s:nxt]
        # statement: until line with := or a line starting with '  |'
        stmt = []
        for k, ln in enumerate(body):
            code = ln.split("--")[0]
            if k > 0 and re.match(r'^\s+\|', ln): break
            stmt.append(ln)
            if ":=" in code or re.search(r'\bwhere\s*$', code): break
        text = " ".join(x.strip() for x in stmt)
        full = "\n".join(body)
        if token in full:
            where = "STMT" if token in text else "PROOF"
            print(f"--- {mod}:{s+1} [{where}] {text[:400]}")
