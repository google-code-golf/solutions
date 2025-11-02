import re
p=lambda m:eval(re.sub("5[0, ]+5(?!, 5)","5,*(n:=-len('\g<0>')%4)*[5+n],5",str(m)))