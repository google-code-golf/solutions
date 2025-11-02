f=lambda g,c:[r for*r,in zip(*g)if c in r]
p=lambda g,c=9:-c*g or p([g,[[*map({c:5}.get,r,r)]for r in g]][c!=(t:=max(g[0][0],g[1][1]))!=f(f(g,c),c)==[[*map({t:c}.get,r,r)]for*r,in f(f(g,t),t)]],c-1)