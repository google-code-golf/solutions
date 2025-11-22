p=lambda g,s=[0]*10:[(y:=0)or[[0,*[a for a in sum(g,[])if a%5],s:=[y:=x and(s[9]or(w:=y)&0)-~w]+s][y]for x in r]for r in g]
# ----------------------------------------------------------------
# post-comp-diamonds, base: cgi

import re
p=lambda i:eval(re.sub("5(, 5)+",lambda m:re.findall("[^50](?:, [1-9])+",s*2)[-s[m.end()-1::32].count('5')],s:=str(i)))
# ----------------------------------------------------------------
# oxjam
