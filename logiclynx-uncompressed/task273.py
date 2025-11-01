def p(g):
 d=c=0
 for r in g:
  try:i=r.index;d^=i(4,c:=i(4)+1)-c
  except:r[c:c+d]=d*[2]
 return g