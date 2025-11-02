import re;p=lambda g:[g:=eval(re.sub("0(?=, 8.{19}8)","1",str([*zip(*g[::-1])])))for _ in g][3]
