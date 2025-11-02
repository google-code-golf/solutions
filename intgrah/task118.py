def p(m):
	n=lambda t,e:[t and(n(t[1:],e)or not e&t[0]and n(t[1:],e|t[0])),e][{(e,d)for e in range(len(m))for d in range(len(m[0]))if m[e][d]&2}<=e]
	for d in 2,3:
		if e:=n([e for n in range(len(m))for t in range(len(m[0]))for e in[{(e,d)for e in range(-d,d+1)for e,d in[(e+n,t),(n,e+t)]if len(m)>e>-1<d<len(m[0])}]if min(m[e][d]for e,d in e)&2],set()):
			for e,d in e:m[e][d]+=(m[e][d]&1)*3
			return m