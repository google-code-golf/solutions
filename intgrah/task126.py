p=lambda m:m[:-1]+[[sum(c)%~max(c)%2*4for c in zip(*m)]]
# p=lambda m:[*zip(*[c+[sum(c)%~max(c)%2*4]for*c,_ in zip(*m)])]