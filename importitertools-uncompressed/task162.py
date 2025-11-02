import re
p=lambda g:[g:=eval(re.sub("0, 0, 0(.{55})"*3+"{0}",r"1,1,1\1 1,1,1\2 1,1,1",str(g)))for _ in g][1]