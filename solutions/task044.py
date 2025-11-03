def p(i):
 for f in range(100):
  r=[n for n in range(100)if i[n//10][n%10]<5in i[n//10][:n%10]and 5in i[n//10][n%10:]and n<50]
  t=[n for n in range(100)if i[n//10][n%10]==f]
  if[r[0]-f for f in r]==[t[0]-f for f in t]:
   for n in r:i[n//10][n%10]=f
   for n in t:i[n//10][n%10]=0
 for f in range(100):
  r=[n for n in range(100)if i[n//10][n%10]<5in i[n//10][:n%10]and 5in i[n//10][n%10:]and n>50]
  t=[n for n in range(100)if i[n//10][n%10]==f]
  if[r[0]-f for f in r]==[t[0]-f for f in t]:
   for n in r:i[n//10][n%10]=f
   for n in t:i[n//10][n%10]=0
 return i
# ----------------------------------------------------------------
# compression: auto
# jailctf
