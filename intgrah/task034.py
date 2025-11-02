import re
p=lambda m:[m:=eval(re.sub("(?=(0.{31})*(.{29}|0, |)2.{28}[^0]{4}).",max({*str(m)}-{*"2[]"}),str([*zip(*m[::-1])])))for _ in m][3]