def p(z):
 for n in z*4:
  n=-1
  for i in[i for i in range(30)if{*z[i][5:]}-{0,3}-{13}]+[30]:
   if i>n+6:
    for n in z[n+2:i-1]:n[5:]=[13]*25
   n=i
  for i in[i for i in range(30)if not any(13 not in n or {*n[:n.index(13)]}-{0,3}-{13} for n in z[:i+2][-3:])]:
   z[i][:z[i].index(13)]=[3]*z[i].index(13)
  z=[[*n]for n in zip(*z[::-1])]
 return[[i%10 for i in n]for n in z]