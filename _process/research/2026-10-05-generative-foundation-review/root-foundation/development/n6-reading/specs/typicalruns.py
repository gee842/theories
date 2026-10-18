"""TypicalRuns: the record of n steps is Learning.prefixOf of the course, so prose "record" reads
"prefix" (L-prefix). Lines are rewritten outside backticks only, then reviewed by hand."""
import re, sys
sys.path.insert(0, '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/n6-reading')
from gen_edits import gen, base_text
D='_process/research/2026-10-05-generative-foundation-review/root-foundation/development/n6-reading'
L='experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
path=L+'/TypicalRuns.lean'
src=base_text(path)
def fix(line):
    parts=re.split(r'(`[^`]*`)',line)
    out=[]
    for p in parts:
        if p.startswith('`'): out.append(p); continue
        p=re.sub(r'\brecords\b','prefixes',p); p=re.sub(r'\brecord\b','prefix',p)
        out.append(p)
    return ''.join(out)
# comment lines: inside /-! ... -/ or /-- ... -/ blocks
reps=[]; seen=set()
inside=False
for line in src.split('\n'):
    starts = line.lstrip().startswith('/-')
    if starts: inside=True
    if inside and re.search(r'\brecords?\b', re.sub(r'`[^`]*`','',line)):
        new=fix(line)
        if line not in seen: reps.append(('L-prefix',line,new)); seen.add(line)
    if inside and '-/' in line: inside=False
# grammar touch-ups after substitution
manual={
 "`n` steps are exactly the prefixes a run of free branching on two values shows in its first `n`":"`n` steps are exactly the prefixes of `n` steps a run of free branching on two values shows",
 "steps (`Learning.prefixOf` of `Parting.course`), each listed once, so every count over them is a":"(`Learning.prefixOf` of `Parting.course`), each listed once, so every count over them is a",
 "  where some run of free branching shows it as its prefix of `n` steps (`mem_courses_iff`), and":"  where some run of free branching shows it as its prefix of `n` steps (`mem_courses_iff`), and",
}
reps=[(s,a,manual.get(b,b)) for s,a,b in reps]
reps.append(('L-prefix','\nsteps (`Learning.prefixOf` of `Parting.course`), each listed once,','\n(`Learning.prefixOf` of `Parting.course`), each listed once,'))
gen(D+'/edits/lean-typicalruns.txt','TypicalRuns.lean: the record of `n` steps is `Learning.prefixOf` of the course, so it is a prefix (L-prefix); `record`, `Records`, `records_*`, `ofRecord` are names, in the names table.','lean:TypicalRuns',path,reps)
