import re
p=lambda g:[g:=[*zip(*eval(re.sub("0(?=.{25}2|, (1))",r"1^\1+5",str(g)))[::-1])]for _ in g][3]