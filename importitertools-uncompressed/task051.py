import re
p=lambda g,i=71:-i*g or p(eval(re.sub(r'(0, ([^0]), (?!0|\2)[^)]+)0',r'\1\2',str([*zip(*g[::-1])]))),i-1)