p=lambda g:[[*map(max,*(r*max(-a^-b for a,b in zip(r,t))+t for t in g))]for*r,in zip(*g)]
# ----------------------------------------------------------------
# post-comp-diamond, logiclynx + cgi


p=lambda g:[[*map(max,*[r*any(-i^-j>0for i,j in zip(r,s))+s for s in g])]for*r,in zip(*g)]
