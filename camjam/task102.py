def p(q):
 for s in range(5):
  for y in range(12):
   for x in range(12):
    if(sum(sum(r[x:x+s])for r in q[y:y+s])==0)*(sum(sum(r[x-1:x+s+1])for r in q[y-1:y+s+1])/20==s+1):
     for a in range(s*s):q[y+a//s][x+a%s]=2
 return q