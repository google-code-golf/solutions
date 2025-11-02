e=enumerate
p=lambda g:[[r[x]or max({*r[:x:3]}&{*r[x:]}|{*c[:y+1:3]}&{*c[y:]})for x,c in e(zip(*g))]for y,r in e(g)]