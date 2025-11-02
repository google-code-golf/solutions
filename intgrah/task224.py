E=enumerate
p=lambda g:exec("Y,X=zip(*[(y,x)for y,r in E(g)for x,v in E(r)if(v%5<1or(c:=v)<1)&v]);l=min(X)+1;r=max(X);g[min(Y)+1][l:r]=[c]*(r-l);g[:]=map(list,zip(*g[::-1]));"*4)or g
