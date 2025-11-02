E=enumerate
p=lambda m:[[v*any(0in[0,*r][x:x+3]for r in[r,*m][y:y+3])for x,v in E(r)]for y,r in E(m)]