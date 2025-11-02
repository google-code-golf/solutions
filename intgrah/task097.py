E=enumerate
p=lambda m:[[v*(v<sum(sum([0,*r][x:x+3])for r in[[],*m][y:y+3]))for x,v in E(r)]for y,r in E(m)]