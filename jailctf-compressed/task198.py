import re
p=lambda g:exec(r'g[::-1]=zip(*eval(re.sub("(?=0|3(, [^3])(\\1|\))|3, 4)","6^5-",f"{g}")));'*48)or g