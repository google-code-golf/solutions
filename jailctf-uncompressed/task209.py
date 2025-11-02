def p(z,e=-99):
 def p(z,e=-99):return z*e or p([[*p]for p in zip(*z[any(z[-1])-2::-1])],e+1)
 e=-4-(2in z[-5]);q= p(z[e:]);z= p(z[:e])
 for e in range(len(z)):
  for p in range(len(z)-e*len(q)+1):
   for o in range(len(z[0])-e*len(q[0])+1):
    if sum((z[p+r][o+n] in [q[r//e][n//e]])*z[p+r][o+n]for r in range(e*len(q))for n in range(e*len(q[0])))+17>sum(sum(z,[0])):[[1for z[p+r][o+n] in [q[r//e][n//e]]]for r in range(e*len(q))for n in range(e*len(q[0]))];return z