import re
p=lambda g:eval(re.sub('(2|3), [31]|0',r'*7%3\1%5*[3\1%31]',f'{*zip(*g[20470:]or p(g*2)),}'))[::-1]