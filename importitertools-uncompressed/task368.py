e=enumerate
def p(g):
 a=[(x,y,v)for y,r in e(g)for x,v in e(r)if~v%5<4];X,Y,_=a[0]
 for y,r in e(g):
  for x,v in e(r):
   for q,r,s in(v==5)*a:g[y+r-Y][x+q-X]=s
 return g