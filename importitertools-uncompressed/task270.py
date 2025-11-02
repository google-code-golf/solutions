import re
p=lambda g:[g:=eval(re.sub('(1|(2)), 0([^)]*)(, (?(2)3|7))',r'\1\4\3,0',str([*zip(*g[::-1])])))for _ in g][7]