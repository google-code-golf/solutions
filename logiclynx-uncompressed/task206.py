def p(g):
 e=enumerate;h=[(i,j)for i,r in e(g)for j,v in e(r)if(v-5or(s:=i,t:=j))*-v];a,b=map(min,*h)
 for i,j in h:g[i+s+~a][j+t+~b]=g[i][j]
 return g