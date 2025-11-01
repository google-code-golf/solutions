def p(g):
 f=[]
 for t in range(len(g)):
  for n in range(len(g[0])):
   p=0
   for r in range(t+1,len(g)+1):
    for s in range(n+1,len(g[0])+1):
     if len({*sum(s:=[r[n:s]for r in g[t:r]],[0])})*all(map(sum,s+[*zip(*s)]))>4:q=s;p=len(q);e=len(q[0])
   if p:f+=q,
   for r in range(p):g[t+r][n:n+e]=[0]*e
 for q in f:
  for r in range(8):
   p=len(q);e=len(q[0])
   for t in range(len(g)+1-p):
    for n in range(len(g[0])+1-e):
     if all((str(q).count(str(f:=q[r//e][r%e]))<2)*f==g[t+r//e][n+r%e]for r in range(p*e)):
      for r in range(p):g[t+r][n:n+e]=q[r]
   q=[*zip(*q[::-1])];r^3or q.reverse()
 return g
