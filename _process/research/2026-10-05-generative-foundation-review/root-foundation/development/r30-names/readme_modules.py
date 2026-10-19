"""R30: the Lean READMEs name modules bare in backticks in their import-order prose and in one table row
(`Generation`, `Return`, `Coupling`, `PositiveGround`); every such bare use there is the module, so it follows the
module rename. Run from the checkout root."""
M = {'Generation': 'Arising', 'Return': 'Restoration', 'Coupling': 'MoveFormation', 'PositiveGround': 'SecuredContent'}
D = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
for f in (D + 'README.md', D + 'README.zh.md'):
    s = open(f, encoding='utf-8').read()
    n = 0
    for o, new in M.items():
        n += s.count('`' + o + '`')
        s = s.replace('`' + o + '`', '`' + new + '`')
    open(f, 'w', encoding='utf-8').write(s)
    print(f, n)
