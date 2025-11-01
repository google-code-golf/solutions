def p(g):
 m=len(g);f=len(g[0])
 def p(r,o):
  w=[(r,o,g[r][o])];g[r][o]=0
  for r,o in(r+1,o),(r,o+1),(r-1,o),(r,o-1):
   if f>o>-1<r<m>g[r][o]>0:w+=p(r,o)
  return w
 m=[p(r,o)for r in range(m)for o in range(f)if g[r][o]]
 d=min((len(m)<3,len(m),m)for m in m)[2];h,f,e=min((sum(v==m[2]for r,o,v in d),m)for m in d)[1]
 for m in m:
  w=[(r,o)for r,o,v in m if v==e]
  for r,o,v in d:
   for i,p in w:g[(r-h)*int(len(w)**.5)+i][(o-f)*int(len(w)**.5)+p]=(min(v for r,o,v in m if v^e),e)[v==e]
 return g