import re
p=lambda m,*k:[*zip(*eval(re.sub("([50, ]{9}2[^2]{9})",r"*[\1][::-1]",str(k or p(m,*m)))))]