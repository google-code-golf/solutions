def p(k):
 for b in range(19):
  for i in range(19):
   if all(sum(k[b+e][i+a]for a in range(3))for e in range(3))and all(sum(k[b+e][i+a]for e in range(3))for a in range(3)):
    for o in range(3):
     for u in range(3):
      q,s=b,i
      for e in range(3):
       for e in range(3):
        q+=o*4-4;s+=u*4-4
        for e in range(3):
         for a in range(3):
          if k[b+e][i+a]and-1<q+e<21and-1<s+a<21:k[q+e][s+a]=max(k[b+o*4-4+e][i+u*4-4+a]for e in range(3)for a in range(3))
    return k