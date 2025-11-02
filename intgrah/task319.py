def p(p):
	r=max(sum(p,[]),key=sum(p,[]).count)
	n=[f for f in sum(p,[])if f"{r}, {f}, {r}"not in str(p+[*zip(*p)])][0]
	o=[[[r,n][f==n]for f in f[::2]]for f in p[::2]]
	m=[f*2for f in p*2]
	for s,f in enumerate(m):
		for e,f in enumerate(f):
			for t in{*sum(p,[])}:
				if o==[[[r,n][f==t]for f in f[e:e+len(o[0])]]for f in m[s:s+len(o)]]:
					f=p
					f=[[[r,t][f==t]for f in s]for s in zip(*f)if t in s]
					f=[[[r,t][f==t]for f in s]for s in zip(*f)if t in s]
					return f