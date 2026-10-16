#!/usr/bin/env python3
"""Independent compilation, receipt binding and finite whole-state reconstruction."""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
ROOT = next(p for p in HERE.parents if (p / "AGENTS.md").is_file())
STUDY = ROOT / "_process/research/2026-10-05-generative-foundation-review/root-foundation"


def digest(data):
    return sha256(data).hexdigest()


def start(**changes):
    s = dict(context=0, cash=14, fund=200, spent=0, goal=0, rule=0,
             judgment=0, quote=0, adopts=True, authority=True, approval=True,
             halted=False, losses=0, performed=0, fulfilled=0, archive=[], acquired=[])
    s.update(changes)
    return s


def impact(context, practice):
    return [int(practice == (2 if context == 0 else 1)), 1,
            int(practice == 2), int(practice == 1)]


def compare(a, b):
    # A direct bitwise inclusion comparison, without importing author's code.
    basic_superset = all(x >= y for x, y in zip(a[:2], b[:2]))
    basic_extra = any(x > y for x, y in zip(a[:2], b[:2]))
    if basic_superset and basic_extra:
        return True
    return (a[:2] == b[:2] and all(x >= y for x, y in zip(a[2:], b[2:]))
            and any(x > y for x, y in zip(a[2:], b[2:])))


def lookup(s, practice):
    return next((p for p in s["acquired"] if p[0] == practice), None)


def settle(s, cost, credit=0):
    if s["cash"] < cost or s["fund"] < credit:
        return None
    t = deepcopy(s)
    t.update(cash=s["cash"]-cost+credit, fund=s["fund"]-credit,
             spent=s["spent"]+cost)
    return t


def can_continue(s, credit, n):
    t = deepcopy(s)
    for _ in range(n):
        t = settle(t, 2, credit)
        if t is None:
            return False
    return True


def simulate(previous, event):
    s = deepcopy(previous)
    if s["halted"]:
        return s
    kind, value = event
    if kind in {"read", "learn", "assess", "enact", "quote"}:
        t = settle(s, 1)
        if t is None:
            s["halted"] = True
            return s
        s = t
    if kind == "read":
        s["acquired"] = deepcopy(s["archive"]) if value != "missing" else []
        for p in s["acquired"]:
            if value == "reversed":
                p[2] = 1 - p[2]
            elif value == "creditInflated" and p[0] == 2:
                p[7] = 2
        s["judgment"] = 0
    elif kind == "learn":
        a, b = lookup(s, 1), lookup(s, 2)
        av, bv = (a[6] if a else 0), (b[6] if b else 0)
        s["goal"] = 1 if av > bv else (2 if bv > av else 0)
    elif kind == "assess":
        a, b = lookup(s, 1), lookup(s, 2)
        s["judgment"] = 0
        if s["adopts"] and a and b and a[1] == b[1] == s["context"]:
            s["judgment"] = 2 if compare(b[2:6], a[2:6]) else (1 if compare(a[2:6], b[2:6]) else 0)
    elif kind == "enact":
        if value and s["judgment"]:
            s["goal"] = s["judgment"]
    elif kind == "quote":
        s["quote"] = 2
    elif kind == "reform":
        p = lookup(s, 2)
        if (p and s["quote"] == 2 and s["goal"] == s["judgment"] == 2
                and s["authority"] and s["rule"] == 0 and p[1] == s["context"]):
            installed = settle(s, 2)
            if (installed is not None and not can_continue(s, p[7], value)
                    and can_continue(installed, 2, value)):
                s = installed
                s["rule"] = 1
    elif kind in {"probe", "act"}:
        practice = value if kind == "probe" else 0
        if kind == "act":
            a, b = lookup(s, 1), lookup(s, 2)
            if a and b:
                if s["goal"] == 1:
                    practice = 1 if a[6] > b[6] else (2 if b[6] > a[6] else 0)
                elif s["goal"] == 2:
                    practice = 2 if compare(b[2:6], a[2:6]) else (1 if compare(a[2:6], b[2:6]) else 0)
            evidence = lookup(s, practice)
            if evidence is None or evidence[1] != s["context"]:
                s["halted"] = True
                return s
        credit = ((3, 1), (1, 2))[s["rule"]][practice-1]
        t = settle(s, 2, credit)
        if t is None:
            s["halted"] = True
            return s
        s = t
        effect = impact(s["context"], practice)
        s["archive"].insert(0, [practice, s["context"], *effect, 8 if practice == 1 else 3, credit])
        intact = bool(effect[0] and effect[1])
        s["losses"] += int(not intact)
        s["performed"] += int(kind == "act")
        s["fulfilled"] += int(kind == "act" and intact)
    elif kind == "shift":
        s.update(context=value, acquired=[], judgment=0, quote=0)
    else:
        raise AssertionError(event)
    return s


def preparation(meter="faithful", write=True):
    return [["probe",1],["read","faithful"],["learn",None],
            ["probe",2],["read",meter],["assess",None],["enact",write],["quote",None]]


def history(meter="faithful", write=True, reform=True):
    return preparation(meter, write) + ([["reform",8]] if reform else []) + [["act",None]]*8


def menu():
    return [
        ("success",start(),history()),
        ("unreformed",start(),history(reform=False)),
        ("write_clamp",start(),history(write=False,reform=False)),
        ("no_adoption",start(adopts=False),history()),
        ("approval_reversed",start(approval=False),history()),
        ("missing",start(),history(meter="missing")),
        ("restriction",start(context=1),history()),
        ("misleading",start(context=1),history(meter="reversed")),
        ("unauthorized",start(authority=False),history()),
        ("unfunded",start(fund=5),history()),
        ("credit_inflated",start(),history(meter="creditInflated")),
        ("short_demand",start(),preparation()+[["reform",3]]+[["act",None]]*3),
        ("context_shift",start(),preparation()+[["shift",1],["assess",None],["act",None]]),
    ]


def encode(s):
    keys = ["context","cash","fund","spent","goal","rule","judgment","quote",
            "adopts","authority","approval","halted","losses","performed","fulfilled"]
    return ([int(s[k]) for k in keys]+[len(s["archive"])]+
            [v for p in s["archive"] for v in p]+[len(s["acquired"])]+
            [v for p in s["acquired"] for v in p])


def main():
    rbytes = (BASE / "goal-revision-verification.json").read_bytes()
    r = json.loads(rbytes)
    assert r["status"] == "passed"
    frozen = BASE / r["retained_run"]
    assert (frozen / "verification.json").read_bytes() == rbytes
    for name, h in r["artifact_sha256"].items():
        assert digest((frozen / name).read_bytes()) == h, name
    for name, h in r["checker_sha256"].items():
        assert digest((BASE / name).read_bytes()) == h, name
    sources = {name:(BASE/(name+".lean")).read_bytes() for name in r["source_sha256"]}
    for name, data in sources.items():
        assert digest(data) == r["source_sha256"][name]
        assert data == (frozen/(name+".lean")).read_bytes()
    document_paths = [STUDY/"GOAL-REVISION-CONTINUATION-PROTOCOL.md", STUDY/"GOAL-REVISION-CONTINUATION.md"]
    document_hashes = {str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in document_paths}
    result_bytes = (HERE.parent/"results.json").read_bytes()
    authored = json.loads(result_bytes)
    assert authored["source_sha256"] == r["source_sha256"]
    assert authored["formal_run"] == r["retained_run"]
    assert authored["replay_sha256"] == digest((HERE.parent/"replay.py").read_bytes())
    binary = Path.home()/".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
    assert digest(binary.read_bytes()) == r["lean_binary_sha256"]
    counts = {}
    with tempfile.TemporaryDirectory(prefix="goal-revision-independent-") as temp:
        work = Path(temp)
        def run(args, log):
            proc = subprocess.run([str(binary)]+args,cwd=work,
                                  env={**os.environ,"LEAN_PATH":str(work)},text=True,
                                  stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=120)
            (HERE/log).write_text(proc.stdout)
            assert proc.returncode == 0, proc.stdout
            assert not re.search(r"\b(?:error|warning):",proc.stdout), proc.stdout
            return proc.stdout
        version = run(["--version"],"version.log").strip()
        assert version == r["lean_version"]
        for name,data in sources.items():
            (work/(name+".lean")).write_bytes(data)
        for name,data in sources.items():
            clean = re.sub(r"/-.*?-/","",data.decode(),flags=re.S)
            clean = re.sub(r"--[^\n]*","",clean)
            assert not re.search(r"\b(?:sorry|admit|axiom|unsafe|native_decide|implemented_by)\b|debug\.skipKernelTC",clean)
            assert re.findall(r"^namespace (\w+)$",clean,re.M) == [name]
            declarations = [{"kind":k,"name":name+"."+n} for k,n in re.findall(r"^(def|theorem|structure|inductive) (\w+)\b",clean,re.M)]
            record = next(m for m in r["modules"] if m["module"]==name)
            assert declarations == record["declarations"]
            counts[name] = [sum(d["kind"]=="theorem" for d in declarations),len(declarations)]
            output = run(["-o",name+".olean",name+".lean"],name+".log")
            assert output == (frozen/(name+".log")).read_text()
            for mode, directive, ds in [("AxiomAudit","#print axioms",declarations),
                                        ("Signatures","#check",[d for d in declarations if d["kind"]=="theorem"])]:
                file = name+mode+".lean"
                (work/file).write_text("import "+name+"\n"+"\n".join(directive+" "+d["name"] for d in ds)+"\n")
                text = run([file],name+mode+".log")
                assert text == (frozen/(name+mode+".log")).read_text()
                if mode == "AxiomAudit":
                    for d in ds:
                        full=d["name"]
                        if "'"+full+"' does not depend on any axioms" in text:
                            deps=[]
                        else:
                            m=re.search(r"'"+re.escape(full)+r"' depends on axioms:\s*\[([^]]*)\]",text)
                            assert m,full
                            deps=[a.strip() for a in m[1].split(",") if a.strip()]
                        assert deps==record["axiom_dependencies"][full]
                        assert set(deps)<={"propext","Quot.sound","Classical.choice"}
    compiled={}
    for line in (HERE/"GoalRevision.log").read_text().splitlines():
        m=re.fullmatch(r"TRACE (\w+) (\d+) (\[.*\])",line)
        assert m,line
        key=(m[1],int(m[2])); assert key not in compiled
        compiled[key]=json.loads(m[3])
    independent={}; summaries={}; records={}
    for name,s,events in menu():
        expected=authored["results"][name]
        assert expected["events"]==events
        states=[deepcopy(s)]
        conserved=s["cash"]+s["fund"]+s["spent"]
        for event in events:
            nxt=simulate(s,event)
            assert nxt["cash"]+nxt["fund"]+nxt["spent"]==conserved
            assert nxt["losses"]>=s["losses"]
            assert min(nxt["cash"],nxt["fund"],nxt["spent"])>=0
            assert nxt["archive"][-len(s["archive"]):]==s["archive"] if s["archive"] else True
            states.append(nxt); s=nxt
        assert states==expected["states"],name
        assert s==expected["final"],name
        for i,state in enumerate(states): independent[name,i]=encode(state)
        summaries[name]={k:s[k] for k in ["goal","rule","fulfilled","cash","fund","spent","losses","halted"]}
        records[name]=states
    assert independent==compiled
    assert len(records)==13 and len(independent)==221
    # Exact causal contrasts use the same acquired records and judgments.
    assert records["success"][8]["acquired"]==records["write_clamp"][8]["acquired"]
    assert records["success"][8]["judgment"]==records["write_clamp"][8]["judgment"]==2
    assert records["success"][8]["cash"]==records["write_clamp"][8]["cash"]==8
    assert summaries["success"]["fulfilled"]==8 and summaries["unreformed"]["fulfilled"]==7
    assert summaries["credit_inflated"]["fulfilled"]==7 and summaries["credit_inflated"]["rule"]==0
    assert summaries["misleading"]["fulfilled"]==0 and summaries["misleading"]["losses"]==9
    assert rbytes==(BASE/"goal-revision-verification.json").read_bytes()
    assert result_bytes==(HERE.parent/"results.json").read_bytes()
    for name,data in sources.items(): assert data==(BASE/(name+".lean")).read_bytes()
    for p,h in document_hashes.items(): assert digest((ROOT/p).read_bytes())==h
    report={
        "status":"passed_independent_recompilation_and_221_state_reconstruction",
        "utc":datetime.now(timezone.utc).isoformat(),"source_sha256":r["source_sha256"],
        "documents_sha256":document_hashes,"author_receipt_sha256":digest(rbytes),
        "author_results_sha256":digest(result_bytes),"author_run":r["retained_run"],
        "retained_artifacts":len(r["artifact_sha256"]),"counts":counts,
        "lean_version":version,"lean_binary_sha256":r["lean_binary_sha256"],
        "cases":13,"complete_state_comparisons":221,"final_states":summaries,
        "script_sha256":digest(Path(__file__).read_bytes()),
        "log_sha256":{p.name:digest(p.read_bytes()) for p in sorted(HERE.glob("*.log"))},
        "scope":"Independent isolated Lean compilation and finite reconstruction. No empirical verification, general interpreter refinement or ethical origin proof.",
    }
    (HERE/"verification.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ["status","counts","cases","complete_state_comparisons","source_sha256","documents_sha256"]},ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
