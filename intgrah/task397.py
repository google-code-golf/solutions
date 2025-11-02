R=range(9)
def p(m):
	for y in R:
		for x in R:
			for r in m[y+2:][:len(J:={*m[y][x:x+2]+m[y+1][x:x+2]})*(not{0,3}&J)]:r[x:x+2]=3,3
	return m