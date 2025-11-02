def p(i):
 l=1+min(f for f in range(len(i))if i[0][0]!=i[0][f])
 for u in range(l,len(i),l):
  for f in range(l,len(i),l):
   if i[u-l][f]==i[u][f-l]>0:return[[o[n]or((len(o)>n-l>-1and o[n-l])==i[u][f]or(len(o)>n+l>-1and o[n+l])==i[u][f])*i[u][f-l]or((len(o)>n-l>-1and o[n-l])==i[u][f-l]and not(len(o)>n-l*2>-1and o[n-l*2])or(len(o)>n+l>-1and o[n+l])==i[u][f-l]and not(len(o)>n+l*2>-1and o[n+l*2]))*i[u-l][f-l]for n in range(len(o))]for o in zip(*[[o[n]or((len(o)>n-l>-1and o[n-l])==i[u][f]or(len(o)>n+l>-1and o[n+l])==i[u][f])*i[u][f-l]or((len(o)>n-l>-1and o[n-l])==i[u][f-l]and not(len(o)>n-l*2>-1and o[n-l*2])or(len(o)>n+l>-1and o[n+l])==i[u][f-l]and not(len(o)>n+l*2>-1and o[n+l*2]))*i[u-l][f-l]for n in range(len(o))]for o in zip(*i)])]