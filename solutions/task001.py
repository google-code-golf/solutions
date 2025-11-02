p=lambda*g:[[*g,min,p][2](r,s)for r in g[0]for s in g[-1]]
# ----------------------------------------------------------------
# many
# g is a 1-tuple on the first call, so g[0] and g[-1] are equal. On the second call, g is a 2-tuple.
p=lambda*g:[[*g,min,p][2](r,s)for r in g[0]for s in g[-1]]
p=lambda*g:[[p,min][r*0==0](r,s)for r in g[0]for s in g[-1]]
# r*0==0 is true when r is an integer and false when r is a list

# Sort of like a Kronecker product
p=lambda g:[[a&b for a in r for b in s]for r in g for s in g]
