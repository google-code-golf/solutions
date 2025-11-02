R=range(10)
p=lambda m:[[m[0][max(x,y)%(4+all(m[0]))]for x in R]for y in R]