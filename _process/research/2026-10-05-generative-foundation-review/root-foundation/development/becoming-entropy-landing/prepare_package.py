#!/usr/bin/env python3
"""Reconstruct the additive R5 landing drafts from their preserved Git source.
Run from a repository root. Writes only beside this script; never edits canonical files.
"""
from pathlib import Path
import ast
import hashlib
import importlib.util
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
BRANCH = '52ff83a4'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
D = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RECORD = 'theories/becoming/results/records/entropy-history-and-record.json'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-11-difference-in-becoming.md'


def old(path):
    return subprocess.check_output(['git', 'show', f'{BRANCH}:{path}'], cwd=ROOT)


def put(path, content):
    path = HERE / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content if isinstance(content, bytes) else content.encode())


def reconciled(s):
    # Editorial scope repairs only. Original bytes remain in BRANCH.
    s = s.replace('新模块 Becoming.Entropy（导入 Becoming.Resolution）', '新模块 Becoming.Entropy（导入 Becoming.Resolution 与 Becoming.Recurrence）')
    s = s.replace('（导入 Resolution）', '（导入 Resolution 与 Recurrence）')
    s = s.replace('(importing Resolution)', '(importing Resolution and Recurrence)')
    s = s.replace('2587 项定理、3801 项声明审计', '{N_THM} 项定理、{N_DECL} 项声明审计')
    s = s.replace('Entropy 185', 'Entropy {N_MODULE}')
    s = s.replace('20261011T170859.998618Z', '{RECEIPT}').replace('@PERI@', '{PERIPHERY}')
    s = s.replace('在表示中唯一不加前提就有的那个', '在此表示中不加耗散前提就已说明的一个量；这里未证明它是唯一的')
    s = s.replace('平衡的流中水平每次变化都是交换，所以交换的历史不加前提地增长', '平衡的流中水平每次变化都是交换，所以交换的历史在每次水平变化时增长；这里不另加耗散前提')
    s = s.replace('平衡的流中交换的历史不加前提地增长', '平衡的流中交换的历史在每次水平变化时增长，不另加耗散前提')
    s = s.replace('so the history of exchanges grows with no premise', 'so the history of exchanges grows at every level change without a dissipation premise')
    s = s.replace('change with no premise,', 'change without a dissipation premise,')
    return s


original_lean = old(f'{D}/Becoming/Entropy.lean')
# The later Weighted and OneStep packages already occupy these generic names.
# Qualify this module's local helpers; retain their bodies and every public statement.
HELPER_NAMES = ['joinMap', 'mem_joinMap', 'mem_append_cases', 'distinct_append']
lean_text = original_lean.decode()
for name in HELPER_NAMES:
    lean_text = re.sub(r'(?<![\w.])' + re.escape(name) + r'(?![\w])',
                       'EntropyLists.' + name, lean_text)
lean = lean_text.encode()
put('evidence/Entropy.original.lean', original_lean)
put('lean/Becoming/Entropy.lean', lean)
ks = importlib.util.spec_from_file_location('kit', HERE.parent/'becoming-landing-kit/kit.py')
kit = importlib.util.module_from_spec(ks)
ks.loader.exec_module(kit)
declarations = kit.declared(HERE/'lean/Becoming/Entropy.lean')

study = old(f'{RF}/BECOMING-RENEWAL-READING.md').decode()
zh = study[study.index('## 80. 熵：'):study.index('## English summary')].strip()
zh = reconciled(zh).replace('## 80.', '## {S}.', 1)
# Make the unconditional/counterfactual distinction explicit without altering proofs.
zh = zh.replace('Supplied premises / correspondence: 历史的结论只用平衡；', 'Supplied premises / correspondence: history_mono 本身不用平衡；由水平变化推出交换、逆转恢复水平等结论使用平衡；')
zh = zh.replace('**读法（AI，待 Ren）。** 生成留下差异，这一点不需要前提：每次变化都是一次交换，逆转也是一次交换，历史只增不减。', '**读法（AI，待 Ren）。** 交换历史的计数只增不减；平衡之下每次水平变化都是一次交换，逆转也是一次交换。此处不由这些结论推出平衡本身。')
zh += '\n\n**2026-10-13 整合说明。** 从 R5 分支 `52ff83a4` 保留已完成的陈述与证明，不新增定理。四个通用列表辅助名称与后落地模块冲突，现只将其限定到 `EntropyLists` 命名空间；原始源码另按原字节保存。将暂定节号、回执和总数按当前落地更新；补全 Resolution 与 Recurrence 的导入说明；区分历史计数的单调性与使用平衡的变化／逆转结论，并去掉未证明的“唯一”读法。原文与历史验证保留在该分支的 Git 历史中。\n'
put('docs/study/r5_zh.md', zh)
en = study[study.index('**Entropy: what becoming leaves, and what holding it costs (R5).**'):]
en = en[:en.index('The package now has ')].strip()
en = reconciled(en).replace('section 80 of the integration note', 'section {S} of the integration note')
en += '\n\n**Integration note, 13 October 2026.** The statements and proofs are retained from R5 branch `52ff83a4`; this landing adds no theorem. Four generic list helper names that collide with later modules are qualified under `EntropyLists`, with the exact original source retained separately. The provisional section, receipts and totals are replaced by the current landing values; both Resolution and Recurrence imports are named. Exchange-history monotonicity needs no balance premise, while connecting level changes and reversals to that history uses balance; no uniqueness of the history as an increasing quantity is claimed. The original prose and historical verification remain in that branch’s Git history.\n'
put('docs/study/r5_en.md', en)

record = json.loads(old(RECORD))
draft = {k:v for k,v in record.items() if k not in ['schema_version','kind','status','reviewed_at_utc','canonical_source','validation_scope','references','proof_bindings','history']}
draft['title'] = {
 'zh': '熵的历史与记录：无损交换可不息而复返；平衡与第一律下有限家族的箭头受界；守恒量中的逐次记录恰好分解最小损失',
 'en': 'Entropy, history and record: lossless exchange can continue and return; under balance and the first law an arrow on a finite family is bounded; recording each exchange within the conserved amount decomposes the least loss',
}
draft['claim']['zh'] = draft['claim']['zh'].replace('不加前提：平衡的流中', '历史计数的单调性不用平衡；以下变化与逆转的结论使用平衡：平衡的流中', 1)
draft['claim']['en'] = draft['claim']['en'].replace('With no premise: in a balanced flow', 'History-count monotonicity uses no balance premise; the following change and reversal results use balance: in a balanced flow', 1)
draft['hypotheses'][0] = {
 'zh': 'Flow.history_mono 本身不用平衡；由水平变化推出交换（Flow.Balances.exchanges_of_change）、逆转恢复水平（Flow.Balances.restores_levels_not_history）等结论使用平衡及所陈述的局部条件。',
 'en': 'Flow.history_mono itself uses no balance premise; connecting a level change to an exchange (Flow.Balances.exchanges_of_change), restoring levels under a reversal (Flow.Balances.restores_levels_not_history), and the other conditional results use balance and their stated local hypotheses.',
}
put('docs/records/entropy-history-and-record.json',json.dumps(draft,ensure_ascii=False,indent=2)+'\n')
put('docs/original-history.json',json.dumps(record['history'],ensure_ascii=False,indent=2)+'\n')

plan = old(f'{RF}/BECOMING-UNIFICATION-PLAN.md').decode()
plan_zh = next(l for l in plan.splitlines() if l.startswith('| R5 熵：'))
plan_en = next(l for l in plan.splitlines() if l.startswith('- **R5:**'))
def plan_text(s):
    s=reconciled(s).replace('§80','§{S_ENTROPY}').replace('section 80','section {S_ENTROPY}')
    s=s.replace('#80-熵生成留下的历史与守住它的代价r5', '#{ANCHOR_ENTROPY}')
    return s.replace('{N_MODULE}', '{N_ENTROPY}')
put('docs/plan_zh.md',plan_text(plan_zh)+'\n')
put('docs/plan_en.md',plan_text(plan_en)+'\n')

chapter = old(CHAPTER).decode()
put('docs/chapter_zh.md',reconciled(next(l for l in chapter.splitlines() if l.startswith('- **熵：')))+'\n')
put('docs/chapter_en.md',reconciled(next(l for l in chapter.splitlines() if l.startswith('- **Entropy:')))+'\n')
spine = next(l for l in chapter.splitlines() if l.startswith('| L3 | [Becoming.Entropy]'))
put('docs/chapter_spine.md',reconciled(spine).replace('| 185 |','| {N_ENTROPY} |')+'\n')

root = old(f'{D}/Becoming.lean').decode()
i = root.index('* `Becoming.Entropy` ('); j=root.index('\n* `',i)
put('docs/root_bullet.md',reconciled(root[i:j])+'\n')
scope = old(f'{D}/check_becoming.py').decode()
i=scope.index('    "Entropy:');j=scope.index('    "Continuation:',i)
text=''.join(ast.literal_eval(l.strip()) for l in scope[i:j].splitlines())
# history_within uses dissipation, not merely Gainless; loss_ceases concerns loss, not its accumulated amount.
text=text.replace('under the first law the amount dissipated with the stock is conserved, is what the record receives, bounds the history and does not recur, and in proportion q', 'under the first law the amount dissipated with the stock is conserved and is what the record receives; under dissipation it bounds the history, loss does not recur under the first law, and in proportion q')
put('docs/checker_scope.txt', text+'\n')
readme = old(f'{D}/README.md').decode()
row = next(l for l in readme.splitlines() if '[`Becoming.Entropy`]' in l)
body=row.split(' | ',2)[2].removesuffix(' |')
rzh,ren=body.split(' / ',1)
put('docs/readme_zh.md',reconciled(rzh)+'\n')
put('docs/readme_en.md',reconciled(ren)+'\n')
directive=next(l for l in old('_process/RESEARCH-DIRECTIVES.md').decode().splitlines() if l.startswith("[Ren's reading of the least loss as entropy"))
put('docs/directive.md',reconciled(directive)+'\n')

spec={
 'sections':list(dict.fromkeys(declarations.values())),
 'named':['Flow.history_mono','Flow.Balances.restores_levels_not_history','Flow.dissipatesOn_iff_conserved','Passing.passes','Flow.Balances.no_arrow','Flow.Balances.recurs','Flow.Balances.present_forgets'],
 'builds_on':[n.removeprefix('Becoming.') for r in record['references'] if r['role']=='proof' and not r['path'].endswith('/Entropy.lean') for n in r['declarations']],
 'provenance':[SOURCE],
}
put('docs/record_spec.json',json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
put('provenance.json',json.dumps({
 'branch':'claude/jolly-pike-140c94','commit':subprocess.check_output(['git','rev-parse',BRANCH],text=True).strip(),
 'lean_source':f'{D}/Becoming/Entropy.lean','source_sha256':hashlib.sha256(original_lean).hexdigest(),
 'landing_source_sha256':hashlib.sha256(lean).hexdigest(),
 'original_source_artifact':'evidence/Entropy.original.lean',
 'helper_name_reconciliation':{n:'EntropyLists.'+n for n in HELPER_NAMES},
 'original_record':RECORD,'historical_receipt':'20261011T170859.998618Z',
 'historical_module_theorems':185,'historical_declaration_audits':233,
 'package_status':'prepared; current consolidated core and periphery check required at landing',
},ensure_ascii=False,indent=2)+'\n')
print('Prepared source, bilingual drafts, record spec and provenance. Canonical files unchanged.')
