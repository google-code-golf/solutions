import re
p=lambda m:[[int(re.search(r"([^0]), (0, )+\1",str(m))[1])]]