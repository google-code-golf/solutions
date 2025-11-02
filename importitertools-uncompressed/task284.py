def p(e):
 for t in e*4:
  e=[[t for t in e]for e in zip(*e[::-1])];(i,u,f),*t,(r,m,t)=[(r,m,t)for r,t in enumerate(e)for m,t in enumerate(t)if t];r=i+r>>1
  for t in e[i:r]*(u==m):t[u]=f;e[r-1][u-2:u+3]=[f]*5;e[r][u-2:u+3:4]=[f]*2
 return e