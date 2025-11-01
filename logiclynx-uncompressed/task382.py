def p(g):
 a,*_,b=g;t=*map(list,zip(*g)),;d=2in t[0]or-1;c=a<b
 if s:=2in a+b:return*zip(*p(t)),
 for r in g[::-c|1]:s+=2in r;r[s^d>>1::d]=g[-c][::d][:-s|64]
 return g