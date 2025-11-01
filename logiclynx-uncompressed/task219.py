def p(l):
 e=[*map(any,l)];f=e.index(1);i=e.index(0,f);a=i-f
 while i<14:
  i+=1;p=a+1
  if e[i]:
   while e[i]:i+=1;p-=1
   for g in range(9):
    w=g%p+i-a;r=t=w>l[1][3]>a*3>l[7][7]>l[1][4]
    for d in range(100):k=d%10;m=d%9%a;l[12][d%6+4]|=d%2<r;t|=l[w+m][k]>1>l[f+m][k-g//p]<=k-g//p;l[w+m][k]|=l[f+m][k-g//p]>1>t==l[w+m][k]<=k-g//p<50<d
    if~-t:break
 return l
