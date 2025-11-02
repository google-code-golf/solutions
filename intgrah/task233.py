def p(p,**f):
	for o in range(len(p)-2):
		for m in range(len(p[0])-2):
			d=[p[o+e//3][m+e%3]for e in range(9)]
			if len(r:={*d})==2and 0 not in r and 2 in r:
				d=tuple(e==2for e in d)
				r={d:sum(r)-2}
				for e in range(4):f[d]=r;d=tuple(d[e%3*3+2-e//3]for e in range(9))
				for e in range(9):p[o+e//3][m+e%3]=0
	p=[r for*r,in zip(*p)if any(r)]
	p=[r for*r,in zip(*p)if any(r)]
	for c in range(2):
		for o in range(len(p)-2):
			for m in range(len(p[0])-2):
				d=[p[o+e//3][m+e%3]for e in range(9)]
				d=tuple(e==0for e in d)
				r=f.get(d)
				if r and(c or d in r):
					r=r.popitem()[1]
					for e in range(9):p[o+e//3][m+e%3]=[r,2][d[e]]
	return p