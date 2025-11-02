z=enumerate
def p(m):
	e=[(i,e)for i,r in z(m)for e,r in z(r)if r==8]
	a,f=zip(*e)
	r=max(f)-min(f)
	n=[[r for*i,r in zip(*m,r)if{*i}-{0,8}]for r in m if{*r}-{0,8}]
	for i,e in e:
		i-=min(a);e-=min(f)
		n[i+1][e+1]=[[[n[1][-1],n[0][1]],[n[-1][1],n[1][0]]][e<i][e<r-i],8][e in{i,r-i}]
	return n