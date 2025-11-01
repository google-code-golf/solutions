def p(n):
 (a,u,r),(a,g,t),(f,u,p),(f,g,p)=e=[(p,u,g)for p,u in enumerate(n)for u,g in enumerate(u)if g]
 for p in range(u,g+1):n[a][p]=n[f][p]=5-min(p-u,g-p)%2*5
 for p in range(a,f+1):n[p][u]=n[p][g]=5-min(p-a,f-p)%2*5
 for p,u,g in e:n[p][u-1:u+2]=n[p-1][u-1:u+2]=n[p+1][u-1:u+2]=[r^t^g]*3;n[p][u]=g
 return n