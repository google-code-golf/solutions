import re
def p(m):m=eval("[[m "+"for m in m for _ in[*{*'%s'}][5:]]"%m*2);return[m:=eval(re.sub("0(?=, 0, 0.{%d}0, [^0].{%d}0)"%(n:=len(m)*3-5,n+3),"2",str([*zip(*m[::-1])])))for _ in m*3][23]