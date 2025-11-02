p=lambda g:[eval('r.pop(0)*r[3]*2,'*3)for r in g]
# ----------------------------------------------------------------
# many

# With some pop tricks
p=lambda g:[[2*b*r.pop(0)for b in r[4:]]for r in g]
p=lambda g:[[2*a*b for a,b in zip(r,r[4:])]for r in g]
