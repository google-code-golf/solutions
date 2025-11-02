p=lambda m,k=67:-k*m or p([[r.pop()%sum(r[-1:],4)or k>>4&4for _ in m]for*r,in zip(*m)],k-1)
#
# p=lambda m,k=66:[[r.pop()%sum(r[-1:],4)or(k<0)*4for _ in m]for*r,in zip(*-k*m or p(m,k-1))]