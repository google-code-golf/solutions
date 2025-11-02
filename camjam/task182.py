def p(n):
	for e in range(14):
		for v in range(14):
			for j in range(16):
				for r in range(16):
					if(sum(5==n[e+f][v+j]for f in range(7)for j in range(7))==24)*all([f>0for f in n[e+1+f][v+1:v+6]]==n[j+f][r:r+5]for f in range(5)):
						for f in range(5):n[j+f][r:r+5]=n[e+1+f][v+1:v+6]
	return n