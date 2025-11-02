import re
p=lambda m,k=3:-k*m or p(eval(re.sub("0(?=, 0.{%d} 5, 5)"%len(m*3),"2**k%5",str([*zip(*m[::-1])]))),k-1)