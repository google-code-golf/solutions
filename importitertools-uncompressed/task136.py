import re
p=lambda g:[g:=eval(re.sub('(((2).{34}){2})0|0(?=(.{34}(1)){2})',r'\1\3\5',str(g)))for _ in g][9]