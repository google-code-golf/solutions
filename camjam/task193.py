p=lambda m,*k:[[x&max(o)for*o,x in zip([0]+r,r[1:]+[0],r)]for*r,in zip(*k or p(m,*m))]
# import re;p=lambda m,*k:eval(re.sub("(?<![^0], )\d(?!, [^0])","0",str([*zip(*k or p(m,*m))])))