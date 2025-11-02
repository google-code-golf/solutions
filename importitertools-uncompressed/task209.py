def p(g):
 r,n=[z for z,i in enumerate(g)if 4in i];x,u=[z for z,i in enumerate(g[r])if i];t=[z for z,i in enumerate(g)if sum(i)*(z>n)][0];m=[z for z,i in enumerate(g)if sum(i)*(z>n)][-1];p,*z,i=[z for z,i in enumerate(zip(*g[t:]))if sum(i)];a,y=m-t+1,i-p+1;*z,m,z,i=max((sum(g[z+k][i+a]==g[t+k//m][p+a//m]>0for k in range(a*m)for a in range(y*m)),-m,z,i)for m in range(5)for z in range(r,n-a*m+2)for i in range(x,u-y*m+2));m=-m
 for k in range(a*m):
  for a in range(y*m):g[z+k][i+a]=g[t+k//m][p+a//m]
 return[i[x:u+1]for i in g[r:n+1]]