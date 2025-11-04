*Z,p=0,lambda g:[Z+g[0]+Z,*[r[:1]+r+r[-1:]for r in g],Z+g[-1]+Z]
# ----------------------------------------------------------------
# many


# recursive
p=lambda g,v=1:g*0!=0and[v*p(g[0],0),*map(p,g),v*p(g[-1],0)]or g
