"""Split doc-comment lines longer than 100 characters that are not in the original file, at a space,
with the indentation of the line (a bullet's text indentation for a bullet line). Code is untouched.
usage: rewrap.py ORIGINAL EDITED"""
import re
import sys

orig, path = sys.argv[1], sys.argv[2]
before = set(open(orig).read().split('\n'))
s = open(path).read()
spans = [(m.start(), m.end()) for m in re.finditer(r'/-.*?-/', s, re.S)]


def in_comment(pos):
    return any(a <= pos < b for a, b in spans)


out, pos = [], 0
for line in s.split('\n'):
    start = pos
    pos += len(line) + 1
    if len(line) <= 100 or line in before or not in_comment(start):
        out.append(line)
        continue
    while len(line) > 100:
        m = re.match(r'(\s*)(\* |- )?', line)
        indent = m.group(1) + ('  ' if m.group(2) else '')
        cut = line.rfind(' ', 0, 100)
        if cut <= len(indent):
            break
        out.append(line[:cut])
        line = indent + line[cut + 1:]
    out.append(line)
open(path, 'w').write('\n'.join(out))
