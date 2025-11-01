def p(g):
 for z in[{*g[0]}]*2:g=[c for c in zip(*g)if{*c}-z]
 return[[(q==q[:1]*4)*sum({*q}-z)for q in zip(B,D,B[1:],D[1:])]for B,D in zip(g,g[1:])]