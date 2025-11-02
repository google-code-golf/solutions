import re
p=lambda g:eval(re.sub("4",lambda m:s[-m.end()],s:=str(g)))