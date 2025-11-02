def p(p,g=range,o=1):
	i=len(p)
	for a in g(4):
		n=[(a,t)for a in g(i)for t in g(i)if p[a][t]];t,n=zip(*n);t,r,f,u=min(t),max(t),min(n),max(n);a=p[t][f];n=p[t].count(a)
		if n<p[r].count(a)*o:
			n,m=f+n//2,u-n//2
			o=0
			for a in g(r):p[a][n:m+1]=[4]*(m-n+1)
			for a in g(t+1,r):p[a][f+1:u]=[4]*(u-f-1)
			for u in g(t+1):
				a=t-u
				if n>=u:p[a][n-u]=4
				if m+u<i:p[a][m+u]=4
		*p,=map(list,zip(*p[::-1]))
	return p