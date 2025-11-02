import re
p=lambda g:eval(re.sub(r"([^0], )((?!\1|0).)(.+\1.{32})0",r"\1 0\3\2",f'{*zip(*g[70:]or p(g*2)),}'))[::-1]