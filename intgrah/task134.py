import math
def p(m):f=sum(m,[]);n,k=max((min(6,math.gcd(*[r.count(k)for r in m])),k)for k in f);return[[(sum({*f})-k)*(v==k)for*c,v in zip(*m,r)if k in c][::n]for r in m[::n]if k in r]
