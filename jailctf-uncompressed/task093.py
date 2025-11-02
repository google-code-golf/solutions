import re
p=lambda g:exec("g[::-1]=zip(*eval(re.sub('[^05],([, 0]*5)',r'\\1,5',str(g))));"*12)or g