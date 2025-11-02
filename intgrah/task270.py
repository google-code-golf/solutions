import re
p=lambda m,k=7:-k*m or p(eval(re.sub(f"({1+k//4}, )0([^)]*)({3|7-k})",r"\1\3\2 0",str([*zip(*m)][::-1]))),k-1)