import re
p=lambda g:eval(re.sub('1, 0(?=, 1)','1,2',str(g)))