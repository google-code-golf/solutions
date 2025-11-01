def p(n):
 for e,f,u,p,o in[(e,f,u,n[e+1][f+1],2-(n[e+3][f]<1))for e,r in enumerate(n)for f,u in enumerate(r)if u>n[e-1][f]+r[f-1]<1]:
  for i in range(-o,o+o+2):
   for r in range(o+2):n[e+i][f+r]=u
  for i in range(o+2):
   for r in range(-o,o+o+2):n[e+i][f+r]=u
  for i in range(o+2):
   for r in range(o+2):n[e+i][f+r]=p
  for i in range(1,o+1):
   for r in range(1,o+1):n[e+i][f+r]=u
 return n