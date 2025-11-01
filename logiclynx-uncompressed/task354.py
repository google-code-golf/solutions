def p(g):
 for r in g:
  while 5in r:a=r.index(5);r[a]=max(r[a-1:a]+g[0][a:],key=bool)
 return g