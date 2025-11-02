p=lambda g:g[99:]or[eval("r.pop()|r[-1]%4,"*9)for*r,in zip(*p(g*2)*2)]
# ----------------------------------------------------------------
# cgi, jailctf

# jailctf sol
p=lambda g:exec(f"g[:]={'[r.pop()or[0]<r[-1:]for r in g],'*9};"*4)or g
