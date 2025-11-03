def	p(i):
	e=i
	for	o	in	e*4:e=[[*o]for	o	in	zip(*e[~4:])if{*o}-{0,4}];i=[[*o]for	o	in	zip(*i[(4in	i[-1])-2::-1])]
	for	o,f	in	enumerate(i):
		if[0for	t,f	in	enumerate(i)for	a,f	in	enumerate(o*f)for	r,f	in	enumerate(o*all(i	in[0,((e+20*[[]])[(r-t)//o]+20*[4])[(n-a)//o]]for	r,i	in	enumerate(i)for	n,i	in	enumerate(i))*e)for	n,f	in	enumerate(o*f)for	i[r+t][n+a]in[e[r//o][n//o]]]:return	i
# ----------------------------------------------------------------
# compression: auto
# oxjam
