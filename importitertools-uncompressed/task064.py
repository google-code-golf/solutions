import re
def p(g):A=sum(g,g[6]);a,b,c=sorted({*A},key=A.count);[g:=eval(re.sub(f'{a}, {c}(?=[^)]*{b})','a,a',str([*zip(*g[::-1])])))for _ in g*8];return g