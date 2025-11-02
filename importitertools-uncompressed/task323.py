import re
p=lambda g,i=35:-i*g or p(eval(re.sub(f'(?<=8.{ {o:=40+i//4*76+i%-4*3%44}})0|0(?=.{ {o}}8)','5',str(g))),i-1)