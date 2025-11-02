def p(g):
 for x in range(81):
  y=x//9;x%=9
  for r in g[-y:][:all(v:=g[8-y][x:x+2]+g[~y][x:x+2])*len({*v})]:r[x:x+2]=3,3
 return g