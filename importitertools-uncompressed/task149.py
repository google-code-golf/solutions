r=0,4,8
p=lambda g:[[sum(sum(r[j:j+3])for r in g[i:i+3])>6for j in r]for i in r]