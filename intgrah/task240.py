def p(m):
	for _ in'@'*8:m[1][5:11:2]=[m[1][3]]*3;m[3][7:11:2]=[m[3][5]]*2;m[5][9]=m[5][7];m=[[*map(max,r,s)]for*r,s in zip(*m,m[::-1])]
	return m