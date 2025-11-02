def p(o):
 for e in range(4):
  o=[[*e]for e in zip(*o[::-1])]
  for q in range(len(o)):
   for g in range(len(o[0])):
    if len({*sum(g:=[e[g:g+3]for e in o[q:q+3]],[])})*g==[[*e]for e in zip(*g)]*4:n=g
 for e in range(4):
  o=[[*e]for e in zip(*o[::-1])]
  for e in range(4):
   for q in range(len(o)-3*e+1):
    for g in range(len(o[0])-3*e+1):
     r=1
     for p in range(3*e*r):
      for f in range(3*e*r):r*=o[p+q][f+g]==[o[0][2],n[p//e][f//e]][p//e==f//e!=1]
     for p in range(3*e*r):
      for f in range(3*e*r):o[p+q][f+g]=n[p//e][f//e]
 return o