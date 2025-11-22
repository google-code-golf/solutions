p=lambda g:[[c:=[max(j and c,*g[0][j:],key=bool),x][x<5]for j,x in enumerate(r)]for r in g]
# ----------------------------------------------------------------
# post-comp-diamonds, base: fuunagent

R=range(10)
p=lambda g:[[max(g[0][k]*all(r[j:k+1]+r[k:j+1])for k in R)for j in R]for r in g]
# ----------------------------------------------------------------
# lv1dev
