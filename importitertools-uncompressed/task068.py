R=range(10)
p=lambda g:[[(3587>>(d:=abs(r*10+c-(a:=sum(g,[])).index(b:=min(a,key=a.count))))&1)*(b,2)[d>0]for c in R]for r in R]