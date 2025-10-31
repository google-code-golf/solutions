f=lambda g:[*zip(*g)][::-1]
p=lambda g:f(f(y:=f(g+f(g))))+y