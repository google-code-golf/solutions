R=range(10)
p=lambda m:[[m[y][x]or max(max({*[0,0,*r][x:x+5],0}-{1})for r in[[],*m][y:y+5])*any(m[y-9])for x in R]for y in R]