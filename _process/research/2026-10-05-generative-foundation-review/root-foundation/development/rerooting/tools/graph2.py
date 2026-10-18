import sys,json
sys.path.insert(0,sys.argv[1])
sys.dont_write_bytecode=True
import check_becoming as cb
idx=cb.module_index()
order=cb.closure(idx)
imp={n:cb.imports_of(idx[n][0].read_bytes()) for n in order}
L={k:getattr(cb,k) for k in ['FOUNDATION','CORE','BRIDGE','PERIPHERY_JOINS','PURE']}
json.dump({'layers':L,'imports':imp,'paths':{n:str(idx[n][0].relative_to(cb.LEAN_ROOT)) for n in order}},open(sys.argv[2],'w'),indent=1)
print(len(order))
