def p(k):
 import re;i=sum(k,[]);c=i.count;a=max(i,key=c);r=[]
 for n in{*i}-{a}:
  i=str(n);m=1|2*(c(n)>1);p=m,n,m
  for m in range(112):o=m//28+2;t=m%7+1;p=any(re.search(i*o+f"[^{i}]"*t+i,str(n)[1::3])for n in k)and(2*o+t,n,o)or p;k=[*map(list,zip(*k[::-1]))]
  r+=p,
 j=max(r)[0];k=[[a]*j for m in range(j)]
 for r,n,o in r:
  for m in range(o):k[i:=j-r>>1][i+m]=k[i+m][i]=n
  k=[*map(list,zip(*k[::-1]))]
  for m in range(o):k[i:=j-r>>1][i+m]=k[i+m][i]=n
  k=[*map(list,zip(*k[::-1]))]
  for m in range(o):k[i:=j-r>>1][i+m]=k[i+m][i]=n
  k=[*map(list,zip(*k[::-1]))]
  for m in range(o):k[i:=j-r>>1][i+m]=k[i+m][i]=n
  k=[*map(list,zip(*k[::-1]))]
 return k