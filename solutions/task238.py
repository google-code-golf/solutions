def p(g,s='[[8,*r,8]for r in zip(*%s)if 8in r]'):R=range(l:=len(B:=eval(s%s%g)));return[[B[i][j]*[[*{c/8:0for c in sum(g,[])if c%8}][(i>j)+(~i+l<j)*2],0<i<l-1][i in(j,~j+l)]for j in R]for i in R]
# ----------------------------------------------------------------
# jailctf
