import re
p=lambda g,i=7:g*-i or p(eval(re.search(r'.[^(]*(([^0])(, \2){3,})(?!.*\1\3).*\d.|$'*i,s:=f'{*zip(*g[::-1]),}')[0]or re.sub(s[2],*{*s}-{*')0'+s[:5]},s)),i-1)