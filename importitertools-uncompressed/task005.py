def p(r):
 f,q=max((l,n)for l in range(19)for n in range(19)if all(map(max,(z:=[z[n:n+3]for z in r[l:l+3]])+[*zip(*z)])))
 for o in-4,0,4:
  for p in-4,0,4:
   for z in range(1,4):
    for l in range(4):
     for n in range(4):
      if r[f+l][q+n]>0<21>f+o*z+l>-1<q+p*z+n<21:r[f+o*z+l][q+p*z+n]=max((r[f+o+z][q+p+l]for z in range(4)for l in range(4)))
 return r