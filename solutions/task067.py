p=lambda m:[r[:len(m)]for r in m]
# ----------------------------------------------------------------
# many

p=lambda g:[*zip(*zip(g,*g))][1:]
# stupid alt solution from jailctf