import re
p=lambda g,k=11:-k*g or p(eval(re.sub('(5(, 0)*), [^05]','5,\\1',f'{*zip(*g[::-1]),}')),k-1)