import re
s=re.sub
p=lambda g:eval(s('(?<!5, )5(, 0)+, 5',lambda m:s('0',str(4+len(m[0])//3),m[0]),str(g)))