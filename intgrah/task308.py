def p(u,d=3):
	try:
		r=[d*[sorted(u[0])[3]]for e in[0]*d]
		for o in{*sum(u,[])}-{sorted(u[0])[3]}:
			e=[divmod(m,len(u[0]))[::-1]for m,d in enumerate(sum(u,[]))if d==o]
			for n,m in e:r[(d-e[0][1]-e[-1][1])//2+m][n+(d-min(e)[0]-max(e)[0])//2]=o
		return r
	except:return p(u,d+2)