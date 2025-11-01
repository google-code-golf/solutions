def p(g):
 for s in range(-2,8):
  for r in range(-2,8):
   for c in range(-2,8):
    for d in range(-2,8):
     if min(g[s+i][r+j]^g[c+i][d+j]for j in range(3)for i in range(3)):
      return[[g[s+i][r+j]^g[c+i][d+j]for j in range(3)]for i in range(3)]
