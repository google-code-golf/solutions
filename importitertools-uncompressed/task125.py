import re
p=lambda g,k=31:-k*g or p(eval(re.sub("[38](?=(, ([46]))?.{43}[46])",r'\2+12>>2',str([*zip(*g[::-1])]))),k-1)