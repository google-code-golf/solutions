def p(a,u=1):
 for c in range(10):
  if len(m:=[(p,n)for p,a in enumerate(a)for n,l in enumerate(a)if l==c])==4:
   l,r=map(min,*m);p,i=map(max,*m);u=max(u,p-l+1)
 n=[[max(a[0],key=a[0].count)for c in range(u)]for c in range(u)]
 for c in range(10):
  if len(m:=[(p,n)for p,a in enumerate(a)for n,l in enumerate(a)if l==c])==4:
   l,r=map(min,*m);p,i=map(max,*m)
   for x,m in m:n[2*x-l-p+u-1>>1][2*m-r-i+u-1>>1]=c
 return n