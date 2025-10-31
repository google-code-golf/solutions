import re
R=re.sub
p=lambda g,i=14:i and p(R('([^5]..)0(?=.{28}(5..0.+|.{6})([^05\D]))',r'\1\3',f' {g}'[::-1]),i-1)or eval(R(*'50',g))