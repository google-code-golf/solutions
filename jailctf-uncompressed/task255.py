def p(z):
 for i in range(2,30):
  for i in range(2,30):
   for o in range(23,30):
    for f in range(i+3,30):
     if all({0,3,30}>{*z[o][i-1:2+f]} for o in range(o+2)if o in range(30)):
      for o in range(o+1):
       for f in range(i,f+1):z[o][f]=3
       if all({0,3,30}>{*z[o][:f]} for o in range(o-1,o+2)if o in range(30)):z[o][:f]=[3]*f
       if all({0,3,30}>{*z[o][f:]} for o in range(o-1,o+2)if o in range(30)):z[o][f:]=[3]*(30-f)
  z=[[*o] for o in zip(*z)][::-1]
 return z