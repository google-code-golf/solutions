p=lambda g,d=8,s=0:d and p([*zip(*(g,[[c,*[0]*(s:=s+(c==2)),*g[0][1:]]for c,*v in g])[g[1>s]>g[1]])][::1|-(d%4>0)],d-1)or g
# ----------------------------------------------------------------
# theoreticalsyntaxgolfers
