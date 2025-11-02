R=0,4,8
p=lambda m:[[6<sum(sum(r[c:c+3])for r in m[r:r+3])for c in R]for r in R]