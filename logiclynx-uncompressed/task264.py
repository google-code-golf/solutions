R=range(9);p=lambda g:[[{(*map(5 .__eq__,u[1::2]),):u for r in zip(g,g[1:],g[2:])for u in zip(*(r[i//3][i%3:]for i in R)) if min(u)}[r>2,c>2,c<6,r<6][r*3%9+c%3]for c in R]for r in R]
