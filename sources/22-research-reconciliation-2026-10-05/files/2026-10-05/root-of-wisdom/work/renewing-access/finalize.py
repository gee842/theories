"""Record evidence, check links, and verify preservation of earlier outputs."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'work/renewing-access'
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
baseline=json.loads((WORK/'preservation-manifest.json').read_text())
changed=[name for name,sha in baseline.items() if not (ROOT/name).exists() or digest(ROOT/name)!=sha]
assert not changed,changed
checks=json.loads((WORK/'checks.json').read_text())
assert checks['all_checks_passed']

artifacts=[
 'outputs/renewing-access-to-support.md',
 'outputs/renewing-access-to-support-mathematics.md',
 'outputs/renewing-access-to-support.png',
 'outputs/renewing-access-to-support.svg',
 'work/renewing-access/verify.py',
 'work/renewing-access/checks.json',
 'work/renewing-access/preservation-manifest.json',
 'work/renewing-access/finalize.py',
]
checked_links=[]
for name in artifacts[:2]:
    path=ROOT/name
    for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
        if target.startswith(('https://','http://')): continue
        local=Path(target) if target.startswith('/') else path.parent/target
        if local.name=='renewing-access-to-support-evidence.json': continue
        assert local.exists(),(name,target)
        checked_links.append(str(local.resolve()))

evidence={
 'title':'Renewing access to supporting conditions',
 'created_utc':datetime.now(timezone.utc).isoformat(),
 'local_date':'2026-10-05','timezone':'Asia/Bangkok',
 'user_request':'lets explore this stronger working formulation',
 'interpretation':'Make access to support endogenous; distinguish continued renewal from preservation of a material form; retain the coupled situation as the explanatory unit.',
 'continuity':[
  'Conditions-of-generativity supplied usable power; this extension makes its capture depend on maintained machinery.',
  'Earlier identity and missing-possibility work motivates the distinction between an adequate aggregate for one function and omitted consequential functions.',
  'All earlier outputs are retained unchanged.'
 ],
 'claim_status':{
  'capture_budget':'Exact reduced model with Pcaptured=eta I C/M <= I; full molecular thermodynamics not derived.',
  'equilibrium_fold':'Proved existence of two positive equilibria above gf=epsilon b+4s ell b/(kM^2), one double equilibrium at gf, none below.',
  'bistability':'Proved local asymptotic stability of inactivity at every finite g and of the upper positive branch above gf. Lower branch is a saddle.',
  'global_scope':'No complete basin boundary or classification of nonstationary attractors. Fold is not asserted as a global survival threshold.',
  'small_preparation_failure':'Proved invariant region and convergence to inactive equilibrium; exact unit-parameter certificate at g17, R0=.01, C0=E0=0, D0=.99.',
  'formation':'Exact initial machinery formation and second derivative of captured reserve from R0>0; long-term activation from R0=1 is illustrated numerically.',
  'succession':'Exact X-to-Y replacement at fixed aggregate equilibrium; a supplied Y-only channel activates finite substrate conversion.',
  'novelty_scope':'Newly accessible function in a stipulated repertoire; no derived invention of chemistry or open-ended novelty.',
  'universal_direction':'No universal increase of generativity or direction toward kindness proved; wider environmental effects remain to be modeled.'
 },
 'sources':[
  {'authors':'Anne Shiu and Bernd Sturmfels','title':'Siphons in chemical reaction networks',
   'url':'https://people.tamu.edu/~annejls/SiphonsInCRNs.pdf',
   'read_scope':'Section 2 definitions and Proposition 2.1, PDF page 4',
   'used_for':'Standard structural criterion for forward invariance of an empty species face.',
   'not_used_for':'Novel theorem priority or direct molecular implementation of the energy coordinate.'},
  {'authors':'Katarzyna Adamala and Jack W. Szostak','title':'Competition between model protocells driven by an encapsulated catalyst',
   'year':2013,'doi':'10.1038/nchem.1650','url':'https://doi.org/10.1038/nchem.1650',
   'read_url':'https://protobiology.org/wp3/wp-content/uploads/2013/04/Adamala_Szostak_NatChem_2013.pdf',
   'read_scope':'Abstract; membrane effects and competitive growth on journal pages 497-500; discussion on page 501.',
   'used_for':'Experimental example of internal chemistry changing a material interface.',
   'not_used_for':'Autonomous catalyst renewal, improved general permeability, or a universal direction of reality.'}
 ],
 'checks':checks,
 'review':{
  'mathematical':'Separate agent reviewed equations, proofs, numerical-check scope and succession. No material errors found.',
  'conceptual':'Separate agent reviewed relational interpretation and source scope. Tightened experimental language and asymptotic replacement wording.',
  'succession':'Separate derivation confirmed aggregate closure after endogenous capture was added.',
  'status':'Internal AI-assisted review, not external scientific peer review.',
  'plot':'PNG visually inspected; legend moved away from curves before final delivery.',
  'markdown':'Local links checked; no claim of native Markdown layout verification.'
 },
 'preservation':{'baseline_files':len(baseline),'changed_files':changed,'all_unchanged':True},
 'checked_local_links':checked_links,
 'artifacts':{name:digest(ROOT/name) for name in artifacts}
}
path=ROOT/'outputs/renewing-access-to-support-evidence.json'
path.write_text(json.dumps(evidence,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'evidence_path':str(path),'earlier_outputs_preserved':len(baseline),
                  'checks_passed':True,'checked_local_links':len(checked_links)},indent=2))
