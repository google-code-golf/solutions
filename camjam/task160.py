import re
p=lambda m:[m:=eval(re.sub("1, ., 1(.{25})?"*3,r"0,2,0\1 2,2,2\2 0,2,0\3",str(m)))for _ in m][2]