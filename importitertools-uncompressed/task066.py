def p(e):
 for z in"3131 1331 1313 3113 0332 0310 2132 2110 0112".split():
  s=e
  for z,d in zip(z,[3,3,1,0]):
   for z in[0]*eval(z):*s,=zip(*s[::-1])
   s=eval(str(s).replace("3, 3,","3,3,1|",d))
   for z in e:s=eval(str(s).replace("1, 0","3,1",d))
   s=eval(str(s).replace("1, 2","3,2",d))
  if("1"in str(s))==("9"in str(s))==0:return s