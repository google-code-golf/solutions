R=range(10)
p=lambda m,*k:[[sum({*(f:=sum(k or p(m,*m),[]))[10*y+x::9]}&{*f[10*y+x::-9]})for x in R]for y in R][::-1]