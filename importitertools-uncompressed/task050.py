import re
p=lambda g,i=51:-i*g or p(eval(re.sub('(8[^)]*)0(?=[^)]*8)',r'\1 3',str([*zip(*g)]))),i-1)