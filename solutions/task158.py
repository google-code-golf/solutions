def	p(r):
	n,s=max((len({*str(m:=[n[o:o+3]for	n	in	r[n:n+3]])}),m)for	n	in	range(len(r))for	o	in	range(len(r[-1])))
	for	m	in	range(len(r[-1])):
		for	n	in	range(len(r)-m*3):
			for	o	in	range(len(r[-1])-m*3):
				for	p	in	range(len(r[-1])):
					for	p	in	range(m*3*all(r[n+p][o+q]==s[p//m][q//m]or	r[n+p][o+q]==r[-1][-1]!=s[p//m][q//m]==max({*s[1]}-{r[-1][-1]})for	p	in	range(m*3)for	q	in	range(m*3))):
						for	q	in	range(m*3):r[n+p][o+q]=s[p//m][q//m]
					s=*zip(*s[::-1]),
	return	r
# ----------------------------------------------------------------
# compression: auto
# oxjam
