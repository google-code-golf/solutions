import re
p=lambda g,k=0:eval(re.sub("0, 0, 0(.{55})?"*3," 1,1,1\%d"*3%(1,2,3),str(k or p(g,g))))