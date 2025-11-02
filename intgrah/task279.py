p=lambda m,k=55:-k*m or p([[9&r.pop()%[9|3-u,u+9][k>9]or(k<1)*9for u in[0]+r[:0:-1]]for*r,in zip(*m)],k-1)
# Similar to 196
# 1. Flood fill 0s from the edges inwards
# 2. Replace any 1 that touches 9, or  8, with 8
# 3. Replace 0 with 9