def p(r):
	x=0
	n={1,2,3,4}
	for t in range(len(r)):
		for o in range(len(r[0])):
			for i in range(len(r)+1):
				for a in range(len(r[0])+1):
					d=[t[o:a]for t in r[t:i]]
					if len(sum(d,[]))<64 and all(map(any,d+[*zip(*d)]))and n&{*sum(d,[])}==n and sum(sum(d,[]))>x:
						x=sum(sum(d,[]))
						l=d
	d=[]
	l=[*zip(*l)]
	d+=l,
	l=l[::-1]
	d+=l,
	l=[*zip(*l)]
	d+=l,
	l=l[::-1]
	d+=l,
	l=[*zip(*l)]
	d+=l,
	l=l[::-1]
	d+=l,
	l=[*zip(*l)]
	d+=l,
	l=l[::-1]
	d+=l,
	for t in range(len(r)):
		for o in range(len(r[0])):
			for l in d:
				for i in range(len(l)*all(i+t<len(r)and a+o<len(r[0])and(r[i+t][a+o]==l[i][a]or l[i][a]%2)for i in range(len(l))for a in range(len(l[0])))):
					for a in range(len(l[0])):r[i+t][a+o]=l[i][a]
	return r