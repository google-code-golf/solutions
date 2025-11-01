def p(g):
 a=sum(g,[]);k=a.index(8);j=0;c=10
 for v in a:g[j//c][j%c]-=v;g[k//c+(j>k)][k%c+(j%c>k%c)]+=v&v%~7;j+=1
 return g