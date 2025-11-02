def p(n):
 a=min(sum(n,[]),key=sum(n,[]).count);d,u=[(e,m)for e,m in enumerate(n)for m,l in enumerate(m)if l==a][0];p=[(e,m)for e,m in enumerate(n)for m,l in enumerate(m)if l==0];f,c=min(p);e,m=map(max,*p);o=m-c+(n[f][c]<1)
 for l in 1,2,3,4:
  for e,m in p:
   e+=((f+e<d*2)*2-1)*l*o;m+=((c+m<u*2)*2-1)*l*o
   if len(n)>e>-1<m<len(n[0]):n[e][m]=a
 return n