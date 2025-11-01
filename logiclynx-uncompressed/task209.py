def p(g):
 a=e=i=99;l=m=()
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v&4:
    b=y;d=x
    if a>y:a=y;c=x
   elif v>0<b>a:
    m+=(y,x,v),
    if e>y:e=y
    if i>x:i=x
   elif v:l+=(y,x,v),
 for k in range(1,5):
  for q in range(c,d):
   for p in range(a,b):
    try:
     for y,x,v in l:1/(v==g[e+(y-p)//k][i+(x-q)//k])
     for y,x,v in m:
       for r in range(k):
        for s in range(k):g[p+r+(y-e)*k][q+s+(x-i)*k]=v
     return[g[p][c:d+1]for p in range(a,b+1)]
    except:0