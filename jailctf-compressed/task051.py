import re
p=lambda g:[g:=eval(re.sub(r'0(?=[^)]*(([^0]), (?!\2)){2}0)',r'\2',f'{*zip(*g[::-1]),}'))for _ in g][3]