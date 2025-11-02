def p(g):
 for _ in g*4:
  a,b,c,*_=filter(any,g:=[*zip(*g[::-1])]);i,j=map(g.index,(a,b))
  if{*a}=={0,8}:g[i:j+1]=b,*[c]*(j-i)
 return g