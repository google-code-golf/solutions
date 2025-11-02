import re
p=lambda g,k=15:-k*g or p(eval(re.sub('0(?=.{%d}[^0].{19}[^0], (.))'%(5*(19|39-k)/6),r'\1',str([*zip(*g[::-1])]))),k-1)