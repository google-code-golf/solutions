q=[0]*3
p=lambda m:(i:=sum(m,z:=q*5).index(2),[(r+r)[4-i%5:][:5]for r in[z,q+[3,0,6],z,q+[8,0,7],z][5-i//5:][:3]])[1]