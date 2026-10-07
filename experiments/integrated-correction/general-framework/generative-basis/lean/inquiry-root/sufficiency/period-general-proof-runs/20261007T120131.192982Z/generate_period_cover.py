#!/usr/bin/env python3
"""Generate witness tables; every witness is subsequently checked in Lean.
Not a trusted proof procedure: a wrong witness makes its Lean certificate fail.
"""
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
    low=mx(x&(c.FULL^obs) for x in prev);high=mx(x&obs for x in prev)
    return mx([c.BITS[p]]+raw(d-1,p+1)+[x|y for x in low for y in high])
def family(d,p,v):
    if d+p>=7:return []
    return raw(d,p) if v else [c.flip_words(x) for x in raw(d,p)]
def lit(x):
    if isinstance(x,list):return '['+', '.join(map(lit,x))+']'
    return str(x)
def dominator(f,x):return next(i for i,y in enumerate(f) if x&y==x)
fs=[];stops=[];adv=[];reads=[]
for d in range(7):
 for p in range(7):
  for v in (False,True):
   f=family(d,p,v);fs.append(f)
   if not f:stops.append(0);adv.append([]);reads.append([]);continue
   stops.append(dominator(f,c.BITS[p] if v else c.FULL^c.BITS[p]))
   adv.append([dominator(f,x) for x in family(d-1,p+1,v)] if d else [])
   prev=family(d-1,p,v) if d else []
   reads.append([[dominator(f,(x&(c.FULL^c.OBSERVATIONS[p]))|(y&c.OBSERVATIONS[p])) for y in prev] for x in prev])
s='''import PeriodLocalCertificate
import PhasePeriodSelection

/-! Finite witness certificates for every bounded-policy constructor. The tables
are untrusted choices; kernel-checked pointwise rules establish that each
selected parent mask covers the indicated successful words. Thus the later
policy induction needs no unproved general arithmetic bitset correspondence. -/
namespace Generative.InquirySufficiency.PeriodCoverRules
open PhaseCycleDerivation (allOf upto)
open PhasePeriodSelection (allOf_member member_upto)
open PeriodLocalCertificate (Mask bit)

def item {α : Type} (fallback : α) : List α → Nat → α
  | [], _ => fallback
  | x :: _, 0 => x
  | _ :: xs, n + 1 => item fallback xs n

'''
for name,x,typ in [('familyData',fs,'List (List Mask)'),('stopData',stops,'List Nat'),('advanceData',adv,'List (List Nat)'),('readData',reads,'List (List (List Nat))')]:
 s+=f'def {name} : {typ} := {lit(x)}\n\n'
s+='''def key (budget position : Nat) (value : Bool) : Nat := 2 * (7 * budget + position) + value.toNat

def family (budget position : Nat) (value : Bool) : List Mask := item [] familyData (key budget position value)

def mask (budget position : Nat) (value : Bool) (index : Nat) : Mask := item 0 (family budget position value) index

def stopIndex (budget position : Nat) (value : Bool) : Nat := item 0 stopData (key budget position value)

def advanceIndex (budget position : Nat) (value : Bool) (index : Nat) : Nat :=
  item 0 (item [] advanceData (key budget position value)) index

def readIndex (budget position : Nat) (value : Bool) (low high : Nat) : Nat :=
  item 0 (item [] (item [] readData (key budget position value)) low) high

def stopOK (budget position : Nat) (value : Bool) : Bool :=
  decide (stopIndex budget position value < (family budget position value).length) &&
  allOf (upto 128) (fun word => !(bit word position == value) ||
    bit (mask budget position value (stopIndex budget position value)) word)

def advanceOK (budget position : Nat) (value : Bool) : Bool :=
  allOf (upto (family budget (position + 1) value).length) fun child =>
    decide (advanceIndex (budget + 1) position value child < (family (budget + 1) position value).length) &&
    allOf (upto 128) (fun word => !bit (mask budget (position + 1) value child) word ||
      bit (mask (budget + 1) position value (advanceIndex (budget + 1) position value child)) word)

def readOK (budget position : Nat) (value : Bool) : Bool :=
  allOf (upto (family budget position value).length) fun low =>
    allOf (upto (family budget position value).length) fun high =>
      decide (readIndex (budget + 1) position value low high < (family (budget + 1) position value).length) &&
      allOf (upto 128) (fun word =>
        !(if bit word position != bit word 0 then bit (mask budget position value high) word
          else bit (mask budget position value low) word) ||
        bit (mask (budget + 1) position value (readIndex (budget + 1) position value low high)) word)

def cellOK : Nat → Nat → Bool → Bool
  | 0, position, value => stopOK 0 position value
  | budget + 1, position, value => stopOK (budget + 1) position value &&
      advanceOK budget position value && readOK budget position value

theorem both_true {a b : Bool} (left : a = true) (right : b = true) : (a && b) = true := by
  rw [left,right]; rfl

theorem left_true {a b : Bool} (both : (a && b) = true) : a = true := by
  cases a <;> cases b <;> first | rfl | cases both

theorem right_true {a b : Bool} (both : (a && b) = true) : b = true := by
  cases a <;> cases b <;> first | rfl | cases both

theorem implies_true {a b : Bool} (implication : (!a || b) = true) (first : a = true) : b = true := by
  rw [first] at implication
  exact implication

'''
s+='''theorem allOfCons {α : Type} (test : α → Bool) (head : α) (rest : List α)
    (first : test head = true) (later : allOf rest test = true) :
    allOf (head :: rest) test = true := both_true first later

'''
for d in range(7):
 for p in range(7-d):
  for v in ('false','true'):
   s+=f'set_option maxHeartbeats 0 in\nset_option maxRecDepth 100000 in\ntheorem rule_{d}_{p}_{v} : cellOK {d} {p} {v} = true := by\n  decide +kernel\n\n'
def nested(proofs,test):
 r='rfl'
 for i in reversed(range(len(proofs))):
  rest='['+', '.join(map(str,range(i+1,len(proofs))))+']'
  r=f'(allOfCons {test} {i} {rest} {proofs[i]} {r})'
 return r
rows=[]
for d in range(7):
 cells=[]
 for p in range(7):
  cells.append(f'(both_true (a := cellOK {d} {p} false) (b := cellOK {d} {p} true) rule_{d}_{p}_false rule_{d}_{p}_true)' if d+p<7 else 'rfl')
 test=f'(fun position => if {d} + position < 7 then cellOK {d} position false && cellOK {d} position true else true)'
 rows.append(nested(cells,test))
outer='(fun budget => allOf (upto 7) (fun position => if budget + position < 7 then cellOK budget position false && cellOK budget position true else true))'
s+='''set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem all_rules : allOf (upto 7) (fun budget => allOf (upto 7) fun position =>
    if budget + position < 7 then cellOK budget position false && cellOK budget position true else true) = true := by
  exact '''+nested(rows,outer)+'\n\n'
s+='''theorem checked_cell (budget position : Nat) (value : Bool) (bounded : budget + position < 7) :
    cellOK budget position value = true := by
  have bd := Nat.lt_of_le_of_lt (Nat.le_add_right budget position) bounded
  have bp := Nat.lt_of_le_of_lt (Nat.le_add_left position budget) bounded
  have row := allOf_member _ _ _ all_rules (member_upto 7 budget bd)
  have cell := allOf_member _ _ _ row (member_upto 7 position bp)
  rw [if_pos bounded] at cell
  cases value with
  | false => exact left_true cell
  | true => exact right_true cell

theorem stop_rule (budget position : Nat) (value : Bool) (bounded : budget + position < 7) :
    stopOK budget position value = true := by
  have valid := checked_cell budget position value bounded
  cases budget with
  | zero => exact valid
  | succ budget => exact left_true (left_true valid)

theorem advance_rule (budget position : Nat) (value : Bool) (bounded : budget + 1 + position < 7) :
    advanceOK budget position value = true :=
  right_true (left_true (checked_cell (budget + 1) position value bounded))

theorem read_rule (budget position : Nat) (value : Bool) (bounded : budget + 1 + position < 7) :
    readOK budget position value = true := right_true (checked_cell (budget + 1) position value bounded)

end Generative.InquirySufficiency.PeriodCoverRules
'''
import re
boundary=s.index('set_option maxHeartbeats 0 in')
header=s[s.index('namespace Generative.InquirySufficiency.PeriodCoverRules'):s.index('def item')]
parts={'PeriodCoverData':s[:boundary]+'end Generative.InquirySufficiency.PeriodCoverRules\n',
       'PeriodCoverRules':'import PeriodCoverData\n\n'+header+s[boundary:]}
for module,body in parts.items():
 for n in re.findall(r'^(?:def|abbrev|theorem|structure|inductive)\s+(\w+)',body,re.M):
  body+='\n#print axioms Generative.InquirySufficiency.PeriodCoverRules.'+n
 (HERE/(module+'.lean')).write_text(body+'\n')
 print('Generated',module,len(body),'bytes with checked stop/advance/read witnesses')
