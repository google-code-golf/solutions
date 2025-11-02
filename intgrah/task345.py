import re
p=lambda m:[m:=eval(re.sub("(?<=5.{31}2, )0|0(?=.{31}2)","2",str(m)))for _ in m][9]