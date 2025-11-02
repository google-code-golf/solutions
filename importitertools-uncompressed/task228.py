import re
p=lambda g:[g:=[*zip(*eval(re.sub(r"0(.{34}([1-9]).+)(.)(.{34}\2)",r"\3\1 0\4",str(g)))[::-1])]for _ in g][3]