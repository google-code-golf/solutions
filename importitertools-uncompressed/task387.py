def p(g):
	o=g
	for i in[2,4,2]*4:
		for r,t,u in zip(g:=[*zip(*g[::-1])],o:=[*map(list,zip(*o[::-1]))],o[1:]):
			for x,c in enumerate(r):
				if c:u[x]=u[x+1]=sum(max(g))-c;[t*2,t][any(r[x+i*2:])][x+i]=5
	return o