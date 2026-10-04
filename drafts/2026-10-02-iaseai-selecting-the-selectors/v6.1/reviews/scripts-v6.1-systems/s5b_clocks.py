# S5b: E3 rerun with alpha_cor=0 so that the capture clock and the host clock are comparable.
import importlib.util, io, contextlib
spec=importlib.util.spec_from_file_location("s5","s5_joint2.py"); s5=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(s5)
print("E3'. alpha_cor=0 (QS capture ~23.5); host: rho=0.05, h_V=0.08, race share from 0.05 at rate 0.12")
print(f"   independent: {s5.E3('QS',None,acor=0.0,m_in=0.05)}")
for m,par in (('QS',None),('R',1.0),('R',0.1),('R',0.03),('GA',1.0)):
    print(f"   {m}{'' if par is None else '('+str(par)+')'}: {s5.E3(m,par,acor=0.0)}")
