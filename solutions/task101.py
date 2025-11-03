def p(e):
 w,f,r,o,q=[{a+m*20for m,e in enumerate(e)for a,e in enumerate(e)if e==d}for d in range(5)]
 for d in r:o|={d for d in r for m in f|o if abs(d-m)in(1,20)}
 for d in r:p={d}-q and{d-min(len({d+m*(n-2)for n in range(5)}&r)for m in(1,20))*(min(o)-max(o))}&r;q|=p;e=[[e or a+m*20in(p and{d-min(len({d+m*(n-2)for n in range(5)}&r)for m in(1,20))*(min(o)-m)for m in f})for a,e in enumerate(e)]for m,e in enumerate(e)]
 return e
# ----------------------------------------------------------------
# compression: auto
# oxjam
