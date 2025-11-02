def p(g):
 s=sum(g,[]);i=s.index(1);r,c=divmod(i+s.index(1,i+1)>>1,len(g[0]))
 for k in-1,0,1:g[r][c+k]=g[r+k][c]=3
 return g