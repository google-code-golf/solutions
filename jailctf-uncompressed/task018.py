def p(q):
 f=[]
 for o in range(len(q)):
  for p in range(len(q[o])):
   r=[[p,o]]
   for e,n in r:r+=[[p+e,o+n]for o in[1,-1,-0]for p in[1,-1,-0]if((q*2)[o+n]+[0]*9)[p+e]>([p+e,o+n]in r)*9]
   if r[3:]*q[o][p]:
    f+=[[q[n][e],-p+e,-o+n]for e,n in r],
    for e,n in r:q[n][e]=0
 for r in f:
  for o in[1,-1,-1,-1,1,-1,-1,-1]:
   q=[[*o]for o in zip(*q)][::o]
   for o in range(len(q)):
    for p in range(len(q[o])):
     for s,e,n in r*(len({s for s,e,n in r if((q*2)[o+n]+[0]*9)[p+e]-s})<2):q[o+n][p+e]=s;r=[]
 return q