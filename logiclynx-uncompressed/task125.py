def p(g):
 for i in range(6**6):t,u=g[x:=i//135%-15][y:=i//9%-15],g[x+i%9//3-1][y+i%3-1];g[x][y]-=(5*(t>u>5)-4*(u-t==4),~t&4)[i<2e3]
 return g