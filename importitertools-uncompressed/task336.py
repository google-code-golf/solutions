import re
p=lambda g,i=31:-i*g or p(eval(re.sub('0, (?=5.{28}5|8, [58])','8,',str([*zip(*g[::-1])]))),i-1)