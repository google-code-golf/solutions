def p(n):
 e=sum(n,[]);a=e[e.count(e[0])<3];*s,=zip(*n);t={}
 for i,r in enumerate(n):
  for l,m in enumerate(r):
   if e.count(m)<3:s+=i+l,i-l-60;t[a in r and a in s[l]]=m
 for i,r in enumerate(n):
  for l,m in enumerate(r):
   if i+l in s or i-l-60 in s:r[l]=t[a in r and a in s[l]]
 return n