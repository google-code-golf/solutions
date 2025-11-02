E=enumerate
def p(m,*P):
	for k in 8,1:
		for y,r in E(m):
			for x,v in E(r):
				if v%k:P+=(y,x,v),;r[x]=0;i,j,_=P[0]
				for Y,X,c in(k<8==v)*P:m[y+Y-i][x+X-j]=c
	return m
