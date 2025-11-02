def p(m,y=0):
	for r in m:y-=1;m[y]=[8]*len(r);m[y][~abs(~y%(2*(w:=len(r)-1))-w)]=1
	return m