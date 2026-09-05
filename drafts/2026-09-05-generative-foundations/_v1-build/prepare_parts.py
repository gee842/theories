from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parent.parent
PARTS = BASE / '_v1-parts'
S = json.loads((BASE / '_v1-build/v06-sections.json').read_text())

# Only parent-owned parts are assembled here. Other chapters are independently
# rewritten and reviewed before the final assembly.
plan = {
    '05-形式核心.md': (5, '形式核心：保持、观察与风险',
        ['5.1','5.2','5.3','5.4','5.5','6.7','6.3','6.4','6.5','6.6']),
    '06-认知选择.md': (6, 'Meta-Attractor：认知、规则与长期趋向',
        [f'7.{i}' for i in range(1,15)]),
    '08-情境决策.md': (8, '情境中的公共判断与跨时决策',
        [f'11.{i}' for i in range(1,10)]),
    '09-智能向善.md': (9, '智能向善与可纠正的发展',
        [f'9.{i}' for i in range(1,7)] + [f'10.{i}' for i in range(1,4)]),
    '10-共同未来.md': (10, '共同未来、大同与合作的形成条件',
        [f'12.{i}' for i in range(1,4)] + [f'13.{i}' for i in range(1,4)] + [f'14.{i}' for i in range(1,6)]),
}
loc = {}
for name,(chapter,title,keys) in plan.items():
    for i,key in enumerate(keys,1):
        loc[key] = f'{chapter}.{i}'

phrase_map = {
    '第五、六、九、十一节':'第五、第八及第九章',
    '第五、六、九、十一章':'第五、第八及第九章',
    '第二章讨论的物质及依赖条件':'第三章讨论的物质及依赖条件',
    '第二章的三层框架':'第三章的三层框架',
    '第八章 C3':'第二章 C3',
    '第八章的 C3':'第二章的 C3',
    '第八章':'第二章及第七章',
    '第七章':'第六章',
    '第六节':'第五章',
    '第六章':'第五章',
    '第十一章':'第八章',
    '第十一节':'第八章',
    '第十二章':'第十章',
    '第十三章':'第十章',
    '第十四章':'第十章',
    '第十五章':'第十一章',
    '原稿尝试':'一种可检验的尝试是',
    '原稿关于开放未来的讨论，可整理为':'开放未来可以通过以下',
    '作者提出的六个子吸引子':'六类候选反馈结构',
    '原 Meta-Attractor 数学稿还讨论':'Meta-Attractor 分析还涉及',
    '原材料讨论':'一种情景分析是',
    '作者称作“总体化”的':'本文称作“总体化”的',
    '本轮':'本文',
    '本版 Lean':'随附 Lean',
}
pat = re.compile('|'.join(re.escape(k) for k in sorted(phrase_map,key=len,reverse=True)))
def clean(body):
    # One substitution pass avoids rewriting inserted new chapter numbers.
    body = pat.sub(lambda m:phrase_map[m[0]],body)
    body = re.sub(r'§(\d+\.\d+)', lambda m:'§'+loc.get(m[1],m[1]), body)
    return body

for name,(chapter,title,keys) in plan.items():
    blocks=[f'## {dict(zip(range(1,13),"一 二 三 四 五 六 七 八 九 十 十一 十二".split()))[chapter]}、{title}']
    for i,key in enumerate(keys,1):
        sec=S[key]
        blocks.append(f'### {chapter}.{i} {sec["title"]}\n\n'+clean(sec['body']))
    (PARTS/name).write_text('\n\n'.join(blocks).strip()+'\n')

(BASE/'_v1-build/reused-section-map.json').write_text(json.dumps(loc,ensure_ascii=False,indent=2)+'\n')
print('Prepared',len(plan),'parent-owned parts')
