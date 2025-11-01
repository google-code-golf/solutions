def p(g,r=range(9)):
 def f(i,j,c=1):
  if-1<i<10>j>=0<g[i][j]!=c:g[i][j]=c;return-~sum(f(i+s//3-1,j+s%3-1,c)or-0for s in r)
 f(*min((f(i,j)or 17,i,j)for i in r for j in r)[1:],2);return g