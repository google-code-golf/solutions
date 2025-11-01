def p(e):
 q=eval(str(e));n=2;p=range
 while 1:
  b,f,h,n=max((sum((-6,0,3,0,0,0)[q[f+n][h]]+(n and 0<=h+n<len(q[0]) and(-6,0,3,0,0,0)[q[f][h+n]])for n in p(-n,n+1))-n,f,h,n)for n in p(n,4)for f in p(n,len(q)-n)for h in p(len(q[0])))
  if b<3:return e
  for n in p(-n,n+1):
   q[f+n][h]//=5;e[f+n][h]+=q[f+n][h]*3;q[f][h+n]//=5;e[f][h+n]+=q[f][h+n]*3