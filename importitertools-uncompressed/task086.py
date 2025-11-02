def p(e):
 for z in range(len(e)):
  for r in range(len(e)):
   for l in 1,2:
    if 0<e[z][r]!=e[z-1][r]==e[z][r-1]==e[z][r+l]:
     for t in range(l+2):
      for s in range(l):e[z-1+t][r-s-2]=e[z-1+t][r+l-~s]=e[z-2-s][r-1+t]=e[z+l-~s][r-1+t]=e[z][r]
 return[[s and sum({*max(e)})-s for s in s]for s in e]