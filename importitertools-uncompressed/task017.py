import re
p=lambda g,k=31:-k*g or p(eval(re.sub(r"(([^0], ){5})0(?=.*?\1(.))",r"\1\3",str([*zip(*g[::-1])]))),k-1)