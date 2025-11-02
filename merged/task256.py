def p(g):
 b=sum(m:=max(g))//2+g.index(m)
 for r in g:r[:b]=[2+(r<m)-m[b]]*b;b-=b>0
 return g