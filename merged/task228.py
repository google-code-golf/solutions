import re
p=lambda g:eval(re.sub(r'([^0])((, (?!\1|0).).*0\3.{28})0',r'0\2\1',f'{*zip(*g[70:]or p(g*2)),}'))[::-1]