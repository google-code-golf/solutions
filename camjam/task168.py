import re
p=lambda m,k=39:-k*m or p(eval(re.sub(r"0(?=.{%d}([^0]).{28}\1, \1)"%(37+k//4*35),r"\1",str([*zip(*m[::-1])]))),k-1)