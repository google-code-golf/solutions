p=lambda m:[[p,int][r*0==0](r)for r in m for _ in m]
# Alternative
# p=lambda m,*k:[*zip(*sum(zip(*k*3or[p(0,m)]*3),()))]