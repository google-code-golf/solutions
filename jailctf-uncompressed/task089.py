def p(r,**x):
 for p in range(13):
  for n in range(13):
   if(i:=max(r[p+f][n+e]for f in range(-1,2)for e in range(-1,2)if p+f in range(13)!=n+e in range(13)!=f|e!=0)):x[r[p][n]]=[(p-f,n-e,i)for f in range(13)for e in range(13)if r[f][e]==i]
 for p in range(13):
  for n in range(13):
   if(i:=max(r[p+f][n+e]for f in range(-1,2)for e in range(-1,2)if p+f in range(13)!=n+e in range(13)!=f|e!=0))<1:
    for f,e,i in x[r[p][n]]*r[p][n]:r[p-f][n-e*(2*r[p][n]-5)]=i
 return r