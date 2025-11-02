import re
p=lambda g:[g:=eval(re.sub("([^0]), "*2+r"0(.{31}\2,) 0(.{40})0",r"\1,\2,\2\3\1\4\1",str([*zip(*g[::-1])])))for _ in g][7]