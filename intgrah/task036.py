p=lambda g:min([eval((s:=f"[i for i in zip(*%s)if {c}in i]")%s%(g[:1]*2+g))for c in sum(g,[])],key=len)
# p=lambda m:[[v for*c,v in zip(*m,r)if ? in c]for r in m if ? in r]
# p=lambda m,*k:[r for r in zip(*k or p(m,*m))if ? in r]
###########################################################################
