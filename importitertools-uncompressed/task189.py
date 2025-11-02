r=range(3,9)
p=lambda g:[[g[j-3*(a:=g[6][0]>7)][i-3*(b:=g[0][6]>7)]%2*g[7*a+j//6][7*b+i//6]for i in r]for j in r]