def p(g):
 for k in 2,3:
  p=[(d,j)for d in range(13)for j in range(13)if g[d][j]==k]
  for s in p:
   i,f=s
   if(m:=sorted((n,d,j)for d in range(-2,3)for j in range(-2,3)if 0<=i+d<13>f+j>=0<(n:=g[i+d][f+j])!=k))[2:]:e=s;l=m[len(m)//2][0];break
  for s in p:
   i,f=s
   for n,d,j in m:
    if n==l:g[i+d][f+j*(k-2 or s==e or-1)]=l
 return g