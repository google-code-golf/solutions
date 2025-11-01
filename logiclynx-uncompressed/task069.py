def p(g):
 g=sum(g,[]);r=range(100);p=[i for i in r if g[i]%8];h=g*1
 for i in r:
  for j in(h[i]==8)*p:h[i+j-p[0]]=g[j];h[j]=0
 return*zip(*[iter(h)]*10),