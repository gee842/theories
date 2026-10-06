import Exposure
open StochasticPrediction

def asBool (n : Nat) : Bool := n != 0

def asArm (n : Nat) : Arm :=
  match n with
  | 0 => .variable | 1 => .conventional | 2 => .fixedFast | 3 => .fixedSlow
  | 4 => .directRecord | 5 => .frozenRegister | 6 => .invertedRecord | _ => .invertedAction

def statusCode : Status → Nat
  | .inactive => 0 | .rentFailed => 1 | .noWork => 2 | .workedUnpaid => 3 | .workedPaid => 4

def evaluate (xs : List Nat) : Except String (List Nat) :=
  match xs with
  | [ga,bc,rc,rent,tc,wc,rn,gn,pk,lt,gt,f,g,gl,st,l,q,last,written,arm,z,gb,pb,av] =>
    let p : Parameters := ⟨ga,bc,rc,rent,tc,wc,rn,gn,pk,lt,gt⟩
    let s : State := ⟨f,g,gl,st,l,q,asBool last,asBool written⟩
    let b : Seed := ⟨asBool gb,asBool pb,asBool av⟩
    let r := exposure p (asArm arm) (asBool z) b s
    .ok [r.state.fuel,r.state.gate,r.state.gateLife,r.state.stage,r.state.life,r.state.q,
      r.state.last.toNat,r.state.written.toNat,r.spent,r.waste,
      r.worked.toNat,r.captured.toNat,r.wrote.toNat,statusCode r.status]
  | _ => .error "expected exactly 24 natural-number fields"

def parse (line : String) : Except String (List Nat) :=
  (line.trimAscii.toString.splitOn "\t").mapM fun x =>
    match x.toNat? with | some n => .ok n | none => .error "non-natural field"

def main : IO Unit := do
  let input ← IO.getStdin
  let output ← IO.getStdout
  repeat
    let line ← input.getLine
    if line.isEmpty then break
    match parse line >>= evaluate with
    | .error e => throw (IO.userError e)
    | .ok ns => output.putStrLn (String.intercalate "\t" (ns.map toString))
