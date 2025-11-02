import re
f=lambda g,c:eval(re.sub('(?<=4.{34})4(?=.{34}4)',c,str(g)))
def p(g):i=g.index([0]*10,1)+1;x,y,*_='121'[sum(sum(a:=g[:i],[]))>sum(sum(b:=g[i:],[])):];return f(a,x)+f(b,y)