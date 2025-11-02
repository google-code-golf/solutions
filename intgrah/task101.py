def p(r,*m):
	p=[divmod(sum(r,[]).index(1),len(r[0]))]
	for n,o in p:
		if 0<=o<len(r[0])>0<=n<len(r)>0<r[n][o]!=(n,o)not in m:m+=(n,o),;p+=(n-1,o),(n+1,o),(n,o-1),(n,o+1)
	o,a=zip(*m)
	p=[d[min(a):max(a)+1]for d in r[min(o):max(o)+1]]
	for n in range(1,4):
		a=p
		a=[d for d in zip(*a)for p in range(n)]
		a=[d for d in zip(*a)for p in range(n)]
		for n in range(len(r)-len(a)+1):
			for o in range(-2,len(r[0])-len(a[0])+1):
				for d in range(len(a[0])*all((n+e,o+d)not in m!=r[n+e][o+d]&2==a[e][d]&2for d in range(len(a[0]))for e in range(len(a)))):
					for e in range(len(a)):
						if 0<=o+d:r[n+e][o+d]=a[e][d]
	return r