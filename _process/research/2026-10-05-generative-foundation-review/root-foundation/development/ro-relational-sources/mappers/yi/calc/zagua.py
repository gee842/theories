import re, sys
src = open(sys.argv[1], encoding='utf-8').read()
i = src.index('def order : List Hexagram := [')
block = src[i:src.index(']', src.index('64 未濟', i))]
rows = re.findall(r'⟨(\w+), (\w+), (\w+), (\w+), (\w+), (\w+)⟩,?\s*--\s*(\d+) (\S+):', block)
H = {r[7]: tuple(v == 'true' for v in r[:6]) for r in rows}
seq = "乾 坤 比 師 臨 觀 屯 蒙 震 艮 損 益 大畜 无妄 萃 升 謙 豫 噬嗑 賁 兌 巽 隨 蠱 剝 復 晉 明夷 井 困 咸 恒 渙 節 解 蹇 睽 家人 否 泰 大壯 遯 大有 同人 革 鼎 小過 中孚 豐 旅 離 坎 小畜 履 需 訟 大過 姤 漸 頤 既濟 歸妹 未濟 夬".split()
assert len(seq) == 64 and len(set(seq)) == 64, (len(seq), len(set(seq)))
rev = lambda s: tuple(reversed(s)); comp = lambda s: tuple(not v for v in s)
def rel(a, b):
    a, b = H[a], H[b]
    r = []
    if b == rev(a) and a != b: r.append('綜')
    if b == comp(a): r.append('錯')
    return r
for k in range(0, 64, 2):
    print(seq[k], seq[k+1], rel(seq[k], seq[k+1]))
# last 8: check pairings
last = seq[56:]
print('last eight', last)
for x in last:
    partners = [y for y in last if y != x and rel(x, y)]
    print(x, partners, [rel(x, y) for y in partners])
