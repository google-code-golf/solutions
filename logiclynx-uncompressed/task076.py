def p(p):
 s=len(p);l=len(p[0]);f=[divmod(sum(p,[]).index(3),l)]
 for n,e in f:f+=[(u,r)for u in range(n-1,n+2)for r in range(e-1,e+2)if s>u>-1<r<l>p[u][r]>((u,r)in f)<1]
 r,m=zip(*f);f=[r[min(m):max(m)+1]for r in p[min(r):max(r)+1]]
 for m in range(8):
  for n in range(s-len(f)+1):
   for e in range(l-len(f[0])+1):
    if all(f[u][r]&1or p[n+u][e+r]==f[u][r]for u in range(len(f))for r in range(len(f[0]))):
     for u in range(len(f)):p[n+u][e:e+len(f[0])]=f[u]
  f=[*zip(*f[::-1])]
  if m==3:f=f[::-1]
 return p
