import re
p=lambda g,i=11:-i*g or p(eval(re.sub(r"(([1-9]).{28,34})(?=(.{29}|.{35})*\2)0",r"\1\2",str(g))),i-1)