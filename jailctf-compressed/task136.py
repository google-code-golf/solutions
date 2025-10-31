import re
p=lambda g:[p,eval][g==(x:=re.sub('(((2).{34}){2})0|0(?=(.{34}(1)){2})',r'\1\3\5',str(g)))](x)