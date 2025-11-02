import re
p=lambda g,i=35:-i*g or p([*zip(*eval(re.sub("0(?=(..{%d}0, [^0])+.{%d}0.{%d}0, (.))"%(w:=len(g)*3,w+7,w-2),r"\2",str(g)))[::-1])],i-1)