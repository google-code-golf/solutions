r=0,1,2
p=lambda m:[[max(m[d//9+i][d%9+j]for d in range(81)if m[d//9+1][d%9+1]==5)for j in r]for i in r]