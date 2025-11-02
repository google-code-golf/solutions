e=enumerate
p=lambda g:[[c*(sum(sum(r[~1%-~j:j+2])for r in g[~1%-~i:i+2])>c)for j,c in e(r)]for i,r in e(g)]