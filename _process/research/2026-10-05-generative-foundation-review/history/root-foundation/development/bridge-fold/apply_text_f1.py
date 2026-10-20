#!/usr/bin/env python3
"""F1, the bridge fold (18 October 2026): re-point the record text that names the moved declarations' module.

usage (from the checkout root): python3 -B apply_text_f1.py

Exact replacements in the live fields of four records, each read before writing; every replacement must
match once. Each changed record gets one history note, which rebind_f1.py extends with what it moves and
rebinds. Claims are unchanged.
"""
import json

R = 'theories/becoming/results/records/'
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
EDITS = {
    'levels-of-closure': [
        (('laws', 1, 'en'), 'the seed–edge closure of Becoming.Bridge from the one seed f',
         'the seed–edge closure of Becoming.EdgeClosure from the one seed f'),
        (('laws', 1, 'zh'), 'Becoming.Bridge 中从 f 这一个种子出发', 'Becoming.EdgeClosure 中从 f 这一个种子出发'),
        (('validation_scope', 'en'),
         'current Becoming.Bridge and Becoming.Continuation bound to receipt 20261014T141427.442103Z): the theorems '
         'of Becoming.Feedback and the closure adapter of Becoming.Bridge, not an independent result, have empty '
         'axiom reports',
         'current Becoming.Feedback, Becoming.EdgeClosure and Becoming.Continuation bound to the latest receipt in '
         'the references): the theorems of Becoming.Feedback and Becoming.EdgeClosure have empty axiom reports'),
        (('validation_scope', 'zh'),
         'Bridge 与 Continuation 的当前字节绑定回执 20261014T141427.442103Z）：Becoming.Feedback 的定理与 Bridge 的闭包适配'
         '（不另计为独立成果）公理报告为空',
         'Feedback、EdgeClosure 与 Continuation 的当前字节绑定参考中最新的回执）：Becoming.Feedback 与 '
         'Becoming.EdgeClosure 的定理公理报告为空'),
        (('dependencies', 3, 'detail', 'en'),
         "Reuses Becoming.Bridge's seed–edge closure Closure; the closure is equivalent to it "
         '(withinClosure_iff_closure, in the bridge).',
         "Reuses the core's seed–edge closure Closure (Becoming.EdgeClosure); the closure is equivalent to it "
         '(withinClosure_iff_closure).'),
        (('dependencies', 3, 'detail', 'zh'), '复用 Becoming.Bridge 的种子—边闭包 Closure；闭包与之等价（withinClosure_iff_closure，在桥接中）。',
         '复用核心的种子—边闭包 Closure（Becoming.EdgeClosure）；闭包与之等价（withinClosure_iff_closure）。'),
        (('dependencies', 3, 'interface', 'evidence'), PKG + 'Bridge.lean', PKG + 'EdgeClosure.lean'),
    ],
    'relational-renewal-classification': [
        (('counterexamples', 3, 'path'), PKG + 'RenewalBridge.lean', PKG + 'RenewalFlow.lean'),
        (('counterexamples', 3, 'detail', 'en'), 'What the general laws do not give (Becoming.RenewalBridge)',
         'What the general laws do not give (Becoming.RenewalFlow)'),
        (('counterexamples', 3, 'detail', 'zh'), '不由一般定律推出的部分（Becoming.RenewalBridge）',
         '不由一般定律推出的部分（Becoming.RenewalFlow）'),
        (('validation_scope', 'en'),
         '(Becoming.Continuation, bridge module Becoming.RenewalBridge) are checked in consolidated receipt '
         '20261013T221720.428753Z with empty axiom reports',
         '(Becoming.Continuation, Becoming.RenewalFlow) are checked by the consolidated checker with empty axiom '
         'reports'),
        (('validation_scope', 'zh'),
         '（Becoming.Continuation 与桥接模块 Becoming.RenewalBridge）经合并检查器回执 20261013T221720.428753Z 检查',
         '（Becoming.Continuation 与 Becoming.RenewalFlow）经合并检查器检查'),
    ],
    'supported-renewal-recovery': [
        (('validation_scope', 'en'),
         '(Becoming.Continuation, bridge module Becoming.RenewalBridge) are checked in consolidated receipt '
         '20261013T221720.428753Z with empty axiom reports',
         '(Becoming.Continuation, Becoming.RenewalFlow) are checked by the consolidated checker with empty axiom '
         'reports'),
        (('validation_scope', 'zh'),
         '（Becoming.Continuation 与桥接模块 Becoming.RenewalBridge）经合并检查器回执 20261013T221720.428753Z 检查',
         '（Becoming.Continuation 与 Becoming.RenewalFlow）经合并检查器检查'),
    ],
    'becoming-spine-instances': [
        (('validation_scope', 'en'),
         '14 October 2026: the current bytes of Becoming.Bridge are bound to consolidated receipt '
         '20261013T204910.042715Z (passed: 85 package modules, 4861 theorems, 6856 declaration audits, every source '
         'declaration with an empty axiom report; the 86-module core closure compiles from the prelude).',
         'The current bytes of Becoming.Bridge, Becoming.Lifting (the lifting rule L and its countermodels) and '
         'Becoming.EdgeClosure (the seed–edge closure) are bound to the latest consolidated receipt in the '
         'references, every source declaration with an empty axiom report.'),
        (('related', 6, 'detail', 'en'), '(withinClosure_iff_closure, in the bridge)',
         '(withinClosure_iff_closure, Becoming.EdgeClosure)'),
        (('related', 6, 'detail', 'zh'), '（withinClosure_iff_closure，在桥接中）', '（withinClosure_iff_closure，Becoming.EdgeClosure）'),
        (('counterexamples', 0, 'path'), PKG + 'Bridge.lean', PKG + 'Lifting.lean'),
        (('counterexamples', 1, 'path'), PKG + 'Bridge.lean', PKG + 'Lifting.lean'),
    ],
}


for ident, edits in EDITS.items():
    f = R + ident + '.json'
    d = json.load(open(f))
    for path, old, new in edits:
        node = d
        for step in path[:-1]:
            node = node[step]
        assert node[path[-1]].count(old) == 1, (ident, path, old[:50])
        node[path[-1]] = node[path[-1]].replace(old, new)
    d['history'].append({
        'en': '18 October 2026, F1, the bridge fold (Ren: "so there seems to be a lot bridges in our code, how do they '
              'work? do we really need a bridge?", then "please do all"): the text names the core modules that now hold '
              'the declarations it cites (Becoming.Lifting, Becoming.EdgeClosure, Becoming.RenewalFlow).',
        'zh': '2026年10月18日，F1 桥接折叠（Ren：“so there seems to be a lot bridges in our code, how do they work? do we '
              'really need a bridge?”，然后“please do all”）：正文改为指名现在承载所引声明的核心模块（Becoming.Lifting、'
              'Becoming.EdgeClosure、Becoming.RenewalFlow）。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(ident, len(edits))
