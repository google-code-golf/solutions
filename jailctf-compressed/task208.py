import re
R=re.sub
p=lambda a:eval(R(R(d:=min(v:=str(a),key=(v+"[]"*9).count),f'[^{d}]',f"({-len((k:=re.findall(d+'[^]]*'+d,v))[0])%65*'.'})".join(k)),"\%d ".join(k)%(*range(1,len(k)),),v))