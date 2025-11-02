import re
p=lambda g:[g:=eval(re.sub("1, 1, 1(.{25})1, 0, 1(.{25}).{7}",r"0,2,0\1 2,2,2\2 0,2,0",str(g)))for _ in g][1]