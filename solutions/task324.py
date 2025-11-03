def p(s):
 c=sum(s,[]);t=c.count;a=c[t(c[0])<4];o,f={},{()}
 for d,e in enumerate(s):
  for m,i in enumerate(e):
   if t(i)<4:o[a in e and a in c[m::len(e)]]=i;f|={d+m,(d-m,)}
 for d,e in enumerate(s):
  for m,i in enumerate(e):
   if{d+m,(d-m,)}&f:e[m]=o[a in e and a in c[m::len(e)]]
 return s
# ----------------------------------------------------------------
# compression: auto
# post-comp-diamonds
