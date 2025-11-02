def p(g):
	O=[];t=o=j=C=0
	for*r,c in zip(*g,[*zip(*g)][1:]+[()]):
		if 5in r:o+=t*(j-(j:=r.index(5)));t=~t
		C=max({*r,*c}-{5})or C;O+=any(r)*[[C*(v>0)for v in r[o:]+r[:o]]]
	return[*zip(*O)]