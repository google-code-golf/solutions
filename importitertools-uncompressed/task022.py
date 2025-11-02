R=range(10);F=-1,0,1
p=lambda g:[[max(g[i+x][j+y]*(g[i][j]==5)for i in R for j in R)for y in F]for x in F]