import re
p=lambda m,k=23:-k*m or p(eval(re.sub("0(?=, 4|.{%d}5, 0.{%d}0)"%(a:=len(m)*3+4,a-6),"4",str([*zip(*m[::-1])]))),k-1)