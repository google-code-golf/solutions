def p(g,j=0):
 for r in g:r[j]=r[~j]=0;j+=1
 return g