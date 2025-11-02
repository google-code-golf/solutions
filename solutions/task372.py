p=lambda g:eval("[*map(max,g.pop(0),g[5])],"*5)
# ----------------------------------------------------------------
# cgi, jailctf

# jailctf sol
p=lambda g,h=[]:[*map([p,max][h>[]],g,h+g[6:])]
