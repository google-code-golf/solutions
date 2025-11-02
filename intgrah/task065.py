# def p(m):f=sum(m,[]);y,x=divmod(f.index(min(f,key=f.count)),n:=len(m));k=n//2;return[r[-k*(x>k):][:k]for r in m[-k*(y>k):][:k]]
# def p(m,*k):f=sum(m:=[*zip(*k or p(m,*m))],());t=len(m)//2;return m[-t*(f.index(min(f,key=f.count))//len(m[0])>t):][:t]
p=lambda g:(n:=len(g)//2)and min(f:=[[r[j:j+n]for r in g[i:i+n]]for i in(0,n+1)for j in(0,n+1)],key=f.count)
