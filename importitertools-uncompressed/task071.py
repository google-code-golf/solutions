R=range(16)
p=lambda g:[[r[((I:=[j for j in R if(a:=max(g,key=any))[j]])[0]+I[-1]-j,j)[r[j]in a]]for j in R]for r in g]