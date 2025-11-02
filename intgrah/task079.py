p=lambda g:max(m:=[s for i in range(144)if min(map(max,(s:=[r[i%12:][:3]for r in g[i//12:][:3]])+[*zip(*s)]))],key=m.count)
