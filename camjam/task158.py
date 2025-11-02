def p(f,e=0):
	n=max((len(set(str([r[u:u+3]for r in f[r:r+3]]))),[r[u:u+3]for r in f[r:r+3]])for r in range(23)for u in range(23))[1]
	x=n
	x=[r for r in zip(*x)for s in range(e)]
	x=[r for r in zip(*x)for s in range(e)]
	for r in range(23):
		for u in range(23):
			for s in range(e*3*([r[u:u+3*e]for r in f[r:r+3*e]]==[[[e,sorted(f[0])[8]][e in n[1]]for e in r]for r in x])):f[r+s][u:u+3*e]=x[s]
	x=[*zip(*x[::-1])]
	for r in range(23):
		for u in range(23):
			for s in range(e*3*([r[u:u+3*e]for r in f[r:r+3*e]]==[[[e,sorted(f[0])[8]][e in n[1]]for e in r]for r in x])):f[r+s][u:u+3*e]=x[s]
	x=[*zip(*x[::-1])]
	for r in range(23):
		for u in range(23):
			for s in range(e*3*([r[u:u+3*e]for r in f[r:r+3*e]]==[[[e,sorted(f[0])[8]][e in n[1]]for e in r]for r in x])):f[r+s][u:u+3*e]=x[s]
	x=[*zip(*x[::-1])]
	for r in range(23):
		for u in range(23):
			for s in range(e*3*([r[u:u+3*e]for r in f[r:r+3*e]]==[[[e,sorted(f[0])[8]][e in n[1]]for e in r]for r in x])):f[r+s][u:u+3*e]=x[s]
	return f