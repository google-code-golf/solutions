def p(g):
 for i in range(25):x,y=[[*map(any,a)].index(1)for a in(g,zip(*g))];j=i%5;i//=5;g[x+i][y+j]|=g[x+4-i][y+4-j]|g[x+j][y+4-i]|g[x+4-j][y+i]
 return g