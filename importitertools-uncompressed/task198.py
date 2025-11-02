import re
p=lambda g,k=99:-k*g or p(eval(re.sub('(3)(?=, 4|[^)]+[^34)], [^34])|0',r'1^\1+2',str([*zip(*g[::-1])]))),k-1)