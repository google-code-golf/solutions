def p(g,i=0):
 for x in g:x[i]=x[~i]=0;i+=1
 return g