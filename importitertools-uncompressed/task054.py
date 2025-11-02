def p(m):
 p=m[0][0];l=min(m[9][8:10]);z=[(f,e)for e,u in enumerate(m)for f,n in enumerate(u)if p!=n!=l==u[f+1]!=(a:=n)];(f,e),*a,(t,n)=[(f,e)for e,u in enumerate(m)for f,n in enumerate(u)if{n}-{p,l,a}];l=f+t>>1;i=e+n>>1
 for e in-1,0,1:
  for f in-1,0,1:
   for t,n in z:
    r=m[i+e][l+f]
    while(f|e)*(p-r):
     t+=f;n+=e;m[n][t]=r
     if(m[n+e][t+f]!=p!=m[i+e+e][l+f+f])<1:r=p
 for u in m[i-2:i+3]:u[l-2:l+3]=[p]*5
 return m