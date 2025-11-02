def p(g):
 for M in range(289):
  x=slice(j:=M%17,j+2);r,s,*_=g[M//17:]
  if[2,0]!=r[j:-5]!=max(r[x]+s[x])<3:r[x]=s[x]=2,2
 return g