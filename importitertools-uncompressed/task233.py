def p(e,*f):
 for u,n in enumerate(e):
  for z,n in enumerate(n):
   i=[i[z:z+3]for i in e[u:u+3]]
   if(sum(sum(i,[]))!=18)*all(sum(i,[])):
    f=i,*f
    for n in(0,1,2):e[u+n][z:z+3]=[0]*3
 e=[n for*n,in zip(*e)if sum(n)]
 e=[n for*n,in zip(*e)if sum(n)]
 for i in f:
  for n in(f:=1,0,1,2):
   for u,n in enumerate(e,-2):
    for z,n in enumerate(n,-2):
     if f*all(e[u+n][z+f]>>1==(i[n][f]!=2)for n in(0,1,2)for f in(0,1,2)):
      for n in(0,1,2):e[u+n][z:z+3]=i[n];f=0
   i=[*zip(*i[::-1])]
 return e