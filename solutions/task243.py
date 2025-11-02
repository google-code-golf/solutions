p=lambda g:exec('g[::-1]=zip(*eval(str(g).replace("1, 0","1,1")));'*80)or g
# ----------------------------------------------------------------
# many

# jailctf: without str.replace
p=lambda g,i=-79:g*i or p([[r.pop()or 1in r[-1:]for r in g]for*r,in g],i+1)
