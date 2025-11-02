import re
p=lambda g,i=15:-i*g or p(eval(re.sub("5(([^2]{32})*)(?=[^2]*\).*2)",r"0\1+5",str([*zip(*g[::-1])]))),i-1)