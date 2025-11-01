def p(g):
 b=sum(g,[]);I=b.index;j=0
 for v in b:g[j//10][j%10]-=v;g[(j+I(1)-I(v or 1))//10][j%10]+=v;j+=1
 return g