def p(f):
 for o in range(len(f)):
  for e in range(len(f[o])):
   r=[[o,e]]
   for i,a in r:r+=[[i+o,a+e]for o in range(-1,2)for e in range(-1,2)if i+o in range(len(f))!=a+e in range(len(f[o]))!=f[i+o][a+e]>([i+o,a+e]in r)*9]
   r=[[f[i][a],i-o,a-e]for i,a in r]
   for l in f[o][e]%2*(-1,-1,-1,1)*2:
    f=[[*l]for l in zip(*f)][::l]
    for o in range(len(f)):
     for e in range(len(f[o])):
      for n,i,a in r*all(n%2or i+o in range(len(f))!=a+e in range(len(f[o]))!=f[i+o][a+e]==n for n,i,a in r):f[i+o][a+e]=n
 return f