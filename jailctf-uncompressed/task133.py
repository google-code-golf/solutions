def p(f):
 for e in range(len(f)):
  for n in range(len(f[e])):
   r=[[n,e]]
   for g,h in r:r+=[[g+n,h+e]for e in range(-1,2)for n in range(-1,2)if h+e in range(len(f))!=g+n in range(len(f[e]))!=f[h+e][g+n]>([g+n,h+e]in r)*9]
   i=[f[e][n]for n,e in r]
   if f[e][n]>=i.count(f[e][n])<2<len(i):m=[[g-n,h-e]for g,h in r][1:];q=f[e][n]
 for e in range(len(f)):
  for n in range(len(f[e])):
   r=[[n,e]]
   for g,h in r:r+=[[g+n,h+e]for e in range(-1,2)for n in range(-1,2)if h+e in range(len(f))!=g+n in range(len(f[e]))!=f[h+e][g+n]>([g+n,h+e]in r)*9]
   i=[f[e][n]for n,e in r]
   if f[e][n]==q:
    for g,h in m:f[969//i.count(f[e][n])%8*h+e][969//i.count(f[e][n])%8*g+n]=min({*i}-{q})
 return f