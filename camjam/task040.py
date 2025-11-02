p=lambda*m:[*map(p,r[:1]*5+r[9:]*5,m[-1])]if(r:=m[0])*0!=0else m[1]and r
# R=range(10);p=lambda m:[[m[y][x]and m[-(y>4)][-(x>4)]for x in R]for y in R]
# R=range(10);p=lambda m:[[m[y][x]and m[0-y//5][0-x//5]for x in R]for y in R]
# R=range(10);p=lambda m:[[m[y][x]and m[y//5*9][x//5*9]for x in R]for y in R]