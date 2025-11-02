def p(e):
 g=[h for h in zip(*[h for h in zip(*e)if 1in h])if 1in h]
 for u,h in enumerate(e):
  for d,h in enumerate(h):
   for p in[0,1]*4:
    g=p*[*zip(*g)]or g[::-1]
    if all((0<p+u<24>i+d>0<e[p+u-1][i+d-1])==h//3for p,h in enumerate(g)for i,h in enumerate(h)):
     for p,h in enumerate(g):
      for i,h in enumerate(h):
       if 0<p+u<24>i+d>0:e[p+u-1][i+d-1]=h
 return e