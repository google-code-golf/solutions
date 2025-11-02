def p(i):
	for f in sum(i,[]):
		u=i
		u=[[5,*[[5,r][r==f]for r in r],5]for r in zip(*u)if f in r]
		u=[[5,*[[5,r][r==f]for r in r],5]for r in zip(*u)if f in r]
		u=[[5]*len(u[0])]+u+[[5]*len(u[0])]
		for r in range(10):
			for t in range(10):
				if[[r or f for r in r[t:t+len(u[0])]]for r in i[r:r+len(u)]]==u:
					for p in range(10):
						for l in range(10):
							if f==i[p][l]:i[p][l]=0
					for p in range(len(u)):i[r+p][t:t+len(u[0])]=u[p]
	return i