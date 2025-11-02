e=enumerate
def p(g):
 for k in[0]*4:
  for i,r in e(g:=[*map(list,zip(*g[::-1]))]):
   for j,v in e(r[:-1]):
    for t in g[i-k:i-~k]*(v%3>r[j+1]):t[j:]=[3-(t==r)]*(len(r)-j)
    k=v%2*-~k
 return g