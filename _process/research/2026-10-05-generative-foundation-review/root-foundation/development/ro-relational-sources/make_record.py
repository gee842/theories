#!/usr/bin/env python3
"""Write RO's record chinese-sources-on-the-spine: python3 -B make_record.py STUDY_SECTION D_NUMBER

The passage map is checked first (verify_ro.py must pass, with the chapter in place), and the study section and the
decision must exist. No Lean is added: the record is an assessment, reviewed and scoped, whose evidence is the passage
map and its check. Run after apply_text.py."""
import datetime
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
KIT = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/ro-relational-sources'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
DC = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md'
RECORDS = ROOT / 'theories/becoming/results/records'
CHAPTER = 'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md'
CANON = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-19-relational-ontology-of-chinese-thought.md'
PROVENANCE = 'sources/chinese-classical-texts/PROVENANCE.json'
section, d = sys.argv[1], sys.argv[2]
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
ASK = ('“整个中国思想的源头，道家，易经，以及整个文字符号系统，包括武（止戈 ），和一些其他的理论体系中，例如儒家，也延续了这一套'
       '“relational ontology”，因此，我希望你好好阅读，把两者之间的关系map出来，可以用sub agents，然后再体系性的整合进我们的理论”')


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


check = subprocess.run([sys.executable, '-B', str(HERE / 'verify_ro.py')], capture_output=True, text=True)
assert check.returncode == 0, check.stdout + check.stderr
assert re.search(rf'^## {section}\. The Chinese sources on the spine \(RO\)$', (ROOT / STUDY).read_text(), re.M), section
assert f'| D{d} | the readings of the Chinese sources on the spine' in (ROOT / DC).read_text(), d
passages = json.loads((HERE / 'passages.json').read_text())['passages']
n = len(passages)
kinds = {k: sum(p['kind'] == k for p in passages) for k in ('agreement', 'scope', 'divergence')}
decls = len({x for p in passages for x in p['declarations']})
records = sorted({r for p in passages for r in p['records']})
files = len(json.loads((ROOT / PROVENANCE).read_text())['files'])
ANCHOR = f'{STUDY}#{section}-the-chinese-sources-on-the-spine-ro'

record = {
    'schema_version': 2,
    'id': 'chinese-sources-on-the-spine',
    'title': {'en': 'The Chinese sources on the spine', 'zh': '中国思想诸传统在脊柱上'},
    'kind': 'assessment',
    'status': 'reviewed-scoped',
    'family': 'F01',
    'reviewed_at_utc': NOW,
    'statement': {
        'en': (f'{n} passages of nine parts of Chinese thought, quoted verbatim, are tied to the spine as agreement, '
               f'exact scope or divergence. The relational start holds across the lines; their universal forms mostly '
               f'need a scope; four non-relational overlays recur, each answered inside its tradition.'),
        'zh': (f'中国思想九个部分的 {n} 段文字，从所存文本逐字引出，逐段以相合、定域或相分对应到脊柱。关系性的起点贯穿诸线；其全称形式'
               f'大多需要定域；四种非关系之层反复出现，各在本传统内部得到回应。')},
    'hypotheses': [{
        'en': ('No Lean and no premise is added: each passage is tied to audited declarations and records as they '
               'stand; its kind and reading are the AI\'s (D' + d + '). A passage counts as relational when it reads the '
               'relation first and lets the terms differentiate within it, not from a prior ground, a nature or value '
               'fixed before relations, a will or single centre, or a contest or rank: a method requirement, not a '
               'proof of the ontology.'),
        'zh': ('不新增 Lean，不加前提：每段对应到现有的已审计声明与记录，其关系类别与读法是 AI 的（D' + d + '）。“关系的”以方法的要求检验：'
               '先读关系，让诸项在其中分化；其反面是先在的根据、先于关系而定的性或价值、意志或单一中心、争胜与等级。这是方法的要求，'
               '不是本体论的证明。')}],
    'does_not_show': [
        {'en': ('That any passage is true as stated, or that its authors meant these laws; agreement means the spine '
                'has a law of that structure, often under conditions the reading names.'),
         'zh': '任何一段如所说那样为真，或其作者意谓这些律；相合是说脊柱上有结构相同之律，常在读法写明的条件下。',
         'kind': 'correspondence'},
        {'en': ('That one relational ontology is the doctrine of every line or the consensus of the commentaries; it is '
                'a dominant thread and a position within each tradition.'),
         'zh': '一种关系本体是每一家的学说或注疏传统的共识；它是一条主导的线索，也是每一传统内部的一个立场。',
         'kind': 'non-implication'},
        {'en': ('That the graphs encode a relational ontology: the script is relational as a system of readings, while '
                'most graphs pair a category and a sound. That 武 means 止戈 by origin: the paleographic reading is kept '
                'beside the speech\'s.'),
         'zh': '文字的字形编码了一种关系本体：文字作为读法系统是关系的，而多数字形是类与声的配对。'
               '武的本义是止戈：字形史之读与楚庄王之语分开保留。',
         'kind': 'scope'},
        {'en': ('That a divergence of status (a text asserting what the theory gives only under the continuation '
                'condition) shows the text wrong; the theory asserts no ethical axiom.'),
         'zh': '地位的相分（原文断言理论只在延续条件之下给出者）说明原文错了；理论不断言伦理公理。',
         'kind': 'non-implication'}],
    'counterexamples': [],
    'standard_boundaries': ['no-ethical-premise', 'formal-not-empirical', 'names-provisional',
                            'omission-not-refutation', 'nondual-method-not-proof'],
    'validation_scope': {
        'en': (f'verify_ro.py passes: {n} passages ({kinds["agreement"]} agreements, {kinds["scope"]} exact scopes, '
               f'{kinds["divergence"]} divergences), every fragment verbatim in its preserved text ({files} files bound '
               f'by SHA-256), {decls} declarations in the current receipt, {len(records)} records, the atlas ids in an '
               f'excerpt rebuilt from the two archives, and the chapter\'s tables. Five mappers drafted; the integrator '
               f'checked every quotation, declaration and record and read every reading, correcting six (study section '
               f'{section}). Not independently reviewed; no collation with a printed edition.'),
        'zh': (f'verify_ro.py 通过：{n} 段（相合 {kinds["agreement"]}、定域 {kinds["scope"]}、相分 {kinds["divergence"]}），'
               f'每段原文逐字见于所存文本（{files} 个文件以 SHA-256 绑定），{decls} 个声明在现行回执中，{len(records)} 份记录，'
               f'图谱编号在由两个存档重建的摘录中，以及章节之表。五个映射者起草；整合者核对每条引文、声明与记录，通读每条读法，'
               f'改正六处（研究第 {section} 节）。未经独立审查；未与刻本对校。')},
    'next_delta': {
        'en': ('Seven gaps, each to be claimed before it is written: two-sided regulation of a level and its late-reading '
               'form; a code formed between formations; capture through the rule; a graded order by closure level; '
               'division across several conditions; tolerance compared across laws; the hexagram world\'s order, '
               'exchange, parity and 雜卦. Then the earlier Chinese chapters\' superseded parts moved to history.'),
        'zh': ('七项缺口，各先认领再写：水平的双向调节及迟到读法之形；在形成之间形成的编码；经由规则的捕获；以闭包层级分等的次序；'
               '跨多个条件的分；跨律比较容忍；卦的世界的卦序、互换、奇偶与杂卦。然后把较早各中国章节中被取代的部分移入历史。')},
    'correspondence': {
        'en': (f'Ren, 19 October 2026, after sharing the 易道体系图 v1.3.0: {ASK} (provenance, not warrant). The chapter '
               f'maps {n} passages of the 易传 beyond Y1–Y4, the 老子 with three commentaries and the excavated witnesses, '
               f'the 儒家 line, the script with 止戈, 庄子 and 玄学, 墨辩 and 名家, 兵家, 法家, 管子 and 纵横, the Buddhist '
               f'lines received in China, and others. Reading (the AI\'s, D{d}): the thesis holds for what the lines '
               f'start from and observe, its universal forms mostly need a scope, and four non-relational overlays recur, '
               f'each answered inside its tradition.'),
        'zh': (f'Ren，2026年10月19日，分享易道体系图 v1.3.0 之后说：{ASK}（来历，不是根据）。章节对应 {n} 段：易传（Y1–Y4 之外）、'
               f'老子及三家注与出土诸本、儒家、文字与止戈、庄子与玄学、墨辩与名家、兵家、法家、管子与纵横、汉传佛教及其他。读法（AI 的，'
               f'D{d}）：论题在诸线的起点与观察上成立，其全称形式大多需要定域，四种非关系之层反复出现，各在本传统内部得到回应。')},
    'canonical_source': CHAPTER,
    'aliases': ['the Chinese sources on the spine', '中国思想诸传统在脊柱上', 'relational ontology of Chinese thought',
                '中国思想的关系本体', '止戈为武', '止戈為武'],
    'dependencies': [
        {'id': 'hexagrams-on-the-spine', 'relation': 'interpretive',
         'detail': {'en': 'Extends the 易传 passage map beyond Y1–Y4 with the same three kinds and its own checked map.',
                    'zh': '以同样的三种关系与另一份已检查的对应，把易传的逐句对应扩展到 Y1–Y4 之外。'}},
        {'id': 'configurations-alike-by-relation', 'relation': 'interpretive',
         'detail': {'en': 'What "relational" means in the test: a configuration is how it relates.',
                    'zh': '检验中“关系的”之义：一个构形就是它怎样相关。'}}],
    'related': [{'id': r, 'detail': {'en': 'Cited by passages of the map.', 'zh': '为对应中的段落所引。'}}
                for r in ('relative-position-is-zero-sum', 'place-relations-in-context')
                if r in records and (RECORDS / f'{r}.json').exists()],
    'references': [
        {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        {'path': f'{KIT}/passages.json', 'role': 'integration', 'sha256': sha(f'{KIT}/passages.json')},
        {'path': f'{KIT}/verify_ro.py', 'role': 'integration', 'sha256': sha(f'{KIT}/verify_ro.py')},
        {'path': f'{KIT}/atlas-excerpt.json', 'role': 'integration', 'sha256': sha(f'{KIT}/atlas-excerpt.json')},
        {'path': STUDY, 'role': 'review', 'sha256': sha(STUDY)},
        {'path': CANON, 'role': 'statement', 'sha256': sha(CANON)},
        {'path': PROVENANCE, 'role': 'provenance', 'sha256': sha(PROVENANCE)},
        {'path': SOURCE, 'role': 'provenance', 'sha256': sha(SOURCE)}],
    'proof_bindings': [],
    'progress': [{'en': 'What the map found, the six corrections and the seven gaps.',
                  'zh': '对应所得、六处改正与七项缺口。', 'source': ANCHOR}],
    'history': [{'en': (f'19 October 2026: added (RO), on Ren\'s request to map and integrate the relational ontology '
                        f'of Chinese thought; study section {section}; readings D{d}.'),
                 'zh': f'2026年10月19日：新增（RO），按 Ren 关于对应并整合中国思想之关系本体的要求；研究第 {section} 节；读法 D{d}。'}],
}
path = RECORDS / 'chinese-sources-on-the-spine.json'
assert not path.exists(), path
path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(path.relative_to(ROOT))
