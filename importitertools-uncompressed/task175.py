R=range(21)
p=lambda g:[[g[y][x]|g[x][y]or g[0][x!=y]for x in R]for y in R]