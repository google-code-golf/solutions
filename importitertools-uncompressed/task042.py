import re
p=lambda g:exec('g[:]=eval(re.sub("0(?=.{%d}3.{%d}3)","8",str([*zip(*g[::-1])])));'%((h:=sum(max(zip(*g)))/3)*38-1,h*29-1)*4)or g