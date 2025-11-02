def p(r):
 for d in(u:=sum(r,[])):
  e=[(f%10,f//10)for f in range(100)if u[f]==d]
  for f in range(-7,7):
   for n in range(-7,7):
    for i,s in e*all((u,d)in e or s+f<9>i+n>r[s+f][i+n]<r[d+f][u+n]==5for i,s in e for u,d in[(i+1,s),(i-1,s),(i,s+1),(i,s-1)]):r[s][i],r[s+f][i+n]=0,d
 return r