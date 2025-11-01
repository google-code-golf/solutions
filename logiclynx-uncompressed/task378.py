def p(g):
 for z in range((m:=~-len(g))*m):
  t=g[y:=z//m];d=g[y+1][z:=z%m]>0;d-=g[y-1][z]>0;e=t[z+1]>0;e-=t[z-1]>0
  if t[z]>g[a:=y+d][b:=z+e]:
   while m>y>0<z<m:g[y:=y-d][z:=z-e]=g[a+d][b+e]
 return g
