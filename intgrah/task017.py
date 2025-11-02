R=range(21)
p=lambda g:[[[max([*map(max,*2*g[i%s::s])][j%s::s])for j in R]for i in R]for s in R if s>=5>len([*{*g[9][1::s],0},*{*g[0][::s],0}])][0]
# p=lambda m:[*zip(*[(sum(min([set(sum(m,[])[i%s::s])for s in range(21,21*10,21)],key=sum))for i in range(441))]*21)]