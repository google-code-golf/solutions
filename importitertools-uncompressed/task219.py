def p(m):
 f,*r=[],
 for e,a in enumerate(m):
  if max(a)<1and r:f+={*r},;r=[]
  for d,a in enumerate(a):r+=[(d,e)]*a
 for i in f:
  for d,e in max([{(d+m,e-min(f[0])[1]+min(i)[1])for d,e in f[0]}for m in(2,1,0,-1)],key=i.__and__):
   if 0<d<10:m[e][d]+=m[e][d]<1
 return m