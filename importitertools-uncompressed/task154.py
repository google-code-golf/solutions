import re
p=lambda g:[g:=eval(re.sub("[^2(]{9}2[^2]{9}",lambda m:m[0][::-1],str([*zip(*g)])))for _ in g][1]