import re
p=lambda g:eval(re.sub('(?<!1, )1,(.+?)1',r'1,*[2+(c:=len([\1]))%2*5]*c,1',str(g)))