R=range(29)
p=lambda g:next([[max(r[x]for r in g[y%Y::Y])or x-1for x in R]for y in R]for Y in R[4:]if all(3>len({*c})for i in R for c in zip(*g[i::Y])))
