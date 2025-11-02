R=range(17);p=lambda m:[[m[y][x]or m[y%6][x%6]and m[5][0]for x in R]for y in R]
# Alternatives
# p=lambda m:[[r[x]or s[x%6]and r[5]for x in range(17)]for r,s in zip(m,m[:6]*3)]
# p=lambda m:[[u or(v>0)*r[5]for u,v in zip(r,s[:6]*3)]for r,s in zip(m,m[:6]*3)]