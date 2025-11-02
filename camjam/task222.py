p=lambda g:[g:=[[v*(v in{*r[j-1:j+2:2]})*(sum(g,g[0]).count(v)>4)for j,v in enumerate(r)]for r in zip(*g)]for _ in g][3]
