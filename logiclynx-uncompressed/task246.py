def p(g):
 s,e=map(sum(g,[]).index,(3,2));w=len(g[0])
 while(s:=s+(1|-(s>e))*w**(e//w!=s//w))-e:g[s//w][s%w]=8
 return g