E=enumerate
p=lambda m:exec("Y,X=zip(*[(y,x)for y,r in E(m)for x,v in E(r)if v])\nfor y,r in E(m[(t:=min(Y)):t+5]):\n for x,v in E(r[(l:=min(X)):l+5]):m[t+x][l+4-y]|=v\n"*4)or m
# TODO
