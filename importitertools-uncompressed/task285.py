o=(0,0),(0,1),(1,0),(1,1)
def p(n):
 t=eval(str(n))
 def e(r,f,m,o):
  if f<len(n)>r>0<t[f][r]==m:t[f][r]=0;o+=(f,r),;[e(r+a,f+i,m,o)for a in[-1,0,1]for i in[-1,0,1]]
 for i,r in enumerate(n):
  for a,m in enumerate(r):
   if len({n[i-u][a-m]for u,m in o})>3:
    for u,m in o:
     e(a-m,i-u,n[i-u][a-m],p:=[])
     for d,j in o:
      for f,r in p:n[[f,i*2+~f][j^u]][[r,a*2+~r][d^m]]=n[i-j][a-d]
 return n