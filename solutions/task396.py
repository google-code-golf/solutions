p=lambda m,n=266,*f:[[sum({*e*sum(m,[-f])})for e in s]for r in m if(f:=((X:=n>>5)*[a:=(r*3)[x:=n%32]]in(s:=r[x:x+X],[f]*X))*a)]or p(m,n-1)
# ----------------------------------------------------------------
# post-comp-diamonds, base: oxjam
