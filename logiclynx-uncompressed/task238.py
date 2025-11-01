def p(r):
 n=min(u for u,r in enumerate(r)for f,d in enumerate(r)if d==8)
 m=min(f for u,r in enumerate(r)for f,d in enumerate(r)if d==8)
 d=[(e:=u-n,f-m)for u,r in enumerate(r)for f,d in enumerate(r)if d==8]
 n=min(u for u,r in enumerate(r)for f,d in enumerate(r)if d%8)
 m=min(f for u,r in enumerate(r)for f,d in enumerate(r)if d%8)
 r=[r[m:m+e+3]for r in r[n:n+e+3]]
 for u,f in d:r[u+1][f+1]=(u-f)*(u+f-e)and(r[-1][1],r[1][0],r[1][-1],r[0][1])[(u<f)*2+(u+f<e)]or 8
 return r