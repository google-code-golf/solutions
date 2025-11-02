def p(m):
	i,e=[p for p,n in enumerate(m)if 4in n]
	f,r=[p for p,n in enumerate(zip(*m))if 4in n]
	f=[n[f:r+1]for n in m[i:e+1]]
	n=m[e+1:]
	n=[n for n in zip(*n)if any(n)]
	n=[n for n in zip(*n)if any(n)]
	for p in range(23):
		e=n
		e=[n for n in zip(*e)for r in range(p)]
		e=[n for n in zip(*e)for r in range(p)]
		for p in range(23):
			for r in range(23):
				if sum(sum(n)for n in f)==sum(sum(n)for n in[n[r:r+len(e[0])]for n in f[p:p+len(e)]])+16 and all(r in [n,0] for n,r in zip(e,[n[r:r+len(e[0])]for n in f[p:p+len(e)]])for n,r in zip(n,r)):
					for n in f[p:p+len(e)]:n[r:r+len(e[0])]=e[0];e.pop(0)
					return f