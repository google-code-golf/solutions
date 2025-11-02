import re
p=lambda g,i=3:-i*g or p(eval(re.sub(r"3((.*?\)).+?)0(?=\2.*4)",r"0\1 3",str([*zip(*g[::-1])]))),i-1)