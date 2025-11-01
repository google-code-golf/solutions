def p(l):
 for i in range(26):
  for n in range(26):
   t=[l[i+e//5][n+e%5]for e in range(25)]
   if t==t[::-1]and len(set(t))>2:
    for e in range(25):l[i+e//5][n+e%5]=t[0]
    for i,n in[(i,n)for i in range(26)for n in range(26)if l[i+2][n+2]==t[12]]:
     for e in -1,1:
      h,f=i+2,n+2;r=t[12+10*e]
      while r!=t[0]!=l[h][f]:l[h][f]=r;h+=e
     for e in -1,1:
      h,f=i+2,n+2;r=t[12+2*e]
      while r!=t[0]!=l[h][f]:l[h][f]=r;f+=e
     for e in range(25):
      if t[e]!=t[0]!=l[i+e//5][n+e%5]:l[i+e//5][n+e%5]=t[e]
    return l