import re
p=lambda m,*k:eval(re.sub("(0, 0, 0)(.{55})"*2+r"\1",r"1,1,1\2 1,1,1\4 1,1,1",str(k or p(m,*m))))