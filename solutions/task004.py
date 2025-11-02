import re;p=lambda i:eval(re.sub(r"(.),(?=.*\1.*0, \1)",r"0,\1|",str(i)))
# ----------------------------------------------------------------
# oxjam

p=lambda g:[[r[b>[f]+b]for*r,f in zip(a,[0]+a,[0]+b)]for a,b in zip(g,g[1:]+g)]
p=lambda g:[*map(lambda a,b,m=0:[m+v-(m:=v*any(b:=b[1:]))for v in a],g,g[1:]+g)]
