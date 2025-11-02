def p(i,o=0):
 for e in range(len(i)):
  for n in range(len(i[e])):
   r=[[n,e]]
   for p,g in r:r+=[[n+p,g+e]for e in range(-1,2)for n in range(-1,2)if[*[*i,[0]*62][g+e],0][n+p]>([n+p,g+e]in r)*9+o]
   if i[e][n]>1in(i[g][p]for p,g in r):f=[[-n+p,g-e]for p,g in r];o=1
 for e in range(len(i)):
  for n in range(len(i[e])):
   r=[[n,e]]
   for p,g in r:r+=[[n+p,g+e]for e in range(-1,2)for n in range(-1,2)if[*[*i,[0]*62][g+e],0][n+p]>([n+p,g+e]in r)*9+o]
   if i[e][n]==2:
    for p,g in f:i[len(r)**8%62%7*g+e][len(r)**8%62%7*p+n]|=len(r)**8%62%7*p+n>-1
 for e in range(len(i)):
  for n in range(len(i[e])):i[e][n]=i[e][n]**8%62%7
 return i