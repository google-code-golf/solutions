e=enumerate
def p(g,*P):
 for v in-1,8:
  for i,r in e(g):
   for j,d in e(r):
    if v*d%8:P or(a:=i,b:=j);P+=[i-a,j-b,d],;r[j]=0
    for y,x,s in(d==v>0)*P:g[i+y][j+x]=s
 return g