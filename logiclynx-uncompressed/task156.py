def p(g):
 S=Q=[];f=s=0
 for r in g:p,s=s,sum(r)>>2;S+=Q*s;Q=[(r,s-2,f)]*p*s;f^=p>s
 for r,w,f in S:x=r.index(4)+1;r[x:x+w]=w*[2-(f^S[len(S)//2][2])]
 return g