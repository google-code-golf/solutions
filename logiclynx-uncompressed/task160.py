import re
f=lambda x:eval(re.sub(r'(1.+)(.{25})1.{5}1(.{25})\1',r'0,2,0\2 2,2,2\3 0,2,0',str(x)))
p=lambda g:f(f(g))