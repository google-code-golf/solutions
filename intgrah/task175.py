R=range(21)
p=lambda m:[[m[y][x]|m[x][y]or m[0][x!=y]for x in R]for y in R]