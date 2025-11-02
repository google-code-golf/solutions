p=lambda i,k=18:~k*i or p([[x.pop()or[0,*x][k%-2]%5&6-(5in x)for x in i]for*x,in i],k-1)
# ----------------------------------------------------------------
# oxjam w/ pop recursion
p=lambda i,k=18:~k*i or[[x.pop()or[0,*x][k%-2]%5&6-(5in x)for _ in i]for*x,in zip(*p(i,k-1))]
