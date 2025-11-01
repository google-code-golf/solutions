def p(g):
 p=[u for r in range(len(g))for t in range(len(g[0]))for s in range(len(g),r,-1)for q in range(len(g[0]),t,-1)if'1'in str(u:=[s[t:q]for s in g[r:s]])*all(map(max,u+[*zip(*u)]))][0]
 for s in 3,2,1:[all(t+a in range(len(g[0]))and g[r+q][t+a]>1 for a in range(len(p[0])*s)for q in range(len(p)*s)if p[q//s][a//s]>1)and[t+a in range(len(g[0]))and g[r+q].__setitem__(t+a,-p[q//s][a//s])for a in range(len(p[0])*s)for q in range(len(p)*s)]for r in range(len(g)-len(p)*s+1)for t in range(1-len(p[0])*s,len(g[0]))]
 return[[abs(t)for t in r]for r in g]