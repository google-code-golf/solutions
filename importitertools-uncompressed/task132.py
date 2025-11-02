import re
p=lambda g,i=63:-i*g or p(eval(re.sub(fr"(\d),(?=(.{ {len(g)*3+2}})*[^)]*\1)",r"\1,\1|",str([*zip(*g[::-1])]))),i-1)