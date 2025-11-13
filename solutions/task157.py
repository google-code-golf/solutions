def p(r):i,u=range,15;f=sum(r,p:=[]);r=[[]];[(r:=[r+[(n,p)]for r in r for n in i(3*u)if f[n]<1],p:=[])for n in i(3*u)if p==(p:=p+[i for i in i(n,150,u)if f[i]&(n<u)])>[]];return max([*zip(*[((any(i+min(r)-n in r for n,r in r if n%u<5+i%u)+f[i]%5)%3for i in i(150))]*u)]for r in r)
# ----------------------------------------------------------------
# compression: auto
# garrymoss
