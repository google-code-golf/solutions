def p(g):
 for k in-1,1:
  r,i=divmod(sum(g,[]).index(k%3),10)
  while~r*~i%11:g[r][i]=k%3;r-=k;i-=k
 return g