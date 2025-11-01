def p(g):
 *a,h,i=g;t=s=h.count(0)//2
 while s:s-=1;r=a[s-t];r[s]=r[~s]=i[t]
 return g