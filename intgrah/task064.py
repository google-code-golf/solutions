import re
p=lambda m:[m:=[*zip(*eval(re.sub(r"([^%d]), (%d)[^([]+((?!\1|\2)., ){3}"%((sorted(m[0])[5],)*2),lambda m:re.sub(m[2],m[1],m[0]),str(m))))][::-1]for _ in m][3]
# TODO: avoid using regex
# Maybe avoid using lambda in the substitution