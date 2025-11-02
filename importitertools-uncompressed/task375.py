def p(g,c=0):
 for r in g:r[~c]=r[c]=0;c+=1
 return g