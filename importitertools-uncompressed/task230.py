import re
p=lambda g:[g:=eval(re.sub(f'0(?=, 0{"."*len(g)*3} 5, 5)',k,str([*zip(*g[::-1])])))for k in'3421'][3]