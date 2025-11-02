R=range(9)
p=lambda g,i=15:-i*g or p([[g[x][~y]or g[x][-y]*g[x-1][~y]%3*7for x in R]for y in R],i-1)