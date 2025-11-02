p=lambda m:[[r[x+4]or s[x]or s[x+4]or r[x]for x in range(4)]for r,s in zip(m,m[4:])]
# Alternative:
# p=lambda m:[[max(9*r.pop(4),6*s.pop(0),s[3],v)%10for v in r]for r,s in zip(m,m[4:])]