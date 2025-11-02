def p(s):
 c=eval(str(s));t=[]
 def f(r,o,n,e):
  if len(s)>o>-1<r<len(s[0])>0<c[o][r]:c[o][r]=0;e+=(s[o][r],r,o),;[f(r+j,o+l,n,e)for j in(-1,0,1)for l in(-1,0,1)]
 for o,e in enumerate(s):
  for r,n in enumerate(e):f(r,o,n,e:=[]);t+=[e]*bool(e and n)
 for e in[[(n,[0,r,o][l]*s+f,[0,o,r][l]*j+e)for n,r,o in max(t,key=len)]for e in range(-12,26)for f in range(-12,26)for s in(-1,0,1)for j in(-1,0,1)for l in(-1,0,1)]:
  for n in t:
   for n,r,o in(set(n)<set(e))*e:s[o][r]=n
 return s