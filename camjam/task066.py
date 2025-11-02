def p(r):
	s,n=divmod(sum(r,[]).index(2),len(r))
	i,u=divmod(sum(r,[]).index(3),len(r))
	if r[s][n+1]!=2:
		r=[*map(list,zip(*r))]
		r=p(r)
		r=[*map(list,zip(*r))]
		return r
	if 8in r[i][u:]:
		o=u+r[i][u:].index(8)-1
		if(r[s+1][o]+r[s-1][o])*~-any([*zip(*r)][o][min(s,i):max(s,i)]):
			for l in r[min(s,i):max(s,i)]:l[o]=3
			for l in range(min(n,o),max(n,o)+1):r[s][l]=r[s][l]or 3
			for l in range(min(o,u),max(o,u)+1):r[i][l]=3
			return r
	if 8:
		o=u-r[i][u::-1].index(8)+1
		if(r[s+1][o]+r[s-1][o])*~-any([*zip(*r)][o][min(s,i):max(s,i)]):
			for l in r[min(s,i):max(s,i)]:l[o]=3
			for l in range(min(n,o),max(n,o)+1):r[s][l]=r[s][l]or 3
			for l in range(min(o,u),max(o,u)+1):r[i][l]=3
			return r