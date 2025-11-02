import re
p=lambda g:eval(re.sub('0(?=.{31}(2(?!.+5)|1(?=.+5)))',r'\1',str(g[5110:]or p(g*2))))[::-1]