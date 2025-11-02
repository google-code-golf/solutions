def p(i,*a):
	e=sum(i,[])
	f=e.index(4)
	e=168-e[::-1].index(4)
	for n in i[f//13:e//13+1]:a+=n[f%13:e%13+1],;n[f%13]=n[e%13]=0
	for n,e in zip(a[1:],filter(max,zip(*filter(max,zip(*i))))):n[1:-1]=e[::(n[0]==max(e[:len(e)//2]))*2-1]
	return a