import re
p=lambda g,k=7:-k*g or p(eval(re.sub('0(?=(.{35})*.{34}[38].{34}[28])','3',f'{*zip(*g[::-1]),}')),k-1)