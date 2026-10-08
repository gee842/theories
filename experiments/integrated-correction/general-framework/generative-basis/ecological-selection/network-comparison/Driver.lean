import Lean
import EvolutionNetworkComparison

open Lean EvolutionNetworkComparison

def parseState (j : Json) : Except String Network := do
  let cells : Array (Array Nat) ← j.getObjValAs? (Array (Array Nat)) "cells"
  let edges : Array (Array Nat) ← j.getObjValAs? (Array (Array Nat)) "edges"
  let s : Array Nat ← j.getObjValAs? (Array Nat) "stocks"
  if s.size != 7 || cells.any (fun c => c.size != 2) || edges.any (fun e => e.size != 2) then
    throw "invalid state shape"
  let get (i k : Nat) := ((cells[i]?).getD #[])[k]?.getD 0
  pure ⟨⟨cells.size, s[0]!, s[1]!, s[2]!, fun i => get i 0 == 1,
    fun i => get i 1, edges.toList.map (fun e => (e[0]!, e[1]!))⟩,
    s[3]!, s[4]!, s[5]!, s[6]!⟩

def parseEvent (a : Array Nat) : Except String DevelopmentalReconstruction.Event := do
  match a.toList with
  | [0, p] => pure (.develop [.divide p])
  | [1, p, v] => if v ≤ 1 then pure (.develop [.changeRetention p (v == 1)]) else throw "trait"
  | [2, p, c] => pure (.develop [.detach p c])
  | [3, p, c] => pure (.develop [.aggregate p c])
  | [4, r, p, m, f] =>
    if r ≤ 1 then pure (.transfer (if r == 0 then .anyCell else .attachedCell) p m f)
    else throw "requirement"
  | _ => throw "invalid event"

def serialize (n : Network) : Json :=
  Json.mkObj [
    ("cells", toJson ((List.range n.graph.nodes).map (fun i =>
      [if n.graph.inherited i then 1 else 0, n.graph.origin i]))),
    ("edges", toJson (n.graph.edges.map (fun (a, b) => [a, b]))),
    ("stocks", toJson [n.graph.substrate, n.graph.fuel, n.graph.used,
      n.substrateStore, n.fuelStore, n.discardedSubstrate, n.discardedFuel])]

def evaluate (j : Json) : Except String Json := do
  let n ← parseState (← j.getObjVal? "state")
  let raw : Array (Array Nat) ← j.getObjValAs? (Array (Array Nat)) "events"
  let es ← raw.toList.mapM parseEvent
  pure (match history es n with | none => Json.null | some t => serialize t)

def main : IO Unit := do
  let input ← IO.getStdin
  let output ← IO.getStdout
  repeat
    let line ← input.getLine
    if line.isEmpty then break
    match Json.parse line >>= evaluate with
    | .error e => throw (IO.userError e)
    | .ok result => output.putStrLn result.compress
