def p(g,b=99,h=1):
 v=g[r:=b//10][c:=b%10]
 while~r%11>0<5>g[r][c]:g[r][c]|=v;r-=h^v%2or-1
 if b:p(g,b-1,h*5>v);return g