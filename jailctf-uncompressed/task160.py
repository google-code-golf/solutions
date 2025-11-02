import re
p=lambda g:eval(re.sub("1..1..1(.{25})1,",r"0,2,0\1 2,1+",str([*zip(*g[70:]or p(g*2))][::-1])))