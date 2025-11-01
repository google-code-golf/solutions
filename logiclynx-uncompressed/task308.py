def p(n):
 q=~-len(n)//5;o=q+-~q;o=[[g:=max(n[0],key=n[0].count)]*o for j in[0]*o];e=[0]*20
 for r,f in enumerate(n):
  for j,f in enumerate(f):
   if f^g:e[f]+=r;e[~f]+=j
 for r,f in enumerate(n):
  for j,f in enumerate(f):
   if f^g:o[q+r-e[f]//4][q+j-e[~f]//4]=f
 return o