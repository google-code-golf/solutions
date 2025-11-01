def p(g,x=0,y=9):
 while y*g[y][x]:a=g[y-1][x]>4;g[y:=y-1+a][x:=x+a]=2
 x>7or p(g,x+1);return g