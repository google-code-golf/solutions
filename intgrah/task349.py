def p(i):
	for m in range(len(i)):
		for f in range(len(i)):
			for n in range((len(i)-f)//2+1):
				if{*i[m][f:f+n*2]}=={9}:
					for e in i[max(0,m-n):m+n+1]:e[max(0,f-n):f+n*3]=map(max,e[max(0,f-n):f+n*3],[3]*len(i))
					for e in i[m:]:e[f:f+n*2]=map(max,e[f:f+n*2],[1]*len(i))
	return i