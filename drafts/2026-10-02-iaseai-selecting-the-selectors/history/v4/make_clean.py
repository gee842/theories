"""Make THEORY-clean.md, a reading copy of THEORY.md without repair notes and version history.

Removes: the header's version history; parentheticals that cite repairs or reviews; sentences that
begin with a version tag (v3.1, v4.x); the version notes of Section 1.6; Appendix C. Leaves every
result, proof and number. Run after any change to THEORY.md.
"""
import os, re
here = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(here, 'THEORY.md')).read()

# header: keep title, replace history with one line, keep the Chinese summary onward
i = s.index('*Theory draft v4.5'); j = s.index('**中文概要.**')
s = s[:i] + '*Reading copy of v4.5, generated from `THEORY.md` by `make_clean.py`. It omits repair notes, version history and Appendix C; the working document keeps them.*\n\n' + s[j:]
s = s.replace('\nv3.1 起的每个结果都保留了。各轮评审指出的问题都在原处逐条修复（附录 C）。\n', '\n')

# Section 1.6 version notes
i = s.index('v4.1 claimed one meaning throughout'); j = s.index('Overlaps that remain are between')
s = s[:i] + s[j:]

# Appendix C
i = s.index('## Appendix C.'); j = s.index('## References')
s = s[:i] + s[j:]

# bold-title qualifiers such as "; restated, repairs M-N1" or "; new, from E-N13"
s = re.sub(r';\s*(?:restated|repaired|rewritten|new|was Proposition 29|replaces Lemma E0|relabelled in v4\.5)[^()]*?(?=\)\.?\*\*|\)\*)', '', s)
s = re.sub(r'\((?:restated|repaired|rewritten|new)(?:, [^()]*)?\)', '', s)

# trailing repair citations inside parentheses that contain nested parentheses
s = re.sub(r'[;,]\s*(?:repairs?|reviews?)\b[^()]*?(?=\))', '', s)
# repair paragraphs and blocks that only narrate earlier versions
s = '\n'.join(l for l in s.split('\n') if not l.lstrip(' -0123456789.').startswith('*Repair'))
s = s.replace('Three qualifications follow from the economics review (E10):', 'Three qualifications follow:')
i = s.find('v4.1 stated Theorem A as one claim under K1–K7.')
if i >= 0:
    j = s.index('Each consequence carries the condition it inherits.', i)
    s = s[:i] + 'Theorem A is a classification along two axes. The first is decisiveness: $r$, and whether a decisive winner extends its dominance (L4). The second is speed: $g_s$ and $a$, under (L1). ' + s[j:]

# parentheticals that cite repairs or reviews (no nested parentheses)
pat = re.compile(r'\s?\((?:[^()]*?(?:\brepairs?\b|\breview\b|\breviews\b|review\'s|-N\d+)[^()]*)\)')
for _ in range(3):
    s = pat.sub('', s)
s = re.sub(r'\s?\((?:M|E|IR|S|A)\d+(?:, ?(?:M|E|IR|S|A)\d+)*\)', lambda m: m.group(0) if re.fullmatch(r'\s?\((?:A[1-8]|E[0-3]|S)\)', m.group(0)) else '', s)

# sentences that begin with a version tag
out = []
for line in s.split('\n'):
    st = line.lstrip()
    if st.startswith('|') or st.startswith('$$') or st.startswith('#') or st.startswith('```') or st.startswith('- *v4.') or st.startswith('`'):
        out.append(line); continue
    if re.match(r'^(\d+\.\s+|-\s+)?\*?v(3\.1|4\.\d)(–4\.\d)?\b', st):
        lead = re.match(r'^(\s*(?:\d+\.\s+|-\s+)?)', line).group(1)
        body = line[len(lead):]
        parts = re.split(r'(?<=[.!?])\s+(?=[A-Z*"(v])', body)
        keep = [p for p in parts if not re.match(r'^\*?v(3\.1|4\.\d)', p)]
        if not keep:
            continue
        line = lead + ' '.join(keep)
    else:
        lead = re.match(r'^(\s*(?:\d+\.\s+|-\s+)?)', line).group(1)
        body = line[len(lead):]
        parts = re.split(r'(?<=[.!?])\s+(?=[A-Z*"(v])', body)
        keep = [p for p in parts if not re.match(r'^\*?v(3\.1|4\.\d)(–4\.\d)?\b', p)]
        line = lead + ' '.join(keep) if keep else ''
    # balance a stray italic marker left by a removed sentence
    t = re.sub(r'\*\*', '', line)
    if t.count('*') % 2 == 1:
        if line.rstrip().endswith('*') and not line.lstrip(' -0123456789.').startswith('*'):
            line = line.rstrip()[:-1]
        elif line.lstrip(' -0123456789.').startswith('*') and not line.rstrip().endswith('*'):
            line = line.rstrip() + '*'
    out.append(line)
s = '\n'.join(out)
s = re.sub(r'\n{3,}', '\n\n', s)
s = re.sub(r' +([.,;:])', r'\1', s)
s = re.sub(r'\(\s*\)', '', s)
open(os.path.join(here, 'THEORY-clean.md'), 'w').write(s)
print('clean words', len(s.split()))
