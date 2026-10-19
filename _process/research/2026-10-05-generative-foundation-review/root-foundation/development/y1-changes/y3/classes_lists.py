"""Print the Lean literals of pairClasses and fourClasses for HexagramLaws.lean: each class of the four
symmetries named by its member of least binary value (line 1 the lowest place), classes of two first,
each list in increasing binary value. usage: python3 -B classes_lists.py"""
import itertools
def val(s): return sum(1 << i for i in range(6) if s[i])
def comp(s): return tuple(not x for x in s)
def rev(s): return tuple(reversed(s))
def cls(s): return {s, comp(s), rev(s), comp(rev(s))}
def rep(s): return min(cls(s), key=val)
allh = list(itertools.product([False, True], repeat=6))
reps = sorted({rep(s) for s in allh}, key=val)
lit = lambda s: '⟨' + ', '.join('true' if x else 'false' for x in s) + '⟩'
two = [r for r in reps if len(cls(r)) == 2]
four = [r for r in reps if len(cls(r)) == 4]
print(len(reps), len(two), len(four))
print('[' + ',\n    '.join(lit(r) for r in two) + ']')
print('[' + ',\n    '.join(lit(r) for r in four) + ']')
