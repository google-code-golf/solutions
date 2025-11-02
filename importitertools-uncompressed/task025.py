import re
p=lambda g:[g:=eval(re.sub('([1-9])([^)]*0(?=, (?<='+(w:=fr'\1..{ {len(g)*3}}'*3)+fr')\1|, {w})|)',r'0\2+\1*(X.count("\1")>9)',X:=str([*zip(*g[::-1])])))for _ in g][7]