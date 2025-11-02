def p(r):
	e=len(r)
	s=len(r[0])
	m,k,f=[],[],[]
	for p in [(t//s,t%s)for t in range(e*s)]:
		l,u=[],[]
		p=[p]
		for n,t in p:
			if s>t>=0<=n<e!=(n,t)not in f!=0<r[n][t]:f+=(n,t),;l+=n,;u+=t,;p+=(n-1,t),(n+1,t),(n,t-1),(n,t+1)
		if len(u)<4:m+=zip(l,u)
		else:
			t=[r[min(u):max(u)+1]for r in r[min(l):max(l)+1]]
			t=[*zip(*t)]
			k+=t,
			t=t[::-1]
			k+=t,
			t=[*zip(*t)]
			k+=t,
			t=t[::-1]
			k+=t,
			t=[*zip(*t)]
			k+=t,
			t=t[::-1]
			k+=t,
			t=[*zip(*t)]
			k+=t,
			t=t[::-1]
			k+=t,
	o=[s*[0]for r in r]
	for n,t in [(t//s,t%s)for t in range(e*s)]:
		for u in k:
			if sum(p+n<e>0<s>f+t and r[p+n][f+t]==u[p][f]!=(p+n,f+t)in m for p,f in [(t//len(u[0]),t%len(u[0]))for t in range(len(u[0])*len(u))])==3:
				for p,f in [(t//len(u[0]),t%len(u[0]))for t in range(len(u[0])*len(u))]:o[p+n][f+t]=u[p][f]
	return o