"""Extract authored tower primitives without Blender; estimate logistics, not dynamics."""
import ast, json, math, hashlib
from pathlib import Path
HERE = Path(__file__).resolve().parent
PROD = HERE.parent
SOURCE = PROD / 'blender/build_assets.py'
class Node(dict):
    def __init__(self, name): super().__init__(); self.name = name
records=[]
class Geo:
    def __init__(self): self.parts=[]
    def box(self, center, size, mat): self.parts.append(('box',mat,math.prod(size),list(size)))
    def beam(self,p,q,depth=.44,width=.22,web=.014,flange=.022,mat='Steel'):
        area=2*width*flange+(depth-2*flange)*web
        self.parts.append(('beam',mat,math.dist(p,q)*area,[depth,width,web,flange,math.dist(p,q)]))
    def tube(self,p,q,r=.035,mat='Steel',sides=10):
        self.parts.append(('tube',mat,math.dist(p,q)*sides*r*r*math.sin(2*math.pi/sides)/2,[r,math.dist(p,q)]))
    def bolt(self,*a,**k): pass # Hardware excluded from masses, retained in source.
    def drilled_plate(self,*a,**k): pass
    def commit(self,name,parent=None,bevel=0):
        records.append({'name':name,'parent':parent.name if parent else None,'parts':self.parts})
        return Node(name)
def empty(name,parent=None,location=(0,0,0)): return Node(name)
def main():
    source=SOURCE.read_text(); tree=ast.parse(source)
    defs=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {'tower','joint','yard'}]
    env={'Geo':Geo,'empty':empty,'setup':lambda:None,'material':lambda *a:None,'math':math}
    exec(compile(ast.Module(body=defs,type_ignores=[]),str(SOURCE),'exec'),env)
    site=env['tower']()
    structural=[r for r in records if r['name']=='StructuralSteel']
    beams=sum(sum(p[0]=='beam' for p in r['parts']) for r in structural)
    decks=[r for r in records if r['name']=='FloorCassettes']
    facade=[r for r in records if r['name']=='FacadeModules']
    cores=[r for r in records if r['name'].startswith('CoreModule_')]
    core_parts=[p for p in cores[0]['parts'] if p[1]=='Concrete']
    panels=[p for p in core_parts if p[3][2]>.6]
    xbeam=next(p for p in structural[0]['parts'] if p[0]=='beam' and abs(p[3][-1]-5.58)<1e-8)
    ybeam=next(p for p in structural[0]['parts'] if p[0]=='beam' and p[3][0]==.42)
    lower_col=next(p for p in structural[0]['parts'] if p[0]=='beam' and abs(p[3][-1]-3.6)<1e-8)
    upper_col=next(p for p in structural[-1]['parts'] if p[0]=='beam' and abs(p[3][-1]-3.6)<1e-8)
    climb=json.loads((PROD/'physics/climb-prototype/nominal-metrics.json').read_text())
    work=json.loads((PROD/'physics/mujoco/nominal-validation.json').read_text())
    column_count=sum(sum(p[0]=='beam' and abs(p[3][-1]-3.6)<1e-8 for p in r['parts']) for r in structural)
    brace_count=sum(sum(p[0]=='tube' for p in r['parts']) for r in records if r['name'] in {'StructuralSteel','TemporaryYBraces'})
    full_decks=max(sum(p[1]=='Deck' for p in r['parts']) for r in decks)*site['storeys']
    full_facade=max(sum(p[1]=='Glass' for p in r['parts']) for r in facade)*site['storeys']
    counts={'columns':column_count,'horizontal_beams':beams-column_count+1,'braces':brace_count,'floor_cassettes':full_decks,'facade_modules':full_facade,'core_wall_panels_including_lintel':len(panels)*20,'stair_flights_and_landings_assumed_modules':80}
    lifts=sum(counts.values())
    scenarios=[]
    for days in [1,3,7,14]:
        available=days*10*3600*.65
        takt=available/lifts
        scenarios.append({'target_calendar_days':days,'hours_per_day':10,'productive_utilization':.65,'available_productive_seconds':available,'required_lift_takt_seconds':takt,'parallel_crane_lower_bound_at_180s':math.ceil(lifts*180/available),'parallel_crane_lower_bound_at_300s':math.ceil(lifts*300/available),'robot_lower_bound_beam_end_work_only':max(2,math.ceil(2*1160*work['durationSeconds']/available)),'warning':'Robot bound omits all non-beam work, horizontal travel, battery, tool changes and safety separation.'})
    mass={'steel_density_assumption_kg_m3':7850,'concrete_density_assumption_kg_m3':2400,'beam_x_profile_kg':xbeam[2]*7850,'beam_y_profile_kg':ybeam[2]*7850,'lower_column_profile_kg':lower_col[2]*7850,'upper_column_profile_kg':upper_col[2]*7850,'core_panel_concrete_only_kg':[p[2]*2400 for p in panels],'deck_solid_geometry_volume_m3':5.89**2*.09,'deck_mass_at_assumed_2400kg_m3':5.89**2*.09*2400,'mass_caveat':'Profile masses exclude connectors/coatings; panels exclude frames/inserts; Deck material has no declared density or engineered layup, so its mass is a conditional solid-slab proxy.'}
    output={'status':'analytical planning only; no whole-building simulation','source_sha256':hashlib.sha256(source.encode()).hexdigest(),'geometry_source':str(SOURCE.relative_to(PROD.parent)),'actual_authored_geometry':{'storeys':site['storeys'],'height_m':72,'footprint_m2':864,'grid_nodes_per_floor':35,'columns':column_count,'horizontal_beams_installed':beams-column_count,'lifted_active_beam':1,'floor_cassettes':sum(sum(p[0]=='box' and p[1]=='Deck' for p in r['parts']) for r in decks),'facade_modules':sum(sum(p[0]=='box' and p[1]=='Glass' for p in r['parts']) for r in facade),'core_storeys':len(cores),'core_wall_panels_including_lintel':len(cores)*len(panels),'yard_beams':36,'yard_decks':12},'hypothetical_completed_20_storey_catalogue':counts,'assumed_individual_crane_lifts':lifts,'payloads':mass,'simulation_evidence':{'climb_seconds_per_3_6m':climb['durationSeconds'],'climb_mean_m_s':climb['chassisAdvanceM']/climb['durationSeconds'],'20_storey_ascent_extrapolated_minutes':20*climb['durationSeconds']/60,'local_beam_episode_seconds':work['durationSeconds'],'local_episode_complete_fastened_cycle':work['completeFastenedCycle'],'all_horizontal_beam_local_episodes_serial_hours':1160*work['durationSeconds']/3600,'climb_warning':'One storey tested on ideal rail locks; twenty-storey ascent is arithmetic extrapolation, not tested.'},'scenarios':scenarios,'single_crane_days_at_10h_and_65percent_utilization':{str(c):lifts*c/(10*3600*.65) for c in [24,180,300]},'crane_cycle_assumptions':{'180_seconds':'optimistic complete pick, travel, set, release and empty return; unvalidated','300_seconds':'sensitivity case; unvalidated','24_seconds':'invalid as complete crane cycle: local prepositioned beam simulation only'},'crane_geometry_constraints':{'crane_center_xy_m':[24,-12],'illustrated_max_long_jib_radius_m':45,'furthest_building_corner_radius_m':math.hypot(42,24),'furthest_staged_beam_endpoint_radius_m':math.hypot(38,37.6),'note':'Illustrated jib reaches x=-21 from x=24: 45m. Even if slewing is assumed, furthest building corner and beam-yard endpoint exceed this radius. No capacity chart, slew or full-site travel simulation exists.'},'robot_climb_amortization':{'beam_tasks_per_storey':58,'one_pair_one_climb_per_storey_then_58_local_episodes_seconds':58*work['durationSeconds']+climb['durationSeconds'],'robot_lower_bound_24s_takt_one_climb_per_task':2*math.ceil((work['durationSeconds']+climb['durationSeconds'])/24),'note':'20 robots assumes ten pairs cycling through one climb per beam task; batching tasks per floor can reduce this overhead. Neither lateral transfer nor coordinated multi-robot construction is tested.'},'excluded_scope':['foundation and crane erection','rail installation and horizontal robot transfer','manufacturing and inbound delivery','rigging and inspection','complete mechanical fastening','MEP, envelope sealing, roof, fire protection, fit-out','weather, clashes, permits, certification, fault recovery'],'checks':{'structural_beam_primitives_equal_1859':beams==1859,'deck_count_equal_286':sum(sum(p[1]=='Deck' for p in r['parts']) for r in decks)==286,'core_panels_per_storey_equal_9':len(panels)==9}}
    assert all(output['checks'].values()),output['checks']
    (HERE/'throughput-study.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'lifts':lifts,'actual':output['actual_authored_geometry'],'days':output['single_crane_days_at_10h_and_65percent_utilization'],'payloads':mass},indent=2))
if __name__=='__main__': main()
