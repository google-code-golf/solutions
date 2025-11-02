import re
def p(g):
 if'5'not in(S:=str(g)):return g
 for P in[(f'5, 5(.{ {W:=len(g[0])*3-2}})5, 5',r'8,8\1 8,8'),(f'(.{ {W+3}})5'*3,r'\1 2\2 2\3 2'),('5, 5, 5','2,2,2')]:
  if g!=(t:=eval(re.sub(*P,S,1)))and p(t):return p(t)