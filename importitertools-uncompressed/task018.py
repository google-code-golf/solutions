def p(l):
	v=eval(str(l))
	def f(g,e,h,i):
		if len(l)>e>-1<g<len(l[0])>0<v[e][g]:v[e][g]=0;i+=(l[e][g],g,e),;[f(g+t,e+q,h,i)for t in[-1,0,1]for q in[-1,0,1]]
	u=[]
	for e,g in enumerate(l):
		for g,h in enumerate(g):f(g,e,h,i:=[]);u+=len(i)//5*[i]
	for d in u:
		for h,g,e in d:l[e][g]=0
	v=eval(str(l))
	for d in u:
		for t in range(-18,38):
			for q in range(-18,38):
				for g in[[(h,[0,g,e][u]*i+t,[0,e,g][u]*m+q)for h,g,e in d]for i in[1,-1]for m in[1,-1]for u in[1,-1]]:
					for h,g,e in(sum(len(l)>e>-1<g<len(l[0])>h==v[e][g]for h,g,e in g)==3)*g:l[e][g]=h
	return l