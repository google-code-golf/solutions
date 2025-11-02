p=lambda m,*k:[[v or(8in{*r[:x]}&{*r[x:]})*3for x,v in enumerate(r)]for*r,in zip(*k or p(m,*m))]
# Regex alternative (longer):
# import re;p=lambda m,k=0:[*zip(*eval(re.sub("8[, 03]*8",lambda s:re.sub(*"03",s[0]),str(k or p(0,m)))))]