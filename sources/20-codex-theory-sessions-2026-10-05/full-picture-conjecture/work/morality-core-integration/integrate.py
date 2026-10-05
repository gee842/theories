from pathlib import Path
import difflib
import hashlib
import json
import re

workspace = Path('/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture')
work = workspace / 'work/morality-core-integration'
root = Path('/Users/ren/theories')
canonical = root / 'theories/shengsheng-buxi-generative-existence/README.md'
index = root / 'sources/SOURCES.md'
source = root / 'sources/15-codex-theory-conversations/2026-10-05-conscience-and-universal-morality.md'
manifest = json.loads((work / 'baseline.json').read_text())
for name, record in manifest.items():
    assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == record['sha256'], f'Concurrent change: {name}'
assert not source.exists(), 'Source already exists'

before = canonical.read_text()
text = before
fragment = (work / 'core-final.md').read_text().rstrip()
source_ref = '../../sources/15-codex-theory-conversations/2026-10-05-conscience-and-universal-morality.md'

def replace_once(old, new):
    global text
    assert text.count(old) == 1, f'Expected one occurrence: {old[:90]}'
    text = text.replace(old, new, 1)

replace_once(
    'Because anyone who can ask "what ought I to do?" already exists, and existing already depends on the process continuing, no agent can coherently repudiate the process it is a form of; the further step — that one ought to keep those conditions open *for others too* — is not squeezed out of that fact but openly declared as a minimal public commitment, defended by what is destroyed when it is denied.',
    'For an agent committed to continued agency, preserving its indispensable conditions is a conditional requirement. The further step — that the basic interests and standing of others matter too — is openly declared as a minimal public commitment: relevant reasons cannot be arbitrarily erased merely by changing whose pain, needs or capacities are at stake. 良知 (conscience) names the fallible capacity to feel another\'s situation and to reflect on and revise one\'s own action; its formation and correction belong inside the theory.'
)
replace_once('## The argument\n',
    '## The argument\n\n**Current normative core, 2026-10-05.** At Ren\'s explicit request, the section [良知与共同生成的规范核心](#良知与共同生成的规范核心) now joins conscience, publicly defended cross-subject reasons, and the feasibility of shared generative conditions. It governs the present normative reading of the earlier formulations preserved below. Moral commitment, evidence about its biological and social mechanisms, feedback hypotheses, and conditional mathematical results retain their distinct status. [Source and verbatim request](' + source_ref + ').\n'
)
replace_once('### The value chain: one criterion in many dimensions',
    fragment + '\n\n### The value chain: one criterion in many dimensions')
replace_once(
    'Nothing in the ethics is an independent axiom. Each value is the same openness criterion seen along a different dimension, and the derivation was written out by Ren and the model together in one sitting on 2026-05-02:',
    'The May 2026 formulation presented the virtues as requiring no independent ethical axiom: each was the same openness criterion seen along a different dimension, developed by Ren and the model together on 2026-05-02. That is the genealogy of the following account. The current normative core follows the v2 reset and the 2026-10-05 incorporation: the moral standing of others and the rejection of arbitrary exclusion are explicit commitments. Within that commitment, the virtues articulate different requirements of shared generation; their authority does not follow from evolutionary success alone. [Current formulation and provenance](' + source_ref + ').'
)

conscience_end = 'which is the theory\'s greatest hope and its deepest fear in one sentence.'
replace_once(conscience_end, conscience_end + ' The current core above gives this account a functional definition and separates the proposed evolutionary mechanism from the normative test of its judgements; evidence for helping or neural involvement does not establish an infallible conscience. [2026-10-05 clarification](' + source_ref + ').')

claims = '''### R 良知与共同生成 2026年10月5日

These are the current core formulations, incorporated at Ren's request. Their wording is AI-assisted; the source preserves Ren's own words separately. Earlier claims remain as genealogy. Source for claims 450–455: [Conscience and universal morality](SOURCE), especially 纳入正文的核心表述, 经验依据及其边界, and 与条件结果的接口.

450. **Cross-subject reasons are a normative root.** Pain, basic needs and capacities that count as reasons cannot be arbitrarily discounted merely because the subject changes. Relevant differences require defensible reasons; this is an openly defended commitment, not a deduction from selection or survival. [value stance]
451. **Shared generation concerns standing, relations and costs.** Growth, innovation, cooperation and stability are insufficient moral tests. Rest, exit, limits and ending harmful processes can protect shared generative conditions. Universal consideration permits context-sensitive decisions and does not supply a unique aggregation rule for every conflict. [value stance; practical direction]
452. **良知 is fallible moral orientation and reflection.** Its functional definition is the capacity, formed in shared life, to feel another's situation and reflect on and revise one's action. Evolutionary, developmental, cultural and institutional contributions form a mechanism hypothesis; the cited helping and neural studies support parts of it, not an innate infallible moral code. [definition; mechanism hypothesis; limited empirical support]
453. **Protection and responsibility have different conditions.** Inability to reciprocate, argue or bear duties does not cancel standing. Responsibility depends on knowledge, control, actual alternatives and participation in creating the constraints. Functional agency alone does not prove an artificial system's sentience or moral patienthood. [value stance; conceptual distinction]
454. **Generative and destructive feedback are two proposed mechanism families.** Their moral direction is evaluated through the normative commitment; occurrence, stability, transitions and attractors require specific models and evidence. This is not an exactly-two-attractors theorem and allows mixed states, cycles and persistent domination. [mechanism hypothesis]
455. **Continuation mathematics tests the realizability of independently justified requirements.** Protected conditions and progress targets are inputs. Conditional results about compatible policies cannot derive moral standing, excuse every infeasible obligation, or identify recurring specified progress with inexhaustible novelty. [conditional; interpretation boundary]

'''.replace('SOURCE', source_ref)
assert not re.search(r'^450\.', text, re.M)
replace_once('---\n\n## Terms', claims + '---\n\n## Terms')

for claim, note in [
    ('128.', ' **Current clarification:** this earlier argument against relativism is preserved as genealogy; cross-cultural discussion itself does not prove moral universality. Claims 450–451 state the current normative commitment and its limits.'),
    ('251.', ' **Current clarification:** claim 452 distinguishes the functional definition, the evolutionary hypothesis and the limited empirical support; claims 450 and 453 specify the normative commitments.')
]:
    matched = [line for line in text.splitlines() if line.startswith(claim)]
    assert len(matched) == 1
    replace_once(matched[0], matched[0] + note + ' [Source](' + source_ref + ').')

old_row = '| innate knowing | 良知 | 生生感应器 | 2026-07-14 第七章 | The generative grain\'s first appearance in the human mind — a sensor, not a finished product |'
new_row = '| conscience and innate knowing | 良知 | 生生感应器 | 2026-07-14 第七章; 2026-10-05 core incorporation | A fallible capacity, formed in shared life, to feel another\'s situation and reflect on and revise one\'s action; evolved and learned mechanisms remain empirically testable. [Current source](' + source_ref + ') |'
replace_once(old_row, new_row)

replace_once('**Which formulation is strongest, and for what.**',
    '**2026-10-05 · conscience and the normative core.** Ren proposed an evolved basis for conscience and a connection to universal morality, then explicitly requested incorporation into the core. The present addition joins a public cross-subject principle to fallible moral capacities, two testable feedback families, and the conditional feasibility of protected continuation. It preserves the v2 distinction between mechanism and commitment and qualifies the earlier independent-axiom claim. The original statements and the AI-assisted formulation are kept separately in the [new source](' + source_ref + ').\n\n**Which formulation is strongest, and for what.**')

replace_once('### Process files consulted',
    '### 15-codex-theory-conversations\n\n- [2026-10-05-conscience-and-universal-morality.md](' + source_ref + ') — Ren\'s verbatim proposal and incorporation request; the AI-assisted current normative core; five primary studies with limits; the boundary between ethical justification and conditional continuation results.\n\n### Process files consulted')

header = (work / 'source-header.md').read_text()
body = fragment[fragment.index('**共同生成是本论的伦理方向。**'):]
footer = (work / 'source-footer.md').read_text()
source_text = header.rstrip() + '\n\n' + body + '\n' + footer
index_before = index.read_text()
entry = '''Added 2026-10-05: [15-codex-theory-conversations/2026-10-05-conscience-and-universal-morality.md](15-codex-theory-conversations/2026-10-05-conscience-and-universal-morality.md). Ren's proposal connecting evolution, conscience and universal morality, followed by his explicit request to incorporate it into the theoretical core. Preserves his words separately from the AI-assisted formulation and internal reviews. The canonical 生生 theory now states a public cross-subject normative principle, fallible conscience, distinct conditions for moral standing and responsibility, two testable feedback families, and a conditional interface to continuation mathematics. Five primary studies support limited biological and behavioral claims; no exactly-two-attractor law, derivation of unique morality from selection, or complete universal theory is established. Existing source snapshots remain unchanged.\n'''
index_after = index_before.rstrip() + '\n\n' + entry

# Every existing byte is retained except the explicit replacements above and
# trailing blank lines in the source index, which are normalized at the append.
source.write_text(source_text)
index.write_text(index_after)
canonical.write_text(text)

out = workspace / 'outputs/conscience-and-morality-core.md'
assert not out.exists(), 'Output already exists'
display_fragment = fragment.replace('### 良知与共同生成的规范核心\n\n', '', 1)
display_fragment = display_fragment.replace('../../sources/', '/Users/ren/theories/sources/')
out.write_text('# 良知与共同生成的理论核心修订\n\n'
    '已于2026年10月5日纳入生生不息论的权威正文。本文件是本次新增核心段落的审阅副本；正文中的总论、价值链、良知条目、主张450至455及来源谱系也已协调更新。\n\n'
    '权威正文位置：`/Users/ren/theories/theories/shengsheng-buxi-generative-existence/README.md`。\n\n'
    + display_fragment + '\n')

diff = ''.join(difflib.unified_diff(before.splitlines(True), text.splitlines(True), fromfile='canonical.before.md', tofile=str(canonical)))
diff += ''.join(difflib.unified_diff(index_before.splitlines(True), index_after.splitlines(True), fromfile='sources-index.before.md', tofile=str(index)))
(work / 'integration.diff').write_text(diff)
(work / 'changed-files.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [canonical,index,source,out]},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'canonical':str(canonical),'new_source':str(source),'output':str(out),'added_claims':[450,451,452,453,454,455],'canonical_delta_lines':len(text.splitlines())-len(before.splitlines())},ensure_ascii=False,indent=2))
