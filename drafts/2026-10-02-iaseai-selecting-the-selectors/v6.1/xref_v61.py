"""Structure checks for Theory V6.1. Run from v6.1/:  python3 xref_v61.py

1. Re-assembles THEORY, SUPPLEMENT, DISCUSSION and the registers from src/ (src/assemble_v61.py), which checks
   unknown and duplicate keys, use of a core result before its declaration, words per section, the share of
   Parts III-IV, and banned phrases.
2. Citation coverage: every author-year citation in the three documents has an entry in that document's list.
3. Must stay in the core: the 32 items of the structure plan appear in THEORY.md.
4. The Chinese guide and Section 1.2 have the same number of items.
5. No particular state or firm is named in the core's prose (references and registers are exempt).
"""
import re, subprocess, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ok = True
r = subprocess.run([sys.executable, str(HERE / 'src' / 'assemble_v61.py')], capture_output=True, text=True)
print(r.stdout.strip())
if r.returncode:
    ok = False

CIT = re.compile(r"\b([A-Z][A-Za-zÀ-ÿ'’\-]+)(?:(?:,| and) (?:[A-Z][A-Za-zÀ-ÿ'’\-]+|de|van|von)(?: [A-Z][A-Za-zÀ-ÿ'’\-]+)?)*(?: et al\.)? \(?((?:1[5-9]|20)\d\d[ab]?)(?:/\d+)?")
SKIP = {'Section', 'Sections', 'Proposition', 'Theorem', 'Lemma', 'Remark', 'Definition', 'Corollary', 'Assumption', 'Stage',
        'Convention', 'Treaty', 'Protocol', 'September', 'October', 'December', 'In', 'Test', 'The', 'EV', 'Branch'}
ALIAS = {'Mesquita': 'Bueno', 'Bó': 'Dal', 'Evera': 'Van', 'Reenen': 'Van'}
print('\ncitation coverage:')
for doc in ('THEORY', 'SUPPLEMENT', 'DISCUSSION'):
    text = (HERE / f'{doc}.md').read_text()
    body, _, refs = text.partition('\n## References')
    have = set()
    for line in refs.splitlines():
        if not line.startswith('- '):
            continue
        first = line[2:].split(',')[0].split(' ')[0].strip('.*')
        for pre, k in (('Dal Bó', 'Dal'), ('Bueno de', 'Bueno'), ('Van Evera', 'Van'), ('Van Reenen', 'Van'),
                       ('Maynard Smith', 'Maynard'), ('Yan Fu', 'Yan')):
            if line[2:].startswith(pre):
                first = k
        for y in re.findall(r'\b((?:1[5-9]|20)\d\d[ab]?)', line):
            have.add((first, y))
    missing = set()
    for m in CIT.finditer(body):
        a = re.sub(r"['’]s$", '', m.group(1)); a = ALIAS.get(a, a)
        if a in SKIP:
            continue
        if (a, m.group(2)) not in have:
            missing.add(f'{a} {m.group(2)}')
    print(f'  {doc}: {"all cited works listed" if not missing else "MISSING " + ", ".join(sorted(missing))}')
    ok &= not missing

theory = (HERE / 'THEORY.md').read_text().split('\n## References')[0]
MUST = ['distinct from contribution', 'removes the balanced', 'The primitive is selection, not greed',
        'rewarded with anything other than more advantage', 'Why "meta-attractor"', '讲理', '局部胜出的策略拿走了理性的名字',
        'molochlization', 'change the basin, then add speed', 'another planet', 'Federations', 'not a weight $\\theta$',
        '和实生物，同则不继', '我们即是集', 'The game, not the act', 'growth is not the danger; the mind is',
        'The meaning is affirmative', 'prediction has to be shared', 'Survival as the minimum', 'instrument and incarnation',
        'individual–collective axis', '力之所及，责之所在', '共开、共续、不夺共续', 'Trees are the image', 'Trust is mainly an outcome',
        'way out of an optimization trap', 'The reform dilemma', 'guardian test', 'no better guardian is an answer',
        'five endgames', 'plurality of decorrelated units', 'They are different arrangements']
miss = [m for m in MUST if m not in theory]
print(f'\nmust stay in the core: {len(MUST) - len(miss)}/{len(MUST)} present' + (f'; missing {miss}' if miss else ''))
ok &= not miss

guide = theory.split('**论证链')[1].split('**判断')[0]
n_guide = len(re.findall(r'(?m)^\d+\. ', guide))
s12 = theory.split('### 1.2')[1].split('### 1.3')[0]
n_12 = len(re.findall(r'(?m)^\d+\. ', s12))
print(f'\nguide items {n_guide}, Section 1.2 items {n_12}: {"match" if n_guide == n_12 else "MISMATCH"}')
ok &= n_guide == n_12

NAMES = r'\b(United States|U\.S\.|America(n)?|China|Chinese government|Russia|European Union|OpenAI|Anthropic|Google|DeepMind|Microsoft|Meta Platforms|xAI|Beijing|Washington)\b'
hits = [m.group(0) for m in re.finditer(NAMES, theory)]
print(f'\nnamed states or firms in core prose: {"none" if not hits else hits}')
ok &= not hits

print('\nALL CHECKS PASS' if ok else '\nSOME CHECKS FAIL')
sys.exit(0 if ok else 1)
