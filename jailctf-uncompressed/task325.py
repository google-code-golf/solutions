import re
p=lambda g,x=0:g in[g:=eval(re.sub(s,'1',f'{*zip(*g),}',1))[::-1]for s in['8']+['8(?=, 1)']*27]and[*zip(*[iter([8,*[0]*x]*x)]*x)][:x]or p(g,x+1)