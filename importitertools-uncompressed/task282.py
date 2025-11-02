R=range(9)
p=lambda g:[[max(g[y-i//3*8%15][x-i**3%9]>>-14**i%~57%4for i in R)for x in R]for y in R]