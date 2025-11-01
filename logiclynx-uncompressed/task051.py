import re
p=lambda g,k=63:-k*g or p(eval(re.sub(r'(0, ([^0]), (?!\2|0)[^)]+)0',r'\1\2',f'{[*zip(*g[::-1])]}')),k-1)