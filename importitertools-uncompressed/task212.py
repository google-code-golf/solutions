import re
p=lambda g,i=19:-i*g or p(eval(re.sub('(0, (1)|(2), 0)(?=[^(]*5)',r'\2\3,\2\3',str([*zip(*g[::-1])]))),i-1)