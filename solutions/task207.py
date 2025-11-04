p=lambda*g:min(g,key=g.count)if g[3:]else[*map(p,*g,*[h[3:]for h in g])]
# ----------------------------------------------------------------
# post-comp-diamond, base: cgi

# same as t065
p=lambda g:[p(i)for*i,in map(zip,g,g[3:])]or min(q:=g[0]+g[1],key=q.count)
# jailctf, oxjam
