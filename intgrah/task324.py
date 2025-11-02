def p(t):
	e=len(t[0])
	p=sum(t,[])
	i,n,f,s=sorted({*p},key=p.count)
	r=p.index(i)
	a=[p[l+u]for l,u in[(r,1),(r,-1),(r+e,0),(r-e,0)]if e>r%e+u>=0<=l<e*len(t)].count
	for d,o in[*enumerate(p)]:
		for l,u in(e,1),(e,-1),(-e,-1),(-e,1):
			r=d
			m=d%e
			while o in[i,n]and e>m>=0<=r<e*len(t):
				if p[r]==f:p[r]=[n,i][a(f)>a(s)]
				if p[r]==s:p[r]=[i,n][a(f)>a(s)]
				r+=l+u
				m+=u
	return[*zip(*e*[iter(p)])]