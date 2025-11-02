import re
p=lambda g:exec(r'g[::-1]=zip(*eval(re.sub("((3)|7)([^[(]+)0(, (?(2)2|1))",r"0\3\1\4",str(g))));'*8)or g
# ----------------------------------------------------------------
# post-comp-diamond-himagine the future
