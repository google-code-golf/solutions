def p(g):
 e=enumerate;(u,*_,a),v,w=zip(*((i,b,c)for i,r in e(g)for b,c in e(r)if c));m=max(v)
 for r in g[u+1:a]:r[c:=min(v)+1]=r[m-1]=k=w[3]
 g[u+1][c:m]=r[c:m]=[k]*(m-c);return g