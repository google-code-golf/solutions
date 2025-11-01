def p(g):
 w=len(g);f=sum(g,[]);k=b=0
 while(f[k+~w]*f[k-w+1]==f[k+w-1]*f[k-~w]>0)<1:k-=1
 for v in f:
  if v:m=2*k-b;r=g[m//w+w];r[b%w]=r[m%w]=g[b//w][m%w]=v
  b+=1
 return g