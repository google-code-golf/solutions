import re
p=lambda g:eval(re.sub("(?<!5, )5,(.+?)5",r"5,*[(v:=len([\1]))+5]*v,5",str(g)))