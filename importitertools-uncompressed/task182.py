def p(p):
 for i in range(14):
  for j in range(14):
   if all(p[i+f][j+r]for f in(0,6)for r in range(7)):q=i+1;g=j+1
 for i in range(16):
  for j in range(16):
   if all((p[i+f][j+r]>0)==(p[q+f][g+r]>0)for f in range(5)for r in range(5)):
    for f in range(5):p[i+f][j:j+5]=p[q+f][g:g+5]
 return p