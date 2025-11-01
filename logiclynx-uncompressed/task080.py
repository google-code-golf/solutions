def p(s,l=range,n=0):
 while 0in s[n]:n+=1
 a=n+1;m=len(s)//a+1;i=max(([s[a*(f+u//3-1)][a*(x+u%3-1)]for u in l(9)]for f in l(1,m-1)for x in l(1,m-1)),key=sum)
 for f in l(m):
  for x in l(m):
   for u in l(9):
    for r in l(n*n*(m>=f+u//3>0)*(m>=x+u%3>0)*(i[4]==s[a*f][a*x])):s[a*(f+u//3-1)+r//n][a*(x+u%3-1)+r%n]=i[u]
 return s