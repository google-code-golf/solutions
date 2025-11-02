import re
p=lambda g,k=7:-k*g or p(eval(re.sub("., 4, .","3,4-(k<1),3",re.sub(r"1(.*) 0\1 1",r"1\1 4\1 1",str([*zip(*g)])))),k-1)
