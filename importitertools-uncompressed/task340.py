import re
p=lambda g:[g:=eval(re.sub(r'(\d)([^)]*0(?=, \1\))|)',r'0\2+\1*(X.count("\1")>3)',X:=str([*zip(*g[::-1])])))for _ in g][3]