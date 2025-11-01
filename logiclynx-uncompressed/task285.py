def p(r):
 o=[i[:]for i in r];i=len(r)
 for k in range(i):
  for e in range(i):
   if d:=o[k][e]:
    o[k][e]=0;a=[(k,e)]
    for n,j in a:
     for t in-1,0,1:
      for u in-1,0,1:
       if f:=o[(n+t)%i][(j+u)%i]:
        if f==d:o[(n+t)%i][(j+u)%i]=0;a+=((n+t)%i,(j+u)%i),
    for n,j in a:
     for t in-1,0,1:
      for u in-1,0,1:
       if f:=o[(n+t)%i][(j+u)%i]:
        if t*u==0:k,e=n,j
    for n,j in a:
     for t in-1,0,1:
      for u in-1,0,1:
       if f:=o[(k+t)%i][(e+u)%i]:r[(n,2*k+t-n)[t&1]][(j,2*e+u-j)[u&1]]=f
    o[k][e]=d
 return r