def	p(f):
	for*i,in[[]]*8:
		f=[i[::-1]for*i,in	zip(*f)]
		for	n,o	in	enumerate(f):
			for	t,o	in	enumerate(o):
				if	o:
					u={(n,t)}
					for	r	in*i,:
						if{(~-n,t),(n,~-t),(~-n,~-t),(~-n,-~t)}&r:i.remove(r);u|=r
					i+=[u]
		for	n,o	in	enumerate(f):
			for	t,o	in	enumerate(o):
				for	r	in*i,:
					for	u,e	in	r:
						if{(u-t,e-~n),(u-~t,e-n)}&r:f[u-t][e-n]|=len({*str([i[e:e+2]for*i,in	f[u:u+2]])})//8*f[u][e]
	return	f