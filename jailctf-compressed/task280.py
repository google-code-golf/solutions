p=lambda g:exec("""
r,g[::-1]=0,map(list,zip(*g))
for x in g:
 r+=1;j=[*x,0].index(0,c:=[*x,2].index(2))-c
 for i in-~-x[c-1]*g[r-j:r-1+j]:i[:c]=[i[c]]*c"""*4)or g