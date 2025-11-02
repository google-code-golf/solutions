def p(r):
 a=r[0],;w=3-any(r[2])>>any(r[1])
 while any(r[w]):a+=r[w],;w+=1
 for l in 0,1,2,-1:
  for w in range(16-len(a)):
   for y in range(2+(l<0),10):
    for f in range(len(a)):
     for g in range(10):
      if l+g in range(10)!=r[w+f][l+g]!=a[f][g]:y*=g>=y
      if l+g in range(10)!=r[w+f][l+g]!=0:y*=g<y
    for f in range(len(a)):
     for g in range(10):
      if l+g in range(10)!=r[w+f][l+g]!=a[f][g]>0<y:r[w+f][l+g]=1
 return r