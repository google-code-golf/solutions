p=lambda g:[[v*2for v in r]for r in g+g[g[0]==g[3]:][2:5]]
# ----------------------------------------------------------------
# many

# Tied
p=lambda g:eval(str(g+g[g[2]==g[5]:][2:5]).replace(*'12'))
