def p(b):
 e=()
 while any((c:=i,h:=o)for i in range(len(b)-2)for o in range(len(b[0])-2)if 0<min(l:=sum(f:=[b[i+n][o:o+3]for n in range(3)],[]))<max(l)):
  e+=(-l.count(2),f),
  for n in range(3):b[c+n][h:h+3]=[0,0,0]
 b=[*map(list,zip(*filter(any,zip(*filter(any,b)))))]
 for _,f in sorted(e):
  while 1>any((c:=i,h:=o)for i in range(len(b)-2)for o in range(len(b[0])-2)if all(b[i+n][o+l]==2-2*(f[n][l]==2)for l in range(3) for n in range(3))):f=[*zip(*f[::-1])]
  for n in range(3):b[c+n][h:h+3]=f[n]
 return b