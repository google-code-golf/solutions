def p(k,t=0):
 while len(set(f:=sum(j:=[v[t//-~len(k[0]):][:3]for v in k[t%-~len(k[0]):][:3]],[])))<4:t+=1
 h=f.count
 for _ in range(4):
  for o in 3,2,1:
   for t in range(-~len(k[0])-3*o):
    for s in range(-~len(k)-3*o):
     if all((k[-1][0],j[m//o][e//o])[h(j[m//o][e//o])<2]==k[s+m][t+e]for e in range(3*o)for m in range(3*o)):
      for m in range(3*o):k[s+m][t:t+3*o]=[j[m//o][e//o]for e in range(3*o)]
  j=[*zip(*j[::-1])]
 return k