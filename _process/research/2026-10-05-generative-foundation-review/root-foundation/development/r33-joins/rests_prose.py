"""R33 (G5): the prose of the four learning-through-a-map modules says "predicts" where it said an
extrapolation "rests in accord"; only comment text changes, never a name in backticks or code."""
import re
import sys

W = r'(\s+(?:-- )?)'  # a space or a line break with indentation inside a doc comment


def sub(s):
    rules = [
        (r'comes' + W + r'to' + W + r'rest' + W + r'in' + W + r'accord' + W + r'with', 'predicts'),
        (r'come' + W + r'to' + W + r'rest' + W + r'in' + W + r'accord' + W + r'with', 'predict'),
        (r'rests' + W + r'in' + W + r'accord' + W + r'with', 'predicts'),
        (r'rests' + W + r'in' + W + r'accord' + W + r'on', 'predicts on'),
        (r'rests' + W + r'in' + W + r'accord\b', 'predicts'),
        (r'resting' + W + r'in' + W + r'accord' + W + r'with', 'predicting'),
        (r'resting on both', 'predicting on both'),
        (r'resting on two', 'predicting on two'),
        (r'rests on both', 'predicts on both'),
    ]
    n = 0
    for pat, rep in rules:
        s, k = re.subn(pat, rep, s)
        n += k
    return s, n


def doc_spans(s):
    """Spans of doc and block comments."""
    for m in re.finditer(r'/-.*?-/', s, re.S):
        yield m.start(), m.end()


for path in sys.argv[1:]:
    s = open(path).read()
    out, last, total = [], 0, 0
    for a, b in doc_spans(s):
        out.append(s[last:a])
        seg, k = sub(s[a:b])
        out.append(seg)
        total += k
        last = b
    out.append(s[last:])
    open(path, 'w').write(''.join(out))
    print(path, total)
