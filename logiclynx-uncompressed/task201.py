def p(e):
 r=l=13
 u=1
 for t,o in enumerate(e):
  for n,o in enumerate(o):
   if o==4:
    if u:j,i=t,n;u=0
    p,m=t,n
 u=[o[i:m+1]for o in e[j:p+1]]
 for t,o in enumerate(e):
  for n,o in enumerate(o):
   if t-j|p-t|n-i|m-n<0<o:
    if t<r:r=t
    if n<l:l,f=n,o!=u[1][0]
 for t,o in enumerate(u[1:-1]):o[1:-1]=e[r+t][l:l+m-i-1][::1-2*f]
 return u