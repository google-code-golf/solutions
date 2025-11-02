def p(t):
	e,n,r,o=min([((o:=[t[n+p][r+a]for p in range(3)for a in range(3)]).count(0),n,r,o)for n in range(19)for r in range(19)])
	for u in range(-4,6,4):
		for e in range(-4,6,4):
			for m in range(1,19):
				for p in range(3):
					for a in range(3):
						if u|e!=0<=r+e*m+a<21>n+u*m+p>=0:t[n+u*m+p][r+e*m+a]=o[p*3+a]and max(t[u+n+p][e+r+a]for p in range(3)for a in range(3))
	return t