def p(n):
 e=sum(n,[]);n=e[:];f={};o={}
 for i,p in enumerate(n):
  if p-5:
   q=[i];n[i]=5;r=1>p;t=0,
   for m in q:
    for m in m-1,m+1,m-10,m+10:
     if n[m:m+1]==[p]:n[m]=5;q+=m,;t+=m-i,
     r*=n[m:m+1]==[5]
   if r:f[t]=i
   if e.count(p)==len(t)>1:o[t]=i,p
 for t in o:
  if t in f:
   i,p=o[t]
   for m in t:e[i+m],e[f[t]+m]=0,p
 return*zip(*[iter(e)]*10),