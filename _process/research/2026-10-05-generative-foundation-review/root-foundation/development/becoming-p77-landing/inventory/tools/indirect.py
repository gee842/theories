import re, sys
from pathlib import Path
from collections import defaultdict
root = Path(sys.argv[1])
KW = re.compile(r'^(?:private |protected |noncomputable |@\[[^\]]*\] )*(theorem|def|lemma|structure|abbrev|instance|inductive|example)\s+([^\s:({\[]*)')
toks = {
 "Listed": r"\bListed\b", "Census": r"\bCensus\b", "StandingCensus": r"StandingCensus\b", "DependenceCensus": r"DependenceCensus\b",
 "ListsAt": r"\bListsAt\b", "Counted": r"\bCounted\b", "CountedBy/Within": r"CountedBy|CountedWithin",
 "Dissipative": r"\bDissipative\b", "DissipativeBy": r"DissipativeBy\b", "Enclosed": r"\bEnclosed\b", "Around": r"\bAround\b",
 "AroundStanding": r"AroundStanding\b", "RunsDownOn(At)": r"RunsDownOn", "Once": r"\.Once\b|\bOnce\b",
 "World.Finite": r"\.Finite\b|\bFinite\b", "LosesAtEverySize": r"LosesAtEverySize", "Distinct(direct)": r"\bDistinct\b",
}
per_mod = defaultdict(lambda: defaultdict(int)); per_tok_total = defaultdict(int); decl_any = defaultdict(int); decl_total = defaultdict(int)
for path in sorted(root.glob("Becoming/*.lean")):
    mod = path.stem
    lines = path.read_text().split("\n")
    starts = [i for i, ln in enumerate(lines) if KW.match(ln)]
    for j, s in enumerate(starts):
        nxt = starts[j+1] if j+1 < len(starts) else len(lines)
        body = lines[s:nxt]; stmt = []
        for k, ln in enumerate(body):
            code = ln.split("--")[0]
            if k > 0 and re.match(r'^\s+\|', ln): break
            stmt.append(code)
            if ":=" in code or re.search(r'\bwhere\s*$', code): break
        text = " ".join(stmt)
        decl_total[mod] += 1
        hit = False
        for name, rx in toks.items():
            if re.search(rx, text):
                per_mod[mod][name] += 1; per_tok_total[name] += 1; hit = True
        if hit: decl_any[mod] += 1
print("module\tdecls\twith-any\t" + "\t".join(toks))
for mod in sorted(per_mod):
    print(mod + "\t" + str(decl_total[mod]) + "\t" + str(decl_any[mod]) + "\t" + "\t".join(str(per_mod[mod][t]) for t in toks))
print("TOTAL\t" + str(sum(decl_total.values())) + "\t" + str(sum(decl_any.values())) + "\t" + "\t".join(str(per_tok_total[t]) for t in toks))
