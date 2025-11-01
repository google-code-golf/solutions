def p(r):
 e=[]
 def p(f,d):
  if len(r)>f>-1<d<len(r[-1])>r[f][d]==0:r[f][d]=-len(e);e[-1]+=1;p(f+1,d);p(f-1,d);p(f,d+1);p(f,d-1)
 for d in range(len(r[-1])):
  for f in range(len(r)):
   if len(r)>f>-1<d<len(r[-1])>r[f][d]==0:e+=0,;p(f,d)
 for d in range(len(r[-1])):
  for f in range(len(r)):
   if len(r)>f>-1<d<len(r[-1])>r[f][d]<0:r[f][d]=(e[~r[f][d]]==max(e))+8*(e[~r[f][d]]==min(e))
 return r