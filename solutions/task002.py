p=lambda g,i=67:g*-i or p([[r.pop()%sum(r[-1:],4)or i>>4&4for r in g]for r in g],i-1)
# ----------------------------------------------------------------
# post-comp-diamonds

# oxjam
p=lambda g,k=11:-k*g or[*map(lambda*b,d=0:[d:=c^c-0**k>>d&4for c in b][::-1],*p(g,k-1))]

# A few iterations of golfing on the "rotate and do stuff" line of solutions
# %(u+4) costs some parentheses. In this case it happens that sum() is cheaper.
p=lambda g,k=67:-k*g or p([[r.pop()%sum(r[-1:],4)or k>>4&4for _ in g]for*r,in zip(*g)],k-1)
# r.pop() is mutating, so u is equivalent to r[-1], except that we need out of bounds protection.
p=lambda g,k=67:-k*g or p([[r.pop()%([0,*r][-1]+4)or k>>4&4for _ in g]for*r,in zip(*g)],k-1)
# Rotation = transpose + reverse. r.pop() and r[:0:-1] do the same job of g[::-1] 
p=lambda g,k=67:-k*g or p([[r.pop()%(u+4)or k>>4&4for u in[0]+r[:0:-1]]for*r,in zip(*g)],k-1)
# v%(u+4) is pysearch. When k = 64, 65, 66, 67, k>>4&4 is 4, otherwise 0.
p=lambda g,k=67:-k*g or p([[v%(u+4)or k>>4&4for u,v in zip([0]+r,r)]for*r,in zip(*g[::-1])],k-1)
# The idea is to set all 0s to 4s at the start, and then flood fill from the edges inwards
# Here, v is the current cell, and u is its neighbour
# Treat out of bounds cells as 0, as in zip([0]+r,r)
p=lambda g,k=67:g if k<0 else p([[3 if v==3 else 4 if v==4 and u>0 or k==67 else 0 for u,v in zip([0]+r,r)]for r in zip(*g[::-1])],k-1)
