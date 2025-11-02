def p(m):
	for k in 1,2:
		y,x=divmod(sum(m,[]).index(k),10)
		while-1<y<10>x>=0:m[y][x]=k;y+=2*k-3;x+=2*k-3
	return m