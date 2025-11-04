p=lambda g:[[*[u%4]*4+[u%5]*4,0][::1|1-g[1][2]]for u in b"####0000("][::1|1-g[2][1]]
# ----------------------------------------------------------------
# many

# ox jam recursive
p=lambda g,h=2,w=3:h and[p(g,h-1,w&2-A//4)for A in range(9)][::1-g[h][-h]|1]or-w%3^w