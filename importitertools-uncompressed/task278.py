import re
p=lambda g:[g:=eval(re.sub("0(?=(.{%d}.{,9}|, )2, 2)"%(len(g)*3-5),"3",str([*zip(*g[::-1])])))for _ in g][3]