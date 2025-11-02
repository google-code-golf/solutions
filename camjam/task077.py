import re
p=lambda g,k=39:-k*g or p(eval(re.sub("(?<=[24], )[^2](?=.( |.{%d})[24])"%len(g*3),"4",str([*zip(*g[::-1])]))),k-1)