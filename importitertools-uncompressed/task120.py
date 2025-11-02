import re
p=lambda g:eval(re.sub(fr'(?<=([1-9]).{ {o:=len(g[0])*3+4}})\1(?=.{ {o}}\1)','8',str(g)))