#!/usr/bin/env python3
"""Write an I3d periphery instance checker from the I3c continuation checker (run from the repository root):
python3 -B make_checker.py SPEC.json. The spec names the directory, target, receipt stem, depth of the Lean root,
the declarations that must have empty axiom reports, the docstring and the scope."""
import json
import re
import sys
from pathlib import Path

LEAN = Path('experiments/integrated-correction/general-framework/generative-basis/lean')
TEMPLATE = LEAN / 'systems-complexity/analysis/check_continuation_correspondence.py'

spec = json.loads(Path(sys.argv[1]).read_text())
s = TEMPLATE.read_text()
doc_end = s.index('"""', s.index('"""') + 3) + 3
s = '#!/usr/bin/env python3\n"""' + spec['doc'].strip() + '\n"""' + s[doc_end:]
s = s.replace('LEAN_ROOT = HERE.parents[1]', f'LEAN_ROOT = HERE.parents[{spec["depth"]}]')
s = s.replace('TARGET = "ContinuationCorrespondence"', f'TARGET = "{spec["target"]}"')
s = s.replace('HERE / "continuation-correspondence-verification.json"', f'HERE / "{spec["stem"]}-verification.json"')
s = s.replace('HERE / "continuation-correspondence-checks"', f'HERE / "{spec["stem"]}-checks"')
s = s.replace('prefix="continuation-correspondence-"', f'prefix="{spec["stem"]}-"')
start = s.index('# The single-plan correspondence')
end = s.index('AUDIT = re.compile')
names = ', '.join(json.dumps(n) for n in spec['empty'])
s = s[:start] + spec['empty_comment'].rstrip() + '\n' + \
    f'EMPTY = {{"{spec["namespace"]}." + n for n in\n         [{names}]}}\n' + s[end:]
start = s.index('SCOPE = (')
end = s.index('\n)\n', start) + 3
scope = spec['scope']
lines, line = [], ''
for word in scope.split(' '):
    if len(line) + len(word) + 1 > 96:
        lines.append(line)
        line = word
    else:
        line = (line + ' ' + word) if line else word
lines.append(line)
body = '\n'.join(f'    {json.dumps(l + (" " if i < len(lines) - 1 else ""), ensure_ascii=False)}' for i, l in enumerate(lines))
s = s[:start] + 'SCOPE = (\n' + body + '\n)\n' + s[end:]
for old in ('ContinuationCorrespondence', 'continuation-correspondence'):
    assert old not in s, old
out = LEAN / spec['dir'] / spec['checker']
out.write_text(s)
print(out)
