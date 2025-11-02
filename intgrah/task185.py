R=0,1,2
def p(g):
 c={*g[0]}
 for _ in c:g=[*zip(*[r for r in g if{*r}-c])]
 return[[(e:=g[i][j])*(g[i+1][j]==g[i][j+1]==g[i+1][j+1]==e not in c)for j in R]for i in R]