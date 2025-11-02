def p(c,*e):
 for o,u in enumerate(c):
  for h,n in enumerate(u):
   l=b=1
   while u[h:h+l]==[n]*l:l+=1
   while[u[h]for u in c[o:o+b]]==[n]*b:b+=1
   e+=[[n and min(sum(c,[]),key=sum(c,[]).count)for n in u[h:h+l-1]]for u in c[o:o+b-1]],
 return max(e)