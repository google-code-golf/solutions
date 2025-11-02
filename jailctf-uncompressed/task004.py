import re
p=lambda g:eval(re.sub(r'(\d),(?=.+\1.*].+\1)',r'0,\1+',str(g)))