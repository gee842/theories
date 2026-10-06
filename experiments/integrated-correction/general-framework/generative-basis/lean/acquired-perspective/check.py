#!/usr/bin/env python3
"""Fresh-check the acquired perspective bridge against unchanged source receipts."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
REPOSITORY = HERE.parents[5]
LEAN_ROOT = HERE.parent
TOOLCHAIN = "leanprover/lean4:v4.29.1"
BASELINE_JSON = {'experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/verification.json': '56eb4b70d285c83ca27dd6264ebf1e1a6565312efab2b27289ad8b4380642dab',
 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/formal/verification.json': '51662eed968f7aa66253d0d40c23c145c5902875376667df66b91e23cdec69a7',
 'experiments/integrated-correction/general-framework/generative-basis/lean/verification.json': '0e446764280518fc43fa040f4325789da2899ebaf8ae7e0493fa3ac42c64e665'}
INHERITED = {'GenerativeCore': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean',
                    'source_sha256': 'e3daca1b729118fc309585a5d3ba1af60ac99cd80bab41e477aed204177069e8',
                    'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/GenerativeCore.txt',
                    'receipt_sha256': 'eae342f61e22744208cddbc5144ff1f5b58b3849a5a827563fb58e65833a3257'},
 'BoundaryModels': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/BoundaryModels.lean',
                    'source_sha256': 'a9c171e4a20857c82a7c8f6f8e4f48729f0900a671937e2421ec4c20ac69431e',
                    'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/BoundaryModels.txt',
                    'receipt_sha256': '6201e6d14ea683862919e61b0eb0e143b478a6c972026fdf8565c9ae0ada6783'},
 'Depletion': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/Depletion.lean',
               'source_sha256': 'd18e23ae33c6f018b1af22f2596fc6509848d501f042af026a76b3d2982696f0',
               'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/Depletion.txt',
               'receipt_sha256': 'c42329c2ab8d545a7897037b50887d4944cf95c47e781d1da19be42a18cb319a'},
 'RootRealization': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/RootRealization.lean',
                     'source_sha256': '5e0b273caa73be01f38781427a1b7838d6fa291963ccf7a784b5bcbe5994ecf6',
                     'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/RootRealization.txt',
                     'receipt_sha256': '7e93c850b1204842a29c299dbbd9622804c59a604449a635eff9ca5dd2323f37'},
 'ProductTower': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ProductTower.lean',
                  'source_sha256': '68cefbd0cf76251a434b81dee7f4fa8916f25474ff73f66ab6f92aa2393fff54',
                  'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/ProductTower.txt',
                  'receipt_sha256': 'e675ad8be5cdd58ddb0298f2c412f57714adba5492a5a7f66c22964dcb0a2948'},
 'DynamicUnderdetermination': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/deeper/DynamicUnderdetermination.lean',
                               'source_sha256': '0b5e930ba0a91306e73746c811b71e74fb9ccbc9e152c2e1116c4d19c4147f6c',
                               'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/DynamicUnderdetermination.txt',
                               'receipt_sha256': '7123d6b8a7695a709de7c94219460a1887c155bd92c9fed256a126939d823a07'},
 'GeneratedPaths': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/deeper/GeneratedPaths.lean',
                    'source_sha256': 'c9194672eca9625ef95ece823ef98a7bca46ead33215246dd97ebe3e8cecbbc1',
                    'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/GeneratedPaths.txt',
                    'receipt_sha256': '3ba7fc4e0f2dd8d477a7a250d44bc5b3dfa1484805f4313385907dfcb9da7048'},
 'HistoryRealization': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/deeper/HistoryRealization.lean',
                        'source_sha256': '22785f31280a7bbac5f89d7754cb6896830a6dc2d81949b9f3adfabd126e8fa9',
                        'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/HistoryRealization.txt',
                        'receipt_sha256': '97266bca4133cb46c4605b714397a8978a46343bd795429e184693890f223efe'},
 'DynamicSymmetry': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/deeper/DynamicSymmetry.lean',
                     'source_sha256': '5f71b9cc6c69070b5033852a0809ad795ad5dd18a44eb2ca068d1915d744673b',
                     'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/DynamicSymmetry.txt',
                     'receipt_sha256': 'e452e738d7ed39e8a7c3f357fa9efb04fec15dc1bb30eee25963df1d3a06aa98'},
 'DynamicConsequences': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/deeper/DynamicConsequences.lean',
                         'source_sha256': 'd4a0dfc019fd1009d0230b0aa88ea4d940d42b6394ff44f59568e95edbd27692',
                         'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/DynamicConsequences.txt',
                         'receipt_sha256': '3c8bf5fe8360f932907008709c8e8c400246d853dd1a4af23ae928cb563302e4'},
 'DynamicClassification': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/deeper/DynamicClassification.lean',
                           'source_sha256': '0da653296377300a7f77af100a7d2bcd46433e3f0882fe5a9b9bc8c697e32698',
                           'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/DynamicClassification.txt',
                           'receipt_sha256': 'e6dda2f9ff8c5795eb23159ec3aaecae1324c014145f006b8020acd4273d7e71'},
 'GeneratedSelf': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/GeneratedSelf.lean',
                   'source_sha256': '96b5b5a71e465abbf6139bb230cecfa8b28bb48b58d519fd2a5c7cccdf165c6d',
                   'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/GeneratedSelf.txt',
                   'receipt_sha256': 'cc19a153226c56e71e7c389e6602ae781cb3216735a93e9dd3c34e42431fea75'},
 'EthicalOrientation': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/EthicalOrientation.lean',
                        'source_sha256': '00bcc4a7542d4b81f1e924207d1d5b82e1ae032c4e26d7031d2779914fd56cc4',
                        'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/EthicalOrientation.txt',
                        'receipt_sha256': 'e196aa6a026847585956303bc3b11a70c4f24a23794cef950063427ed1a6e1fd'},
 'OutcomeContinuation': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/OutcomeContinuation.lean',
                         'source_sha256': '30700141aeb7be1ef30ea8848a4ee1fd8fcd73673e6d2ce09e74636a15b81deb',
                         'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/OutcomeContinuation.txt',
                         'receipt_sha256': 'fe8575aa7381e9267e1c76ea34050e89249e05a41b2453afd20777a9ce41955d'},
 'GenerativeModel': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeModel.lean',
                     'source_sha256': 'c9752ea54674fc5b3fedd89c64af133c19838a20a83c363d0fac5272c84ff33b',
                     'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/GenerativeModel.txt',
                     'receipt_sha256': '3bf8a416db44d77a5de4d5188bf3af6f0dcad48a6a0b9b8ce66653bf541d2f8d'},
 'GenerativeOutcomeModel': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeOutcomeModel.lean',
                            'source_sha256': '3412a61fe07953bd326db6b06ba7991117712581de47721ad5a8959fffff9aa9',
                            'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/verification/GenerativeOutcomeModel.txt',
                            'receipt_sha256': '42ee9db54ea181621fac597d7c04898fc532060ecbbe27fa810c163c2f3612cd'},
 'FormedSelection': {'source': 'experiments/shared-renewal-capability/regulation/retention/formation/formal/FormedSelection.lean',
                     'source_sha256': 'a7bdce34f00ab07edd8b234eb1a7abd435a0cfe8034257ff3928209d0966bf37',
                     'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/verification/FormedSelection.txt',
                     'receipt_sha256': 'bc40309a6c1a1107769f5ba127164fb16e53dc9dd85949d57285d63a6eaa8686'},
 'SelectorRevision': {'source': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/formal/SelectorRevision.lean',
                      'source_sha256': '2a93d72c5546106200225c5eabc08e08a7f78ac218541146e006f51f261c8d5a',
                      'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/verification/SelectorRevision.txt',
                      'receipt_sha256': '8be9f06f8e3931ccfdf0095fbb71c2af4021bd44fe3fadd2101ff57fb22275cc'},
 'UpdaterFormation': {'source': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/formal/UpdaterFormation.lean',
                      'source_sha256': 'f04266c1745c71437a5500a955fb6da364eb9cce56b1a4655a04968ac450d5c3',
                      'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/verification/UpdaterFormation.txt',
                      'receipt_sha256': '7244069bca5a50cc4445e864c905bb4d4327ca7896651008d2ffd15279bab904'},
 'ConstructedUpdater': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater/ConstructedUpdater.lean',
                        'source_sha256': 'c59f5c934ed1884ffddfa36d982b89e6f934386d462a56927478004018e02023',
                        'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/verification/ConstructedUpdater.txt',
                        'receipt_sha256': '8d9362e4a7aa4b29954a620eea9ae423a97d9bb89371b96c3573066e5da43ad9'},
 'PredictionAction': {'source': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/formal/PredictionAction.lean',
                      'source_sha256': '021cdb25eca55e42ea471f68b08a7b5e91a2145578bf0254db2332d7e16afd8c',
                      'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/verification/PredictionAction.txt',
                      'receipt_sha256': '98b624c0824c4e621ee6fdebc17ed4d6fbd64b18d412ad347545e7bd140fe2d4'},
 'ConstructedPrediction': {'source': 'experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/ConstructedPrediction.lean',
                           'source_sha256': 'b3dca9bd1fa58b1c45450c3c77d66ad2bdbbe153c1797fbc4fca534d6878d51f',
                           'receipt': 'experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/verification/ConstructedPrediction.txt',
                           'receipt_sha256': 'f419242fff5b399f6594c4a643f0c133d78b8f872609c74e87f3bd35352f46b2'},
 'RecipientCorrection': {'source': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/formal/RecipientCorrection.lean',
                         'source_sha256': 'b42588f0fa631f858142cabc596f693482f30d933e793543005ab40494d00fc1',
                         'receipt': 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/formal/verification/RecipientCorrection.txt',
                         'receipt_sha256': '797b6ef74c6d412e922bd75d25cc1719e5919c5bfcdbdfa0a0995326caed8ab7'}}
NEW_MODULES = ["AcquiredPerspective", "GenerativeAcquisitionModel"]
AUDIT = re.compile(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def audits(text):
    return [(name, sorted(x.strip() for x in deps.split(",") if x.strip()))
            for name, deps in AUDIT.findall(text)]


def run(command, cwd, env=None):
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)


def main():
    checker = Path(__file__).read_bytes()
    for path, sha in BASELINE_JSON.items():
        assert digest((REPOSITORY / path).read_bytes()) == sha, path
    frozen = {}
    old_audits = {}
    for name, item in INHERITED.items():
        source = (REPOSITORY / item["source"]).read_bytes()
        receipt = (REPOSITORY / item["receipt"]).read_bytes()
        assert digest(source) == item["source_sha256"], name
        assert digest(receipt) == item["receipt_sha256"], name
        frozen[name] = source
        old_audits[name] = audits(receipt.decode())
        assert old_audits[name], name
    for name in NEW_MODULES:
        frozen[name] = (LEAN_ROOT / (name + ".lean")).read_bytes()
    allowed = {axiom for entries in old_audits.values()
               for _, dependencies in entries for axiom in dependencies}
    assert allowed <= {"propext", "Quot.sound", "Classical.choice"}
    seen = {"Std"}
    for name, source in frozen.items():
        text = source.decode()
        assert not re.search(r"\b(sorry|admit|native_decide|unsafe)\b", text), name
        assert not re.search(r"^\s*(axiom|constant|opaque)\s", text, re.M), name
        imports = re.findall(r"^import\s+(\S+)\s*$", text, re.M)
        assert set(imports) <= seen, (name, imports)
        seen.add(name)
    for name in NEW_MODULES:
        source = frozen[name].decode()
        declarations = re.findall(r"^theorem\s+(\w+)", source, re.M)
        requested = re.findall(r"^#print axioms (\S+)", source, re.M)
        assert [n.rsplit(".", 1)[-1] for n in requested] == declarations, name
        assert len(set(declarations)) == len(declarations), name
    version = run(["lean", "+" + TOOLCHAIN, "--version"], HERE)
    version.check_returncode()
    assert "version 4.29.1," in version.stdout
    prefix = run(["lean", "+" + TOOLCHAIN, "--print-prefix"], HERE)
    prefix.check_returncode()
    compiler = Path(prefix.stdout.strip()) / "bin/lean"
    output = HERE / "verification"
    output.mkdir(exist_ok=True)
    results = []
    with tempfile.TemporaryDirectory(prefix="acquired-perspective-lean-") as temporary:
        build = Path(temporary)
        for name, data in frozen.items():
            (build / (name + ".lean")).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(build))
        for name in frozen:
            result = run([str(compiler), "-o", name + ".olean", name + ".lean"], build, env)
            receipt = output / (name + ".txt")
            receipt.write_text(result.stdout)
            actual = audits(result.stdout)
            printed = re.findall(r"^#print axioms (\S+)", frozen[name].decode(), re.M)
            matched = len(actual) == len(printed) and all(
                a == p or a.endswith("." + p) for (a, _), p in zip(actual, printed))
            deps = sorted({d for _, ds in actual for d in ds})
            old_exact = name not in INHERITED or actual == old_audits[name]
            added = sorted(set(deps) - allowed)
            clean = (result.returncode == 0 and matched and bool(actual) and old_exact
                     and not added and "warning:" not in result.stdout
                     and "sorryAx" not in result.stdout)
            results.append({
                "module": name, "source": INHERITED[name]["source"] if name in INHERITED else str((LEAN_ROOT / (name + ".lean")).relative_to(REPOSITORY)),
                "source_sha256": digest(frozen[name]), "exit_code": result.returncode,
                "audited_declarations": [n for n, _ in actual],
                "axioms_by_declaration": dict(actual), "axioms": deps,
                "empty_axiom_audits": sum(not d for _, d in actual),
                "matches_original_dependency_audits": old_exact,
                "axioms_outside_inherited_chain": added, "clean": clean,
                "output": "verification/" + receipt.name,
                "output_sha256": digest(receipt.read_bytes())})
            if not clean:
                print(result.stdout)
                break
    unchanged = all((REPOSITORY / item["source"]).read_bytes() == frozen[name]
                    for name, item in INHERITED.items())
    unchanged = unchanged and all((LEAN_ROOT / (name + ".lean")).read_bytes() == frozen[name]
                                  for name in NEW_MODULES)
    unchanged = unchanged and Path(__file__).read_bytes() == checker
    baseline_receipts_unchanged = all(
        digest((REPOSITORY / path).read_bytes()) == sha
        for path, sha in BASELINE_JSON.items()) and all(
        digest((REPOSITORY / item["receipt"]).read_bytes()) == item["receipt_sha256"]
        for item in INHERITED.values())
    passed = (unchanged and baseline_receipts_unchanged and len(results) == len(frozen)
              and all(r["clean"] for r in results))
    new_results = [r for r in results if r["module"] in NEW_MODULES]
    record = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed", "lean_version": version.stdout.strip(),
        "toolchain": TOOLCHAIN, "compiler_binary": str(compiler),
        "compiler_sha256": digest(compiler.read_bytes()), "checker_sha256": digest(checker),
        "fresh_temporary_build": True, "sources_unchanged_during_check": unchanged,
        "baseline_receipts_unchanged_during_check": baseline_receipts_unchanged,
        "pinned_baseline_json": BASELINE_JSON, "inherited_source_and_receipt_pins": INHERITED,
        "inherited_axiom_union": sorted(allowed), "modules": results,
        "new_declarations_by_module": {r["module"]: len(r["audited_declarations"]) for r in new_results},
        "new_audited_declarations": sum(len(r["audited_declarations"]) for r in new_results),
        "new_empty_axiom_audits": sum(r["empty_axiom_audits"] for r in new_results),
        "new_axiom_union": sorted({d for r in new_results for d in r["axioms"]}),
        "scope": "Actual retained action-effect acquisition, correction and organizational use "
                 "under unchanged ConstructedPrediction dynamics. No new world law, custom axiom, "
                 "target identity or controller. Imported recipes, funding, binary response and "
                 "noiseless availability remain model inputs; inherited standard dependencies "
                 "are retained, not eliminated. Recipient comparison is not a composed physical history."
    }
    (HERE / "verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({k: record[k] for k in ["status", "new_audited_declarations", "new_empty_axiom_audits", "new_axiom_union"]}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
