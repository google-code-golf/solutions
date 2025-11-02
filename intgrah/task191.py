def p(u):
	u=[[0,*r,0]for r in zip(*u)]
	u=[[0,*r,0]for r in zip(*u)]
	i=u
	i=[[*r]for r in zip(*i)if 1in r]
	i=[[*r]for r in zip(*i)if 1in r]
	for i in[i:=[[*r]for r in zip(*i[::-1])],i:=[[*r]for r in zip(*i[::-1])],i:=[[*r]for r in zip(*i[::-1])],i:=[[*r]for r in zip(*i[::-1])],i:=i[::-1],i:=[[*r]for r in zip(*i[::-1])]]:
		for e in range(23):
			for n in range(23):
				if i==[[r or 1for r in r[n:n+len(i[0])]]for r in u[e:e+len(i)]]:
					for f,r in zip(i,u[e:e+len(i)]):r[n:n+len(i[0])]=f
	u=[r[1:-1]for r in zip(*u)]
	u=[r[1:-1]for r in zip(*u)]
	return u