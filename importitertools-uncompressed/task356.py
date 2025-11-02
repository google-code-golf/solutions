e=enumerate
p=lambda g:[[max({*r[:j]}&{*r[j:]}|{*y[:i]}&{*y[i:]}|{r[j]})for j,y in e(zip(*g))]for i,r in e(g)]