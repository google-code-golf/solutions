import re
p=lambda m:[m:=eval(re.sub("0(?=(.{%d}0)*.{%d}[^0].{%d}0, 0.{%d}0, ([^0]))"%(n:=len(m)*3+4,n,n,n-6),r"\2",str([*zip(*m[::-1])])))for _ in m][3]