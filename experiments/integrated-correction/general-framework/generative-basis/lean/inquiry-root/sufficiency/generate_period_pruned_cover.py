#!/usr/bin/env python3
"""Generate untrusted deletion paths. PeriodPrunedCover checks every edge in Lean."""
from pathlib import Path
from functools import lru_cache
import check_period_general as c
HERE=Path(__file__).resolve().parent

def mx(items):
    kept=[]
    for x in items:
        if not any(x&y==x for y in kept): kept=[x]+[y for y in kept if y&x!=y]
    return kept
@lru_cache(None)
def raw(d,p):
    if d==0:return [c.BITS[p]]
    prev=raw(d-1,p);obs=c.OBSERVATIONS[p]
    return mx([c.BITS[p]]+raw(d-1,p+1)+[x|y for x in mx(t&(c.FULL^obs) for t in prev) for y in mx(t&obs for t in prev)])
def path(x):
    p=[x]
    while c.trim_once(p[-1])!=p[-1]:p.append(c.trim_once(p[-1]))
    return p

def lit(x):
    if isinstance(x,list):return '['+', '.join(map(lit,x))+']'
    return str(x)
roots=[];targets=[];recs=[];joint=[];kinds=[]
native=sum(1<<w for w in (18,36,73));ends=[0,native,c.flip_words(native)]
for budget in (5,6):
    rp=[path(x) for x in raw(budget,0)];rec=mx(p[-1] for p in rp)
    bothrec=[]
    for v in (False,True):
        r=rec if v else [c.flip_words(x) for x in rec];bothrec.append(r);recs.append(r)
        ps=[p[:] if v else [c.flip_words(x) for x in p] for p in rp]
        ts=[next(i for i,y in enumerate(r) if p[-1]&y==p[-1]) for p in ps]
        for p,t in zip(ps,ts):
            if p[-1]!=r[t]:p.append(r[t])
        roots.append(ps);targets.append(ts)
    js=[];ks=[]
    for low in bothrec[0]:
        row=[];kr=[]
        for high in bothrec[1]:
            p=path(low&high)
            kind=next(i for i,y in enumerate(ends) if p[-1]&y==p[-1])
            assert budget==6 or kind==0
            if p[-1]!=ends[kind]:p.append(ends[kind])
            row.append(p);kr.append(kind)
        js.append(row);ks.append(kr)
    joint.append(js);kinds.append(ks)
s='''import PeriodCoverData
import PeriodCycleWindows

/-!
Checked concrete deletion certificates for arbitrary cyclic histories.
Every route edge is checked pointwise on all seven-bit words; generated
routes are witnesses, not trusted computation. Cyclic adjacency proves that
these deletions preserve every window of the actual history. One common
final mask covers all phases; the conclusion is not pointwise union coverage.
This constrains recognition under the supplied native inquiry law; it does
not infer normative warrant or universal ethical compliance.
-/
set_option maxRecDepth 100000
set_option maxHeartbeats 0

namespace Generative.InquirySufficiency.PeriodPrunedCover
open PhaseCycleDerivation (allOf upto)
open PhasePeriodSelection (allOf_member member_upto)
open PeriodLocalCertificate (Mask bit nativeWords invertedWords)
open PeriodCoverRules (item both_true left_true right_true implies_true)
open PeriodCycleWindows (window next_window previous_window next_bounded)

'''
for name,data,typ in [('rootData',roots,'List (List (List Mask))'),('targetData',targets,'List (List Nat)'),('recurrentData',recs,'List (List Mask)'),('jointData',joint,'List (List (List (List Mask)))'),('kindData',kinds,'List (List (List Nat))')]:
    s+=f'def {name} : {typ} := {lit(data)}\n\n'
s+='''def key (budget : Nat) (value : Bool) := 2 * (budget - 5) + value.toNat

def recurrent (budget : Nat) (value : Bool) : List Mask := item [] recurrentData (key budget value)
def rootRoute (budget : Nat) (value : Bool) (index : Nat) : List Mask :=
  item [] (item [] rootData (key budget value)) index
def rootTarget (budget : Nat) (value : Bool) (index : Nat) : Nat :=
  item 0 (item [] targetData (key budget value)) index

def last : List Mask → Mask
  | [] => 0
  | [x] => x
  | _ :: y :: rest => last (y :: rest)

def localPrune (mask word : Nat) : Bool :=
  bit mask word && (bit mask (word / 2) || bit mask (word / 2 + 64)) &&
    (bit mask (word * 2 % 128) || bit mask (word * 2 % 128 + 1))

def stepOK (old new : Mask) : Bool :=
  allOf (upto 128) fun word => !localPrune old word || bit new word

def routeOK : List Mask → Bool
  | [] => false
  | [_] => true
  | a :: b :: rest => stepOK a b && routeOK (b :: rest)

def rootOK (budget : Nat) (value : Bool) (index : Nat) : Bool :=
  let route := rootRoute budget value index
  (item 0 route 0 == PeriodCoverRules.mask budget 0 value index) &&
    routeOK route &&
    decide (rootTarget budget value index < (recurrent budget value).length) &&
    (last route == item 0 (recurrent budget value) (rootTarget budget value index))

def rootsOK (budget : Nat) (value : Bool) : Bool :=
  allOf (upto (PeriodCoverRules.family budget 0 value).length) (rootOK budget value)

def jointRoute (budget low high : Nat) : List Mask :=
  item [] (item [] (item [] jointData (budget - 5)) low) high

def jointKind (budget low high : Nat) : Nat :=
  item 0 (item [] (item [] kindData (budget - 5)) low) high

def endMask : Nat → Mask
  | 0 => 0
  | 1 => nativeWords
  | _ => invertedWords

def jointOK (budget low high : Nat) : Bool :=
  let route := jointRoute budget low high
  allOf (upto 128) (fun word =>
    !(bit (item 0 (recurrent budget false) low) word &&
      bit (item 0 (recurrent budget true) high) word) || bit (item 0 route 0) word) &&
    routeOK route && (last route == endMask (jointKind budget low high)) &&
    decide (jointKind budget low high < (if budget == 5 then 1 else 3))

def jointsOK (budget : Nat) : Bool :=
  allOf (upto (recurrent budget false).length) fun low =>
    allOf (upto (recurrent budget true).length) (jointOK budget low)

theorem allOfCons (predicate : Nat → Bool) (head : Nat) (rest : List Nat)
    (first : predicate head = true) (others : allOf rest predicate = true) :
    allOf (head :: rest) predicate = true := both_true first others

'''
def nested(predicate, proofs):
    answer='rfl'
    for i in reversed(range(len(proofs))):
        rest=lit(list(range(i+1,len(proofs))))
        answer=f'(allOfCons {predicate} {i} {rest} {proofs[i]} {answer})'
    return answer

for b in (5,6):
 for v in ('false','true'):
  # Per-route certificates bound kernel reduction cost and permit precise diagnosis.
  count=len(raw(b,0))
  for i in range(count):
   s+=f'set_option maxHeartbeats 0 in\nset_option maxRecDepth 100000 in\ntheorem root_{b}_{v}_{i} : rootOK {b} {v} {i} = true := by\n  decide +kernel\n\n'
  s+=f'theorem roots_{b}_{v} : rootsOK {b} {v} = true := by\n  exact '+nested(f'(rootOK {b} {v})',[f'root_{b}_{v}_{i}' for i in range(count)])+'\n\n'
 for low in range(len(recs[2*(b-5)])):
  for high in range(len(recs[2*(b-5)+1])):
   s+=f'set_option maxHeartbeats 0 in\nset_option maxRecDepth 100000 in\ntheorem joint_{b}_{low}_{high} : jointOK {b} {low} {high} = true := by\n  decide +kernel\n\n'
 rc=len(recs[2*(b-5)+1])
 rows=[nested(f'(jointOK {b} {i})',[f'joint_{b}_{i}_{j}' for j in range(rc)]) for i in range(len(recs[2*(b-5)]))]
 s+=f'theorem joints_{b} : jointsOK {b} = true := by\n  exact '+nested(f'(fun low => allOf (upto {rc}) (jointOK {b} low))',rows)+'\n\n'
s+=(HERE/'period_pruned_cover_proofs.txt').read_text()
s+='\nend Generative.InquirySufficiency.PeriodPrunedCover\n'
import re
for name in re.findall(r'^(?:def|theorem)\s+(\w+)',s,re.M):
 s+='\n#print axioms Generative.InquirySufficiency.PeriodPrunedCover.'+name
(HERE/'PeriodPrunedCover.lean').write_text(s+'\n')
print('Generated',len(s),'bytes,',sum(len(x) for x in roots),'root routes')
