def p(e):
 i=max(sum(e,[]),key=sum(e,[]).count);m=[n for n in sum(e,[])if f"{i}, {n}, {i}"not in str(e+[*zip(*e)])][0];k=[[[i,m][n==m]for n in n[::2]]for n in e[::2]];p=[n*2for n in e*2]
 for t,n in enumerate(p):
  for r,n in enumerate(n):
   for f in sum(e,[]):
    if[[[i,m][n==f]for n in n[r:r+len(k[0])]]for n in p[t:t+len(k)]]==k:return[[[i,f][n==f]for n in t]for t in zip(*[[[i,f][n==f]for n in t]for t in zip(*e)if f in t])if f in t]