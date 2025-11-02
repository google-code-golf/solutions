import re
p=lambda g,k=7:g*-k or eval(re.sub(f"{k|3}([^)]*).(?=, {2-k//4})",r"0\1k|3",f'{*zip(*p(g,k-1)),}'))[::-1]