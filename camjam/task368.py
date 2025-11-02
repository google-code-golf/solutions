def p(q,R=range(100)):
 w=sum(q,[]);a=[m for m in R if w[m]%5]
 for m in R:
  for b in(w[m]==5)*a:w[m+b-a[0]]=w[b]
 return[*zip(*[iter(w)]*10)]
