def p(f):
 for r,t in enumerate(f):
  for u,e in enumerate(t):
   if 0<e==f[r-2][u-2]==f[r-2][u]==f[r][u-2]:s,l=u-1,r-1
 for r,t in enumerate(f):
  for u,e in enumerate(t):
   if e:f[l*2-r][u]=f[l*2-r][s*2-u]=t[s*2-u]=e
 return f