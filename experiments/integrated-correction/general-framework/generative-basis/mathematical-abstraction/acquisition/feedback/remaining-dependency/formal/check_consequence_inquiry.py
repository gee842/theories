"""Fresh formal check of remaining access after the relay source is exhausted.

Reads saved artifacts only. Reuses the disclosed old state-literal encoder;
imports no native transition producer and reruns no native history.
"""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'RESEARCH.md').is_file())
FB = HERE.parents[1]
OUT = HERE/'consequence-inquiry'
CORE = ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean'
LEAN = Path('/Users/ren/.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean')
EXPECTED_LEAN = 'b48bc5ab229bd8b320a224b87e20fc428dba6fa8a1c054bd4fa6def846e19997'


def sha(path):
    return sha256(path.read_bytes()).hexdigest()


def load_encoder():
    spec = importlib.util.spec_from_file_location('retained_relay_encoder', HERE/'check.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def generate(original, correction, encoder):
    rows = {c['name']: c for c in original['cases']}
    aliases = {'ordinary':'law_01_learned', 'calibration':'calibration_break',
               'falseContact':'false_dependence'}
    lines = ['import ConsequenceInquiry', 'namespace ConsequenceInquirySaved',
             'open RemainingDependency ConsequenceInquiry',
             'set_option maxRecDepth 32768', 'set_option maxHeartbeats 4000000']
    definitions, theorems = [], []
    def define(name, typ, body):
        definitions.append(name)
        lines.append(f'def {name} : {typ} := {body}')
    def prove(name, statement, proof='by decide'):
        theorems.append(name)
        lines.append(f'theorem {name} : {statement} := {proof}')
    for alias, name in aliases.items():
        case = rows[name]
        assert case['final']['native']['source'] == 0
        define(alias+'Config', 'Config', encoder.config(case))
        define(alias, 'State', encoder.state(case['final'], alias+'Config'))
        prove(alias+'_source_zero', f'{alias}.body.stocks.source = 0')
    prove('ordinary_calibration_same_view', 'view ordinary = view calibration')
    prove('distinct_actual_outcomes',
          'ordinary.body.stocks.load = 10 ∧ ordinary.body.stocks.waste = 0 ∧ '
          'calibration.body.stocks.load = 0 ∧ calibration.body.stocks.waste = 10')
    inherited = encoder.tick(rows['law_01_learned']['inherited_consumption'])
    prove('same_original_account',
          f'wholeTotal {inherited} ordinary = 145 * ticks ∧ '
          f'wholeTotal {inherited} calibration = 145 * ticks')
    prove('all_words_preserve_ambiguity',
          '∀ es : List Event, view (run ordinary es) = view (run calibration es)',
          'by\n  intro es\n  exact equal_view_runs ordinary calibration es '
          'ordinary_source_zero calibration_source_zero ordinary_calibration_same_view')
    prove('no_correct_view_decoder',
          '¬ ∃ f : State → Bool, f (view ordinary) = true ∧ f (view calibration) = false',
          'by\n  rintro ⟨f, hs, hf⟩\n  rw [ordinary_calibration_same_view] at hs\n'
          '  rw [hs] at hf\n  cases hf')
    define('alternateWord','List Event',
           '[.command true, .challenge, .contact false, .write true, .read, .commit, .retain]')
    for alias, name in aliases.items():
        result = next(c for c in correction['cases']
                      if c['source_case'] == name and c['contact_selector'] == 0)
        assert result['old_endpoint'] == rows[name]['final']
        define(alias+'Alternate', 'State', encoder.state(result['final'], alias+'Config'))
        prove(alias+'_alternate_correspondence',
              f'run {alias} alternateWord = {alias}Alternate')
    prove('false_contact_still_separated',
          'falseContactAlternate.body.values = ⟨some false, some false⟩ ∧ '
          'falseContactAlternate.body.selected = none ∧ '
          'calibrationAlternate.body.values = ⟨some false, some true⟩ ∧ '
          'calibrationAlternate.body.selected = some true')
    lines.append('end ConsequenceInquirySaved')
    return '\n\n'.join(lines)+'\n', definitions, theorems


def main():
    assert sha(LEAN) == EXPECTED_LEAN
    old = json.loads((FB/'remaining-dependency-results.json').read_text())
    old_review = json.loads((FB/'remaining-dependency-independent-check.json').read_text())
    correction = json.loads((FB/'correction-localization-results.json').read_text())
    correction_review = json.loads((FB/'correction-localization-independent-check.json').read_text())
    assert old_review['status'] == correction_review['status'] == 'passed'
    assert old_review['results_sha256'] == sha(FB/'remaining-dependency-results.json')
    assert correction_review['results_sha256'] == sha(FB/'correction-localization-results.json')
    assert correction_review['check_source_sha256'] == sha(FB/'correction_localization_check_review.py')
    bindings = dict(correction_review['source_bindings'])
    for name, value in old['source_hashes'].items():
        assert bindings[name] == value
    for path, value in bindings.items():
        assert sha(ROOT/path) == value, path
    for path in (CORE, HERE/'ConsequenceInquiry.lean', HERE/'InquiryRelevance.lean', HERE/'check.py', Path(__file__),
                 OUT/'CONTRACT.md', FB/'correction-localization-results.json',
                 FB/'correction-localization-independent-check.json',
                 FB/'correction_localization_check_review.py'):
        bindings[str(path.relative_to(ROOT))] = sha(path)
    source = (HERE/'ConsequenceInquiry.lean').read_text()
    code = re.sub(r'/\-.*?\-/', '', source, flags=re.S)
    code = re.sub(r'--[^\n]*', '', code)
    assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b', code)
    new_declarations = re.findall(r'^(?:def|theorem)\s+(\w+)', source, flags=re.M)
    general_theorems = re.findall(r'^theorem\s+(\w+)', source, flags=re.M)
    relevance_source = (HERE/'InquiryRelevance.lean').read_text()
    relevance_code = re.sub(r'/\-.*?\-/', '', relevance_source, flags=re.S)
    relevance_code = re.sub(r'--[^\n]*', '', relevance_code)
    assert not re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b', relevance_code)
    relevance_declarations = re.findall(r'^(?:def|theorem)\s+(\w+)', relevance_source, flags=re.M)
    relevance_theorems = re.findall(r'^theorem\s+(\w+)', relevance_source, flags=re.M)
    fixture, fixture_defs, fixture_theorems = generate(old, correction, load_encoder())
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    run = OUT/'runs'/stamp
    run.mkdir(parents=True)
    for name, path in (('GenerativeCore', CORE), ('RemainingDependency', HERE/'RemainingDependency.lean'),
                       ('ConsequenceInquiry', HERE/'ConsequenceInquiry.lean'),
                       ('InquiryRelevance', HERE/'InquiryRelevance.lean')):
        shutil.copyfile(path, run/(name+'.lean'))
    (run/'ConsequenceInquirySaved.lean').write_text(fixture)
    audits = ['ConsequenceInquiry.'+n for n in new_declarations]
    audits += ['InquiryRelevance.'+n for n in relevance_declarations]
    audits += ['ConsequenceInquirySaved.'+n for n in fixture_defs+fixture_theorems]
    (run/'ConsequenceInquiryAudit.lean').write_text(
        'import ConsequenceInquirySaved\nimport InquiryRelevance\n'+
        '\n'.join('#print axioms '+n for n in audits)+'\n')
    modules=[]
    env=dict(os.environ, LEAN_PATH=str(run))
    for name in ('GenerativeCore','RemainingDependency','ConsequenceInquiry','InquiryRelevance',
                 'ConsequenceInquirySaved','ConsequenceInquiryAudit'):
        try:
            result=subprocess.run([str(LEAN),'-o',name+'.olean',name+'.lean'],cwd=run,
                                  env=env,capture_output=True,text=True,timeout=90)
            output=result.stdout+result.stderr
            status=result.returncode
        except subprocess.TimeoutExpired as error:
            output=str(error.stdout or '')+str(error.stderr or '')+'\nTIMEOUT\n'
            status=-1
        (run/(name+'.log')).write_text(output)
        modules.append(dict(module=name,exit_code=status,source_sha256=sha(run/(name+'.lean')),
                            log_sha256=sha(run/(name+'.log'))))
        if status:
            failure=dict(status='failed',source_bindings=bindings,modules=modules,
                         run=str(run.relative_to(ROOT)))
            (run/'verification.json').write_text(json.dumps(failure,indent=2)+'\n')
            print(output[-12000:])
            raise SystemExit(f'Build failed: {name}; preserved at {run}')
    text=(run/'ConsequenceInquiryAudit.log').read_text()
    found={}
    for line in text.splitlines():
        m=re.fullmatch(r"'([^']+)' does not depend on any axioms",line)
        if m: found[m[1]]=[];continue
        m=re.fullmatch(r"'([^']+)' depends on axioms: \[([^]]*)\]",line)
        if m: found[m[1]]=[x.strip() for x in m[2].split(',') if x.strip()]
    assert set(found)==set(audits),(set(audits)-set(found),set(found)-set(audits))
    dependencies=sorted({a for names in found.values() for a in names})
    assert set(dependencies)<= {'propext','Quot.sound','Classical.choice'},dependencies
    for path, value in bindings.items(): assert sha(ROOT/path)==value,path
    receipt=dict(status='passed',scope='Unchanged-law source-zero observation congruence and finite feedback policies; source-bound actual endpoints',
                 run=str(run.relative_to(ROOT)),compiler_sha256=sha(LEAN),source_bindings=bindings,
                 source_binding_count=len(bindings),modules=modules,
                 general_theorem_count=len(general_theorems),saved_fixture_theorem_count=len(fixture_theorems),
                 query_relevance_theorem_count=len(relevance_theorems),
                 explicit_new_declaration_audits=len(audits),declaration_dependencies=found,
                 standard_axioms=dependencies,custom_axioms=[],proof_holes=[],
                 saved_parent_cases=3,alternate_request_correspondences=3,
                 limitations=[
                     'Only the unchanged event law and source-zero states are covered.',
                     'The mathematical view is richer than actual controller input; projection does not erase physical effects.',
                     'The general proofs cover finite request words and the defined finite feedback-policy interpreter.',
                     'Original native ancestry remains bound to its existing independent receipt.',
                     'The saved state encoder is reused and hash-bound; no native producer is imported or rerun.',
                     'No universal Python refinement, new physical contact or ethical criterion is established.',
                     'The separately extended calibration-contact law is outside this old-law obstruction.'])
    receipt['limitations'].append('Query uniqueness concerns one faithful weak-setting read, the complete declared family and the local-agreement question; it does not derive target value, route reliability or policy formation.')
    (run/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    (OUT/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ('status','general_theorem_count','query_relevance_theorem_count','saved_fixture_theorem_count',
          'explicit_new_declaration_audits','source_binding_count','standard_axioms','run')}))


if __name__=='__main__':
    main()
