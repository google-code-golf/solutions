def p(m):
 l=eval(str(m));f=[]
 def p(i,u):
  if len(m)>u>-1<i<len(m[0])>0<l[u][i]:l[u][i]=0;f[:0]=(m[u][i],i,u),;p(i-1,u);p(i+1,u);p(i,u-1);p(i,u+1)
 [p(i,u)for u in range(len(m))for i in range(len(m[0]))if m[u][i]%2];s,e=min((i,u)for p,i,u in f if p>1)
 for l in 3,2,1:
  for n in range(len(m)):
   for t in range(len(m[0])):
    if all(m[u][i]>>1==p>>1if len(m)>u>-1<i<len(m[0])else p==1for p,i,u in[(p,t+(i-s)*l+m,n+(u-e)*l+f)for p,i,u in f for m in range(l)for f in range(l)]):
     for p,i,u in[(p,t+(i-s)*l+m,n+(u-e)*l+f)for p,i,u in f for m in range(l)for f in range(l)]:
      if len(m)>u>-1<i<len(m[0]):m[u][i]=-p
 return[[-p for p in f]for f in m]