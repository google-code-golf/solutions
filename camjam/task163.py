E=enumerate
R=0,4,8
p=lambda m:[[v*(v==5)or sum(m[y%4+i][x%4+j]*(4==m[y//4+i][x//4+j])for i in R for j in R)for x,v in E(r)]for y,r in E(m)]