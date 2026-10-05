"""Record scopes, sources, checks, and preservation for this continuation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[2]; WORK=ROOT/'work/shared-generative-direction'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
baseline=json.loads((WORK/'preservation-manifest.json').read_text())
changed=[name for name,digest in baseline.items() if not (ROOT/name).exists() or sha(ROOT/name)!=digest]
assert not changed,changed
checks=json.loads((WORK/'checks.json').read_text()); assert checks['all_checks_passed']
names=['outputs/shared-generative-direction.md','outputs/shared-generative-direction-mathematics.md',
       'outputs/shared-generative-direction.png','outputs/shared-generative-direction.svg',
       'work/shared-generative-direction/verify.py','work/shared-generative-direction/checks.json',
       'work/shared-generative-direction/preservation-manifest.json','work/shared-generative-direction/finalize.py']
links=[]
for name in names[:2]:
    path=ROOT/name
    for link in re.findall(r'\]\(([^)]+)\)',path.read_text()):
        if link.startswith(('https://','http://')): continue
        target=Path(link) if link.startswith('/') else path.parent/link
        if target.name=='shared-generative-direction-evidence.json': continue
        assert target.exists(),(name,link)
        links.append(str(target.resolve()))
cross_sources=[
 '/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-FOUNDATION.md',
 '/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/PLURAL-CAPACITY.md',
 '/Users/ren/Documents/Codex/2026-10-05/fo/outputs/direction-of-regeneration/EXPLORATION.md',
 '/Users/ren/Documents/Codex/2026-10-05/fo/outputs/concern-theory/THEORY.md']
record={
 'title':'Formalizing a direction toward shared generativity',
 'created_utc':datetime.now(timezone.utc).isoformat(),'local_date':'2026-10-05',
 'request':'continue with The remaining step, my proposed direction of reality is needs to be precise, and I think it can be formalized',
 'scope':'Descriptive direction of the coupled situation; operational capacity order, conditional statistical tendency, and shared-resource mechanism.',
 'cross_session_contributions':{
  'capability_foundation':'Joint implementable response profiles and separate plural requirements motivate a region rather than a scalar score.',
  'direction_research':'Preserves the distinction between physical prevalence and normative standing; avoids treating longer survival as a universal widening law.',
  'concern_research':'Inspected learning and evaluation distinctions; did not substitute a theory of caring for the requested descriptive direction.',
  'read_only_sources':{p:sha(Path(p)) for p in cross_sources}},
 'claim_status':{
  'capability_order':'Operational definition relative to assay functions, horizon and protected supports. Preorder on states; partial order on capacity regions.',
  'polytope_certificate':'Exact inclusion certificate by linear-programming duality under stated bounded/nonempty/executable assumptions. No scientific-priority claim.',
  'stationary_direction':'Proved sufficient ratio ordering for stationary stochastic dominance in a finite irreducible birth-death chain with valid ordered levels.',
  'strict_interpretation':'Strict increase in the numeric level represents strict assessed-capacity improvement only with distinct strictly nested benchmark regions.',
  'transient_scope':'Exact first-order counterexample shows stationary dominance need not hold at finite times from a common initial level.',
  'rate_scope':'Transition rates supplied phenomenologically, not derived energetically or from the differential-equation model.',
  'restart':'Positive formation from level0 is explicit; removing restart and keeping downward access makes eventual absorption at0.',
  'shared_model':'Exact material/energy budget, rare-Y invasion exponent, and locally stable rational coexistence.',
  'connecting_trajectory':'Numerical example checked at two step sizes, not a global basin proof.',
  'coexistence_scope':'Additional compatible renewal is not proof of whole capability-set inclusion; resident throughput can decline.',
  'reciprocity_scope':'Invader initial growth does not require contribution to recycling; positive recycling chemistry supplied.',
  'universal_status':'A falsifiable comparative hypothesis and conditional theorems, not an established universal physical or moral law.'},
 'primary_source':{
  'authors':'Caroline B. Turner, Zachary D. Blount, Daniel H. Mitchell, Richard E. Lenski',
  'title':'Evolution of a cross-feeding interaction following a key innovation in a long-term evolution experiment with Escherichia coli',
  'year':2023,'doi':'10.1099/mic.0.001390',
  'url':'https://pmc.ncbi.nlm.nih.gov/articles/PMC10482366/',
  'read_scope':'Parent inspected abstract and introduction through the stated findings, lines99-133. Later reopen returned a browser challenge; no claim of complete results-section audit.',
  'used_for':'Innovation changed resources and subsequent lineage adaptation, with coexistence and tradeoffs.',
  'not_used_for':'Validation of the new equations, capability-region inclusion, or universal direction.'},
 'checks':checks,
 'review':{
  'formal':'Separate agent verified LP inclusion, horizon conditions and interpretation; corrected preorder and strict-level terminology.',
  'conceptual':'Separate agent checked stationary ordering, transient limit, explicit missing physical reduction, and philosophical scope.',
  'shared_model':'Separate agent derived and checked the shared-resource equilibrium, invasion eigenvalue and stability margins.',
  'status':'Internal AI-assisted derivation/review; no external peer review or new empirical experiment.',
  'figure':'Generated figure visually inspected for legibility and clipping.',
  'local_links_checked':len(links)},
 'preservation':{'prior_output_count':len(baseline),'all_unchanged':True,'changed_files':changed},
 'artifacts':{name:sha(ROOT/name) for name in names}}
dest=ROOT/'outputs/shared-generative-direction-evidence.json'
dest.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'evidence':str(dest),'prior_outputs_preserved':len(baseline),'checks_passed':True,'local_links_checked':len(links)},indent=2))
