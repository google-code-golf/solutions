import re
p=lambda g:eval(re.sub("([1-9])((.{32})+?[^8)]+)8",r"0\2\1",f'{*zip(*g[70:]or p(g*2)),}'))[::-1]