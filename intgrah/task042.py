import re
p=lambda m:[m:=eval(re.sub("0(?=.{%d}3.{%d}3)"%(n:=37+str(m).count('3')//8*38,n*49>>6),"8",str([*zip(*m[::-1])])))for _ in m][3]