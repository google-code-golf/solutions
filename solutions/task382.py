p=lambda g,d=11,s=0:-d*g or p([*zip(*(g,[[c,*[0]*(s:=s+(c==2)),*g[0][1:]]for c,*v in g])[g[1>s]>g[1]])][::d%3-1|1],d-1)
# ----------------------------------------------------------------
# post-comp-diamond, base: theoreticalsyntaxgolfers
