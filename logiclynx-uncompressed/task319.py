def p(u):
 *n,o=sorted({*sum(u,[])},key=sum(u,[]).count)
 def f(r,t=u):
  while r not in t[0]:t=t[1:]
  t=[*zip(*t[::-1])]
  while r not in t[0]:t=t[1:]
  t=[*zip(*t[::-1])]
  while r not in t[0]:t=t[1:]
  t=[*zip(*t[::-1])]
  while r not in t[0]:t=t[1:]
  t=[*zip(*t[::-1])]
  return [[[o,r][t==r]for t in t]for t in t]
 return next(f(r)for r in n for e in n for u in range(len(f(r)[0])*2-len(f(e)[0])+1)for a in range(len(f(r))*2-len(f(e))+1)if(r-e)*all(f(r)[a+n>>1][u+t>>1]==[o,r][f(e)[n][t]==e]for t in range(len(f(e)[0]))for n in range(len(f(e)))))