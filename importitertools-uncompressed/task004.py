import re
p=lambda g:eval(re.sub(fr'([1-9].*), 0(?=.{ {len(g[0]*3)}}.*\1)',r'0,\1',str(g)))