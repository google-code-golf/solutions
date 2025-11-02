E=enumerate
p=lambda m:[[m[y-1][x]or 4*any(any(q[x%2::2])for q in m[y:])for x,v in E(r)]for y,r in E(m)]