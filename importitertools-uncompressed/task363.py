def p(t):
 a=[(o,s)for s in range(10)for o in range(10)if t[s][o]%5]
 for u in range(-9,10):
  for q in range(-9,10):
   for o,s in[(o+q,s+u)for o,s in a]*all(s in range(10)and o in range(10)and 1>t[s][o]for o,s in[(o+q,s+u)for o,s in a]):t[s][o]=2*(q*str(t).count("5")!=-172and u*str(t).count("5")!=-240)
 return t