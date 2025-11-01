def p(g):
 w=len(g[0]);f=sum(g,[]).index
 for i in-w,-1,0,1,w:i+=f(1)+f(1,f(1)+1)>>1;g[i//w][i%w]=3
 return g