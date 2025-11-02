S=sum
T=b""
p=lambda m:[[[(S(S(r[x-3:x])for r in m[y-3:y])==max(S(S(r[x-3:x])for r in m[y-3:y])for y in T for x in T))*S({*S(m,[-5])}),5][x|y>15]for x in T]for y in T]