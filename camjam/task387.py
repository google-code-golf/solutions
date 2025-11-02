def p(o):
	(r,p),*e,(e,u)=m=[(e,a)for e,r in enumerate(o)for a,f in enumerate(r)if f]
	for m,(e,a)in enumerate(m):
		for i in-1,0,1:
			for f in-1,0,1:
				if i|f:o[e+i][a+f]=o[r][[u,p,p,u][m]]
	for f in range(2,e-r>>1|1,2):o[r+f][p]=o[r+f][u]=o[e-f][p]=o[e-f][u]=5
	for f in range(2,u-p>>1|1,2):o[r][p+f]=o[r][u-f]=o[e][p+f]=o[e][u-f]=5
	return o