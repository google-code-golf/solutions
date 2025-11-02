R=range(10)
p=lambda g:[[g[y][x]or 8*all(any(t[:x]>[0]*9<t[x+1:]for t in a)for a in(g[:y],g[y+1:]))for x in R]for y in R]