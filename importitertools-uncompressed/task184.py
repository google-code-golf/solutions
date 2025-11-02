f=lambda g,i=-1:[i for x in g if(i:=i+1)*sum(x)<1]
p=lambda g:[[max(g[i+1][z:],key=bool)for z in f(zip(*g))]for i in f(g)]