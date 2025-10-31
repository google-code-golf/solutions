import re
p=lambda g,*x:eval(re.sub('[^(2]{9}2'*2+'?',"*[\g<0>][::-1]",f"{*zip(*x or p(g,*g)),}"))