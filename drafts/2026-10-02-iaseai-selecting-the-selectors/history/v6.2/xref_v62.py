"""Structure checks for Theory V6.2. Run from v6.2/:  python3 xref_v62.py

1. Re-assembles THEORY, SUPPLEMENT, DISCUSSION and the registers from src/ (src/assemble_v62.py), which checks
   unknown and duplicate keys, use of a core result before its declaration, unresolved markup, doubled kind names
   in every assembled document, and banned phrases; it reports words per section as figures (no caps in V6.2).
2. Citation coverage in both directions: every author-year citation in the three documents has an entry in that
   document's list, cited in the entry's author form, and every listed entry is cited in that document. Keys are
   (first author's surname with particles, second author's surname or "et al.", year), shared with src/refs_v62.py.
   Citations in the registers that no list carries are reported for information.
3. Must stay in the core: the 32 items of the structure plan appear in THEORY.md.
4. The Chinese guide and Section 1.2 have the same number of items, and each guide item carries the key terms of
   its Section 1.2 item (bilingual term list, per-item share against a threshold).
5. No particular state or firm is named in the core's prose (references and registers are exempt).
"""
import re, subprocess, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ok = True
r = subprocess.run([sys.executable, str(HERE / 'src' / 'assemble_v62.py')], capture_output=True, text=True)
print(r.stdout.strip())
if r.returncode:
    ok = False

sys.path.insert(0, str(HERE / 'src'))
from refs_v62 import entry_keys, citations, loose_match      # one keying rule for the build and the check
print('\ncitation coverage (keys: first author with particles, second author or "et al.", year; both directions):')
listed_anywhere = set()
for doc in ('THEORY', 'SUPPLEMENT', 'DISCUSSION'):
    text = (HERE / f'{doc}.md').read_text()
    body, _, refs = text.partition('\n## References')
    entries = [l for l in refs.splitlines() if l.startswith('- ')]
    have = {k: l for l in entries for k in entry_keys(l)}
    listed_anywhere |= set(have)
    cited = citations(body)
    missing, form, used = [], [], set()
    for k, v in sorted(cited.items()):
        if k in have:
            used.add(have[k]); continue
        near = loose_match(k, have)
        if near:
            used.add(have[near]); form.append(f'"{v}" vs entry "{have[near][2:44]}…"')
        else:
            missing.append(v)
    uncited = [l[2:70] + '…' for l in entries if l not in used]
    for l in entries:                                   # a combined entry ('1960. *A*; 1966. *B*.') must have each year cited
        ks = entry_keys(l)
        if l in used and len(ks) > 1:
            uncited += [f'{k[0]} {k[2]} (second work of the combined entry "{l[2:40]}…")' for k in ks if k not in cited]
    nokey = [l[2:60] for l in entries if not entry_keys(l)]
    twice = sorted({f'{k[0]} {k[2]}' for k in have if sum(k in entry_keys(l) for l in entries) > 1})
    print(f'  {doc}: {len(cited)} works cited, {len(entries)} listed')
    for label, xs in (('MISSING (cited, not listed)', missing), ('AUTHOR FORM DIFFERS from the entry', form),
                      ('UNCITED (listed, not cited in this document)', uncited), ('UNKEYED entry (no author-year)', nokey),
                      ('LISTED TWICE (two entries with one key)', twice)):
        if xs:
            print(f'    {label}:'); [print(f'      {x}') for x in xs]
    ok &= not (missing or form or uncited or nokey or twice)
regs = {}
for name in ('CLAIMS', 'EVIDENCE', 'TESTS', 'LEDGER', 'CHANGELOG'):
    p = HERE / f'{name}.md'
    if p.exists():
        for k, v in citations(p.read_text()).items():
            if k not in listed_anywhere and not loose_match(k, listed_anywhere):
                regs.setdefault(name, []).append(v)
print('  registers (information, not a failure): ' + ('every author-year citation is listed in some document' if not regs
      else '; '.join(f'{n} cites {", ".join(sorted(set(v)))} (in no reference list)' for n, v in regs.items())))

theory = (HERE / 'THEORY.md').read_text().split('\n## References')[0]
MUST = ['distinct from contribution', 'removes the balanced', 'The primitive is selection, not greed',
        'rewarded with anything other than more advantage', 'Why "meta-attractor"', '讲理', '局部胜出的策略拿走了理性的名字',
        'molochlization', 'change the basin, then add speed', 'another planet', 'Federations', 'not a weight $\\theta$',
        '和实生物，同则不继', '我们即是集', 'The game, not the act', 'growth is not the danger; the mind is',
        'The meaning is affirmative', 'prediction has to be shared', 'Survival as the minimum', 'instrument and incarnation',
        'individual–collective axis', '力之所及，责之所在', '共开、共续、不夺共续', 'Trees are the image', 'Trust and verification are both conditions',
        'way out of an optimization trap', 'The reform dilemma', 'guardian test', 'no better guardian is an answer',
        'five endgames', 'plurality of decorrelated units', 'They are different arrangements']
miss = [m for m in MUST if m not in theory]
print(f'\nmust stay in the core: {len(MUST) - len(miss)}/{len(MUST)} present' + (f'; missing {miss}' if miss else ''))
ok &= not miss

# The guide and Section 1.2, item by item, by key terms (one bilingual list; a term counts for an item when it is in
# the English item; the item passes when at least GUIDE_MIN of those terms are in the Chinese item of the same number).
TERMS = [('selection', r'select', r'选择'), ('winning', r'\bwin', r'赢|胜'), ('carrier', r'carrier', r'载体'),
    ('reinvest', r'reinvest|compound', r'复利|再投'), ('decisive lead', r'decisive', r'决定性'), ('stakes', r'stakes', r'赌注|筹码|利害'),
    ('defection', r'defection|deviation', r'偏离|背叛'), ('sanction', r'sanction', r'制裁|惩罚|罚'),
    ('correction', r'correct', r'纠错|纠正'), ('shared language', r'language|understanding|\btalk', r'语言|话语|理解'),
    ('selectors', r'selectors', r'选择者'), ('reflexive closure', r'reflexive|closure', r'反身|闭合'),
    ('meta-attractor', r'meta-attractor', r'元吸引子'), ('loop gain', r'loop gain', r'环路增益'), ('interconnected', r'interconnected|not a list', r'互相|相互|不是清单'),
    ('beyond sanction', r'beyond sanction', r'制裁不到|不受制裁|超出制裁'), ('outruns correction', r'outruns', r'跟不上|超过纠错|甩开'),
    ('substrate', r'substrate', r'基质|基底|载体'), ('host', r'\bhost', r'母体'), ('one system', r'one system', r'一体|一个系统'),
    ('equal incidence', r'equal incidence|bind[s]? all alike', r'等额|一律'), ('evasion', r'evasion', r'规避'),
    ('relative objective', r'relative objective', r'相对目标'), ('self-model', r'self-model', r'自我模型|自我'),
    ('irreversible', r'irreversible', r'不可逆'), ('anticipation on a model', r'anticipated|accurate model', r'预先|准确模型'),
    ('understood', r'understood', r'理解'), ('learning', r'learned', r'学习|试错'), ('appropriable', r'appropriable', r'占有'),
    ('cost of control', r'cost of control', r'控制成本'), ('rate', r'\brate\b', r'速率'), ('reform', r'reform', r'改革'),
    ('re-absorbed', r're-absorbed', r'重新吸收|吸收'), ('floor and alarm', r'floor|alarm', r'底线|警报|报警'),
    ('acceleration', r'accelerat', r'加速'), ('enforcement', r'enforc', r'执行|强制'), ('restraint', r'restraint', r'克制'),
    ('threshold', r'threshold', r'门槛|阈值'), ('growth', r'growth', r'增长'), ('tempo', r'tempo|speed', r'速度|速率|节奏'),
    ('blocs', r'bloc', r'集团'), ('principal', r'principal|faithful', r'委托人|忠实'), ('delegation', r'delegation', r'委托'),
    ('outermost loop', r'outermost loop', r'最外层回路'), ('divergence', r'divergence', r'偏差'),
    ('common constraint', r'common constraint', r'共同.{0,6}约束'), ('lineages', r'lineage', r'谱系'),
    ('weak/strong incarnation', r'Weakly|Strongly|incarnation', r'化身'), ('trajectory', r'trajectory', r'轨迹'),
    ('signatures', r'signature', r'征候'), ('evidence gaps', r'gaps in the evidence', r'缺口'), ('race', r'\brace\b', r'竞赛'),
    ('repetition', r'repetition', r'重复'), ('collective course', r'collective course', r'集体路线'),
    ('one standard', r'one standard', r'同一标准|同一个标准'), ('every capable actor', r'every capable actor', r'所有有能力的行动者'),
    ('not alone', r'\balone\b', r'单方面|单独'), ('generative', r'generative', r'生成|生生'), ('contribution', r'contribution', r'贡献'),
    ('through what all share', r'what all share', r'共同之物|共有之物'), ('not through winners', r'not through its winners', r'不经由赢家'),
    ('function by function', r'function by function', r'按功能|逐项功能'), ('trust', r'\btrust', r'信任'),
    ('staged transition', r'staged transition', r'分阶段'), ('three tiers', r'three tiers', r'三个层级|三层|三级'),
    ('cruxes', r'crux', r'关键分歧|症结'), ('warranted now', r'warranted now', r'现在就|此刻|当下就')]
GUIDE_MIN = 0.6
guide = theory.split('**论证链')[1].split('**判断')[0]
s12 = theory.split('### 1.2')[1].split('### 1.3')[0]
def items(txt):
    return [m.group(1) for m in re.finditer(r'(?ms)^\d+\. (.*?)(?=\n\s*\n|\n\d+\. |\Z)', txt)]
g_items, e_items = items(guide), items(s12)
print(f'\nguide items {len(g_items)}, Section 1.2 items {len(e_items)}: {"match" if len(g_items) == len(e_items) else "MISMATCH"}')
ok &= len(g_items) == len(e_items)
print(f'guide against Section 1.2, item by item (share of the English item\'s key terms found in the guide item; pass at {GUIDE_MIN:.0%}):')
for n, (e, g) in enumerate(zip(e_items, g_items), 1):
    want = [t for t, en, _ in TERMS if re.search(en, e, flags=re.I)]
    lost = [t for t, en, zh in TERMS if t in want and not re.search(zh, g)]
    share = 1 - len(lost) / max(len(want), 1)
    print(f'  {n}. {share:4.0%} of {len(want):2} terms' + ('' if share >= GUIDE_MIN else '  BELOW') + (f'; not in the guide: {", ".join(lost)}' if lost else ''))
    ok &= share >= GUIDE_MIN

NAMES = r'\b(United States|U\.S\.|America(n)?|China|Chinese government|Russia|European Union|OpenAI|Anthropic|Google|DeepMind|Microsoft|Meta Platforms|xAI|Beijing|Washington)\b'
hits = [m.group(0) for m in re.finditer(NAMES, theory)]
print(f'\nnamed states or firms in core prose: {"none" if not hits else hits}')
ok &= not hits

print('\nALL CHECKS PASS' if ok else '\nSOME CHECKS FAIL')
sys.exit(0 if ok else 1)
