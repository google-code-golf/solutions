import re
p=lambda g:[g:=eval(re.sub('(?=(.{32})*(.{29}|0, )?2.{28}([^2]), [^0])\d',r'\3',str([*zip(*g)][::-1])))for _ in g][7]