R=range(10)
p=lambda m:[[m[i][j]or 2*m[(m[:3]!=[*map(list,zip(*m))][:-4:-1])+~j][i]for j in R]for i in R]