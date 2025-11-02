E=enumerate
def p(g):Y,X=divmod(sum(g,[]).index(8),13);return[[v%5+5*(abs(y+x-(Y+X+(Y<y)-(Y>y)))<=y-Y+(y!=Y)&1)for x,v in E(r)]for y,r in E(g)]