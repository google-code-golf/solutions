import re
p=lambda g,i=43:g*-i or p(eval(re.sub(f'(?=1, (6|1(.{(a:={len(g)*3-2})}1, 0?)+1)|6, 2|6.{a}6, 6, 6|3)','1106%1',f"{*zip(*g[::-1]),}")),i-1)