def p(g):
 j=g[k:=9].index(c:=max(g[k]))-2
 while j<8:
  j+=2;g[k:=~k][j+(j<9)]=5
  for r in g:r[j]=c
 return g