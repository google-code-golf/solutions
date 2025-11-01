def p(g):
 f=sum(g,[]);c=f.count;a,x=divmod(f.index(k:=min(f,key=c)),21);w=-g[a].count(k);h=c(k)//2-~w;i=j=0
 while sum(sum(R[j+1:~w+j],i^a|j^x<1)for R in g[i+1:i+h]):j+=1;j%=22+w;i+=j<1
 while~h:g[i+h][j:j-w]=g[a+h][x:x-w];h-=1
 return g