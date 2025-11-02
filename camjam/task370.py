def p(q):
 *x,(c,b,i)=sorted((q[b][i],b,i)for b in range(len(q))for i in range(len(q[0]))if q[b][i]-q[0][0])
 e=x[(b>x[0][1])-1][1]
 h=[len(q[0])-1-q[e][::-1].index(0),q[e].index(0)][i>x[0][2]]
 for s in range(1,5):
  for _,p,k in x:
   if len(q)>p+(b-e)*s>-1<k+(i-h)*s<len(q[0]):q[p+(b-e)*s][k+(i-h)*s]=c
 return q
