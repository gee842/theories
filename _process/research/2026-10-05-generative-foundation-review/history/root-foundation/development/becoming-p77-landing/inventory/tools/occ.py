import re, sys
from pathlib import Path
root = Path(sys.argv[1])
token = sys.argv[2] if len(sys.argv) > 2 else "Distinct"
KW = re.compile(r'^(?:private |protected |noncomputable |@\[[^\]]*\] )*(theorem|def|lemma|structure|abbrev|instance|inductive|example)\s+([^\s:({\[]*)')
NS = re.compile(r'^(namespace|end)\s+(\S+)')
for path in sorted(root.glob("Becoming/*.lean")):
    lines = path.read_text().split("\n")
    ns = []
    decls = []  # (start, kind, name, ns)
    for i, ln in enumerate(lines):
        m = NS.match(ln)
        if m:
            if m.group(1) == "namespace": ns.append(m.group(2))
            elif ns and ns[-1].split(".")[-1] == m.group(2).split(".")[-1]: ns.pop()
            elif ns and m.group(2) in ".".join(ns): ns.pop()
        m = KW.match(ln)
        if m:
            decls.append((i, m.group(1), m.group(2), ".".join(ns)))
    # statement end for each decl
    ends = {}
    for j, (s, k, n, nsn) in enumerate(decls):
        nxt = decls[j+1][0] if j+1 < len(decls) else len(lines)
        e = None
        for i in range(s, nxt):
            ln = lines[i]
            # strip comments
            code = ln.split("--")[0]
            if ":=" in code or (i > s and re.match(r'^\s+\|', ln)) or re.search(r'\bwhere\s*$', code):
                e = i; break
        ends[s] = (e if e is not None else nxt, nxt)
    in_doc = False
    for i, ln in enumerate(lines):
        if token not in ln: continue
        stripped = ln.strip()
        if stripped.startswith("--") or stripped.startswith("/-") or stripped.startswith("*") : 
            continue
        # find enclosing decl
        enc = None
        for d in decls:
            if d[0] <= i: enc = d
            else: break
        if enc is None:
            print(f"{path.name}:{i+1}: [no decl] {stripped[:100]}"); continue
        s, k, n, nsn = enc
        e, nxt = ends[s]
        if i >= nxt: where = "after"
        else:
            if i < e: where = "stmt"
            elif i == e:
                code = ln.split("--")[0]
                idx = code.find(":=")
                where = "stmt" if (idx == -1 or code.find(token) < idx) else "proof"
            else: where = "proof"
        print(f"{path.name}:{i+1}\t{k}\t{nsn+'.' if nsn and nsn!='Becoming' else ''}{n}\t{where}\t{stripped[:110]}")
