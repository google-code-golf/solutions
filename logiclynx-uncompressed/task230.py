def p(g,u=1,e=enumerate):
 for r,a in e(g,-1):
  for c,v in e(a):
   if v>4:v=g[r][c]%3;g[r+v][c-u]=v+u%3;u=-u
 return g