"""Check the package README's sentence of direct imports against an import graph."""
import json, re, sys
graph = json.load(open(sys.argv[1]))['imports']
line = open(sys.argv[2]).read().splitlines()[int(sys.argv[3]) - 1]
inner = line[line.index('(') + 1:line.rindex(')')]
def full(x):
    return x if x.startswith('Becoming') or x in ('RelationalRenewal', 'GenerativeCore', 'InquirySufficiency') else 'Becoming.' + x
bad = []
for clause in re.split(r';|, and (?=`)', inner):
    clause = re.sub(r'^\s*(within L\d, )?', '', clause.strip())
    for part in re.split(r', (?=`[^`]+` imports)|, and (?=`[^`]+`(?: and `[^`]+`)* imports?)', clause):
        m = re.match(r'(.*?) imports? (only )?(.*)$', part.strip())
        if not m:
            continue
        subs = re.findall(r'`([^`]+)`', m.group(1))
        objs = re.findall(r'`([^`]+)`', m.group(3))
        for s in subs:
            have = graph.get(full(s))
            if have is None:
                bad.append(('unknown', s)); continue
            for o in objs:
                if full(o) not in have:
                    bad.append((s, 'does not import', o))
            if m.group(2) and set(map(full, objs)) != set(have):
                bad.append((s, 'imports more than', objs, have))
for b in bad:
    print(*b)
print(len(bad), 'false')
