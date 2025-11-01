def p(r):
 for a in range(10,5,-1):
  for e in range(10,5,-1):
   for i in range(len(r)-a):
    for l in range(len(r[0])-e):
     d=[i[l:l+e]for i in r[i:i+a]]
     if len({i[l]for i in d for l in range(e)})<3:
      for i,l in[(i,l)for i in d for l in range(e)if i[l]-i[0]]:
       for a in d:a[l]=i[l]
       for a in range(e):i[a]=i[l]
      return d