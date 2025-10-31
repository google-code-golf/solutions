import re
r=re.sub
p=lambda g,x=0:eval(r(r("2|3","1","(.{47})".join(l:=re.findall("5, ([^5]{15})5(?![^]]*5, 0)",s:=str(x or p(g,g)))[:5])),"\%d ".join(l)%(1,2,3,4),s))