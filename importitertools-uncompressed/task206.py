f=filter
def p(g):x,y=divmod(sum(g,[]).index(5),len(g[0]));g[x][y]=0;g[x-1][s:=slice(y-1,y+2)],g[x][s],g[x+1][s]=zip(*f(any,zip(*f(any,g))));return g