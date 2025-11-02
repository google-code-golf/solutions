f=filter
def p(g):*g,=f(any,zip(*f(any,zip(*g))));return[[*map(min,a,b[::3]*3)]for a,b in zip(g,g[::3]*3)]