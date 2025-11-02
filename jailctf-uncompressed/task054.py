def p(i):
 r,w,e=[(r,w,e)for w in range(26)for e in range(26)if(r:=[i[w+f][e+n]for f in range(5)for n in range(5)])==r[::-1]!=len({*r})>2][0];[i[w+f][e+n]for f in range(5)for n in range(5)for i[w+f][e+n]in r]
 for w,e in[(w,e)for w in range(29)for e in range(29)if i[w][e]==r[12]]:
  for f in-1,1,0:
   for n in-1,1,0:
    if r[0]!=r[12+f*5+n]:i[w+f][e+n]=r[12+f*5+n];exec('while i[w][e+f]!=r[0]!=r[10]!=0!=f:e+=f;i[w][e]=r[10]');exec('while i[w+f][e]!=r[0]!=r[2]!=0!=f:w+=f;i[w][e]=r[2]')
 return i