import re
p=lambda g,i=51:-i*g or p(eval(re.sub('(1[^)]*)0(?=[^)]*1)',r'\1 8',str([*zip(*g)]))),i-1)