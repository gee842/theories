from math import ceil
for n in [1,2,4,8,16,32]:
  rows=[]
  for k in range(1,n+1):
    T=ceil(n/k)+2;C=3*n+(n+2*k)*T;q=4*n-2*k
    if T<=6 and q>=0 and max(8-T,0)*q>=C:
      rows.append((k,T,C))
  print(n,rows)
