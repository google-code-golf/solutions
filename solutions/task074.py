p=lambda g:g[90:]or p(g+[*zip(*map(map,[min]*30,p(g[:30]+g),g[:2]+g[::-1]))])
# ----------------------------------------------------------------
# many

# alt sols
p=lambda i,*c:[*map(min,i,[9,9]+i[::-1],c)]or[i:=[*map(p,i,*i)]for _ in i][2]
p=lambda g:g[:-90]or p([[*map(min,x,y,[9]*2+x[::-1])]for*y,x in zip(*g,g)]+g)