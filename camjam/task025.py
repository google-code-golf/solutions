E=enumerate
p=lambda m:exec("""for y,r in E((e:={r[0]:y for y,r in E(m)if all(r)})and m):
 for x,v in E(r):
  r[x]=0
  if v in e:m[(Y:=e[v])-(y<Y)+(y>Y)][x]=v
m[:]=map(list,zip(*m))
"""*2)or m
