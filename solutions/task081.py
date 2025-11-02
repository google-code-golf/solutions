p=lambda g:exec(f"g[:]={'(q:=1)*[q:=r.pop()or[1]<r[-1:q]for r in g],'*7};"*4)or g
# ----------------------------------------------------------------
# jailctf

# 81 byte tie from ox jam's base sol
p=lambda i,*w:i*0!=0and[*map(p,i,[i]+i,i[1:]+[i],*w)]or i or 8in(8in w[2:])*w[:2]
