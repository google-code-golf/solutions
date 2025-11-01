def p(o):
 n=len(o);(a,r),(c,d)=[(e,b)for e in range(n)for b in range(n)if o[e][b]&1]
 def f(a,r,c,d,s):
  if n>(e:=a+c)>-1<(b:=r+d)<n:
   if o[e][b]==2:return o[e][b]
   if o[e][b]-8 and f(e,b,c,d,abs(s)):o[e][b]=3;return o[e][b]
   if s>0<o[e][b]-7:return f(a,r,d,-c,s-1)or f(a,r,-d,c,s-1)
 f(a,r,a-c,r-d,-2)or f(c,d,c-a,d-r,-2)
 return o