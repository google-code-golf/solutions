import re
p=lambda g:eval(re.sub(r"0(?=(, 0(.){32})+.{37}\2)",r"\2",f'{*zip(*g[70:]or p(g*2)),}'))[::-1]