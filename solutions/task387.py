p=lambda g,n=11:-n*g or[[[(i:=((x:=r.pop())+i>0)+i)%2*sum(r[:2-i])**4%5*5|x,x or-P**4%5*P*4,[x,sum(sum(g,[]))//2-x%15][x>9]][n//4]for P in[0]+r[:0:-1]]for*r,in zip(*p(g,n-1))if[i:=0]]
# ----------------------------------------------------------------
# post-comp-diamonds, base: cgi
