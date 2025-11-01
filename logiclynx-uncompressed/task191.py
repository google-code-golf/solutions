def p(f):
 t=23;p=bytes(sum(f,[]));r=p.find(1);e=p.rfind(1);u=[(*[f&4for f in f[r%t+1:e%t]],)for f in f[r//t+1:e//t]]
 for r in range(4):
  for r in range(t*t):
   e=r%t;r//=t
   [(*[f&4for f in f[e:e+len(u[0])]],)for f in f[r:r+len(u)]]in(u,u[::-1])and[exec('f[r]=1')for f in f[r-(r>0):r-~len(u)]for r in range(t)if-2<r-e<=len(u[0])>f[r]]
  u=[*zip(*u[::-1])]
 return f