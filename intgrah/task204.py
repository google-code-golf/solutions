import re
p=lambda m:eval(re.sub("1[0, ]+1(?!, 1)","1,*(n:=len('\g<0>')//3-1)*[n%2*5+2],1",str(m)))