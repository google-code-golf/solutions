import re
p=lambda g:[g:=eval(re.sub("0(?=.{31}2)|(?<=5.{31}2, )0","2",str(g)))for _ in g][9]