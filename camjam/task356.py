E=enumerate
p=lambda m:[[max({*c[:y+1]}&{*c[y:]}|{*r[:x]}&{*r[x:]})for x,c in E(zip(*m))]for y,r in E(m)]