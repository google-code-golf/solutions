import re
p=lambda g:[p,eval][g==(x:=re.sub('0(?=.{31}2|(?<=5.{31}2, .))','2',str(g)))](x)