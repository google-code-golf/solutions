def p(e):
 r=range(110);a=[i for i in e for i in i+[1]]+[1]*36;u=[i for i in r if a[i]&2];p=[i for i in r if all(a[r+i-u[0]]<1 for r in u)]
 p[1:3]*=p>p[5:];p=p[p==[14,61]:]
 for i in p:
  for r in u:p=r+i-u[0];e[p//11][p%11]=2
 return e