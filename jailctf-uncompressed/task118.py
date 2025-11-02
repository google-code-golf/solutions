def p(e):
 def p(e,f,q=0):
  o=e*1
  if q==len(e)-s*f:return('2,'not in str(e))*e
  for t in{t for n in range(-f,f+1)for t in(q+n,q+n*s)if t%s-q%s<5}:o[t]+=o[t]-2.
  return p(e,f,q+1)or min(o)>=0and p(o,f,q+1)
 s=len(e[0]);e=sum(e,[]);return*zip(*[iter(p(e,2)or p(e,3))]*s),