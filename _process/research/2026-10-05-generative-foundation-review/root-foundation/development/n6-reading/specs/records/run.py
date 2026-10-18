"""Write edits/records-NN.txt from every specs/records/rNN_*.py (N6)."""
import glob, importlib.util, os, sys
H = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(os.path.dirname(H))
sys.path.insert(0, D)
from gen_edits import gen_records
for f in sorted(glob.glob(H + '/r[0-9]*.py')):
    spec = importlib.util.spec_from_file_location('m', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    recs = [m.REC] if hasattr(m, 'REC') else m.RECS
    name = os.path.basename(f)[:3]
    gen_records(D + '/edits/records-' + name[1:] + '.txt', (m.__doc__ or '').strip().split('\n')[0], recs)
