import re
p=lambda g:exec("g[::-1]=zip(*eval(re.sub('0(?=.{40}[83].{40}[832])','3',str(g))));"*40)or g