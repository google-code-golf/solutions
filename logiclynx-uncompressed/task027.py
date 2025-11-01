def p(g,o=4):
 for t in range(89):
  if g[r:=t//9][t%9]:b=g[t%9];o%=b[-r]+2;b[~r+o]=2-b[~r+o]
 return g