from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parent.parent
PARTS = BASE / '_v1-parts'
BUILD = BASE / '_v1-build'

theorems = [
 ('GenerativeCore','viable_safe','可延续状态满足保护要求','§5.2'),
 ('GenerativeCore','viable_invariant','保持集合之并仍可保持','§5.2'),
 ('GenerativeCore','invariant_subset_viable','每个保持集合包含于 V','§5.1'),
 ('GenerativeCore','viable_predecessor','当前安全且能保持 V，则当前属于 V','§5.2'),
 ('GenerativeCore','viable_iff_safe_step','F1 的双向等价','§5.2'),
 ('GenerativeCore','outside_no_guaranteed_return','稳健区域外的后继量词','§5.3'),
 ('GenerativeCore','invariant_run_safe','实际转移服从 T 且行动保持，则路径安全','§5.2'),
 ('GenerativeCore','tighten_shrinks_viability','收紧保护要求不扩大 V','§5.4'),
 ('GenerativeCore','public_viability_protects_each','公共合取中的各项要求成立','§8.1'),
 ('GenerativeCore','constraint_reindexing','按满射重编号保留要求合取','§8.1'),
 ('GenerativeCore','finite_penalty_can_be_outbid','任何自然数惩罚之上存在更大收益数','§5.9'),
 ('GenerativeCore','racing_strictly_dominates','指定矩阵中竞赛严格占优','§9.1'),
 ('GenerativeCore','obedient_racing_worse_for_both','该矩阵中共同竞赛差于共同克制','§9.1'),
 ('GenerativeCore','good_viable','三状态反例中的安全状态可延续','§5.3'),
 ('GenerativeCore','gamble_not_viable','赌局状态不能保证避开失效','§5.3'),
 ('GenerativeCore','outside_can_reach_inside','稳健区域外仍可能幸运返回','§5.3'),
 ('GenerativeCore','deterministic_cycle_viable','确定性循环可以满足保持要求','§5.4'),
 ('GenerativeCore','dominates_irrefl','整数表示的严格改进不可自反','§8.2'),
 ('GenerativeCore','dominates_trans','该严格改进可传递','§8.2'),
 ('GenerativeCore','dominates_asymm','该严格改进不可能双向成立','§8.2'),
 ('OpenFuture','observation_limit','相同观察不能同时区分不同判断','§3.5、§5.6'),
 ('OpenFuture','local_maximum_violates_protection','两行动局部收益模型的保护反例','§4.11'),
 ('OpenFuture','zero_sum_without_closure','零和分数与开放背景可以并存','§9.4'),
 ('ExistenceConditions','cumulative_deficit','自然数缓冲的累积亏损界','§2.4'),
 ('ExistenceConditions','no_persistent_deficit','非负缓冲不能承受永久固定正亏损','§2.4'),
 ('ExistenceConditions','observation_control_obstruction','同观察且无共同安全行动时不能保证控制','§2.5'),
 ('ExistenceConditions','product_invariant','独立转移和行动的保持组合','§2.12'),
 ('ExistenceConditions','abstraction_refinement','较强实现前提下的抽象保持转移','§2.12'),
]
table=['| 模块与定理 | 检查内容 | 正文 |','| --- | --- | --- |']
for module,name,meaning,location in theorems:
    source=(BASE/'formal'/f'{module}.lean').read_text()
    assert re.search(r'^theorem '+re.escape(name)+r'\b',source,re.M),name
    table.append(f'| [{name}](formal/{module}.lean) | {meaning} | {location} |')
a=(BUILD/'appendix-a.md').read_text().replace('<!-- THEOREM_TABLE -->','\n'.join(table))

coverage={
1:('§1.1、§2.2—§2.4','实际依赖及更新条件'),
2:('§2.9、§12.3','相关扰动、替代与共享失效'),
3:('§3.5—§3.6、§5.5','表征限制与模型修订'),
4:('§6.6、§12.3','明确模型稳定边界与反证'),
5:('§1.5、§1.9、§2.13','过程接续与载体改变'),
6:('§2.6、§10.2','协调功能及治理的适用条件'),
7:('§6.1—§6.6','优势、认知选择与规则反馈'),
8:('§6.5、§9.1','比较实际反馈，不按制度名称判定'),
9:('§9.1、§10.7','区分预期协调与偏离激励'),
10:('§4.11、§6.9—§6.10','局部优化与共同条件的冲突'),
11:('§7.8、§9.8—§9.9','损害、响应期限与实际修正能力'),
12:('§9.1—§9.3','个体忠诚不保证共同结果'),
13:('§1.5—§1.9、§4.9','由生成与公共理由形成方向'),
14:('§2.9—§2.11','响应、补充及维持维持者'),
15:('§4.4、§10.8、§11.5','真实反馈、退出与纠正'),
16:('§4.2、§4.7、§11.6','照护与不能自持者的基本地位'),
17:('§4.10、§8.2—§8.4','多维价值与不完备比较'),
18:('§6.15、§10.9','认知、欲望与满足条件共同可塑'),
19:('§6.16、§10.8—§10.11','改变参与、资源与规则条件'),
20:('§3.2—§3.4、§4.7、§9.6','共同感知与新参与者的证据边界'),
21:('§1.8—§1.9、§5.10','有理由的限制、终结与开放未来'),
22:('§4.10—§4.13、§6.5','按实际关系及后果评价'),
23:('§2.1、§5.5、§8.7—§8.11','边界、模型、证据与诊断责任'),
24:('§2.9、§9.8、§11.5、§12.2','恢复、防御与权限退出'),
25:('§10.10—§10.11、§11.8','危机前建设与检验替代条件'),
26:('§6.15、§11.5、§12.2','可塑机制与极端防御的未解边界'),
27:('§10.7、§10.11、§11.8','承诺与转型的实际实现'),
28:('§10.8、§11.7','供给、获得权、资源控制与真实退出'),
29:('§11.9、§12.3','可推翻的判断及修订记录'),
}
src=(BASE/'论证与来源.md').read_text()
rows={}
for line in src.splitlines():
    cells=[c.strip() for c in line.strip().strip('|').split('|')]
    if len(cells)==4 and cells[0].isdigit() and 1<=int(cells[0])<=29:
        rows[int(cells[0])]=cells[1]
assert len(rows)==29
b=['## 附录 B：原则的统一对应',
'本表按[Speculative Future 的基础原则](../../sources/04-speculative-future/history-recovered-from-git/FOUNDATION-PRINCIPLES.md)原编号对应主题。主题栏为概括，正文进行了条件化重建，不能把较弱的条件结果当作原材料所有全称断言的完整证明。跨尺度统一体现为关系、适用条件与检验方法。',
'| 原编号 | 原条目主题 | 统一稿位置 | 论证定位 |','| --- | --- | --- | --- |']
for i in range(1,30):
    loc,note=coverage[i];b.append(f'| {i} | {rows[i]} | {loc} | {note} |')
b += ['', '作者对差异、生命、三层现实、认知可塑性、有效生成和跨时 Pareto 的进一步论述，分别进入第一、三、四、六、七、八章；组织如何确定保护、接受异议和修订，则进入第十一章。它们构成正文的相互约束，而非只作为附加倡议出现。']

paths=sorted(PARTS.glob('[0-9][0-9]-*.md'))
assert [p.name[:2] for p in paths]==[f'{i:02d}' for i in range(1,13)],paths
chapter_blocks=[f'<a id="chapter-{i}"></a>\n\n'+p.read_text() for i,p in enumerate(paths,1)]
blocks=[(BUILD/'frontmatter.md').read_text()]+chapter_blocks+[
    '<a id="appendix-a"></a>\n\n'+a,
    '<a id="appendix-b"></a>\n\n'+'\n\n'.join(b[:2])+'\n\n'+'\n'.join(b[2:]),
    '<a id="appendix-c"></a>\n\n'+(BUILD/'appendix-c.md').read_text()]
full='\n\n---\n\n'.join(block.strip() for block in blocks)+'\n'
(BASE/'WHITEPAPER-v1.0.md').write_text(full)
(BUILD/'coverage-v1.json').write_text(json.dumps({'chapters':[p.name for p in paths],'theorems':[{'module':m,'name':n,'meaning':d,'location':l} for m,n,d,l in theorems],'principles':coverage},ensure_ascii=False,indent=2)+'\n')
print('Unified whitepaper:',len(full),'characters,',len(full.splitlines()),'lines')
