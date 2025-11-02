def p(m,a=-3):
	h=len(m)//2
	for i in range(h+1):
		if m[-2][h-i]<1:m[a][h-i]=m[a][h+i]=m[-1][h];a-=1
	return m