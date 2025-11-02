def p(i):
 for e in range(len(i)):
  for l in range(len(i)):
   d=0
   while l+d in range(len(i))and i[e][l+d]>8:d+=1
   for r in i[max(0,e-d//2):e+d//2+1]:
    for a in range(len(i))[max(0,l-d//2):-max(-l-d//2*3,-len(i))]:r[a]=r[a]or 3
 return[[a[e]or 9in a[:e]for a in zip(*i)]for e in range(len(i))]