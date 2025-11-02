R=range(400)
def p(m):
	for k in R:
		z=3^k>>6;i=k//8%8;j=k%8
		if all(all(r[j:j+z])for r in m[i:i+z]):break
	for k in R:
		try:y=k//10%10;m[i-j+k%10][i+j+z+~y]|=m[y][k%10]
		except:0
	return m