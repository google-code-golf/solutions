r=range(100)
def p(g):
 g=sum(g,[]);a=[i for i in r if g[i]%5]
 for i in r:
  for s in(g[i]==5)*a:g[i+s-a[0]]=g[s]
 return*zip(*[iter(g)]*10),