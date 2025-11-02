import re
p=lambda g,i=19:-i*g or p(eval(re.sub(r"0(?=.{34}(.), 0.{31}\1)",r"\1",str([*zip(*g[::-1])]))),i-1)