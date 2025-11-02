def p(t):
	i=sum(t,[])
	*w,t,n=sorted({*i},key=i.count)
	r=[p for p in range(900)if n!=i[p]!=t==i[p-30]]
	o=[p for p in range(900)if i[p]==i[r[0]]!=i[p-1]!=n!=i[p+1]and{p}-{*r}][0]
	for p in r:
		for t in(-1,1,30,29,31,-30,-29,-31):
			if i[o+t]!=n:
				w=p+t
				i[w]=i[o+t]
				while i[w]!=n!=i[o+t*2]:i[w]=i[o+t];w+=t
	for u in range(5):
		for p in range(5):i[o-2+p+(u-2)*30]=n
	return[*zip(*[iter(i)]*30)]