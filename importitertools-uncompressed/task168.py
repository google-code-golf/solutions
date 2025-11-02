import re
p=lambda g:[g:=[*zip(*eval(re.sub(r"0, (?=(.{35})+([^0], ).{26}\2\2)",r"\2",str(g)))[::-1])]for _ in g][3]