def p(g):
 m,n=[[*map(any,h)].index(1)for h in(g,zip(*g))];k=90
 while k:k-=1;g[m+k%6][n+k%5]|=g[m+~k%5][n+k%6]
 return g
# ----------------------------------------------------------------
# post-comp-diamonds, base:logiclynx
