import re
p=lambda g:exec("x='...'*len(g)+'.0';g[::-1]=zip(*eval(re.sub(f'0(?=({x}, .)*, [^0]{x*2}, (.))',r'\\2',str(g))));"*4)or g