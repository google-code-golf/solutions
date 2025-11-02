import re
p=lambda g,i=23:-i*g or p(eval(re.sub(f"(?<=[24], )[^2](?=.{'.'*len(g)*3}[24]|..2)","4",str([*zip(*g[::-1])]))),i-1)