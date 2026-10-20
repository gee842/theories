#!/usr/bin/env python3
"""F1, the bridge fold, step 3 (18 October 2026): mark the one fully restated periphery module superseded in place.

usage (from the checkout root): python3 -B step3_f1.py

Step 0 (RESTATEMENT-AUDIT.md) found one of the twenty leaf periphery modules fully restated by the core:
`ExplanatoryResiduals`, every theorem of which `Becoming.Granularity` states (eleven as they stand, two with excluded
middle named). It has a live importer outside the run, `deeper/ExplanatoryResumptionCases.lean`, an earlier version
whose witnesses `Becoming.Midway` restates. Both files keep their path and bytes (board rule 8; old receipts bind
them). Superseded in place means: the record of their result takes the core module as its canonical source and lists
the periphery files as the earlier statement. The bridge's readings of the module (GranularityBridge) stay: the
record cites them as the correspondence, and the module stays live through its importer outside the run. Nothing else
changes.
"""
import json

R = 'theories/becoming/results/records/residual-continuation-correspondence.json'
CORE = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Granularity.lean'
d = json.load(open(R))
paths = {x['path'] for x in d['references']}
assert CORE in paths, 'the record already cites the core module'
assert d['canonical_source'].endswith('deeper/ExplanatoryResiduals.lean'), d['canonical_source']
d['canonical_source'] = CORE
d['history'].append({
    'en': '18 October 2026, F1, the bridge fold, step 3 (Ren: "please do all"): the restatement audit of step 0 '
          '(development/bridge-fold/RESTATEMENT-AUDIT.md) found ExplanatoryResiduals fully restated by '
          'Becoming.Granularity, and its importer ExplanatoryResumptionCases an earlier version whose witnesses '
          'Becoming.Midway restates. The canonical source is now the core module; both periphery files keep their '
          'path and bytes and stay cited as the earlier statement. The claim is unchanged.',
    'zh': '2026年10月18日，F1 桥接折叠第 3 步（Ren：“please do all”）：第 0 步的重述审计'
          '（development/bridge-fold/RESTATEMENT-AUDIT.md）查明 ExplanatoryResiduals 已由 Becoming.Granularity 完整重述，'
          '导入它的 ExplanatoryResumptionCases 是较早版本，其见证由 Becoming.Midway 重述。规范来源改为核心模块；两个外围文件'
          '保留路径与字节，仍作为较早的陈述被引用。论断不变。'})
open(R, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('canonical source:', CORE)
